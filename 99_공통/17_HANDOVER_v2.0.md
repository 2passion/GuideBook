# 가이드북 생성기 — 인수인계 파일
파일명: 17_HANDOVER_v2.0.md
작성일: 2026-07-12
이전 파일: 16_HANDOVER_v2.0.md (번호 충돌로 17로 변경)
성격: 구조 정비 완료 마일스톤 문서
목적: 새 AI가 5분 안에 프로젝트를 이어가기 위한 기준 문서

---

## 1. 프로젝트 상태

```
GuideBook Documentation Platform
Generator Stable Release v1.1

Status         : Stable Release v1.1
Feature Freeze : ON
Phase          : Phase B 완료 + 구조 정비 진행 중

GitHub : https://github.com/2passion/GuideBook
Branch : main
Tag    : v1.1
Commit : b1c9a4e (최신 — 42번 GuideBook_배포 구조 전환)
```

---

## 2. 최신 Git 이력

```
b1c9a4e  refactor: move deployment folders under GuideBook_배포
320375a  chore: remove CheckFlow scaffold and add candidate app registry
ecec3f9  docs: link commit reference for incident #012
db9135e  docs: standardize images management
2aeb308  docs: standardize deployment folders
b828a4d  docs: clarify CheckFlow as candidate app in handover v1.4
```

---

## 3. 현재 폴더 구조 (확정)

```
C:\Obsidian\GuideBook\
│
├── GuideBook_배포\          ← 배포 영역 (사용자용 HTML)
│   ├── 01_KingTestMaker\
│   │   ├── KingTestMaker_SOP_v1.0.html
│   │   └── KingTestMaker_튜토리얼_v1.0.html
│   ├── 02_PrintFlow\
│   │   ├── PrintFlow_SOP_v1.0.html
│   │   └── PrintFlow_튜토리얼_v1.0.html
│   └── 03_Dooly\
│       ├── Dooly_SOP_v1.0.html
│       └── Dooly_튜토리얼_v1.0.html
│
├── GuideBook_생성기\        ← 개발 영역 (SSOT + Generator)
│   ├── generator.py
│   ├── analyzer.py
│   ├── apps\
│   │   ├── KingTestMaker\  input/ output/
│   │   ├── PrintFlow\      input/ output/
│   │   └── Dooly\          input/ output/
│   ├── archive\
│   └── templates\
│
└── 99_공통\                 ← 운영 문서
    ├── 15_HANDOVER_v1.4.md
    ├── 17_HANDOVER_v2.0.md  ← 이 파일
    ├── 후보앱_목록.md
    ├── 8_SYSTEM_PROMPT_v5.0.md
    ├── 29_Git_Commit_Workflow_v1.0.md
    ├── 워크플로우_가이드.md
    ├── 시행착오_기록.md
    └── 작업지시서 39~42번
```

---

## 4. 역할 분리 원칙 (확정)

```
GuideBook_생성기\  = 개발 영역
  - SSOT (guide/rule/faq/reference Markdown)
  - Generator (generator.py, analyzer.py)
  - input\images\ = 유일한 이미지 저장 위치

GuideBook_배포\    = 배포 영역
  - 사용자용 HTML만 (SOP.html + 튜토리얼.html)
  - SOP.md 없음
  - 이미지 폴더 없음

99_공통\           = 운영 문서
  - HANDOVER / 작업지시서 / 워크플로우 / 시행착오
```

---

## 5. Phase B 앱 상태

| 앱 | Phase B | 커밋 | Regression |
|---|---|---|---|
| PrintFlow | ✅ 완료 (Reference) | ff72c33 | PASS 16/0/0 |
| KingTestMaker | ✅ 완료 | f43ad16 | PASS 11/0/4 |
| Dooly | ✅ 완료 | da01131 | PASS 11/0/4 |

---

## 6. 구조 정비 완료 항목

```
39번  배포 폴더 표준화 (HTML 전용)         ✅ 2aeb308
40번  images 표준화 (input\images\ 통일)   ✅ db9135e
41번  후보앱 구조 정리 (CheckFlow 삭제 + 후보앱_목록.md 생성)  ✅ 320375a
42번  GuideBook_배포 구조 전환             ✅ b1c9a4e
```

---

## 6-1. 현재 진행률

```
Phase B 콘텐츠 (PrintFlow/KingTestMaker/Dooly)  ✅ 100%
구조 정비 (39~42번)                              ✅ 100%
운영 문서 표준화 (43~45번)                        ▶ 진행 중
README 업데이트                                  ▶ 예정
v1.2 Tag                                        ▶ 예정
```

---

## 7. 후보 앱 관리

```
파일: 99_공통\후보앱_목록.md

운영 원칙:
  폴더 있음 = 개발 중
  폴더 없음 = 후보 (문서로만 관리)

현재 후보:
  CheckFlow — 미승인, 아이디어 단계

⚠️ 중요:
  CheckFlow는 프로젝트가 아니다.
  apps\CheckFlow\ 폴더 없음
  GuideBook_배포\04_CheckFlow\ 폴더 없음
  후보앱_목록.md 에서만 관리한다.
  새 AI는 CheckFlow를 개발 중인 앱으로 착각하지 않는다.
```

---

## 8. Input Standard (확정)

```
apps\{App}\input\
    ├── guide_{App}.md
    ├── rule_{App}.md
    ├── faq_{App}.md
    ├── reference_{App}.md  (optional)
    └── images\
        ├── .gitkeep
        └── README.txt
```

---

## 9. 시행착오 기록

```
#001~#011  Legacy 형식
#012       신규 표준 (### → #### 계층)
           PowerShell New-Item -LiteralPath 미지원
```

시행착오 Standard (#012부터):
```
### #NNN — 제목
#### 문제
#### 원인
#### 해결
#### 재발 방지
#### 적용 프로젝트
#### 관련 작업지시서
#### 관련 Commit
```

---

## 10. 되돌리지 말아야 할 결정

```
Feature Freeze ON — Phase B 기간 신규 기능 없음
SSOT 자동 수정 금지 — Generator는 Read → Generate만
배포 폴더 HTML 전용 — SOP.md / 이미지 폴더 없음
input\images\ 유일 — screenshots 등 별도 폴더 금지
폴더 있음 = 개발 중 — 후보는 문서로만 관리
CheckFlow 삭제 확정 — 후보앱_목록.md로 관리
```

---

## 11. 다음 세션 작업 순서

```
43번  작업지시서 템플릿 표준화 (유형 A~E 분리)
44번  워크플로우 가이드 v1.5 (Layer 구조)
45번  구현계획서 템플릿 개선
README 업데이트
  ↓
v1.2 Tag (Phase B + 구조 정비 완료)
```

---

## 12. 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(17_HANDOVER_v2.0.md) 첨부
3. 입력:
   첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.

### 검증 질문
- "현재 폴더 구조는?"
- "배포 영역과 개발 영역 차이는?"
- "다음 작업은?"
- "최신 커밋은?"
- "CheckFlow 상태는?"
- "되돌리지 말아야 할 결정은?"
