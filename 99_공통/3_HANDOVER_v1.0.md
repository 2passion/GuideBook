# 가이드북 생성기 — 인수인계 파일
파일명: 3_HANDOVER_v1.0.md
생성일시: 2026-07-06
이전 파일: 2_HANDOVER_v1.0.md (2 HANDOVER.md)

---

## 완성된 가이드북 현황

| 번호 | 앱 이름 | SOP | HTML 튜토리얼 | 버전 | 생성 방식 | 비고 |
|------|---------|:---:|:-------------:|------|-----------|------|
| 01 | KingTestMaker | ✅ | ✅ | v1.0 | 수동 | 샘플 내용 |
| 02 | PrintFlow | ✅ | ✅ | v1.0 | 자동(analyzer.py) | 실제 소스 91개 파일 분석 |
| 03 | Dooly | ✅ | ✅ | v1.0 | 수동 | 샘플 내용 |
| 04 | CheckFlow | 🔲 | 🔲 | — | — | 계획중 |

---

## 생성된 작업 파일 목록

| 순번 | 파일명 | 버전 | 설명 |
|------|--------|------|------|
| 1 | 1_구현계획서_v1.0.md | v1.0 | 최초 계획서 |
| 2 | 1_작업지시서_v1.0.md | v1.0 | 전체 구조 생성 (1번) |
| 3 | 2_작업지시서_v2.0.md | v2.0 | analyzer.py 추가 (2번) |
| 4 | 3_작업지시서_v3.0.md | v3.0 | 1+2 통합본 |
| 5 | 4_작업지시서_v3.1.md | v3.1 | 표 버그 + 역할탭 버그 수정 |
| 6 | 5_작업지시서_v3.2.md | v3.2 | PDF 저장 + SOP 버튼 상단 이동 |
| 7 | 시행착오_기록.md | 누적 | 7건 기록 |
| 8 | 4_SYSTEM_PROMPT_v4.0.md | v4.0 | 현재 Claude 프로젝트 지침 |

---

## 구현 완료된 파일 (GuideBook_생성기/)

```
GuideBook_생성기/
├── GuideBook_Generator.bat   ✅ 7개 메뉴 (소스분석 4·5번 포함)
├── generator.py              ✅ SOP + 튜토리얼 생성
│                                 - md_to_html() 표 변환
│                                 - 역할 탭 분리 (강사/조교)
│                                 - 상단 sticky 헤더 버튼
│                                 - PDF 저장 기능
├── analyzer.py               ✅ 소스 폴더 분석 → guide.md 자동 생성
├── README.md                 ✅
├── apps/
│   ├── KingTestMaker/input/output/  ✅
│   ├── PrintFlow/input/output/      ✅ (output에 파일 3개)
│   ├── Dooly/input/output/          ✅
│   └── CheckFlow/input/output/      ✅ (빈 폴더)
├── templates/sop_template.html      ✅
├── templates/tutorial_template.html ✅
└── archive/                         ✅
```

---

## 앱별 소스 폴더 경로 (analyzer.py 자동 매핑)

| 앱 | 소스 경로 | 분석 폴더 |
|----|-----------|-----------|
| KingTestMaker | C:\Obsidian\복테메이커\ | docs, electron, html, log |
| PrintFlow | C:\Obsidian\PrintFlow\ | Archive, command, log, MVP, sync, WORK, 배포 |
| Dooly | C:\Obsidian\Dooly\ | 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs |

---

## 이번 채팅 완료 내용

- [x] GuideBook 전체 폴더 구조 생성
- [x] generator.py 구현 (SOP + 튜토리얼)
- [x] analyzer.py 구현 (소스 분석)
- [x] GuideBook_Generator.bat 구현 (7개 메뉴)
- [x] PrintFlow 소스 분석 → guide.md 자동 생성 (91개 파일)
- [x] PrintFlow SOP·튜토리얼 HTML 생성 확인
- [x] 버그 수정 3건 (표 깨짐, 역할탭, f-string)
- [x] PDF 저장 기능 추가
- [x] SOP 버튼 상단 이동
- [x] 시행착오 기록 7건 작성

---

## 다음 채팅에서 할 것

- [ ] BAT 파일 실행 테스트 (GuideBook_Generator.bat 더블클릭)
- [ ] KingTestMaker 소스 분석 (C:\Obsidian\복테메이커\ → analyzer.py)
- [ ] Dooly 소스 분석 (C:\Obsidian\Dooly\ → analyzer.py)
- [ ] 01_KingTestMaker/, 03_Dooly/ 폴더에 실제 내용 가이드북 생성
- [ ] CheckFlow 앱 정보 수집 → 가이드북 작성
- [ ] 최종 버전 A(개발자용) + 버전 B(사용자용) 생성

---

## 사용자 선호 / 특이사항

- 튜토리얼 형태 강하게 선호 (단계별 이전/다음 버튼 방식)
- SOP와 튜토리얼 버튼 위치·스타일 통일 선호
- 작업지시서는 Claude Code에 바로 붙여넣기 가능한 형태로 작성
- 시행착오 발생 시 즉시 기록 요청
- 파일명 규칙 엄수: {순번}_{내용}_v{버전}
- 소스 분석 자동화 방식 적극 활용

---

## 새 채팅 시작 방법

1. claude.ai → 가이드북 생성기 프로젝트 열기
2. 이 파일(`3_HANDOVER_v1.0.md`) 첨부
3. 입력:
   "첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게."

---

## Claude Code 빠른 시작

```
cd C:\Obsidian\GuideBook\GuideBook_생성기

# BAT 실행 테스트
GuideBook_Generator.bat

# KingTestMaker 소스 분석
python analyzer.py KingTestMaker "C:\Obsidian\복테메이커" "docs,electron,html,log"

# Dooly 소스 분석
python analyzer.py Dooly "C:\Obsidian\Dooly" "00_System,01_Project,docs,api"
```
