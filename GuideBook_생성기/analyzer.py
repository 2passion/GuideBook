# GuideBook Generator — 소스 분석 엔진
# 실제 프로젝트 소스 폴더를 읽어 guide.md 자동 생성
# Python 표준 라이브러리만 사용

import sys
import os
from datetime import datetime
from pathlib import Path

# 읽기 지원 확장자 및 우선순위
PRIORITY_EXTS = [".md", ".txt", ".html", ".jsx", ".js", ".py", ".bat", ".sql", ".css", ".json"]
MAX_LINES = 500  # 파일 1개당 최대 읽기 줄 수

def get_base_dir():
    return Path(__file__).parent

def read_file_safe(filepath):
    """파일을 안전하게 읽기 (실패 시 None 반환)"""
    for enc in ["utf-8", "cp949", "utf-8-sig"]:
        try:
            lines = filepath.read_text(encoding=enc).splitlines()
            return "\n".join(lines[:MAX_LINES])
        except Exception:
            continue
    return None

def scan_folders(src_root, folder_list):
    """지정 폴더들의 파일 목록을 우선순위 순으로 반환"""
    src_path = Path(src_root)
    all_files = []
    for folder in folder_list:
        folder_path = src_path / folder.strip()
        if not folder_path.exists():
            print(f"  [건너뜀] 폴더 없음: {folder_path}")
            continue
        for ext in PRIORITY_EXTS:
            files = sorted(folder_path.rglob(f"*{ext}"))
            all_files.extend(files)
    return all_files

def extract_content(files):
    """파일 목록에서 내용 추출"""
    overview_lines = []   # 앱 개요 (README, docs의 md)
    ui_lines = []         # 화면/메뉴 (html, jsx)
    procedure_lines = []  # 업무 절차 (command, docs의 md)
    error_lines = []      # 오류/주의 (log)
    read_files = []

    for f in files:
        content = read_file_safe(f)
        if not content:
            continue

        print(f"  [읽기] {f.name}")
        read_files.append(str(f))
        parts = f.parts
        folder_name = parts[-2] if len(parts) >= 2 else ""

        # 폴더별 분류
        if folder_name.lower() in ("docs", "readme") or f.name.lower() == "readme.md":
            overview_lines.append(f"\n### {f.name}\n{content[:800]}")
        elif folder_name.lower() in ("log", "archive"):
            error_lines.append(f"\n### {f.name}\n{content[:400]}")
        elif folder_name.lower() in ("command",):
            procedure_lines.append(f"\n### {f.name}\n{content[:600]}")
        elif f.suffix.lower() in (".html", ".jsx"):
            ui_lines.append(f"\n### {f.name}\n{content[:400]}")
        elif f.suffix.lower() in (".md",):
            procedure_lines.append(f"\n### {f.name}\n{content[:500]}")
        else:
            procedure_lines.append(f"\n### {f.name}\n{content[:300]}")

    return overview_lines, ui_lines, procedure_lines, error_lines, read_files

def generate_guide_md(app_name, src_root, folder_list_str, output_path):
    """분석 결과로 guide.md 생성"""
    folder_list = [f.strip() for f in folder_list_str.split(",")]
    today = datetime.now().strftime("%Y-%m-%d")

    print(f"\n[분석 시작] {app_name}")
    print(f"  소스: {src_root}")
    print(f"  폴더: {', '.join(folder_list)}")

    files = scan_folders(src_root, folder_list)
    print(f"\n  총 {len(files)}개 파일 발견")

    overview, ui, procedure, errors, read_files = extract_content(files)

    file_list_str = "\n".join(f"- {f}" for f in read_files)

    guide = f"""# {app_name} 가이드
생성일: {today}
소스 경로: {src_root}
분석 폴더: {', '.join(folder_list)}
분석 파일 수: {len(read_files)}개

---

## 앱 개요
{''.join(overview) if overview else '(docs/ 또는 README.md에서 자동 추출됩니다)'}

---

## 주요 화면 및 메뉴
{''.join(ui) if ui else '(html/jsx 파일에서 자동 추출됩니다)'}

---

## 업무 절차
{''.join(procedure) if procedure else '(command/ 또는 docs/ 파일에서 자동 추출됩니다)'}

---

## 주의사항 및 오류
{''.join(errors) if errors else '(log/ 파일에서 자동 추출됩니다)'}

---

## 자주 하는 실수
| 증상 | 원인 | 해결 |
|------|------|------|
| (log 분석 후 추가 예정) | | |

---

## FAQ
Q. (docs 분석 후 추가 예정)
A.

---

## 분석 파일 목록 ({len(read_files)}개)
{file_list_str}
"""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(guide, encoding="utf-8")
    print(f"\n[완료] {output_path.name} 생성: {output_path}")
    return str(output_path)

def main():
    if len(sys.argv) < 4:
        print("[오류] 사용법: python analyzer.py [앱이름] [소스루트경로] [폴더1,폴더2,...]")
        print("  예시: python analyzer.py PrintFlow C:\\Obsidian\\PrintFlow command,log,WORK")
        sys.exit(1)

    app_name = sys.argv[1]
    src_root = sys.argv[2]
    folders  = sys.argv[3]

    os.chdir(get_base_dir())

    if not Path(src_root).exists():
        print(f"[오류] 소스 경로를 찾을 수 없습니다: {src_root}")
        print("  해결: 경로가 올바른지 확인하세요.")
        sys.exit(1)

    output_path = get_base_dir() / "apps" / app_name / "input" / f"guide_{app_name}.md"
    generate_guide_md(app_name, src_root, folders, output_path)
    print(f"\n[다음 단계] generator.py로 SOP + 튜토리얼을 생성하세요.")
    print(f"  python generator.py {app_name} both")

if __name__ == "__main__":
    main()
