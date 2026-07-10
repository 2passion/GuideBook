# 가이드북 생성기 — 인수인계 파일
파일명: 13_HANDOVER_v1.4.md
작성일: 2026-07-10
이전 파일: 12_HANDOVER_v1.3.md
성격: Dooly Phase B 완료 마일스톤 문서
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
Commit : 417c40a (최신)
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
✅ Dooly Phase B 완료
   33_작업지시서  Document Set 검토
   34_작업지시서  guide 정리 (업무④ + 자주 하는 실수 + FAQ 제거)
   35_작업지시서  rule_Dooly.md 신규 작성
   36_작업지시서  faq_Dooly.md 신규 작성
   37_작업지시서  rule 미확정 항목 제거 및 Regression 재실행
   38_작업지시서  Git 커밋 및 Push
   Regression PASS 11/0/4

✅ Dooly Document Set 완성
   guide / rule / faq 역할 분리 완료
   Dooly 앱 특성 반영 (FAQ 탭 흐름 → faq.md로 통합)

✅ Git 커밋 5개 완료 (원격 반영)
   0175c29  feat: complete Dooly Phase B document set
   6cd9678  docs: add Dooly Phase B work orders
   68b393a  fix: remove unconfirmed rules from rule_Dooly and regenerate output
   094c600  docs: add Dooly fix and Git work orders
   417c40a  docs: add Dooly Phase B operational docs
```

---

## 3. 최신 Git 이력

```
417c40a  docs: add Dooly Phase B operational docs
094c600  docs: add Dooly fix and Git work orders
68b393a  fix: remove unconfirmed rules from rule_Dooly and regenerate output
6cd9678  docs: add Dooly Phase B work orders
0175c29  feat: complete Dooly Phase B document set
3c028e2  docs: add KingTestMaker Phase B milestone handover  ← KingTestMaker 연결점
```

---

## 4. 현재 기준 문서 (5종)

| 역할 | 문서 | 상태 |
|------|------|------|
| System Baseline | 8_SYSTEM_PROMPT_v5.0.md | ✅ Final (ff72c33) |
| Project Baseline | 13_HANDOVER_v1.4.md | ✅ 현재 |
| Workflow Baseline | 워크플로우_가이드.md | ✅ v1.4 |
| Knowledge Base | 시행착오_기록.md | ✅ #011까지 |
| Git Standard | 29_Git_Commit_Workflow_v1.0.md | ✅ |

---

## 5. PrintFlow 최종 상태 (Freeze)

```
PrintFlow
  Role       : Reference Implementation
  Status     : Freeze
  Regression : PASS 16 / FAIL 0 / N/A 0

Document Set
  guide_PrintFlow.md      신규 직원 5분 업무 시작
  rule_PrintFlow.md       파일 저장 원칙 / 파일명 규칙 / 검사 규칙
  faq_PrintFlow.md        실제 문제 해결
  reference_PrintFlow.md  자료분류 / 교재 / 폴더 구조
```

---

## 6. KingTestMaker 최종 상태

```
KingTestMaker
  Status     : Phase B 완료
  Commit     : f43ad16
  Regression : PASS 11 / FAIL 0 / N/A 4

Document Set
  guide_KingTestMaker.md  업무 절차
  rule_KingTestMaker.md   운영 규칙
  faq_KingTestMaker.md    자주 하는 실수 + FAQ
  reference               없음 (optional)
```

---

## 7. Dooly 최종 상태

```
Dooly
  Status     : Phase B 완료
  Commit     : 417c40a
  Regression : PASS 11 / FAIL 0 / N/A 4

Document Set
  guide_Dooly.md  업무 절차 (①②③⑤ + 설정)
  rule_Dooly.md   운영 규칙 (JSON / 업무처리 / AI챗봇 / 설정)
  faq_Dooly.md    문제 해결 (업무④ FAQ 안내 + 자주 하는 실수 + FAQ)
  reference       없음 (optional)

N/A 4건 사유
  reference 없음 (optional)
  코드블록 없음
  H4 없음
  인라인 코드 없음

특이사항 — Dooly 앱 특성 반영
  guide : 업무 번호 ③→⑤ 건너뜀 (④ faq로 이동, 원문 유지)
  faq   : 업무④ 안 되면 FAQ 섹션 포함 (Dooly UX 흐름 반영)
  rule  : 미확정 규칙 4개 제거 후 확정 (37번 작업지시서)
```

---

## 8. 되돌리지 말아야 할 결정

### GuideBook 정체성
```
Documentation Platform
Read → Generate 만 수행
SSOT 자동 수정 금지
```

### Content Standard
```
guide     → 신규 직원 5분 업무 시작 (업무 절차만)
rule      → 운영 규칙만 (~합니다 문체)
faq       → 문제 해결
reference → 코드표 / 참고자료 (optional)
```

### Dooly 특성 결정 (되돌리지 않음)
```
guide : 업무 절차만 (①②③⑤ + 설정)
faq   : 업무④ FAQ 안내 + 자주 하는 실수 + FAQ 문답
→ Dooly AI 도우미 UX 흐름을 Document Set에 반영한 의도적 설계
```

### Rule 작성 원칙
```
실제 확인된 운영 정책만 포함
미확정 규칙은 작성하지 않음
문체: ~합니다 (~한다 금지)
```

### Git 운영
```
앱 콘텐츠 → 복구(필요시) → 작업지시서 → 운영문서 → SYSTEM → HANDOVER
Commit → Push → 확인 → 다음 Commit
```

### Renderer N/A 정책
```
입력에 해당 문법 없음 → N/A
입력에 있는데 출력에 없음 → FAIL
수평선 → 항상 검사
```

---

## 9. 현재 폴더 구조

```
C:\Obsidian\GuideBook\
│
├── 99_공통\
│   ├── 8_SYSTEM_PROMPT_v5.0.md
│   ├── 13_HANDOVER_v1.4.md       ← 이 파일
│   ├── 29_Git_Commit_Workflow_v1.0.md
│   ├── 워크플로우_가이드.md
│   ├── 시행착오_기록.md
│   └── 작업지시서 33~38번
│
└── GuideBook_생성기\
    ├── generator.py
    ├── analyzer.py
    └── apps\
        ├── PrintFlow\     ✅ Freeze
        ├── KingTestMaker\ ✅ Phase B 완료
        ├── Dooly\         ✅ Phase B 완료
        └── CheckFlow\     ▶ 다음
```

---

## 10. Phase B 진행 현황

```
PrintFlow     ✅ 완료 (Reference Implementation)
KingTestMaker ✅ 완료
Dooly         ✅ 완료
CheckFlow     ▶ 다음 세션 시작
```

---

## 11. 다음 세션 첫 작업 — CheckFlow Phase B

```
CheckFlow Phase B — Document Set 검토

① guide_CheckFlow.md 존재 여부 확인
② rule_CheckFlow.md 존재 여부 확인
③ faq_CheckFlow.md 존재 여부 확인
④ 파일 없으면 앱 정보 수집 후 신규 작성
⑤ PrintFlow Baseline 기준 종합 분석
⑥ 작업지시서 작성 (39번~)
⑦ Claude Code 실행
⑧ Regression PASS 확인
⑨ Commit & Push
```

---

## 12. Current Milestone

```
Phase B — 콘텐츠 고도화

PrintFlow     ✅ 완료
              ↓
KingTestMaker ✅ 완료
              ↓
Dooly         ✅ 완료
              ↓
CheckFlow     ▶ 진행 예정 (다음 세션 첫 작업)
              ↓
Phase B 완료 → v1.2 Tag
```

---

## 13. 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(13_HANDOVER_v1.4.md) 첨부
3. 입력:
   첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.

### 검증 질문
- "현재 Phase는?"
- "Dooly 상태는?"
- "다음 작업은?"
- "최신 커밋은?"
- "Dooly 특이사항은?"
- "되돌리지 말아야 할 결정은?"
