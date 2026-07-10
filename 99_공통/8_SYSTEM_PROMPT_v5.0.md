# 8_SYSTEM_PROMPT_v5.0.md
# GuideBook Documentation Platform
# System Baseline — Stable Release v1.1

작성일: 2026-07-10
기준: Stable Release v1.1 / Phase B

---

## 1. 프로젝트 정체성

GuideBook는 학원 애플리케이션 가이드북을 생성하는 Documentation Platform이다.

Generator는 Documentation Engine이다.
SSOT(입력 파일)를 읽고 SOP / Tutorial을 생성한다.
Generator는 읽기(Read) → 생성(Generate)만 수행한다.
SSOT는 절대 자동 수정하지 않는다.

```
SSOT (guide / rule / faq / reference)
        ↓
Generator (generator.py)
        ↓
Output (SOP .md / SOP .html / Tutorial .html)
```

---

## 2. 현재 상태

```
Project   : GuideBook Documentation Platform
Status    : Stable Release v1.1
Freeze    : Feature Freeze ON
Phase     : Phase B — 콘텐츠 고도화
GitHub    : https://github.com/2passion/GuideBook
Branch    : main
Tag       : v1.1
```

### Reference Implementation
PrintFlow는 GuideBook v1.1의 Reference Implementation이다.
KingTestMaker / Dooly / CheckFlow는 PrintFlow 구조를 기준으로 작성한다.

```
PrintFlow     Reference Implementation  ✅ 완료
KingTestMaker                           진행 중
Dooly
CheckFlow
```

---

## 3. GuideBook Standards

GuideBook는 아래 6가지 표준을 운영 기준으로 사용한다.

### 3-1. Input Standard
```
guide_{AppName}.md      신규 직원용 핵심 업무
rule_{AppName}.md       운영 규칙
faq_{AppName}.md        문제 해결
reference_{AppName}.md  코드표 / 참고자료 (optional)
```

### 3-2. Output Standard
```
{AppName}_SOP_v{버전}.md
{AppName}_SOP_v{버전}.html
{AppName}_튜토리얼_v{버전}.html
```

### 3-3. Regression Standard
```
[Core]      입력 파일 읽기 / 출력 파일 생성
[Renderer]  코드블록 / 수평선 / H4 / 인라인 코드
[App]       Sticky Tab / PDF 버튼 / 탭 구조
[Overall]   PASS / FAIL / N/A Summary
```

### 3-4. Git Standard
```
커밋 단위  : 앱 하나 완료 시
커밋 메시지: feat: / fix: / docs: / chore: prefix
archive   : Git 제외 (로컬 복구용만 유지)
Tag       : Phase B 완료 시 v1.2
```

### 3-5. Content Standard
```
guide     → 신규 직원이 5분 안에 업무 시작 가능
rule      → 운영 규칙만 포함
faq       → 실제 업무 문제 해결
reference → 코드표 / 참고자료 (Generator optional 입력)
```

### 3-6. Phase B Execution Standard
```
작업지시서 작성
    ↓
콘텐츠 수정 (SSOT 파일)
    ↓
Regression 실행
    ↓
검토 / 승인
    ↓
Commit & Push
    ↓
다음 앱
```

---

## 4. Document Set Standard

모든 앱의 입력 파일은 아래 구조를 따른다.

```
guide
↓
무엇을 하는가 (신규 직원 5분 업무 시작)

rule
↓
반드시 지켜야 하는 규칙

faq
↓
막혔을 때 해결

reference
↓
코드표 / 교재표 / 과정표 (optional)
```

### 역할 분리 원칙
- 각 문서는 하나의 책임만 갖는다.
- guide에 rule 내용을 넣지 않는다.
- faq는 guide의 반복이 아니다.
- reference는 분류 체계 / 코드표만 담는다.

---

## 5. Workflow Standard

```
① 기획 / 설계
   Claude 채팅 → 요구사항 검토 → 작업지시서 작성

② 구현
   Claude Code → 파일 수정 → Regression 실행

③ 검토
   완료 보고 확인 → Exit Criteria 점검

④ Git
   Commit → Push (앱 단위)

⑤ 인수인계
   HANDOVER 파일 생성 → 다음 세션 전달
```

---

## 6. Git 운영 원칙

```
커밋 단위
  앱 하나 완료 시 (권장)
  또는 하루 작업 종료 시

커밋 메시지 형식
  feat: 신규 기능
  fix:  버그 수정
  docs: 문서 변경
  chore: 빌드 / 설정 변경

archive 정책
  GuideBook_생성기/archive/*  → Git 제외
  archive/.gitkeep            → 폴더 구조 유지
  로컬 archive                → 복구용 유지

Tag 정책
  Phase B 완료 시 → git tag v1.2
  현재 Tag        → v1.1
```

---

## 7. Phase B 운영

Phase B는 Generator Freeze 이후 콘텐츠 고도화 단계다.

### Phase B 검토 기준
```
① 신규 직원이 5분 안에 업무를 시작할 수 있는가?
② guide / rule / faq 역할이 명확한가?
③ 문서 간 중복이 없는가?
④ Generator가 좋은 SOP / Tutorial을 생성하기에 적합한 구조인가?
```

### Phase B 진행 현황
```
PrintFlow     ✅ 완료 (Reference Implementation)
KingTestMaker ▶ 진행 중
Dooly
CheckFlow
```

### Phase B 완료 기준
```
□ 각 앱 Document Set 완성
□ Regression PASS 유지
□ 앱 단위 Commit 완료
□ Phase B 완료 → v1.2 Tag
```

---

## 8. Feature Freeze 운영

```
허용
  ✅ Bug Fix
  ✅ Renderer 개선
  ✅ UI 개선
  ✅ Performance 개선
  ✅ 콘텐츠 고도화 (guide / rule / faq / reference 수정)

불허
  ❌ 신규 기능 추가
  ❌ 관리자 기능
  ❌ 데이터 저장 기능
  ❌ SSOT 자동 수정 기능
```

신규 기능은 v2.x에서만 개발한다.
Generator는 읽기 전용 Documentation Engine을 유지한다.

---

## 9. SSOT 원칙

입력 Markdown이 SSOT다.

```
guide.md    → 사용법
rule.md     → 업무규칙
faq.md      → FAQ
reference.md → 참조 코드표 (optional)
```

Generator는 읽기(Read) → 생성(Generate)만 수행한다.
Markdown 수정은 작업지시서에 명시된 경우만 허용한다.
Generator는 절대로 자동으로 입력 파일을 수정하지 않는다.

---

## 10. 행동 원칙

1. Input Standard 준수 — `{type}_{AppName}.md` 형식 엄수
2. Content Standard 준수 — guide / rule / faq / reference 역할 분리
3. SSOT 우선 — 입력 파일이 진실의 원천
4. Feature Freeze 준수 — Phase B에서는 콘텐츠만 변경
5. Regression 필수 — 모든 콘텐츠 변경 후 반드시 실행
6. 앱 단위 Commit — 앱 하나 완료 시 Commit & Push
7. 행동 중심 서술 — "~클릭합니다" 형태로 작성
8. 역할 분리 — 강사용 / 조교용 절차 명확히 구분
9. 실제 UI 반영 — 실제 버튼명 / 메뉴명 사용
10. HANDOVER 작성 — 세션 종료 시 인수인계 파일 생성

---

## 11. v2.x 로드맵 (Deferred)

```
Decision: Approved (Deferred)
이유: Phase B 완료 후 구현

Future Feature: SSOT 자동 분류 엔진

Expected Flow:
  학원_업무매뉴얼_SOP_v2.md (SSOT 단일 원본)
          ↓
  GuideBook Generator (Auto Classification)
          ↓
  guide.md / rule.md / reference.md / faq.md 자동 생성
```

---

## 파일 경로

```
C:\Obsidian\GuideBook\
│
├── 99_공통\
│   ├── 8_SYSTEM_PROMPT_v5.0.md   ← 이 파일 (현재 기준)
│   ├── 10_HANDOVER_v1.1.md       ← 현재 인수인계
│   ├── archive\
│   │   ├── 1_SYSTEM_PROMPT.md    ← Legacy
│   │   └── 1_HANDOVER.md         ← Legacy
│   └── ...
│
└── GuideBook_생성기\
    ├── generator.py
    ├── analyzer.py
    └── apps\
        ├── PrintFlow\    input/ output/
        ├── KingTestMaker\ input/ output/
        ├── Dooly\        input/ output/
        └── CheckFlow\    input/ output/
```
