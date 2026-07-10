# 33_작업지시서_v1.0
**Dooly Phase B — Document Set 검토 및 정비**
작성일: 2026-07-10 | 대상 앱: Dooly

---

## 공통 원칙

```
- 이 작업지시서를 먼저 읽고 수행할 것
- Feature Freeze 유지
- generator.py 수정 금지
- analyzer.py 수정 금지
- SSOT 원칙 유지 (입력 파일만 수정)
- Generator Regression 기준 변경 금지
```

---

## 작업 목적

Dooly의 guide / rule / faq 파일을 PrintFlow Baseline 기준으로 검토하고,
역할 분리 및 콘텐츠 보완을 통해 KingTestMaker와 동일한 Document Set 구조를 완성한다.

---

## 검토 기준 (PrintFlow Baseline 6가지)

```
1. guide    신규 조교 5분 업무 시작 가능한가
2. rule     운영 규칙만 있는가 / 코드표는 reference 분리 가능한가
3. faq      실제 업무 질문만 있는가
4. reference 코드표 / 분류 체계만 있는가 (optional)
5. Document Set 중복 없는가
6. Regression 기준 유지하는가
```

---

## 작업 순서

```
① guide_Dooly.md 검토
   → 업무 흐름만 남기는가
   → rule / faq 성격 내용이 혼재하지 않는가

② rule_Dooly.md 검토
   → 미작성("추후 작성") 여부 확인
   → 운영 규칙만 포함하는가

③ faq_Dooly.md 검토
   → 미작성("추후 작성") 여부 확인
   → 실제 업무 문제 해결 내용인가

④ reference 필요 여부 판단
   → Dooly에 코드표 / 분류 체계가 있는가

⑤ PrintFlow Baseline 기준 종합 분석
   → 6가지 기준 판정표 작성

⑥ 작업지시서 작성 (34번~)
   → 필요한 수정 항목별 작업지시서 작성

⑦ Claude Code 실행 (34번~)

⑧ Regression PASS 확인
   python generator.py Dooly both

⑨ Commit & Push
   29_Git_Commit_Workflow_v1.0.md 기준 적용
```

---

## 현재 Regression 기준선

```
Dooly  PASS 11 / FAIL 0 / N/A 4
```

작업 완료 후 이 기준선 유지 여부 확인 필수.

---

## 완료 보고 형식

```
수정 파일    : guide / rule / faq _Dooly.md (해당 파일만)
변경 사항    : 항목별 기술
Regression  :
  Core      PASS/FAIL
  Renderer  PASS/FAIL
  App       PASS/FAIL
  Overall   PASS/FAIL
  PASS / FAIL / N/A Summary
특이사항     : 없으면 "없음"
```

---

## 참고 — KingTestMaker 완료 사례

```
guide  "자주 하는 실수" + "FAQ" 제거 → 업무만 유지
rule   "(추후 작성)" → 운영 규칙 3개 섹션 신규 작성 ("~합니다" 문체)
faq    "(추후 작성)" → 자주 하는 실수 표 + FAQ 이동
```

Rule 문체 기준:
```
✅ "~합니다" 형태
❌ "~한다" 형태 사용 금지
```
