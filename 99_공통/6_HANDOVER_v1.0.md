# 가이드북 생성기 — 인수인계 파일
파일명: 6_HANDOVER_v1.0.md
생성일시: 2026-07-07
이전 파일: 5_HANDOVER_v1.0.md

Generator Version: v3.6
Handover Version: v1.0
Last Verified: 2026-07-06

---

## 1. 프로젝트 목적

GuideBook Generator는 각 앱의 문서를 자동 생성하는 도구다.

```
guide.md + rule.md + faq.md + images/
        ↓
   Generator
        ↓
SOP (HTML + MD) + Tutorial (HTML)
        ↓
   Dooly (조교 지식베이스)
```

Generator는 읽기(Read) → 생성(Generate)만 수행한다.

---

## 2. SSOT 원칙 (가장 중요)

입력 Markdown이 SSOT다.

- guide.md → 사용법
- rule.md  → 업무규칙
- faq.md   → FAQ

**Markdown 수정은 작업지시서에 명시된 경우만 허용.**
Generator는 절대로 자동으로 입력 파일을 수정하지 않는다.

---

## 3. 현재 입력/출력 구조

```
apps/
└── {AppName}/
    ├── input/
    │   ├── guide.md
    │   ├── rule.md
    │   ├── faq.md
    │   └── images/
    └── output/
        ├── {App}_SOP_v1.0.html
        ├── {App}_SOP_v1.0.md
        └── {App}_튜토리얼_v1.0.html
```

---

## 4. 완료된 기능

```
✓ analyzer.py               소스 폴더 분석 → guide.md 자동 생성
✓ generator.py              guide/rule/faq 읽기 → SOP + Tutorial 생성
✓ read_input_files()        guide.md + rule.md + faq.md 자동 병합
✓ classify_sections()       guide/rule/faq 섹션 자동 분류
✓ SOP 생성                  HTML + MD
✓ Tutorial 생성             슬라이드 멀티 이미지 + localStorage
✓ SOP 탭 구조               가이드 / 업무규칙 / FAQ 탭
✓ FAQ 중복 제거             guide.md 중복 섹션 제거
✓ archive 자동 백업
✓ PDF 버튼
✓ PrintFlow 검증 완료
```

---

## 5. 현재 진행 중 (Phase A — Generator 안정화)

```
□ A-1. Markdown Renderer 개선
        코드블록(```) → <pre><code>
        수평선(---) → <hr>
        H4(####) → <h4>
        인라인 코드(`text`) → <code>
        작업지시서: 12_작업지시서_v3.7.md

□ A-2. Sticky Tab
        Top Bar + Tab Bar 둘 다 sticky
        작업지시서: 12_작업지시서_v3.7.md (A-1과 묶음)

□ A-3. PDF 전체 출력
        현재: 활성 탭만 출력
        목표: 인쇄 시 Guide → Rule → FAQ 순서 전체 출력
```

---

## 6. 다음 작업 (실행 순서)

```
1. 12_작업지시서_v3.7 실행
   → Markdown Renderer 개선 + Sticky Tab

2. 13_작업지시서_v3.8 작성 + 실행
   → PDF 전체 출력 개선

3. PrintFlow Tutorial 검증
   → python generator.py PrintFlow tutorial

4. KingTestMaker 실제 가이드북 생성
   → python analyzer.py KingTestMaker "C:\Obsidian\복테메이커" "docs,electron,html,log"
   → python generator.py KingTestMaker both

5. Dooly 실제 가이드북 생성
   → python analyzer.py Dooly "C:\Obsidian\Dooly" "00_System,01_Project,docs,api"
   → python generator.py Dooly both

6. Generator 안정화 선언 (Phase A 완료)

7. CheckFlow 개발 시작 (Phase C)
```

---

## 7. 장기 계획 (Phase C — CheckFlow 단계에서 구현)

```
□ 메타데이터 스키마
□ 벡터DB / RAG
□ Supabase 연동
□ 검색 기능
□ 작업지시서 자동 생성
□ Claude Prompt 자동 생성
□ section_rules.json (FAQ/RULE 키워드 외부화)
□ toc.md 목차 자동 생성
□ core/ 폴더 분리 리팩터링
□ config.json 앱별 설정 파일
```

---

## 8. 금지 사항 (절대 넣지 않음)

```
✗ Generator에 자료 분류 코드 편집기 추가
✗ Generator에 localStorage 데이터 저장 기능 추가
✗ Generator에 폴더 경로 설정 기능 추가
✗ Generator에 관리자 기능 추가
✗ SSOT 자동 수정 (guide.md, rule.md, faq.md 자동 변경)
```

이 기능들은 PrintFlow 또는 CheckFlow 관리자 도구(v4.0)에서 구현한다.
Generator는 읽기 전용 Documentation Tool을 유지한다.

---

## 9. 프로젝트 진행률

| 항목 | 진행률 | 상태 |
|------|--------|------|
| GuideBook Generator | 90% | Phase A 진행 중 |
| PrintFlow 가이드북 | 85% | SOP 탭 구조 완료, Tutorial 검증 필요 |
| KingTestMaker 가이드북 | 20% | 샘플만 있음, 실제 소스 분석 필요 |
| Dooly 가이드북 | 20% | 샘플만 있음, 실제 소스 분석 필요 |
| CheckFlow 가이드북 | 0% | 미시작 |

---

## 10. 작업지시서 현황

| 순번 | 파일명 | 내용 | 상태 |
|------|--------|------|------|
| 1 | 1_작업지시서_v1.0 | 전체 구조 생성 | ✅ |
| 2 | 2_작업지시서_v2.0 | analyzer.py 추가 | ✅ |
| 3 | 3_작업지시서_v3.0 | 1+2 통합본 | ✅ |
| 4 | 4_작업지시서_v3.1 | 표 버그 + 역할탭 버그 수정 | ✅ |
| 5 | 5_작업지시서_v3.2 | PDF 저장 + SOP 버튼 상단 이동 | ✅ |
| 6 | 6_작업지시서_v3.3 | 튜토리얼 이미지 드래그앤드롭 | ✅ |
| 7 | (7번 없음) | 슬라이드 멀티 이미지 — 8번으로 기록 | — |
| 8 | 8_작업지시서_v3.5 | input 파일 분리 초안 | ✅ |
| 9 | 9_작업지시서_v3.5 | input 파일 분리 확정본 | ✅ |
| 10 | 10_작업지시서_v3.6 | SOP 탭+편집기 — 보류 | 🔲 미실행 |
| 11 | 11_작업지시서_v3.6 | SOP 탭 구조 (편집기 제거) | ✅ |
| 12 | 12_작업지시서_v3.7 | Markdown Renderer + Sticky Tab | ⬜ 대기 중 |

---

## 11. 앱별 소스 경로

| 앱 | 소스 경로 | 분석 폴더 |
|----|-----------|-----------|
| KingTestMaker | C:\Obsidian\복테메이커\ | docs, electron, html, log |
| PrintFlow | C:\Obsidian\PrintFlow\ | Archive, command, log, MVP, sync, WORK, 배포 |
| Dooly | C:\Obsidian\Dooly\ | 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs |

---

## 12. 새 채팅 시작 방법

1. claude.ai → **가이드북 생성기 프로젝트** 열기
2. 이 파일(`6_HANDOVER_v1.0.md`) 첨부
3. 입력:
```
첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.
```

