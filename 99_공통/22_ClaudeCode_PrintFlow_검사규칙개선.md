# Phase B 표준 실행 템플릿 v1.0
# PrintFlow 검사 규칙 네이밍 개선

---

작업 루트:
C:\Obsidian\GuideBook\GuideBook_생성기

먼저 아래 작업지시서를 읽고 작업을 수행한다.

C:\Obsidian\GuideBook\99_공통\22_작업지시서_v1.0.md

---

## 작업 원칙

- 작업지시서를 먼저 읽고 이해한 후 작업한다.
- Feature Freeze를 유지한다.
- generator.py 수정 금지
- analyzer.py 수정 금지
- SSOT 원칙 유지 (네이밍 개선, 내용 삭제 아님)
- Generator Regression 기준은 변경하지 않는다.

---

## 작업 내용

1. rule_PrintFlow.md 수정
   저장 위치: apps/PrintFlow/input/rule_PrintFlow.md

   검사 규칙 네이밍 교체:
   - 검사 구분 서두: Mark-A/Mark-B → HW/TEST
   - 숙제 검사 코드: Mark-A_X-XX → HW_X-XX
   - 테스트 검사 코드: Mark-B_X-XX → TEST_X-XX

   After 결과:
   ```
   검사는 숙제 검사(HW)와 테스트 검사(TEST) 두 가지로 구분한다.

   HW. 숙제 검사 대상
     HW_A-01 교재 검사
     HW_A-02 복테 검사
     HW_A-03 오답노트 검사
     HW_B-01 숙제 프린트 검사
     HW_C-01 내신모의 검사
     HW_C-02 기출 검사

   TEST. 테스트 검사 대상
     TEST_B-02 테스트 프린트 검사
     TEST_C-01 내신모의 검사
     TEST_C-02 기출 검사
     TEST_D-01 진단평가 검사
     TEST_D-02 입학테스트 검사
   ```

2. reference_PrintFlow.md
   수정하지 않는다.

3. guide_PrintFlow.md
   수정하지 않는다.

4. faq_PrintFlow.md
   수정하지 않는다.

5. Regression 실행
   python generator.py PrintFlow both

---

## 완료 후 보고 형식

1. 수정된 파일 목록
2. rule 변경 사항 (Before / After)
3. reference / guide / faq 변경 여부
4. Regression 결과
   - Core
   - Renderer
   - App
   - Overall
5. PASS / FAIL / N/A Summary
6. 특이사항
7. 권장 사항 (선택)
   작업 중 발견한 개선 아이디어가 있으면
   기능 추가가 아니라 콘텐츠 개선 관점에서만
   1~3개 제안
