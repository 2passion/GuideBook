# GuideBook Generator - AI 인수인계 (Generator 안정화 완료)

작성일 : 2026-07-06
상태 : Generator v3.6 안정화 단계

---

# 1. 프로젝트 목적

GuideBook Generator는 각 프로젝트의 문서를 자동 생성하는 도구이다.

입력

guide.md
rule.md
faq.md
images/

↓

Generator

↓

SOP (HTML + MD)

↓

Tutorial (HTML)

↓

Dooly (조교 지식베이스)

Generator는 문서를 생성하는 역할만 담당한다.

---

# 2. SSOT 원칙 (가장 중요)

입력 Markdown이 SSOT이다.

guide.md
rule.md
faq.md

Generator는

읽기(Read)

↓

생성(Generate)

만 수행한다.

절대로 자동으로

guide.md

rule.md

faq.md

를 수정하지 않는다.

Markdown 수정은

작업지시서에 명시된 경우만 허용한다.

---

# 3. 현재 입력 구조

apps/

AppName/

input/

guide.md
→ 사용법

rule.md
→ 업무규칙

faq.md
→ FAQ

images/

↓

output/

SOP.html
SOP.md
Tutorial.html

---

# 4. 현재 Generator 구현 완료

완료

✓ analyzer.py

✓ generator.py

✓ read_input_files()

✓ guide/rule/faq 병합

✓ classify_sections()

✓ SOP 생성

✓ Tutorial 생성

✓ HTML 생성

✓ archive 자동백업

✓ guide/rule/faq 자동 분리

✓ SOP 탭 구조

Guide

Rule

FAQ

---

# 5. 현재 PrintFlow 검증 결과

정상

✓ guide

✓ rule

✓ faq

자동 분리

✓ FAQ 중복 제거

✓ SOP 생성

✓ Tutorial 생성

✓ HTML 생성

✓ PDF 버튼

✓ archive

정상

---

# 6. 현재 발견된 개선점

Priority 1

Markdown Renderer 개선

현재 미지원

- 코드블록
- H4
- ---
- 인라인 코드

추가 예정

```
``` → <pre><code>

--- → <hr>

#### → h4

`text`
```

---

Priority 2

Sticky Tab

현재

Top Bar만 sticky

추천

Top Bar

+

Tab Bar

둘 다 sticky

---

Priority 3

PDF 출력

현재

활성 탭만 출력

추천

인쇄 시

Guide

↓

Rule

↓

FAQ

순서대로 모두 출력

---

Priority 4

Regression Check

Generator 완료 후

자동 출력

□ guide 읽음

□ rule 읽음

□ faq 읽음

□ SOP 생성

□ Tutorial 생성

□ HTML 생성

□ PDF 생성

□ 오류 없음

---

# 7. 지금 하지 않는 것

Generator에 넣지 않는다.

✗ 자료 분류 코드 편집기

✗ localStorage

✗ 폴더 경로 저장

✗ 관리자 기능

이 기능들은

PrintFlow 또는 CheckFlow 관리자 기능에서 구현한다.

Generator는 읽기 전용 Documentation Tool을 유지한다.

---

# 8. 현재 우선순위

Phase A

Generator 안정화

□ Markdown Renderer 개선

□ Sticky Tab

□ PDF 전체 출력

↓

Phase B

실사용 검증

PrintFlow

↓

KingTestMaker

↓

Dooly

↓

문제 발견

↓

Generator 수정

↓

반복

↓

Generator 안정화

↓

Phase C

CheckFlow

여기서

메타데이터

RAG

Supabase

검색

작업지시서 자동생성

Claude Prompt 자동생성

등을 구현한다.

---

# 9. 작업지시서 작성 규칙

모든 작업지시서는 아래 메타데이터를 가진다.

Project:
App:
Type:
Priority:
Version:
Status:

또한

맨 아래

Regression Check를 추가한다.

---

# 10. 다음 작업

1.

Markdown Renderer 개선

우선순위

① 코드블록

② hr

③ h4

④ 인라인 코드

↓

2.

Sticky Tab

↓

3.

PDF 전체 출력

↓

4.

PrintFlow Tutorial 검증

↓

5.

KingTestMaker 실제 Guide 생성

↓

6.

Dooly 실제 Guide 생성

↓

7.

Generator 안정화 완료

↓

8.

CheckFlow 개발 시작