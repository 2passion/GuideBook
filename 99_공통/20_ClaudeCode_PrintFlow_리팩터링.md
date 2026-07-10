# Phase B 표준 실행 템플릿 v1.0
# PrintFlow 콘텐츠 리팩터링

---

작업 루트:
C:\Obsidian\GuideBook\GuideBook_생성기

먼저 아래 작업지시서를 읽고 작업을 수행한다.

C:\Obsidian\GuideBook\99_공통\20_작업지시서_v1.1.md

---

## 작업 원칙

- 작업지시서를 먼저 읽고 이해한 후 작업한다.
- Feature Freeze를 유지한다.
- generator.py 수정 금지
- analyzer.py 수정 금지
- SSOT 원칙 유지 (내용 삭제 금지, 역할 분리만 수행)
- Generator Regression 기준은 변경하지 않는다.

---

## 작업 내용

1. guide_PrintFlow.md 수정
   - 학생 등록 섹션을 맨 아래 "참고" 섹션으로 이동
   - 업무 중심 구조 유지
   - 나머지 내용 변경 금지

2. reference_PrintFlow.md 생성
   저장 위치: apps/PrintFlow/input/reference_PrintFlow.md
   이동할 내용 (rule_PrintFlow.md에서 그대로 복사):
   - 자료 분류 코드 (01~09)
   - 폴더 구조 표준 / 과정 코드
   - 교재 코드

3. rule_PrintFlow.md 수정
   아래 3개만 남긴다:
   - 파일 저장 원칙 (8가지)
   - 스캔 후 파일명 규칙 (숙제 / 테스트)
   - 검사 규칙 (A. 숙제 검사 / B. 테스트 검사)

4. faq_PrintFlow.md
   수정하지 않는다.

5. reference_PrintFlow.md 생성 확인
   - 파일 존재 여부 확인
   - 이동된 내용 정상 여부 확인

6. Regression 실행
   python generator.py PrintFlow both

---

## 완료 후 보고 형식

1. 수정된 파일 목록
2. reference_PrintFlow.md 생성 여부
3. guide 변경 사항 (Before / After)
4. rule 변경 사항 (Before / After)
5. faq 변경 여부
6. Regression 결과
   - Core
   - Renderer
   - App
   - Overall
7. PASS / FAIL / N/A Summary
8. 특이사항
9. 권장 사항 (선택)
   작업 중 발견한 개선 아이디어가 있으면
   기능 추가가 아니라 콘텐츠 개선 관점에서만
   1~3개 제안
