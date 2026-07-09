# 가이드북 생성기 — 인수인계 파일
파일명: 9_HANDOVER_v1.0.md
작성일: 2026-07-09
이전 파일: 8_HANDOVER_v1.0.md

Generator Version: v3.10
Handover Version: v1.0

---

## 1. 이번 세션 요약

이번 세션에서 완료한 핵심 작업:

```
① 입력 파일명 표준화 (v3.10)
   guide.md → guide_{AppName}.md
   rule.md  → rule_{AppName}.md
   faq.md   → faq_{AppName}.md
   reference_{AppName}.md (optional 신규 추가)

② guide 경량화
   KingTestMaker: 2,065KB → 2KB (신규직원용 최소 문서)
   Dooly: 95KB → 3KB (업무 중심 구조로 재작성)

③ Renderer 조건부 N/A 정책 도입
   입력 원문에 해당 문법 없음 → N/A (PASS 유지)
   입력에 있는데 출력에 없음 → FAIL
   수평선(<hr>)은 항상 검사

④ 시행착오_기록.md #011 추가
```

---

## 2. RC Exit Criteria 현황

```
✅ Regression PASS        (v3.8.1)
✅ PDF 출력 PASS          (v3.9)
✅ PrintFlow PASS         (15/0/1)
✅ KingTestMaker PASS     (11/0/4)
✅ Dooly PASS             (11/0/4)
□ HANDOVER 검증          ← 지금 이것
```

---

## 3. 완료된 작업 목록

| 작업 | 버전 | 결과 |
|------|------|------|
| 입력 파일명 표준화 | v3.10 | ✅ 3개 앱 rename 완료 |
| generator.py 수정 | v3.10 | ✅ 새 파일명 읽기 |
| analyzer.py 수정 | v3.10 | ✅ 새 파일명 출력 |
| GuideBook_Generator.bat 수정 | v3.10 | ✅ 새 앱 생성 시 파일명 반영 |
| guide_KingTestMaker.md 경량화 | v1.0 | ✅ 신규직원용 최소 문서 |
| guide_Dooly.md 경량화 | v1.0 | ✅ 업무 중심 구조 |
| Renderer 조건부 N/A 정책 | v3.10 | ✅ 3개 앱 PASS |
| 시행착오_기록.md #011 | — | ✅ 적용 범위 포함 |

---

## 4. 발견된 문제 및 해결

**문제:** guide 경량화 후 KingTestMaker/Dooly Renderer FAIL

```
원인: 입력 원문에 코드블록/H4/인라인코드 없음
      → Renderer가 필수 태그로 검사하여 3건 FAIL

해결: 입력 원문에 해당 문법이 없으면 N/A 처리
      입력에 있는데 출력에 없으면 FAIL 유지
      수평선(<hr>)은 항상 검사

결과:
  PrintFlow     PASS 15 / 0 / 1
  KingTestMaker PASS 11 / 0 / 4
  Dooly         PASS 11 / 0 / 4
```

> 시행착오_기록.md #011 참고

---

## 5. 이번 세션 핵심 교훈 (번복 금지)

```
① guide는 신규직원용 최소 문서다.
   SOP는 상세 업무 매뉴얼이다.
   Tutorial은 화면 중심 학습 자료다.
   → 역할이 다르므로 guide에 모든 내용을 넣지 않는다.

② guide 표준 구조 (전 앱 공통):
   앱 개요 → 업무 흐름 → 업무①~ → 자주 하는 실수 → FAQ

③ 입력 파일명 규칙 (확정):
   {type}_{AppName}.md
   type: guide / rule / faq / reference
   AppName: PascalCase (PrintFlow / KingTestMaker / Dooly / CheckFlow)

④ Regression 정책 (확정):
   입력에 없으면 N/A
   입력에 있는데 출력에 없으면 FAIL
   N/A는 FAIL이 아니다.
```

---

## 6. 앱별 현황

| 번호 | 앱 | SOP | Tutorial | Regression | guide 크기 |
|------|-----|:---:|:--------:|------------|-----------|
| 01 | PrintFlow | ✅ | ✅ | PASS 15/0/1 | 3KB |
| 02 | KingTestMaker | ✅ | ✅ | PASS 11/0/4 | 2KB |
| 03 | Dooly | ✅ | ✅ | PASS 11/0/4 | 3KB |
| 04 | CheckFlow | 🔲 | 🔲 | — | — |

---

## 7. 주요 파일 경로

| 파일 | 경로 |
|------|------|
| generator.py | `C:\Obsidian\GuideBook\GuideBook_생성기\generator.py` |
| analyzer.py | `C:\Obsidian\GuideBook\GuideBook_생성기\analyzer.py` |
| PrintFlow input | `apps\PrintFlow\input\` |
| KingTestMaker input | `apps\KingTestMaker\input\` |
| Dooly input | `apps\Dooly\input\` |
| 시행착오_기록.md | `99_공통\시행착오_기록.md` |

---

## 8. 다음 세션 첫 작업 (순서 엄수)

```
① HANDOVER 검증 (지금 이것)
   - "현재 RC Exit Criteria 상태는?"
   - "다음에 할 작업은?"
   - "Regression 판정 기준은?"

② 검증 PASS 확인

③ git commit
   fix: conditional N/A renderer regression

④ git commit
   docs: troubleshooting record #011

⑤ GuideBook Generator Stable v1.1 선언

⑥ git tag v1.1 && git push origin v1.1
```

---

## 9. 새 채팅 시작 방법

1. claude.ai → **가이드북 생성기 프로젝트** 열기
2. 이 파일(`9_HANDOVER_v1.0.md`) 첨부
3. 입력:
```
첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.
```

**검증 질문:**
- "현재 RC Exit Criteria 상태는?"
- "다음에 할 작업은?"
- "Renderer N/A 처리 기준은?"
