# 가이드북 생성기 — 인수인계 파일
파일명: 12_HANDOVER_v1.3.md
작성일: 2026-07-10
이전 파일: 11_HANDOVER_v1.2.md
성격: KingTestMaker Phase B 완료 마일스톤 문서
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
Commit : ff72c33 (최신)
```

### Regression Baseline (Phase B)
| 앱 | Overall | PASS | FAIL | N/A |
|----|---------|------|------|-----|
| PrintFlow | ✅ PASS | 16 | 0 | 0 |
| KingTestMaker | ✅ PASS | 11 | 0 | 4 |
| Dooly | ✅ PASS | 11 | 0 | 4 |

---

## 2. 이번 세션 완료 사항 (2026-07-10)

```
✅ KingTestMaker Phase B 완료
   30_작업지시서  guide 역할 정리 (업무만 유지)
   31_작업지시서  rule_KingTestMaker.md 신규 작성
   32_작업지시서  faq_KingTestMaker.md 신규 작성
   Regression PASS 11/0/4

✅ KingTestMaker Document Set 완성
   guide / rule / faq 역할 분리 완료
   PrintFlow Baseline 기준 동일 구조 달성

✅ Git Commit Workflow Standard 확정
   29_Git_Commit_Workflow_v1.0.md 작성
   커밋 구조 5단계 표준화
   모든 앱에 재사용 가능

✅ Git 커밋 3단계 완료
   Commit 1  306423a  작업지시서
   Commit 2  ec56409  운영 문서
   Commit 3  ff72c33  시스템 기준
   워킹트리 클린
```

---

## 3. 최신 Git 이력

```
ff72c33  docs: finalize GuideBook system baseline v5.0
ec56409  docs: update GuideBook workflow and knowledge base
306423a  docs: add KingTestMaker Phase B work orders
f43ad16  feat: complete KingTestMaker Phase B document set
abc08a6  docs: finalize PrintFlow Phase B milestone handover
```

---

## 4. 현재 기준 문서 (5종)

| 역할 | 문서 | 상태 |
|------|------|------|
| System Baseline | 8_SYSTEM_PROMPT_v5.0.md | ✅ Final (ff72c33) |
| Project Baseline | 12_HANDOVER_v1.3.md | ✅ 현재 |
| Workflow Baseline | 워크플로우_가이드.md | ✅ v1.4 |
| Knowledge Base | 시행착오_기록.md | ✅ #011까지 |
| Git Standard | 29_Git_Commit_Workflow_v1.0.md | ✅ 신규 확정 |

---

## 5. PrintFlow 최종 상태 (Freeze)

```
PrintFlow
  Role       : Reference Implementation
  Status     : Freeze
  Commit     : cd0b337
  Regression : PASS 16 / FAIL 0 / N/A 0

Document Set
  guide_PrintFlow.md      신규 직원 5분 업무 시작
  rule_PrintFlow.md       파일 저장 원칙 / 파일명 규칙 / 검사 규칙(HW/TEST)
  faq_PrintFlow.md        실제 문제 해결
  reference_PrintFlow.md  자료분류(A/B/C/D) / 교재(grade/step) / 폴더 구조
```

---

## 6. KingTestMaker 최종 상태

```
KingTestMaker
  Status     : Phase B 완료
  Commit     : f43ad16
  Regression : PASS 11 / FAIL 0 / N/A 4

Document Set
  guide_KingTestMaker.md  업무 절차 (복테 제작 / 오답노트 제작)
  rule_KingTestMaker.md   운영 규칙 (복테 / JSON / 오답노트)
  faq_KingTestMaker.md    자주 하는 실수 + FAQ
  reference               없음 (optional)

N/A 4건 사유
  reference 없음 (optional)
  코드블록 없음
  H4 없음
  인라인 코드 없음
```

---

## 7. 되돌리지 말아야 할 결정

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
앱 하나 완료 → 앱 콘텐츠 Commit
→ 작업지시서 Commit
→ 운영 문서 Commit
→ 시스템 기준 Commit (변경 시)
→ HANDOVER Commit
archive → Git 제외 (로컬 복구용만)
```

### Renderer N/A 정책
```
입력에 해당 문법 없음 → N/A
입력에 있는데 출력에 없음 → FAIL
수평선 → 항상 검사
```

### Rule 문체
```
"~합니다" 형태로 통일
"~한다" 형태 사용 금지
```

---

## 8. 현재 폴더 구조

```
C:\Obsidian\GuideBook\
│
├── 99_공통\
│   ├── 8_SYSTEM_PROMPT_v5.0.md   ← System Baseline (ff72c33)
│   ├── 12_HANDOVER_v1.3.md       ← 이 파일
│   ├── 29_Git_Commit_Workflow_v1.0.md  ← Git 운영 표준
│   ├── 워크플로우_가이드.md        ← v1.4
│   ├── 시행착오_기록.md            ← #011까지
│   └── 작업지시서 20~32번
│
└── GuideBook_생성기\
    ├── generator.py
    ├── analyzer.py
    └── apps\
        ├── PrintFlow\     ✅ Freeze
        ├── KingTestMaker\ ✅ Phase B 완료
        ├── Dooly\         ▶ 다음
        └── CheckFlow\
```

---

## 9. Phase B 진행 현황

```
PrintFlow     ✅ 완료 (Reference Implementation)
KingTestMaker ✅ 완료
Dooly         ▶ 다음 세션 시작
CheckFlow
```

---

## 10. 다음 세션 첫 작업 — Dooly Phase B

```
Dooly Phase B — Document Set 검토

① guide_Dooly.md 검토
② rule_Dooly.md 검토
③ faq_Dooly.md 검토
④ reference 필요 여부 판단
⑤ PrintFlow Baseline 기준 종합 분석
⑥ 작업지시서 작성 (33번~)
⑦ Claude Code 실행
⑧ Regression PASS 확인
⑨ Commit & Push
```

### 검토 기준 (PrintFlow / KingTestMaker 동일)
```
1. guide    신규 조교 5분 업무 시작 가능한가
2. rule     운영 규칙만 있는가 / 코드표는 reference 분리 가능한가
3. faq      실제 업무 질문만 있는가
4. reference 코드표 / 분류 체계만 있는가
5. Document Set 중복 없는가
6. Regression 기준 유지하는가
```

---

## 11. Current Milestone

```
Phase B — 콘텐츠 고도화

PrintFlow     ✅ 완료 (Reference Implementation)
              ↓
KingTestMaker ✅ 완료
              ↓
Dooly         ▶ 진행 예정 (다음 세션 첫 작업)
              ↓
CheckFlow
              ↓
Phase B 완료 → v1.2 Tag
```

---

## 12. 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(12_HANDOVER_v1.3.md) 첨부
3. 입력:
   첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.

### 검증 질문
- "현재 Phase는?"
- "KingTestMaker 상태는?"
- "다음 작업은?"
- "최신 커밋은?"
- "되돌리지 말아야 할 결정은?"
- "Git Commit Workflow Standard는?"
