# GuideBook Generator — 생성 엔진
# guide.md → SOP(.md + .html) + 튜토리얼(.html) 변환
# Python 표준 라이브러리만 사용

import sys
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

def get_base_dir():
    """실행 파일 기준 경로 반환"""
    return Path(__file__).parent

def backup_file(filepath):
    """기존 파일을 archive/에 백업"""
    if not filepath.exists():
        return
    archive_dir = get_base_dir() / "archive"
    archive_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filepath.stem}_{timestamp}{filepath.suffix}"
    shutil.copy2(filepath, archive_dir / backup_name)
    print(f"  [백업] {backup_name}")

def read_guide(app_name):
    """apps/{앱}/input/guide_{app_name}.md 읽기"""
    guide_name = f"guide_{app_name}.md"
    guide_path = get_base_dir() / "apps" / app_name / "input" / guide_name
    if not guide_path.exists():
        print(f"[오류] {guide_name} 파일을 찾을 수 없습니다.")
        print(f"  위치: {guide_path}")
        print(f"  해결: {guide_name}를 직접 작성하거나 소스 분석(4번 메뉴)을 먼저 실행하세요.")
        sys.exit(1)
    return guide_path.read_text(encoding="utf-8")

def read_input_files(app_name):
    """
    input/ 폴더의 md 파일을 아래 순서로 읽어 하나로 합친다.
    읽는 순서: guide_{app}.md → rule_{app}.md → faq_{app}.md → reference_{app}.md
    reference_{app}.md는 optional (없으면 건너뜀, 오류 없음)
    파일명은 매핑 테이블 없이 app_name만으로 생성한다.
    """
    input_dir = get_base_dir() / "apps" / app_name / "input"
    files = [
        f"guide_{app_name}.md",
        f"rule_{app_name}.md",
        f"faq_{app_name}.md",
    ]
    reference_name = f"reference_{app_name}.md"
    combined = []
    found = []

    for fname in files:
        fpath = input_dir / fname
        if fpath.exists():
            try:
                content = fpath.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = fpath.read_text(encoding="cp949")
            combined.append(content)
            found.append(fname)

    # reference — optional. 존재 여부를 항상 출력하여 혼동을 방지한다.
    reference_path = input_dir / reference_name
    reference_found = reference_path.exists()
    if reference_found:
        try:
            content = reference_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = reference_path.read_text(encoding="cp949")
        combined.append(content)

    if reference_found:
        print(f"  읽은 파일: {', '.join(found)},")
        print(f"             {reference_name}")
    else:
        print(f"  읽은 파일: {', '.join(found)}")
        print(f"             {reference_name} — 없음 (optional)")
    return "\n\n---\n\n".join(combined)

def get_images(app_name):
    """images/ 폴더 이미지 목록 반환 (파일명 순)"""
    images_dir = get_base_dir() / "apps" / app_name / "input" / "images"
    if not images_dir.exists():
        return []
    exts = {".png", ".jpg", ".jpeg", ".webp"}
    return sorted([f for f in images_dir.iterdir() if f.suffix.lower() in exts])

# ── 섹션 분류 키워드 ──────────────────────────────────────
FAQ_KEYWORDS   = ['자주 하는 실수', 'FAQ', '자주묻는', '오류', '에러', '트러블']
RULE_KEYWORDS  = ['업무 규칙', '분류 코드', '폴더 구조', '파일명 규칙',
                  '저장 원칙', '검사 규칙', '교재 코드', '과정 코드']

def classify_sections(content):
    """
    마크다운 content를 H1/H2 섹션 단위로 파싱하여
    guide_body / rule_body / faq_body 세 파트로 분류한다.

    분류 기준:
    - H1 제목에 RULE_KEYWORDS → rule 파트
    - H1 제목에 FAQ_KEYWORDS  → faq 파트
    - 그 외 H1                → guide 파트
    - H2 제목에 FAQ_KEYWORDS  → faq 파트 (현재 H1 컨텍스트 무관)
    - H2 제목에 RULE_KEYWORDS → rule 파트 (현재 H1 컨텍스트 무관)
    - 그 외 H2                → 현재 H1 컨텍스트 유지
    """
    lines = content.split('\n')
    guide_lines, rule_lines, faq_lines = [], [], []
    current_target = guide_lines
    current_ctx    = 'guide'   # 현재 H1 컨텍스트

    for line in lines:
        stripped = line.strip()

        # H1 처리 (## 로 시작하지 않는 # 으로 시작하는 라인)
        if stripped.startswith('# ') and not stripped.startswith('## '):
            title = stripped[2:].strip()
            if any(k in title for k in RULE_KEYWORDS):
                current_target = rule_lines
                current_ctx    = 'rule'
            elif any(k in title for k in FAQ_KEYWORDS):
                current_target = faq_lines
                current_ctx    = 'faq'
            else:
                current_target = guide_lines
                current_ctx    = 'guide'
            current_target.append(line)

        # H2 처리
        elif stripped.startswith('## '):
            title = stripped[3:].strip()
            if any(k in title for k in FAQ_KEYWORDS):
                current_target = faq_lines
            elif any(k in title for k in RULE_KEYWORDS):
                current_target = rule_lines
            else:
                # H1 컨텍스트 유지
                if current_ctx == 'rule':
                    current_target = rule_lines
                elif current_ctx == 'faq':
                    current_target = faq_lines
                else:
                    current_target = guide_lines
            current_target.append(line)

        else:
            current_target.append(line)

    return (
        '\n'.join(guide_lines).strip(),
        '\n'.join(rule_lines).strip(),
        '\n'.join(faq_lines).strip()
    )

def apply_inline(text):
    """인라인 마크다운 변환 (인라인 코드, 볼드)"""
    # 인라인 코드: `text` → <code>text</code>
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # 볼드: **text** → <strong>text</strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text

def md_to_html(text):
    """마크다운 → HTML 변환 (코드블록, 표, 제목 H1~H4, 리스트, 수평선,
    인라인 코드/볼드, 경고 지원)"""
    lines = text.split("\n")
    html = ""
    in_table = False
    in_list = False
    in_code = False
    code_buf = []

    for line in lines:
        # 코드블록 펜스(```) 처리 — 멀티라인 상태머신
        if line.lstrip().startswith("```"):
            if not in_code:
                # 진입: 열려있는 표/리스트 닫기
                if in_table:
                    html += "</table>\n"
                    in_table = False
                if in_list:
                    html += "</ul>\n"
                    in_list = False
                in_code = True
                code_buf = []
            else:
                # 종료: 버퍼 내용을 <pre><code>로 출력 (특수문자 이스케이프)
                code = "\n".join(code_buf)
                code = code.replace("&", "&amp;")
                code = code.replace("<", "&lt;")
                code = code.replace(">", "&gt;")
                html += f"<pre><code>{code}</code></pre>\n"
                in_code = False
            continue
        if in_code:
            code_buf.append(line)
            continue

        # 표 행 감지
        if line.startswith("|"):
            stripped = line.strip()
            # 구분선 행(|---|---|) 건너뜀
            if all(c in "|-: " for c in stripped.replace("|", "")):
                if not in_table:
                    html += "<table>\n"
                    in_table = True
                continue
            cells = [apply_inline(c.strip()) for c in stripped.strip("|").split("|")]
            if not in_table:
                html += "<table>\n<tr>"
                html += "".join(f"<th>{c}</th>" for c in cells)
                html += "</tr>\n"
                in_table = True
            else:
                html += "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>\n"
            continue
        else:
            if in_table:
                html += "</table>\n"
                in_table = False

        # 리스트
        if line.startswith("- "):
            if not in_list:
                html += "<ul>\n"
                in_list = True
            html += f"<li>{apply_inline(line[2:])}</li>\n"
            continue
        else:
            if in_list:
                html += "</ul>\n"
                in_list = False

        # 수평선(--- 만 있는 줄) → <hr>
        if line.strip() == "---":
            html += ('<hr style="border:none;border-top:1px solid #e5e7eb;'
                     'margin:20px 0;">\n')
        # 제목
        elif line.startswith("# "):
            html += f"<h1>{apply_inline(line[2:])}</h1>\n"
        elif line.startswith("## "):
            html += f"<h2>{apply_inline(line[3:])}</h2>\n"
        elif line.startswith("### "):
            html += f"<h3>{apply_inline(line[4:])}</h3>\n"
        elif line.startswith("#### "):
            html += f"<h4>{apply_inline(line[5:].strip())}</h4>\n"
        # 경고
        elif line.startswith("> ⚠️") or line.startswith("> "):
            html += f'<div class="warning">{apply_inline(line.lstrip("> "))}</div>\n'
        # 빈 줄
        elif line.strip() == "":
            html += "<br>\n"
        # 일반 텍스트
        else:
            html += f"<p>{apply_inline(line)}</p>\n"

    # 미닫힌 태그 처리
    if in_code:
        code = "\n".join(code_buf)
        code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html += f"<pre><code>{code}</code></pre>\n"
    if in_table:
        html += "</table>\n"
    if in_list:
        html += "</ul>\n"
    return html

def generate_sop(app_name, guide_content):
    """SOP 생성: .md + .html"""
    output_dir = get_base_dir() / "apps" / app_name / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")

    # SOP Markdown
    md_path = output_dir / f"{app_name}_SOP_v1.0.md"
    backup_file(md_path)
    md_content = f"# {app_name} 업무 매뉴얼 (SOP)\n생성일: {today} | 버전: v1.0\n\n---\n\n" + guide_content
    md_path.write_text(md_content, encoding="utf-8")
    print(f"  [생성] {md_path.name}")

    # SOP HTML (마크다운 → HTML 변환)
    html_path = output_dir / f"{app_name}_SOP_v1.0.html"
    backup_file(html_path)

    # 1. 전체 content를 3개 파트로 분류
    guide_md, rule_md, faq_md = classify_sections(guide_content)

    # 2. 각 파트를 HTML로 변환
    guide_html = md_to_html(guide_md) if guide_md else \
        '<div class="tab-empty">내용이 없습니다.</div>'
    rule_html  = md_to_html(rule_md)  if rule_md  else \
        '<div class="tab-empty">업무 규칙이 없습니다. rule.md를 작성해주세요.</div>'
    faq_html   = md_to_html(faq_md)   if faq_md   else \
        '<div class="tab-empty">FAQ가 없습니다. faq.md를 작성해주세요.</div>'

    # 3. 탭 UI 구성 — tab_bar는 sticky-header 안, panels는 스크롤 영역
    tab_bar = '''<div class="tab-bar">
  <button class="tab-btn active" onclick="switchTab('guide', this)">
    📋 가이드
  </button>
  <button class="tab-btn" onclick="switchTab('rule', this)">
    📌 업무규칙
  </button>
  <button class="tab-btn" onclick="switchTab('faq', this)">
    ❓ FAQ
  </button>
</div>'''

    panels = '''
<div id="tab-guide" class="tab-panel active">
''' + guide_html + '''
</div>

<div id="tab-rule" class="tab-panel">
''' + rule_html + '''
</div>

<div id="tab-faq" class="tab-panel">
''' + faq_html + '''
</div>
'''

    html_path.write_text(f"""<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{app_name} 업무 매뉴얼</title>
<style>
  body{{font-family:'Malgun Gothic',sans-serif;max-width:800px;
        margin:0 auto;padding:0 20px 40px;color:#1f2937;line-height:1.7}}
  .sticky-header{{position:sticky;top:0;background:white;z-index:10;
                  margin-bottom:24px}}
  .top-bar{{display:flex;justify-content:space-between;align-items:center;
            padding:20px 0 16px;border-bottom:1px solid #e5e7eb}}
  .top-bar h1{{margin:0;font-size:20px;color:#1e3a5f}}
  .top-meta{{font-size:12px;color:#6b7280;margin-top:4px}}
  .btn-group{{display:flex;gap:8px}}
  .btn-print{{padding:6px 14px;background:white;border:1px solid #d1d5db;
              border-radius:6px;cursor:pointer;font-size:13px;
              font-family:inherit}}
  .btn-pdf{{padding:6px 14px;background:#16a34a;color:white;border:none;
            border-radius:6px;cursor:pointer;font-size:13px;
            font-family:inherit}}
  .btn-print:hover{{background:#f9fafb}}
  .btn-pdf:hover{{background:#15803d}}
  h1{{color:#1e3a5f;border-bottom:3px solid #3b82f6;padding-bottom:10px}}
  h2{{color:#1e40af;border-left:4px solid #3b82f6;padding-left:12px;
      margin-top:32px}}
  h3{{color:#374151;margin-top:20px}}
  h4{{color:#4b5563;margin-top:16px;font-size:14px}}
  ul{{padding-left:20px;margin:8px 0}}
  li{{margin:6px 0}}
  code{{background:#f3f4f6;padding:2px 6px;border-radius:4px;
        font-family:'Consolas',monospace;font-size:13px;color:#1e40af}}
  pre{{background:#1e293b;color:#e2e8f0;padding:16px;border-radius:8px;
       overflow-x:auto;margin:12px 0;font-size:13px;line-height:1.6}}
  pre code{{background:none;color:inherit;padding:0;font-size:inherit}}
  .warning{{background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;
            padding:12px 16px;margin:12px 0;color:#92400e}}
  table{{border-collapse:collapse;width:100%;margin:12px 0}}
  th,td{{border:1px solid #e5e7eb;padding:8px 12px;text-align:left}}
  th{{background:#f3f4f6}}
  .pdf-tip{{margin-top:32px;font-size:12px;color:#9ca3af;
            padding:10px 14px;background:#f9fafb;border-radius:6px}}
  /* ── 탭 구조 ── */
  .tab-bar{{display:flex;gap:0;border-bottom:2px solid #e5e7eb;margin:0}}
  .tab-btn{{padding:10px 24px;background:none;border:none;font-size:14px;
            font-family:inherit;cursor:pointer;color:#6b7280;
            border-bottom:3px solid transparent;margin-bottom:-2px;
            transition:all 0.15s}}
  .tab-btn:hover{{color:#1e40af}}
  .tab-btn.active{{color:#1e40af;font-weight:600;
                   border-bottom:3px solid #3b82f6}}
  .tab-panel{{display:none}}
  .tab-panel.active{{display:block}}
  .tab-empty{{padding:40px 0;text-align:center;color:#9ca3af;font-size:14px}}
  @media print{{
    /* 레이아웃 */
    .sticky-header{{position:static}}
    .top-bar{{border-bottom:none}}
    body{{padding:0}}

    /* 버튼·안내 숨김 */
    .btn-group{{display:none}}
    .pdf-tip{{display:none}}
    .tab-bar{{display:none}}

    /* 탭 전체 출력 */
    .tab-panel{{display:block !important}}

    /* 탭 간 구분선 */
    .tab-panel + .tab-panel{{
      border-top:2px solid #e5e7eb;
      margin-top:32px;
      padding-top:32px;
    }}

    /* 페이지 나누기 — 탭별로 새 페이지 (선택) */
    /* .tab-panel{{page-break-before:always}} */
  }}
</style></head><body>

<div class="sticky-header">
  <div class="top-bar">
    <div>
      <h1 style="margin:0;font-size:20px;border:none;padding:0;">
        {app_name} 업무 매뉴얼 (SOP)
      </h1>
      <div class="top-meta">생성일: {today} | 버전: v1.0</div>
    </div>
    <div class="btn-group">
      <button class="btn-print" onclick="window.print()">🖨️ 인쇄</button>
      <button class="btn-pdf" onclick="savePDF()">📄 PDF 저장</button>
    </div>
  </div>
  {tab_bar}
</div>

{panels}

<div class="pdf-tip">
  💡 <b>PDF 저장 방법</b>: [📄 PDF 저장] 버튼 클릭 →
  인쇄 창에서 프린터를 <b>Microsoft Print to PDF</b> 선택 → 인쇄
</div>

<script>
// ── 탭 전환 ──────────────────────────────────────────────
function switchTab(name, btn) {{
  document.querySelectorAll('.tab-panel').forEach(function(p) {{
    p.classList.remove('active');
  }});
  document.querySelectorAll('.tab-btn').forEach(function(b) {{
    b.classList.remove('active');
  }});
  document.getElementById('tab-' + name).classList.add('active');
  btn.classList.add('active');
}}

function savePDF() {{
  var orig = document.title;
  document.title = '{app_name}_SOP_v1.0';
  window.print();
  setTimeout(function() {{ document.title = orig; }}, 1000);
}}
</script>
</body></html>""", encoding="utf-8")
    print(f"  [생성] {html_path.name}")

def generate_tutorial(app_name, guide_content, images):
    """튜토리얼 HTML 생성 (역할 탭 + STEP 네비게이션)"""
    output_dir = get_base_dir() / "apps" / app_name / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")

    # ## 섹션 파싱
    sections = []
    current = None
    for line in guide_content.split("\n"):
        if line.startswith("## "):
            if current:
                sections.append(current)
            current = {"title": line[3:].strip(), "content": []}
        elif current:
            current["content"].append(line)
    if current:
        sections.append(current)
    if not sections:
        sections = [{"title": f"{app_name} 사용법",
                     "content": guide_content.split("\n")}]

    # 역할 탭 분류
    teacher_kw = ["강사", "teacher", "강사(k)", "강사k"]
    assistant_kw = ["조교", "assistant", "조교(p", "조교p"]

    teacher_secs = []
    assistant_secs = []
    common_secs = []

    for sec in sections:
        t = sec["title"].lower()
        if any(k in t for k in teacher_kw):
            teacher_secs.append(sec)
        elif any(k in t for k in assistant_kw):
            assistant_secs.append(sec)
        else:
            common_secs.append(sec)

    has_roles = bool(teacher_secs or assistant_secs)

    # STEP HTML 블록 생성
    def make_steps(secs, prefix):
        html = ""
        total = len(secs)
        for i, sec in enumerate(secs):
            content_html = ""
            for line in sec["content"]:
                if line.startswith("- "):
                    content_html += f"<li>{line[2:]}</li>"
                elif line.startswith("> ⚠️") or line.startswith("> "):
                    content_html += (f'<div class="warning">'
                                     f'{line.lstrip("> ")}</div>')
                elif line.strip():
                    content_html += f"<p>{line}</p>"
            disp = "block" if i == 0 else "none"
            pct = int((i + 1) / total * 100) if total else 100
            prev_dis = "disabled" if i == 0 else ""
            next_dis = "disabled" if i == total - 1 else ""
            html += f"""
<div class="{prefix}step" id="{prefix}step-{i}" style="display:{disp}">
  <div class="step-num">STEP {i+1} / {total}</div>
  <h2>{sec['title']}</h2>
  <div class="progress-bar">
    <div class="progress-fill" style="width:{pct}%"></div>
  </div>
  <div class="screen-area" id="screen-{prefix}{i}">

    <div class="slide-viewer" id="viewer-{prefix}{i}" style="display:none;">
      <div class="slide-display">
        <img id="slide-img-{prefix}{i}" style="max-width:100%;border-radius:8px;
             border:1px solid #e5e7eb;">
        <button class="img-delete"
                onclick="deleteSlide('{prefix}',{i})"
                title="이 이미지 삭제">✕</button>
      </div>
      <div class="slide-nav">
        <button class="slide-btn" onclick="prevSlide('{prefix}',{i})">&#8592;</button>
        <span class="slide-counter" id="counter-{prefix}{i}">1 / 1</span>
        <button class="slide-btn" onclick="nextSlide('{prefix}',{i})">&#8594;</button>
      </div>
      <div class="thumb-tray" id="tray-{prefix}{i}"></div>
      <button class="add-btn" onclick="triggerUpload('{prefix}',{i})">+ 이미지 추가</button>
    </div>

    <div class="upload-zone" id="zone-{prefix}{i}"
         onclick="triggerUpload('{prefix}',{i})"
         ondragover="event.preventDefault();this.classList.add('drag-over')"
         ondragleave="this.classList.remove('drag-over')"
         ondrop="handleDrop(event,'{prefix}',{i})">
      <div class="upload-icon">📸</div>
      <div class="upload-text">
        클릭하거나 이미지를 여기에 드래그하세요<br>
        <small>JPG, PNG, WebP 지원 · 여러 장 가능</small>
      </div>
    </div>

    <input type="file" id="file-{prefix}{i}" accept="image/*" multiple
           style="display:none"
           onchange="handleFile(event,'{prefix}',{i})">
  </div>
  <div class="content">{content_html}</div>
  <div class="checkpoint">✅ 이 화면이 보이면 다음 단계로 진행하세요.</div>
  <div class="nav">
    <button onclick="{prefix}go({i-1})" {prev_dis}>← 이전</button>
    <span>{i+1} / {total}</span>
    <button onclick="{prefix}go({i+1})" {next_dis}>다음 →</button>
  </div>
</div>"""
        return html

    # 탭 분리 여부에 따라 HTML 구성
    if has_roles:
        # 조교 탭 우선 (조교 먼저 보여줌)
        a_secs = assistant_secs if assistant_secs else common_secs
        t_secs = teacher_secs if teacher_secs else common_secs
        panel_html = f"""
  <div class="role-tabs">
    <div class="role-tab active" onclick="switchRole('a')"
         id="tab-a">조교용</div>
    <div class="role-tab" onclick="switchRole('t')"
         id="tab-t">강사용</div>
  </div>
  <div class="role-panel active" id="panel-a">
    {make_steps(a_secs, 'a')}
  </div>
  <div class="role-panel" id="panel-t">
    {make_steps(t_secs, 't')}
  </div>"""
        role_css = """
  .role-tabs{display:flex;gap:8px;margin-bottom:24px;
             border-bottom:1px solid #e5e7eb}
  .role-tab{flex:1;padding:12px;text-align:center;cursor:pointer;
            font-size:15px;font-weight:600;color:#9ca3af;
            border-bottom:3px solid transparent}
  .role-tab.active{color:#1e3a5f;border-bottom-color:#3b82f6}
  .role-panel{display:none}
  .role-panel.active{display:block}"""
        role_js = """
function switchRole(r){
  document.getElementById('tab-a').classList.toggle('active',r==='a');
  document.getElementById('tab-t').classList.toggle('active',r==='t');
  document.getElementById('panel-a').classList.toggle('active',r==='a');
  document.getElementById('panel-t').classList.toggle('active',r==='t');
}
function ago(n){
  var s=document.querySelectorAll('.astep');
  if(n<0||n>=s.length)return;
  s.forEach(function(x){x.style.display='none'});
  s[n].style.display='block';window.scrollTo(0,0);
}
function tgo(n){
  var s=document.querySelectorAll('.tstep');
  if(n<0||n>=s.length)return;
  s.forEach(function(x){x.style.display='none'});
  s[n].style.display='block';window.scrollTo(0,0);
}
""" + f"""
function tutorialPDF() {{
  var orig = document.title;
  document.title = '{app_name}_튜토리얼_v1.0';
  window.print();
  setTimeout(function() {{ document.title = orig; }}, 1000);
}}"""
    else:
        panel_html = make_steps(sections, 's')
        role_css = ""
        role_js = """
function sgo(n){
  var s=document.querySelectorAll('.sstep');
  if(n<0||n>=s.length)return;
  s.forEach(function(x){x.style.display='none'});
  s[n].style.display='block';window.scrollTo(0,0);
}
""" + f"""
function tutorialPDF() {{
  var orig = document.title;
  document.title = '{app_name}_튜토리얼_v1.0';
  window.print();
  setTimeout(function() {{ document.title = orig; }}, 1000);
}}"""

    image_js = """
// ── 슬라이드 멀티 이미지 ──────────────────────────────

// 각 STEP의 이미지 배열과 현재 인덱스 상태
// slideData[key] = { images: [dataUrl, ...], current: 0 }
var slideData = {};

function _key(prefix, idx) { return prefix + '_' + idx; }

// 페이지 로드 시 localStorage에서 복원
window.addEventListener('DOMContentLoaded', function() {
  for (var k in localStorage) {
    if (k.startsWith('slides_')) {
      var parts = k.replace('slides_', '').split('_');
      // prefix에 _ 없으면 parts[0]=prefix, parts[1]=idx
      // prefix에 _ 있을 경우 대비: 마지막 요소가 idx
      var idx = parseInt(parts[parts.length - 1]);
      var prefix = parts.slice(0, parts.length - 1).join('_');
      try {
        var arr = JSON.parse(localStorage.getItem(k));
        if (Array.isArray(arr) && arr.length > 0) {
          slideData[_key(prefix, idx)] = { images: arr, current: 0 };
          renderSlides(prefix, idx);
        }
      } catch(e) {}
    }
  }
});

function saveSlides(prefix, idx) {
  var k = _key(prefix, idx);
  localStorage.setItem('slides_' + k,
    JSON.stringify(slideData[k] ? slideData[k].images : []));
}

function triggerUpload(prefix, idx) {
  document.getElementById('file-' + prefix + idx).click();
}

function handleFile(event, prefix, idx) {
  var files = Array.from(event.target.files);
  if (!files.length) return;
  readFiles(files, prefix, idx);
  event.target.value = '';
}

function handleDrop(event, prefix, idx) {
  event.preventDefault();
  document.getElementById('zone-' + prefix + idx)
          .classList.remove('drag-over');
  var files = Array.from(event.dataTransfer.files)
                   .filter(function(f){ return f.type.startsWith('image/'); });
  if (!files.length) return;
  readFiles(files, prefix, idx);
}

function readFiles(files, prefix, idx) {
  var k = _key(prefix, idx);
  if (!slideData[k]) slideData[k] = { images: [], current: 0 };
  var pending = files.length;
  files.forEach(function(file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      slideData[k].images.push(e.target.result);
      pending--;
      if (pending === 0) {
        slideData[k].current = slideData[k].images.length - 1;
        saveSlides(prefix, idx);
        renderSlides(prefix, idx);
      }
    };
    reader.readAsDataURL(file);
  });
}

function renderSlides(prefix, idx) {
  var k = _key(prefix, idx);
  var data = slideData[k];
  if (!data || data.images.length === 0) {
    showZone(prefix, idx);
    return;
  }

  // 뷰어 표시, 존 숨김
  var viewer = document.getElementById('viewer-' + prefix + idx);
  var zone   = document.getElementById('zone-'   + prefix + idx);
  if (!viewer || !zone) return;
  viewer.style.display = 'flex';
  zone.style.display   = 'none';

  // 메인 이미지
  var img = document.getElementById('slide-img-' + prefix + idx);
  if (img) img.src = data.images[data.current];

  // 카운터
  var counter = document.getElementById('counter-' + prefix + idx);
  if (counter) counter.textContent =
    (data.current + 1) + ' / ' + data.images.length;

  // 썸네일 트레이
  renderThumbs(prefix, idx);
}

function renderThumbs(prefix, idx) {
  var k    = _key(prefix, idx);
  var data = slideData[k];
  var tray = document.getElementById('tray-' + prefix + idx);
  if (!tray || !data) return;
  tray.innerHTML = '';
  data.images.forEach(function(src, i) {
    var item = document.createElement('div');
    item.className = 'thumb-item' + (i === data.current ? ' active' : '');
    item.draggable = true;
    item.dataset.thumbIdx = i;

    var img = document.createElement('img');
    img.src = src;
    item.appendChild(img);

    // 클릭 → 해당 슬라이드로 이동
    item.addEventListener('click', function() {
      slideData[k].current = i;
      renderSlides(prefix, idx);
    });

    // 드래그 순서 변경
    item.addEventListener('dragstart', function(e) {
      e.dataTransfer.setData('text/plain', i);
      item.style.opacity = '0.5';
    });
    item.addEventListener('dragend', function() {
      item.style.opacity = '1';
    });
    item.addEventListener('dragover', function(e) {
      e.preventDefault();
      item.classList.add('drag-over-thumb');
    });
    item.addEventListener('dragleave', function() {
      item.classList.remove('drag-over-thumb');
    });
    item.addEventListener('drop', function(e) {
      e.preventDefault();
      item.classList.remove('drag-over-thumb');
      var fromIdx = parseInt(e.dataTransfer.getData('text/plain'));
      var toIdx   = i;
      if (fromIdx === toIdx) return;
      // 배열 순서 변경
      var arr = slideData[k].images;
      var moved = arr.splice(fromIdx, 1)[0];
      arr.splice(toIdx, 0, moved);
      slideData[k].current = toIdx;
      saveSlides(prefix, idx);
      renderSlides(prefix, idx);
    });

    tray.appendChild(item);
  });
}

function prevSlide(prefix, idx) {
  var k = _key(prefix, idx);
  if (!slideData[k]) return;
  var len = slideData[k].images.length;
  slideData[k].current = (slideData[k].current - 1 + len) % len;
  renderSlides(prefix, idx);
}

function nextSlide(prefix, idx) {
  var k = _key(prefix, idx);
  if (!slideData[k]) return;
  var len = slideData[k].images.length;
  slideData[k].current = (slideData[k].current + 1) % len;
  renderSlides(prefix, idx);
}

function deleteSlide(prefix, idx) {
  var k = _key(prefix, idx);
  if (!slideData[k]) return;
  var data = slideData[k];
  data.images.splice(data.current, 1);
  if (data.images.length === 0) {
    slideData[k] = { images: [], current: 0 };
    saveSlides(prefix, idx);
    showZone(prefix, idx);
    return;
  }
  data.current = Math.min(data.current, data.images.length - 1);
  saveSlides(prefix, idx);
  renderSlides(prefix, idx);
}

function showZone(prefix, idx) {
  var viewer = document.getElementById('viewer-' + prefix + idx);
  var zone   = document.getElementById('zone-'   + prefix + idx);
  if (viewer) viewer.style.display = 'none';
  if (zone)   zone.style.display   = 'flex';
}

// 전체 초기화
function clearAllImages() {
  if (!confirm('모든 STEP의 이미지를 삭제하시겠습니까?')) return;
  for (var k in localStorage) {
    if (k.startsWith('slides_')) localStorage.removeItem(k);
  }
  slideData = {};
  // 모든 뷰어 숨기고 존 표시
  document.querySelectorAll('.slide-viewer').forEach(function(v) {
    v.style.display = 'none';
  });
  document.querySelectorAll('.upload-zone').forEach(function(z) {
    z.style.display = 'flex';
  });
}"""

    html_path = output_dir / f"{app_name}_튜토리얼_v1.0.html"
    backup_file(html_path)
    html_path.write_text(f"""<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{app_name} 튜토리얼</title>
<style>
  *{{box-sizing:border-box}}
  body{{font-family:'Malgun Gothic',sans-serif;background:#f9fafb;
        margin:0;padding:20px;color:#1f2937}}
  .container{{max-width:720px;margin:0 auto;background:white;
              border-radius:16px;padding:32px;
              box-shadow:0 4px 6px rgba(0,0,0,.07)}}
  {role_css}
  .step-num{{font-size:13px;color:#6b7280;font-weight:600;
             letter-spacing:.05em;margin-bottom:8px}}
  h2{{color:#1e3a5f;margin:0 0 16px;font-size:22px}}
  .progress-bar{{background:#e5e7eb;border-radius:99px;
                 height:6px;margin-bottom:24px}}
  .progress-fill{{background:#3b82f6;height:100%;
                  border-radius:99px;transition:width .3s}}
  .screen-area{{
    background:#f3f4f6;border-radius:12px;min-height:200px;
    display:flex;align-items:center;justify-content:center;
    margin-bottom:24px;padding:16px;text-align:center;
    position:relative;
  }}
  .upload-zone{{
    width:100%;min-height:160px;display:flex;flex-direction:column;
    align-items:center;justify-content:center;gap:10px;
    border:2px dashed #d1d5db;border-radius:10px;cursor:pointer;
    transition:all 0.2s;padding:20px;
  }}
  .upload-zone:hover,.upload-zone.drag-over{{
    border-color:#3b82f6;background:#eff6ff;
  }}
  .upload-icon{{font-size:36px;}}
  .upload-text{{font-size:14px;color:#6b7280;line-height:1.6;}}
  .upload-text small{{font-size:12px;color:#9ca3af;}}
  .img-preview{{
    position:relative;width:100%;display:flex;
    justify-content:center;align-items:center;
  }}
  .img-delete{{
    position:absolute;top:-8px;right:-8px;
    width:24px;height:24px;border-radius:50%;
    background:#ef4444;color:white;border:none;
    cursor:pointer;font-size:12px;font-weight:bold;
    display:flex;align-items:center;justify-content:center;
    line-height:1;
  }}
  .img-delete:hover{{background:#dc2626;}}
  .slide-viewer{{
    width:100%;display:flex;flex-direction:column;
    align-items:center;gap:10px;
  }}
  .slide-display{{
    position:relative;width:100%;display:flex;justify-content:center;
  }}
  .slide-nav{{display:flex;align-items:center;gap:12px;}}
  .slide-btn{{
    background:#3b82f6;color:white;border:none;border-radius:6px;
    width:32px;height:32px;cursor:pointer;font-size:16px;
    display:flex;align-items:center;justify-content:center;
  }}
  .slide-btn:hover{{background:#2563eb;}}
  .slide-counter{{
    font-size:14px;color:#6b7280;min-width:48px;text-align:center;
  }}
  .thumb-tray{{
    display:flex;gap:6px;flex-wrap:wrap;justify-content:center;
    padding:6px;min-height:54px;
  }}
  .thumb-item{{
    width:48px;height:48px;border-radius:6px;overflow:hidden;
    border:2px solid transparent;cursor:grab;position:relative;
    flex-shrink:0;
  }}
  .thumb-item.active{{border-color:#3b82f6;}}
  .thumb-item img{{
    width:100%;height:100%;object-fit:cover;pointer-events:none;
  }}
  .thumb-item.drag-over-thumb{{border-color:#f59e0b;opacity:0.7;}}
  .add-btn{{
    background:white;border:1px dashed #9ca3af;border-radius:6px;
    padding:4px 12px;font-size:13px;color:#6b7280;cursor:pointer;
    margin-top:2px;
  }}
  .add-btn:hover{{border-color:#3b82f6;color:#3b82f6;}}
  .content p,.content li{{font-size:15px;line-height:1.7;margin:6px 0}}
  .content ul{{padding-left:20px;margin:8px 0}}
  .warning{{background:#fffbeb;border:1px solid #f59e0b;
            border-radius:8px;padding:12px 16px;margin:12px 0;
            color:#92400e;font-size:14px}}
  .checkpoint{{background:#f0fdf4;border:1px solid #86efac;
               border-radius:8px;padding:12px 16px;margin:20px 0;
               color:#166534;font-size:14px}}
  .nav{{display:flex;justify-content:space-between;align-items:center;
        margin-top:24px;padding-top:20px;border-top:1px solid #e5e7eb}}
  .nav button{{padding:10px 24px;background:#3b82f6;color:white;
               border:none;border-radius:8px;cursor:pointer;
               font-size:14px;font-family:inherit}}
  .nav button:disabled{{background:#d1d5db;cursor:default}}
  .nav button:hover:not(:disabled){{background:#2563eb}}
  @media(max-width:600px){{.container{{padding:20px}}}}
  @media print{{
    .nav,.role-tabs{{display:none}}
    div[style*="gap:8px"]{{display:none}}
  }}
</style></head><body>
<div class="container">
  <div style="display:flex;justify-content:space-between;
              align-items:center;margin-bottom:24px;">
    <h1 style="margin:0;font-size:18px;color:#1e3a5f;">
      {app_name} 튜토리얼</h1>
    <div style="display:flex;gap:8px;">
      <button onclick="window.print()"
              style="padding:6px 14px;background:white;
                     border:1px solid #d1d5db;border-radius:6px;
                     cursor:pointer;font-size:13px;font-family:inherit;">
        🖨️ 인쇄
      </button>
      <button onclick="tutorialPDF()"
              style="padding:6px 14px;background:#16a34a;color:white;
                     border:none;border-radius:6px;cursor:pointer;
                     font-size:13px;font-family:inherit;">
        📄 PDF
      </button>
      <button onclick="clearAllImages()"
              style="padding:6px 14px;background:white;
                     border:1px solid #d1d5db;border-radius:6px;
                     cursor:pointer;font-size:13px;font-family:inherit;"
              title="모든 STEP 이미지 삭제">
        🗑️ 이미지 초기화
      </button>
    </div>
  </div>
  {panel_html}
</div>
<script>
{role_js}
{image_js}
</script></body></html>""", encoding="utf-8")
    print(f"  [생성] {html_path.name}")

def main():
    # Windows 콘솔(cp949)에서 ✓/✗/— 등 유니코드 출력 시 UnicodeEncodeError 방지
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    if len(sys.argv) < 3:
        print("[오류] 사용법: python generator.py [앱이름] [sop|tutorial|both]")
        sys.exit(1)
    app_name, mode = sys.argv[1], sys.argv[2]
    os.chdir(get_base_dir())
    if not (Path("apps") / app_name).exists():
        print(f"[오류] 앱 폴더 없음: apps/{app_name}")
        print("  해결: 앱 관리 메뉴에서 새 앱을 먼저 생성하세요.")
        sys.exit(1)
    print(f"\n[시작] {app_name} 가이드북 생성 중...")
    guide = read_input_files(app_name)
    images = get_images(app_name)
    print(f"  입력 파일 읽기 완료 ({len(guide)}자) | 이미지 {len(images)}개")
    if mode in ("sop", "both"):
        print("\n[SOP 생성]")
        generate_sop(app_name, guide)
    if mode in ("tutorial", "both"):
        print("\n[튜토리얼 생성]")
        generate_tutorial(app_name, guide, images)
    output_dir = get_base_dir() / "apps" / app_name / "output"
    print(f"\n[완료] {output_dir}")

    # ── Regression Check ─────────────────────────────────────
    input_dir = get_base_dir() / "apps" / app_name / "input"
    sop_html_path      = output_dir / f"{app_name}_SOP_v1.0.html"
    sop_md_path        = output_dir / f"{app_name}_SOP_v1.0.md"
    tutorial_html_path = output_dir / f"{app_name}_튜토리얼_v1.0.html"
    generated_files = {
        'sop_html':      str(sop_html_path)      if mode in ("sop", "both")      else None,
        'sop_md':        str(sop_md_path)        if mode in ("sop", "both")      else None,
        'tutorial_html': str(tutorial_html_path) if mode in ("tutorial", "both") else None,
    }
    run_regression_check(
        app_name=app_name,
        output_dir=output_dir,
        input_dir=input_dir,
        generated_files=generated_files,
        mode=mode,
        input_content=guide,
    )

    os.startfile(str(output_dir))

def detect_md_features(text):
    """
    입력 원문(guide+rule+faq+reference 합친 문자열)에서 Renderer 대상
    마크다운 문법의 존재 여부를 md_to_html과 동일한 트리거 기준으로 감지한다.

    - code_block : 라인이 ``` 로 시작 (펜스)         → <pre><code>
    - h4         : 라인이 '#### ' 로 시작             → <h4>
    - inline_code: 코드펜스 밖 라인에 `...` 패턴 존재  → <code>

    반환: {'code_block': bool, 'h4': bool, 'inline_code': bool}
    """
    code_block = False
    h4 = False
    inline_code = False
    in_code = False
    for line in (text or "").split("\n"):
        if line.lstrip().startswith("```"):
            code_block = True
            in_code = not in_code
            continue
        if in_code:
            # 펜스 내부는 apply_inline을 거치지 않으므로 인라인코드로 세지 않는다
            continue
        if line.startswith("#### "):
            h4 = True
        if re.search(r'`([^`]+)`', line):
            inline_code = True
    return {'code_block': code_block, 'h4': h4, 'inline_code': inline_code}

def run_regression_check(app_name, output_dir, input_dir, generated_files,
                         mode='both', input_content=''):
    """
    4계층 Regression Check 수행 후 터미널 출력 + Regression_Report.md 저장.
    mode: 'both' | 'sop' | 'tutorial'

    판정: ✓ PASS / ✗ FAIL / - N/A
    Result(판정)와 Display(표시)는 분리한다.

    app_name       : 앱 이름 (예: "PrintFlow")
    output_dir     : 출력 폴더 경로
    input_dir      : 입력 폴더 경로 (guide.md 등 위치)
    generated_files: {
        'sop_html':      경로 또는 None,
        'sop_md':        경로 또는 None,
        'tutorial_html': 경로 또는 None,
    }
    input_content  : guide+rule+faq+reference 합친 입력 원문.
                     Renderer 검사에서 해당 마크다운 문법이 원문에 없으면
                     FAIL이 아니라 N/A로 처리하기 위해 사용한다.
    """
    output_dir = str(output_dir)
    input_dir  = str(input_dir)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    # ── 입력 파일 수정 시각 수집 ─────────────────────────────
    guide_name     = f'guide_{app_name}.md'
    rule_name      = f'rule_{app_name}.md'
    faq_name       = f'faq_{app_name}.md'
    reference_name = f'reference_{app_name}.md'  # optional
    input_files = [guide_name, rule_name, faq_name, reference_name]
    input_mtimes = {}
    for fname in input_files:
        fpath = os.path.join(input_dir, fname)
        if os.path.exists(fpath):
            mtime = datetime.fromtimestamp(
                os.path.getmtime(fpath)
            ).strftime('%Y-%m-%d %H:%M')
            input_mtimes[fname] = mtime
        else:
            input_mtimes[fname] = '파일 없음'

    # ── 체크 헬퍼 ────────────────────────────────────────────
    def check(results, fails, na_list, label, condition,
              fail_msg=None, na=False, na_reason=''):
        """
        na=True  → N/A 처리. na_reason으로 이유 표시.
        na=False → 정상 PASS/FAIL 판정.
        """
        if na:
            reason = f' ({na_reason})' if na_reason else ''
            results.append(f'- {label}{reason}')
            na_list.append(label)
        elif condition:
            results.append(f'✓ {label}')
        else:
            results.append(f'✗ {label}')
            fails.append(fail_msg or label)

    # ── 모드별 N/A 규칙 ──────────────────────────────────────
    tutorial_na = (mode == 'sop')
    sop_na      = (mode == 'tutorial')

    # ── 1. Core Regression ───────────────────────────────────
    core_results, core_fails, core_na = [], [], []
    rend_results, rend_fails, rend_na = [], [], []
    app_results,  app_fails,  app_na  = [], [], []
    sop_html      = generated_files.get('sop_html')
    sop_md        = generated_files.get('sop_md')
    tutorial_html = generated_files.get('tutorial_html')

    check(core_results, core_fails, core_na,
          f'{guide_name} 읽기',
          input_mtimes[guide_name] != '파일 없음', f'{guide_name} 없음')
    check(core_results, core_fails, core_na,
          f'{rule_name} 읽기',
          input_mtimes[rule_name]  != '파일 없음', f'{rule_name} 없음')
    check(core_results, core_fails, core_na,
          f'{faq_name} 읽기',
          input_mtimes[faq_name]   != '파일 없음', f'{faq_name} 없음')
    # reference — optional. 있으면 PASS, 없으면 N/A (PASS 유지)
    reference_exists = input_mtimes[reference_name] != '파일 없음'
    check(core_results, core_fails, core_na,
          f'{reference_name} (optional)',
          reference_exists,
          na=not reference_exists, na_reason='reference 없음 → N/A')
    check(core_results, core_fails, core_na,
          'SOP HTML 생성',
          sop_html and os.path.exists(sop_html), 'SOP HTML 생성 실패',
          na=sop_na, na_reason=f'mode={mode}')
    check(core_results, core_fails, core_na,
          'SOP MD 생성',
          sop_md   and os.path.exists(sop_md),   'SOP MD 생성 실패',
          na=sop_na, na_reason=f'mode={mode}')
    check(core_results, core_fails, core_na,
          'Tutorial HTML 생성',
          tutorial_html and os.path.exists(tutorial_html), 'Tutorial HTML 생성 실패',
          na=tutorial_na, na_reason=f'mode={mode}')

    core_pass = not core_fails

    # ── 2. Renderer Regression ───────────────────────────────
    if sop_na:
        # tutorial 모드: SOP 미생성이므로 Renderer 전체 N/A
        for label in ['코드블록 렌더링 (<pre><code>)', '수평선 렌더링 (<hr>)',
                      'H4 렌더링 (<h4>)', '인라인 코드 렌더링 (<code>)']:
            check(rend_results, rend_fails, rend_na, label, False,
                  na=True, na_reason=f'mode={mode}, SOP 미생성')
    elif sop_html and os.path.exists(sop_html):
        html = open(sop_html, encoding='utf-8').read()
        # 입력 원문에 해당 문법이 있어야만 대응 태그를 기대할 수 있다.
        # 원문에 문법이 없으면 FAIL이 아니라 N/A (없는 걸 렌더링할 수 없음).
        feats = detect_md_features(input_content)
        check(rend_results, rend_fails, rend_na,
              '코드블록 렌더링 (<pre><code>)',
              '<pre><code>' in html, 'SOP에 <pre><code> 없음',
              na=not feats['code_block'], na_reason='입력 원문에 코드블록(```) 없음')
        # 수평선(<hr>)은 기존처럼 항상 검사한다.
        check(rend_results, rend_fails, rend_na,
              '수평선 렌더링 (<hr>)',
              '<hr '        in html, 'SOP에 <hr> 없음')
        check(rend_results, rend_fails, rend_na,
              'H4 렌더링 (<h4>)',
              '<h4'         in html, 'SOP에 <h4> 없음',
              na=not feats['h4'], na_reason='입력 원문에 H4(####) 없음')
        check(rend_results, rend_fails, rend_na,
              '인라인 코드 렌더링 (<code>)',
              '<code>'      in html, 'SOP에 인라인 <code> 없음',
              na=not feats['inline_code'], na_reason='입력 원문에 인라인코드(`...`) 없음')
    else:
        rend_results.append('- SOP HTML 없어 Renderer 검사 건너뜀')

    rend_pass = not rend_fails

    # ── 3. App Regression ────────────────────────────────────
    APP_CHECKS = {
        'PrintFlow': [
            ('Sticky Tab',         lambda h: 'sticky-header' in h,   'sticky-header 구조 없음'),
            ('PDF 버튼',           lambda h: 'window.print'  in h,   'PDF 버튼 없음'),
            ('탭 구조 (Guide)',    lambda h: 'id="tab-guide"' in h,  'tab-guide 없음'),
            ('탭 구조 (Rule)',     lambda h: 'id="tab-rule"'  in h,  'tab-rule 없음'),
            ('탭 구조 (FAQ)',      lambda h: 'id="tab-faq"'   in h,  'tab-faq 없음'),
        ],
        'KingTestMaker': [
            ('PDF 버튼',           lambda h: 'window.print'  in h,   'PDF 버튼 없음'),
            ('탭 구조 (Guide)',    lambda h: 'id="tab-guide"' in h,  'tab-guide 없음'),
            ('탭 구조 (Rule)',     lambda h: 'id="tab-rule"'  in h,  'tab-rule 없음'),
            ('탭 구조 (FAQ)',      lambda h: 'id="tab-faq"'   in h,  'tab-faq 없음'),
        ],
        'Dooly': [
            ('PDF 버튼',           lambda h: 'window.print'  in h,   'PDF 버튼 없음'),
            ('탭 구조 (Guide)',    lambda h: 'id="tab-guide"' in h,  'tab-guide 없음'),
            ('탭 구조 (Rule)',     lambda h: 'id="tab-rule"'  in h,  'tab-rule 없음'),
            ('탭 구조 (FAQ)',      lambda h: 'id="tab-faq"'   in h,  'tab-faq 없음'),
        ],
    }

    app_spec = APP_CHECKS.get(app_name, [])
    if app_spec and sop_html and os.path.exists(sop_html):
        html = open(sop_html, encoding='utf-8').read()
        for label, fn, fail_msg in app_spec:
            check(app_results, app_fails, app_na, label, fn(html), fail_msg)
    elif sop_na:
        for label, _, _ in app_spec:
            check(app_results, app_fails, app_na, label, False,
                  na=True, na_reason=f'mode={mode}, SOP 미생성')
    elif not app_spec:
        app_results.append(f'- {app_name} 앱 전용 검사 항목 미정의 (건너뜀)')
    else:
        app_results.append('- SOP HTML 없어 App 검사 건너뜀')

    app_pass = not app_fails

    # ── 4. Overall — Result / Display 분리 ───────────────────
    all_fails   = core_fails + rend_fails + app_fails
    result      = 'FAIL' if all_fails else 'PASS'

    all_na      = core_na + rend_na + app_na
    all_results = core_results + rend_results + app_results
    pass_count  = sum(1 for r in all_results if r.startswith('✓'))
    fail_count  = len(all_fails)
    na_count    = len(all_na)

    result_meta = {
        'pass_count': pass_count,
        'fail_count': fail_count,
        'na_count':   na_count,
        'has_na':     na_count > 0,
        'display':    'PASS (N/A 포함)' if (result == 'PASS' and na_count > 0) else result,
    }
    display = result_meta['display']

    # ── 다음 권장 작업 ───────────────────────────────────────
    if result == 'PASS':
        next_tasks = [
            '□ Phase A-3: PDF 전체 출력 개선 (14_작업지시서_v3.9)',
            '□ Phase B:   PrintFlow 실사용 검증',
            '□ Phase B:   KingTestMaker 실제 가이드북 생성',
            '         python analyzer.py KingTestMaker "C:\\Obsidian\\복테메이커" "docs,electron,html,log"',
            '□ Phase B:   Dooly 실제 가이드북 생성',
            '         python analyzer.py Dooly "C:\\Obsidian\\Dooly" "00_System,01_Project,docs,api"',
        ]
    else:
        next_tasks = [
            '□ 위 FAIL 항목 원인 확인 후 재생성',
            '□ generator.py 오류 수정 후 재실행',
        ]

    # ── 터미널 출력 ──────────────────────────────────────────
    sep = '=' * 42
    def section(title, results, passed):
        mark = 'PASS' if passed else 'FAIL'
        print(f'\n  [{title}] {mark}')
        for r in results:
            print(f'    {r}')

    print(f'\n{sep}')
    print(f'  Regression Check  —  {app_name}')
    print(sep)
    section('Core',     core_results, core_pass)
    section('Renderer', rend_results, rend_pass)
    section('App',      app_results,  app_pass)
    report_path = os.path.join(output_dir, 'Regression_Report.md')
    print(f'\n{sep}')
    print(f'  Overall : {display}')
    if result == 'FAIL':
        for f in all_fails:
            print(f'    - {f}')
    print(f'\n  Summary')
    print(f'    PASS : {result_meta["pass_count"]:>3}')
    print(f'    FAIL : {result_meta["fail_count"]:>3}')
    print(f'    N/A  : {result_meta["na_count"]:>3}')
    print(f'\n  Report  : {report_path}')
    print(f'{sep}\n')

    # ── Regression_Report.md 생성 ────────────────────────────
    def result_block(title, results, passed):
        mark = '✅ PASS' if passed else '❌ FAIL'
        lines = [f'## {title}  {mark}', '']
        lines += results
        lines.append('')
        return lines

    md = []
    md += ['---']
    md += [f'Project: GuideBook Generator']
    md += [f'App: {app_name}']
    md += [f'Generator: v3.8.1']
    md += [f'Result: {result}']
    md += [f'Generated: {now}']
    md += ['']
    md += ['Inputs:']
    for fname, mtime in input_mtimes.items():
        md += [f'  {fname:<10}: {mtime}']
    md += ['---', '']
    md += [f'# Regression Report', '']
    md += [f'생성일: {now}  |  Generator: v3.8.1  |  App: {app_name}  |  Mode: {mode}', '']
    md += ['---', '']
    md += result_block('Core',     core_results, core_pass)
    md += ['---', '']
    md += result_block('Renderer', rend_results, rend_pass)
    md += ['---', '']
    md += result_block('App',      app_results,  app_pass)
    md += ['---', '']
    overall_emoji = '✅' if result == 'PASS' else '❌'
    md += [f'## Overall  {overall_emoji} {display}', '']
    if result == 'FAIL':
        md += ['### 실패 원인', '']
        for f in all_fails:
            md += [f'- {f}']
        md += ['']
    md += ['---', '']
    md += ['## Summary', '']
    md += [f'| 항목 | 수 |']
    md += [f'|------|-----|']
    md += [f'| ✓ PASS | {result_meta["pass_count"]} |']
    md += [f'| ✗ FAIL | {result_meta["fail_count"]} |']
    md += [f'| - N/A  | {result_meta["na_count"]} |']
    md += ['']
    md += ['---', '']
    md += ['## 다음 권장 작업', '']
    md += next_tasks
    md += ['']

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    return result


if __name__ == "__main__":
    main()
