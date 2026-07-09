# 가이드북 생성기 — Claude Code 인수인계 파일
생성일시: 2025년 (claude.ai 프로젝트에서 이관)

---

## 개요
학원에서 사용하는 애플리케이션마다 가이드북 생성이 반복되는 문제를 해결하기 위한 도구.
신규 조교·강사가 바로 사용할 수 있는 **SOP(업무 매뉴얼)**와 **HTML 튜토리얼**을 AI로 자동 생성하는 PWA 앱.

---

## 현재 상태
- [x] 전체 아키텍처 설계 완료
- [x] 시스템 프롬프트 설계 완료 (`SYSTEM_PROMPT.md`)
- [x] CSS 스타일 초안 작성 완료 (`style.css`)
- [x] PWA manifest, Service Worker 초안 완료
- [ ] **`index.html` 메인 UI 미완성 → Claude Code에서 구현**
- [ ] **`app.js` AI 호출 로직 미완성 → Claude Code에서 구현**
- [ ] **Anthropic API 연동 미완성 → Claude Code에서 구현**

---

## Claude Code에서 해야 할 작업

### 즉시 실행할 명령
```bash
# 1. 기존 파일 확인
ls -la

# 2. 로컬 개발 서버 (선택)
npx serve . 
# 또는 VS Code Live Server 확장 사용
```

### 구현할 파일 목록
```
guidebook-generator/
├── index.html       ← 메인 UI (미완성, 아래 스펙 참고)
├── app.js           ← AI 호출 + 다운로드 로직 (미완성)
├── style.css        ← 완성 (수정 최소화)
├── sw.js            ← 완성
├── manifest.json    ← 완성
└── SYSTEM_PROMPT.md ← Claude 프로젝트용 (앱과 별도)
```

---

## index.html 구현 스펙

### 탭 구조 (4개)
```
[📝 생성]  [📂 기록]  [🔄 인수인계]  [❓ 도움말]
```

### 탭 1 — 생성 (메인 기능)
```
[앱 이름 입력]
[대상 선택: 신규 조교 / 신규 강사 / 전체]
[업무 목적 textarea]
[주요 기능 textarea]
[특이사항 textarea (선택)]

[유형 선택 카드]
  ┌─────────────┐  ┌─────────────────────┐
  │  📋 SOP     │  │  🌐 HTML 튜토리얼   │
  │  업무 매뉴얼 │  │  단계별 인터랙티브   │
  └─────────────┘  └─────────────────────┘

[MD 파일 첨부 드롭존] ← 인수인계 파일 첨부용

[생성하기 버튼]

[상태 바: 로딩 / 완료 / 오류]

[출력 미리보기]
  탭: [원본 코드] [미리보기]
  [SOP 다운로드 .md] [HTML 다운로드 .html]
```

### 탭 2 — 기록
```
통계 카드: 총 생성 수 / SOP 수 / HTML 수
생성 기록 리스트 (localStorage)
각 항목: 클릭 시 재다운로드 가능
```

### 탭 3 — 인수인계
```
[인수인계 MD 생성 버튼]
  → 현재까지 생성한 가이드북 목록
  → 진행 상황 요약
  → 다음 채팅에 전달할 컨텍스트
  → .md 파일 다운로드
```

### 탭 4 — 도움말
```
Claude 프로젝트 시스템 프롬프트 전문 표시 (복사 버튼)
사용 방법 설명
API 키 입력란 (선택 — 직접 API 사용 시)
```

---

## app.js 구현 스펙

### Anthropic API 호출 방식
```javascript
// 옵션 A: Anthropic API 직접 호출 (API 키 필요)
const response = await fetch('https://api.anthropic.com/v1/messages', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': apiKey,
    'anthropic-version': '2023-06-01'
  },
  body: JSON.stringify({
    model: 'claude-opus-4-5',
    max_tokens: 4096,
    system: SYSTEM_PROMPT,  // SYSTEM_PROMPT.md 내용을 JS 상수로
    messages: [{ role: 'user', content: buildPrompt(formData) }]
  })
});

// 옵션 B: claude.ai 채팅창에서 프롬프트만 복사
// → API 키 없이도 사용 가능한 폴백
```

### 프롬프트 빌더 함수
```javascript
function buildPrompt(data) {
  return `
다음 정보로 가이드북을 생성해주세요.

- 앱 이름: ${data.appName}
- 대상: ${data.target}
- 업무 목적: ${data.purpose}
- 주요 기능: ${data.features}
- 특이사항: ${data.notes || '없음'}
- 출력 형식: ${data.type === 'sop' ? '업무 매뉴얼(SOP) - Markdown' : 'HTML 튜토리얼 - 완성된 HTML 파일'}

${data.handoverContent ? `\n## 이전 채팅 컨텍스트\n${data.handoverContent}` : ''}
  `.trim();
}
```

### 파일 다운로드 함수
```javascript
function downloadFile(content, filename, type) {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

// SOP: downloadFile(content, `${appName}_SOP.md`, 'text/markdown')
// HTML: downloadFile(content, `${appName}_튜토리얼.html`, 'text/html')
// 인수인계: downloadFile(content, `인수인계_${date}.md`, 'text/markdown')
```

### localStorage 기록 저장
```javascript
function saveToHistory(entry) {
  const history = JSON.parse(localStorage.getItem('guidebook_history') || '[]');
  history.unshift({
    id: Date.now(),
    appName: entry.appName,
    type: entry.type,      // 'sop' | 'html'
    createdAt: new Date().toISOString(),
    content: entry.content
  });
  localStorage.setItem('guidebook_history', JSON.stringify(history.slice(0, 50)));
}
```

---

## 디자인 토큰 (style.css에서 이미 정의됨)
```css
--indigo: #4f46e5;       /* 주 색상 — 버튼, 활성 탭 */
--indigo-light: #eef2ff; /* 배경 강조 */
--teal: #0d9488;         /* HTML 튜토리얼 강조 */
--amber: #d97706;        /* 인수인계, 경고 */
--gray-50 ~ gray-900     /* 중립 색상 */
```

---

## Claude Code 시작 프롬프트 (복사해서 사용)

```
이 프로젝트는 학원 가이드북 생성 PWA입니다.
HANDOVER.md 파일을 읽고 index.html과 app.js를 구현해주세요.

조건:
- style.css, sw.js, manifest.json은 이미 완성되어 있으니 수정 최소화
- Anthropic API 직접 호출 방식 사용 (API 키는 탭4 도움말에서 입력)
- API 키 없을 때는 "클립보드에 프롬프트 복사" 폴백 기능 포함
- 외부 라이브러리 없이 순수 HTML/CSS/JS
- 모바일 반응형 필수
```

---

## 참고 — 인수인계 MD 생성 로직

채팅이 길어질 경우 앱 내 "인수인계" 탭에서 다음 내용을 자동 생성:

```markdown
# 가이드북 생성기 인수인계
생성: [날짜]

## 완성된 가이드북
[localStorage에서 불러온 기록 테이블]

## 미완료 작업
사용자가 직접 입력

## 다음 채팅 시작 방법
1. claude.ai 새 채팅 열기
2. 이 MD 파일 첨부
3. "이전 내용 이어서 진행해줘" 입력
```
