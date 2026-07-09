# GuideBook Generator

학원 앱 가이드북(SOP + HTML 튜토리얼) 자동 생성 도구

## 실행 방법
GuideBook_Generator.bat 더블클릭

## 메뉴 구조
1단계: 가이드북 생성 / 앱 관리 / 설정 / 종료
2단계 (가이드북 생성): apps/ 폴더 자동 스캔 → 앱 목록 표시

## 가이드북 생성 방식 2가지
방식 A — 수동: apps/{앱}/input/guide.md 직접 작성 → 1/2/3번 메뉴 실행
방식 B — 자동: 실제 소스 폴더를 읽어 guide.md 자동 생성 → 4/5번 메뉴 실행

## 앱별 소스 경로 (방식 B)
| 앱 | 소스 경로 | 분석 폴더 |
|-----|-----------|-----------|
| KingTestMaker | C:\Obsidian\복테메이커\ | docs, electron, html, log |
| PrintFlow | C:\Obsidian\PrintFlow\ | Archive, command, log, MVP, sync, WORK, 배포 |
| Dooly | C:\Obsidian\Dooly\ | 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs |

## 새 앱 추가
앱 관리 → 새 앱 생성 → 이름 입력 → apps/{이름}/ 자동 생성

## Python 확인
python --version  (3.8 이상 필요)
