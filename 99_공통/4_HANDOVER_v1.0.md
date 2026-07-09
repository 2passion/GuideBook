# 가이드북 생성기 — 인수인계 파일
파일명: 4_HANDOVER_v1.0.md
생성일시: 2026-07-06
이전 파일: 3_HANDOVER_v1.0.md

---

## 완성된 가이드북 현황

| 번호 | 앱 이름 | SOP | HTML 튜토리얼 | 버전 | 생성 방식 | 비고 |
|------|---------|:---:|:-------------:|------|-----------|------|
| 01 | KingTestMaker | ✅ | ✅ | v1.0 | 수동 | 샘플 내용 |
| 02 | PrintFlow | ✅ | ✅ | v1.0 | 자동(analyzer.py) | 실제 소스 91개 파일 분석 |
| 03 | Dooly | ✅ | ✅ | v1.0 | 수동 | 샘플 내용 |
| 04 | CheckFlow | 🔲 | 🔲 | — | — | 계획중 |

---

## 생성된 작업 파일 목록 (99_공통/)

| 순번 | 파일명 | 버전 | 설명 |
|------|--------|------|------|
| 1 | 1_구현계획서_v1.0.md | v1.0 | 최초 계획서 |
| 2 | 1_작업지시서_v1.0.md | v1.0 | 전체 구조 생성 |
| 3 | 2_작업지시서_v2.0.md | v2.0 | analyzer.py 추가 |
| 4 | 3_작업지시서_v3.0.md | v3.0 | 1+2 통합본 |
| 5 | 4_작업지시서_v3.1.md | v3.1 | 표 버그 + 역할탭 버그 수정 |
| 6 | 5_작업지시서_v3.2.md | v3.2 | PDF 저장 + SOP 버튼 상단 이동 |
| 7 | 6_작업지시서_v3.3.md | v3.3 | 튜토리얼 이미지 드래그앤드롭 업로드 |
| — | 시행착오_기록.md | 누적 | 7건 기록 |
| — | 워크플로우_가이드.md | v1.3 | 누적 이력 관리 방식 |
| — | 4_SYSTEM_PROMPT_v4.0.md | v4.0 | 현재 Claude 프로젝트 지침 |

---

## 구현 완료된 파일 현황 (GuideBook_생성기/)

```
GuideBook_생성기/
├── GuideBook_Generator.bat   ✅ 7개 메뉴
│                                 1.SOP생성 2.튜토리얼생성 3.둘다
│                                 4.소스분석 5.분석+생성 6.입력폴더 7.출력폴더
├── generator.py              ✅ 18KB
│   기능:
│   - md_to_html() 마크다운→HTML 변환 (표 포함)
│   - 역할 탭 분리 (강사/조교 키워드 자동 감지)
│   - 상단 sticky 헤더 (인쇄+PDF 버튼)
│   - PDF 저장 (document.title 자동 입력)
│   - 드래그앤드롭 이미지 업로드 (localStorage 저장)
│   - 이미지 ✕ 삭제 + 🗑️ 전체 초기화
│   - 기존 파일 archive/ 자동 백업
├── analyzer.py               ✅ 6KB
│   기능:
│   - 소스 폴더 경로 + 분석 폴더 목록 입력
│   - 지원 확장자: md/txt/html/js/jsx/py/bat/sql/css/json
│   - 파일 1개당 최대 500줄
│   - 인코딩: UTF-8 → CP949 순으로 시도
│   - guide.md 자동 생성
├── README.md                 ✅
├── apps/
│   ├── KingTestMaker/input/output/  ✅
│   ├── PrintFlow/input/output/      ✅ (output: 파일 3개)
│   │   └── input/images/            ✅ (스크린샷 8장 보관 예정)
│   ├── Dooly/input/output/          ✅
│   └── CheckFlow/input/output/      ✅ (빈 폴더)
├── templates/                ✅
└── archive/                  ✅
```

---

## PrintFlow 최종 결과물

| 파일 | 크기 | 주요 기능 |
|------|------|-----------|
| PrintFlow_SOP_v1.0.md | 4KB | 실제 내용 포함 |
| PrintFlow_SOP_v1.0.html | 7KB | 상단헤더+인쇄+PDF+표렌더링 |
| PrintFlow_튜토리얼_v1.0.html | 21KB | 조교/강사탭+이미지업로드+PDF |

---

## 앱별 소스 폴더 경로

| 앱 | 소스 경로 | 분석 폴더 |
|----|-----------|-----------|
| KingTestMaker | C:\Obsidian\복테메이커\ | docs, electron, html, log |
| PrintFlow | C:\Obsidian\PrintFlow\ | Archive, command, log, MVP, sync, WORK, 배포 |
| Dooly | C:\Obsidian\Dooly\ | 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs |

---

## 시행착오 기록 요약 (7건)

| 번호 | 제목 | 상태 |
|------|------|------|
| 001 | BAT vs PWA 방식 결정 | ✅ |
| 002 | 폴더명 단축 | ✅ |
| 003 | BAT 정적 메뉴 → 동적 스캔 | ✅ |
| 004 | SOP HTML 표 깨짐 | ✅ |
| 005 | 튜토리얼 역할 탭 없음 | ✅ |
| 006 | tutorialPDF f-string 치환 | ✅ |
| 007 | SOP 버튼 위치 하단→상단 | ✅ |

---

## 다음 채팅에서 할 것

- [ ] BAT 파일 실행 테스트 (GuideBook_Generator.bat 더블클릭)
- [ ] KingTestMaker 소스 분석 → 실제 내용 가이드북 생성
- [ ] Dooly 소스 분석 → 실제 내용 가이드북 생성
- [ ] PrintFlow 튜토리얼 이미지 업로드 테스트 (드래그앤드롭)
- [ ] 02_PrintFlow/, 01_KingTestMaker/, 03_Dooly/ 폴더 최종 가이드북 복사
- [ ] CheckFlow 앱 정보 수집 → 가이드북 작성
- [ ] 최종 버전 A(개발자용) + 버전 B(사용자용) 생성

---

## 사용자 선호 / 특이사항

- 튜토리얼 형태 강하게 선호 (단계별 이전/다음 버튼)
- SOP와 튜토리얼 버튼 위치·스타일 통일 선호
- 작업지시서는 Claude Code에 바로 붙여넣기 가능한 형태
- 파일명 규칙 엄수: {순번}_{내용}_v{버전}
- 시행착오_기록.md, 워크플로우_가이드.md 는 누적 관리
- 방식A(HTML 드래그앤드롭) 먼저, 나중에 방식B(BAT+재생성) 추가 예정
- 채팅이 길어지면 인수인계 파일 먼저 생성 후 새 채팅 이동

---

## 새 채팅 시작 방법

1. claude.ai → **가이드북 생성기 프로젝트** 열기
2. 이 파일(`4_HANDOVER_v1.0.md`) 첨부
3. 입력:
```
첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.
```

---

## Claude Code 빠른 시작 명령어

```
cd C:\Obsidian\GuideBook\GuideBook_생성기

# BAT 실행 테스트
GuideBook_Generator.bat

# KingTestMaker 소스 분석 + 가이드북 생성
python analyzer.py KingTestMaker "C:\Obsidian\복테메이커" "docs,electron,html,log"
python generator.py KingTestMaker both

# Dooly 소스 분석 + 가이드북 생성
python analyzer.py Dooly "C:\Obsidian\Dooly" "00_System,01_Project,docs,api"
python generator.py Dooly both
```
