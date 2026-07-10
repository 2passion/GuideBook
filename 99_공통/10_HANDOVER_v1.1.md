# 가이드북 생성기 — 인수인계 파일
파일명: 10_HANDOVER_v1.1.md
작성일: 2026-07-10
이전 파일: 9_HANDOVER_v1.0.md
성격: Stable Release v1.1 기준점(Baseline) 문서
목적: 새 AI가 5분 안에 프로젝트를 이어가기 위한 기준 문서

---

## 1. 프로젝트 상태

```
GuideBook Documentation Platform
Generator Stable Release v1.1

Status         : Stable Release v1.1
Feature Freeze : ON

GitHub : https://github.com/2passion/GuideBook
Branch : main
Tag    : v1.1
Commit : 11f02b9
```

Regression 최종 결과:
| 앱 | Overall | PASS | FAIL | N/A |
|----|---------|------|------|-----|
| PrintFlow | ✅ PASS | 15 | 0 | 1 |
| KingTestMaker | ✅ PASS | 11 | 0 | 4 |
| Dooly | ✅ PASS | 11 | 0 | 4 |

---

## 2. 현재 단계

```
Phase B — 콘텐츠 고도화

Generator는 Freeze 상태.
다음 작업은 각 앱의 guide / rule / faq 콘텐츠 품질 향상이다.
```

---

## 3. 이번 세션 완료 사항

```
✅ 입력 파일명 표준화 (generator.py / analyzer.py / bat)
   guide_{AppName}.md
   rule_{AppName}.md
   faq_{AppName}.md
   reference_{AppName}.md  ← optional 신규

✅ guide 경량화
   PrintFlow     3KB (신규직원용 핵심 업무)
   KingTestMaker 2KB (신규직원용 핵심 업무)
   Dooly         3KB (업무 중심 구조)

✅ Renderer 조건부 N/A 정책
   입력 원문에 해당 문법 없음 → N/A
   입력에 있는데 출력에 없음 → FAIL
   수평선(<hr>) → 항상 검사

✅ GitHub 최초 Commit & Push
   171 files / commit 11f02b9

✅ Stable Release v1.1 선언
   모든 RC Exit Criteria 충족 확인 후 선언
```

---

## 4. 되돌리지 말아야 할 결정

### GuideBook의 정체성
```
GuideBook Generator는 Documentation Platform이다.
읽기(Read) → 생성(Generate)만 수행한다.
SSOT(입력 파일)는 절대 자동 수정하지 않는다.
```

### 문서 역할 분리
```
guide     → 신규 직원용 핵심 업무 (최소 문서)
rule      → 운영 규칙
faq       → 문제 해결
reference → 선택적 참고 자료 (optional)

guide에 모든 내용을 넣지 않는다.
각 문서의 역할이 다르기 때문이다.
```

### Renderer Regression 판정 기준
```
입력 원문에 해당 문법이 없으면 → N/A  (PASS 유지)
입력 원문에 있는데 출력에 없으면 → FAIL
수평선(<hr>)은 항상 검사
N/A는 FAIL이 아니다.
```

### 입력 파일명 규칙 (확정)
```
{type}_{AppName}.md
type    : guide / rule / faq / reference
AppName : PascalCase
         (PrintFlow / KingTestMaker / Dooly / CheckFlow)
```

---

## 5. 현재 구조

```
C:\Obsidian\GuideBook\
│
├── 99_공통\              ← 작업지시서, HANDOVER, SYSTEM_PROMPT
├── GuideBook_생성기\     ← generator.py / analyzer.py / bat
│   └── apps\
│       ├── PrintFlow\    input/ output/
│       ├── KingTestMaker\ input/ output/
│       ├── Dooly\        input/ output/
│       └── CheckFlow\    input/ output/
├── 01_KingTestMaker\
├── 02_PrintFlow\
├── 03_Dooly\
└── 04_CheckFlow\
```

---

## 6. 다음 세션 첫 작업 (순서 엄수)

```
Phase B — 콘텐츠 고도화

① PrintFlow 콘텐츠 고도화
   guide_PrintFlow.md 보강
   rule_PrintFlow.md 작성
   faq_PrintFlow.md 보강
   → Regression PASS 확인

② KingTestMaker
   rule_KingTestMaker.md 정리
   faq_KingTestMaker.md 정리
   → Regression PASS 확인

③ Dooly
   rule_Dooly.md 정리
   faq_Dooly.md 정리
   → Regression PASS 확인

④ CheckFlow Guide 설계
   앱 정보 수집 → guide_CheckFlow.md 작성

⑤ v2.x 준비
   SSOT 자동 분류 엔진 설계
```

---

## 7. Stable 이후 운영 원칙

```
✅ 허용
   Bug Fix
   Renderer 개선
   UI 개선
   콘텐츠 고도화 (guide / rule / faq / reference 수정)

❌ 불허
   신규 기능 추가
   관리자 기능
   데이터 저장 기능
   SSOT 자동 수정 기능

새로운 기능은 v2.x에서만 개발한다.
Generator는 읽기 전용 Documentation Tool을 유지한다.
```

---

## 8. 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(10_HANDOVER_v1.1.md) 첨부
3. 입력:
   첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.

검증 질문:
- "현재 Generator 상태는?"
- "현재 단계(Phase)는?"
- "다음에 할 작업은?"
- "Renderer N/A 처리 기준은?"
- "되돌리지 말아야 할 결정 3가지는?"
- "GuideBook의 정체성은?"
