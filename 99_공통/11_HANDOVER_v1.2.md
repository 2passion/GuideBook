# 가이드북 생성기 — 인수인계 파일
파일명: 11_HANDOVER_v1.2.md
작성일: 2026-07-10
이전 파일: 10_HANDOVER_v1.1.md
성격: PrintFlow Phase B 완료 마일스톤 문서
목적: 새 AI가 5분 안에 프로젝트를 이어가기 위한 기준 문서

---

## 1. 프로젝트 상태

```
GuideBook Documentation Platform
Generator Stable Release v1.1

Status         : Stable Release v1.1
Feature Freeze : ON
Phase          : Phase B — 콘텐츠 고도화

GitHub : https://github.com/2passion/GuideBook
Branch : main
Tag    : v1.1
Commit : 7c591fe (최신)
```

### Regression 기준선 (Phase B 시작 기준)
| 앱 | Overall | PASS | FAIL | N/A |
|----|---------|------|------|-----|
| PrintFlow | ✅ PASS | 16 | 0 | 0 |
| KingTestMaker | ✅ PASS | 11 | 0 | 4 |
| Dooly | ✅ PASS | 11 | 0 | 4 |

---

## 2. 오늘 완료 사항 (2026-07-10)

```
✅ PrintFlow Phase B 완료
   20_작업지시서  문서 역할 분리 (guide/rule/faq/reference)
   21_작업지시서  코드 체계 통일 (A/B/C/D, grade/step)
   22_작업지시서  검사 규칙 네이밍 개선 (HW/TEST)
   Regression PASS 16/0/0

✅ PrintFlow Reference Implementation 확정
   모든 앱의 Document Set 기준

✅ Git 운영 정책 확정
   archive Git 제외 (.gitignore)
   앱 단위 Commit 원칙

✅ GuideBook Standards 6종 확정
   Input / Output / Regression / Git / Content / Phase B Execution

✅ 8_SYSTEM_PROMPT_v5.0 Final
   System Baseline 문서 확정

✅ 워크플로우_가이드 v1.4
   Commit/Push 단계 추가

✅ 시행착오_기록 보강
   관련 파일 / 재발 방지 항목 추가 (#001~#011)

✅ Automation Hooks 설계 완료
   25_구현계획서_Automation_Hooks_v1.1
   Status: Approved (Deferred)
   Implementation: v2.x

✅ GitHub Commit 이력
   cd0b337  docs: finalize PrintFlow content baseline
   76cc3fb  chore: ignore generator archive
   78e23c4  docs: add archive gitignore work orders
   0bc1da3  docs: add deferred automation hooks design
   7c591fe  docs: update automation hooks design to v1.1
```

---

## 3. 현재 기준 문서 (4종)

| 역할 | 문서 | 상태 |
|------|------|------|
| System Baseline | 8_SYSTEM_PROMPT_v5.0.md | ✅ Final |
| Project Baseline | 11_HANDOVER_v1.2.md | ✅ 현재 |
| Workflow Baseline | 워크플로우_가이드.md | ✅ v1.4 |
| Knowledge Base | 시행착오_기록.md | ✅ #011까지 |

---

## 4. PrintFlow 최종 상태 (Freeze)

```
PrintFlow
  Role   : Reference Implementation
  Status : Freeze

Document Set
  guide_PrintFlow.md      신규 직원 5분 업무 시작
  rule_PrintFlow.md       파일 저장 원칙 / 파일명 규칙 / 검사 규칙(HW/TEST)
  faq_PrintFlow.md        실제 문제 해결
  reference_PrintFlow.md  자료분류(A/B/C/D) / 교재(grade/step) / 폴더 구조

코드 체계
  자료 분류  A-01~D-02 (A교재/B프린트/C시험대비/D성취도)
  교재 코드  grade-a/b/c × step-a/b/c/d/e
  검사 규칙  HW_X-XX / TEST_X-XX
```

---

## 5. 되돌리지 말아야 할 결정

### GuideBook 정체성
```
Documentation Platform
Read → Generate 만 수행
SSOT 자동 수정 금지
```

### Content Standard
```
guide     → 신규 직원 5분 업무 시작 (최소 문서)
rule      → 운영 규칙만
faq       → 문제 해결
reference → 코드표 / 참고자료 (optional)
```

### PrintFlow = Reference Implementation
```
KingTestMaker / Dooly / CheckFlow 모두
PrintFlow Document Set 구조를 기준으로 작성한다.
```

### Automation Hooks
```
Status: Approved (Deferred)
Phase B에서는 구현하지 않는다.
v2.x에서 구현한다.
```

### Git 운영
```
앱 하나 완료 → Commit → Push
archive → Git 제외 (로컬 복구용만)
```

### Renderer N/A 정책
```
입력에 해당 문법 없음 → N/A
입력에 있는데 출력에 없음 → FAIL
수평선 → 항상 검사
```

---

## 6. 현재 구조

```
C:\Obsidian\GuideBook\
│
├── 99_공통\
│   ├── 8_SYSTEM_PROMPT_v5.0.md   ← System Baseline
│   ├── 11_HANDOVER_v1.2.md       ← 이 파일
│   ├── 워크플로우_가이드.md        ← v1.4
│   ├── 시행착오_기록.md            ← #011까지
│   └── 작업지시서 20~25번
│
└── GuideBook_생성기\
    ├── generator.py
    ├── analyzer.py
    └── apps\
        ├── PrintFlow\     ✅ Freeze
        ├── KingTestMaker\ ▶ 다음
        ├── Dooly\
        └── CheckFlow\
```

---

## 7. 다음 세션 첫 작업

```
KingTestMaker Phase B — Document Set 검토

순서:
① guide_KingTestMaker.md 검토
② rule_KingTestMaker.md 검토
③ faq_KingTestMaker.md 검토
④ 3개를 Document Set으로 종합 분석
   (PrintFlow Baseline 기준 6가지 검토)
⑤ 작업지시서 작성 (26_작업지시서~)
⑥ Claude Code 실행
⑦ Regression PASS 확인
⑧ Commit & Push
```

### 검토 기준 (PrintFlow 동일)
```
1. guide    신규 조교 5분 업무 시작 가능한가
2. rule     운영 규칙만 있는가 / 코드표는 reference 분리 가능한가
3. faq      실제 업무 질문만 있는가
4. reference 코드표 / 분류 체계만 있는가
5. Document Set 중복 없는가
6. Regression 기준 유지하는가
```

---

## 8. Phase B 진행 현황

```
PrintFlow     ✅ 완료 (Reference Implementation)
KingTestMaker ▶ 다음 세션 시작
Dooly
CheckFlow
```

---

## 9. 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(11_HANDOVER_v1.2.md) 첨부
3. 입력:
   첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.

### 검증 질문
- "현재 Phase는?"
- "PrintFlow 상태는?"
- "다음 작업은?"
- "GuideBook Standards 6종은?"
- "Automation Hooks 결정은?"
- "되돌리지 말아야 할 결정은?"
