# Phase B 표준 실행 템플릿 v1.0
# PrintFlow 코드 체계 통일

---

작업 루트:
C:\Obsidian\GuideBook\GuideBook_생성기

먼저 아래 작업지시서를 읽고 작업을 수행한다.

C:\Obsidian\GuideBook\99_공통\21_작업지시서_v1.0.md

---

## 작업 원칙

- 작업지시서를 먼저 읽고 이해한 후 작업한다.
- Feature Freeze를 유지한다.
- generator.py 수정 금지
- analyzer.py 수정 금지
- SSOT 원칙 유지 (코드 체계 교체, 내용 삭제 아님)
- Generator Regression 기준은 변경하지 않는다.

---

## 작업 내용

1. reference_PrintFlow.md 수정
   저장 위치: apps/PrintFlow/input/reference_PrintFlow.md

   1-1. 자료 분류 코드 교체
        구 코드(01~09) → 신 코드(A/B/C/D 대분류 + 하위번호)
        대분류:
          A 교재(Book)
          B 프린트(Print)
          C 시험대비(Exam)
          D 성취도(Level)
        코드표:
          A-01 교재 원본 자료
          A-02 복습 테스트(복테)
          A-03 학생별 오답노트
          B-01 숙제 출력 자료
          B-02 테스트 출력 자료
          C-01 내신대비 모의고사
          C-02 기출 자료
          D-01 진단평가
          D-02 입학테스트

   1-2. 교재 코드 교체
        구 코드(a~m) → 신 코드(grade/step 체계)
        학년별 grade: grade-a 초등 / grade-b 중등 / grade-c 고등
        단계별 step:  step-a 개념서 / step-b 유형서 / step-c 심화서
                      step-d 모의고사 / step-e 기출
        교재 목록 (grade-a_step-a 형식으로 작성):
          grade-a_step-a  기본+응용  초등 개념서
          grade-a_step-b  쎈         초등 유형서
          grade-a_step-c  최상위S    초등 심화서
          grade-b_step-a  개념+유형  중등 개념서
          grade-b_step-b  쎈         중등 유형서
          grade-b_step-c  일품       중등 심화서
          grade-b_step-c  블랙라벨   중등 심화서
          grade-b_step-d  내신모의   중등 모의고사
          grade-b_step-e  기출       중등 기출
          grade-c_step-a  개념원리   고등 개념서
          grade-c_step-b  쎈         고등 유형서
          grade-c_step-b  마플시너지 고등 유형서
          grade-c_step-c  일품       고등 심화서
          grade-c_step-c  올림포스 고난도  고등 심화서
          grade-c_step-c  고쟁이     고등 심화서
          grade-c_step-c  블랙라벨   고등 심화서
          grade-c_step-d  자이스토리(고1)  고등 모의고사
          grade-c_step-d  자이스토리(고2)  고등 모의고사
          grade-c_step-e  너기출     고등 기출
          grade-c_step-e  자이스토리(고3)  고등 기출

   1-3. 폴더 구조 / 과정 코드
        수정하지 않는다.

2. rule_PrintFlow.md 수정
   저장 위치: apps/PrintFlow/input/rule_PrintFlow.md

   검사 규칙 교체
   구 코드(A-01~B-09) → 신 코드(Mark-A/B 체계)

   Mark-A. 숙제 검사 대상:
     Mark-A_A-01 교재 검사
     Mark-A_A-02 복테 검사
     Mark-A_A-03 오답노트 검사
     Mark-A_B-01 숙제 프린트 검사
     Mark-A_C-01 내신모의 검사
     Mark-A_C-02 기출 검사

   Mark-B. 테스트 검사 대상:
     Mark-B_B-02 테스트 프린트 검사
     Mark-B_C-01 내신모의 검사
     Mark-B_C-02 기출 검사
     Mark-B_D-01 진단평가 검사
     Mark-B_D-02 입학테스트 검사

3. guide_PrintFlow.md
   수정하지 않는다.

4. faq_PrintFlow.md
   수정하지 않는다.

5. Regression 실행
   python generator.py PrintFlow both

---

## 완료 후 보고 형식

1. 수정된 파일 목록
2. reference 변경 사항
   - 자료 분류 코드 (Before / After)
   - 교재 코드 (Before / After)
   - 폴더 구조 / 과정 코드 변경 여부
3. rule 변경 사항
   - 검사 규칙 (Before / After)
4. guide / faq 변경 여부
5. Regression 결과
   - Core
   - Renderer
   - App
   - Overall
6. PASS / FAIL / N/A Summary
7. 특이사항
8. 권장 사항 (선택)
   작업 중 발견한 개선 아이디어가 있으면
   기능 추가가 아니라 콘텐츠 개선 관점에서만
   1~3개 제안
