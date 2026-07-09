# 가이드북 생성기 — 인수인계 파일
파일명: 7_HANDOVER_v1.0.md
생성일시: 2026-07-08
이전 파일: 6_HANDOVER_v1.0.md

Generator Version: v3.9
Handover Version: v1.0
Last Verified: 2026-07-07

---

## 1. 프로젝트 목적

GuideBook Generator는 각 앱의 문서를 자동 생성하는 도구다.

```
guide.md + rule.md + faq.md + images/
        ↓
   Generator
        ↓
SOP (HTML + MD) + Tutorial (HTML)
```

Generator는 읽기(Read) → 생성(Generate)만 수행한다.

---

## 2. RC Exit Criteria 현황

```
✅ Regression PASS        (v3.8.1 — Mode-aware + Result/Display 분리)
✅ PDF 출력 PASS          (v3.9 — 인쇄 시 Guide/Rule/FAQ 전체 출력)
✅ PrintFlow PASS         (both 15/0/0)
✅ KingTestMaker PASS     (analyzer.py → both 14/0/0)
✅ Dooly PASS             (analyzer.py → H4 보강 → both 14/0/0)
□ HANDOVER 새 채팅 검증  ← 지금 이것
```

**다음 단계:**
1. HANDOVER 새 채팅에서 이어받기 검증
2. RC Exit Criteria 최종 확인
3. Generator Stable v1.0 선언
4. Feature Freeze

---

## 3. 완성된 가이드북 현황

| 번호 | 앱 이름 | SOP | Tutorial | 버전 | 생성 방식 | Regression |
|------|---------|:---:|:--------:|------|-----------|------------|
| 01 | PrintFlow | ✅ | ✅ | v1.0 | 수동 | PASS 15/0/0 |
| 02 | KingTestMaker | ✅ | ✅ | v1.0 | analyzer.py | PASS 14/0/0 |
| 03 | Dooly | ✅ | ✅ | v1.0 | analyzer.py | PASS 14/0/0 |
| 04 | CheckFlow | 🔲 | 🔲 | — | 계획중 | — |

---

## 4. Generator 완료된 기능

```
✓ analyzer.py               소스 폴더 분석 → guide.md 자동 생성
✓ generator.py              guide/rule/faq → SOP + Tutorial 생성
✓ Markdown Renderer         코드블록/hr/H4/인라인코드/볼드 (v3.7)
✓ Sticky Tab                Top Bar + Tab Bar 고정 (v3.7)
✓ SOP 탭 구조               가이드 / 업무규칙 / FAQ 탭
✓ PDF 전체 출력             인쇄 시 Guide→Rule→FAQ 전체 (v3.9)
✓ Regression Check          Core/Renderer/App/Overall 4계층 (v3.8)
✓ Mode-aware Regression     sop/tutorial/both 모드별 N/A 처리 (v3.8.1)
✓ Result/Display 분리       result=PASS/FAIL, display=사람이 보는 표시 (v3.8.1)
✓ Summary                   PASS/FAIL/N/A 수 터미널+Report 출력 (v3.8.1)
✓ Regression_Report.md      YAML 메타데이터 + 4계층 결과 + Summary
✓ archive 자동 백업
```

---

## 5. 작업지시서 현황

| 순번 | 파일명 | 내용 | 상태 |
|------|--------|------|------|
| 12 | 12_작업지시서_v3.7 | Markdown Renderer + Sticky Tab | ✅ |
| 14 | 14_작업지시서_v3.8 | Regression Check 4계층 | ✅ |
| 17 | 17_작업지시서_v3.8.1 | Mode-aware + Result/Display 분리 | ✅ |
| 18 | 18_작업지시서_v3.9 | PDF 전체 출력 개선 | ✅ |

---

## 6. 주요 파일 경로

| 파일 | 경로 |
|------|------|
| generator.py | `C:\Obsidian\GuideBook\GuideBook_생성기\generator.py` |
| analyzer.py | `C:\Obsidian\GuideBook\GuideBook_생성기\analyzer.py` |
| PrintFlow input | `apps\PrintFlow\input\` (guide.md, rule.md, faq.md) |
| KingTestMaker input | `apps\KingTestMaker\input\` |
| Dooly input | `apps\Dooly\input\` |
| SYSTEM_PROMPT | `99_공통\7_SYSTEM_PROMPT_v4.3.md` |

---

## 7. 앱별 소스 경로

| 앱 | 소스 경로 | 분석 폴더 |
|----|-----------|-----------|
| KingTestMaker | `C:\Obsidian\복테메이커\` | docs, electron, html, log |
| PrintFlow | `C:\Obsidian\PrintFlow\` | Archive, command, log, MVP, sync, WORK, 배포 |
| Dooly | `C:\Obsidian\Dooly\` | 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs |

---

## 8. 주요 결정 사항

| 결정 | 내용 |
|------|------|
| RC 운영 원칙 | 기능 추가 ❌ / 검증 ✅ / 버그수정 ✅ / 구현정리 ✅ |
| Regression FAIL 진단 순서 | Generator 버그 vs 콘텐츠 부재 구분 (시행착오_기록.md 참고) |
| v2.x 로드맵 | SSOT 자동 분류 엔진 — Approved (Deferred) |
| GitHub 운영 | 개발Commit(feat:/fix:/docs:) + Release(git tag v1.0) 구분 |
| PrintFlow 콘텐츠 보강 | 학원_업무매뉴얼_SOP_v2.md → guide/rule/reference/faq 분리 (Stable 이후) |

---

## 9. Stable v1.0 선언 이후 계획

```
Stable v1.0 선언 + Feature Freeze
        ↓
Phase B 콘텐츠 보강
  PrintFlow: 학원_업무매뉴얼_SOP_v2.md → guide/rule/reference/faq 분리
        ↓
Phase C: CheckFlow 개발 시작
        ↓
v2.x: SSOT 자동 분류 엔진 구현
```

---

## 10. 새 채팅 시작 방법

1. claude.ai → **가이드북 생성기 프로젝트** 열기
2. 이 파일(`7_HANDOVER_v1.0.md`) 첨부
3. 입력:
```
첨부한 인수인계 파일 읽고 이전 내용 파악해줘. 이어서 진행할게.
```

**검증 방법:**
새 채팅에서 아래 질문으로 이어받기 정상 여부 확인:
- "현재 RC Exit Criteria 상태는?"
- "다음에 할 작업은?"
- "Regression 판정 기준은?"

---

## 11. HANDOVER 검증 체크리스트

새 채팅에서 이 파일로 시작한 후 확인:

| # | 확인 항목 | 기대 결과 |
|---|-----------|-----------|
| 1 | RC Exit Criteria 파악 | HANDOVER 검증만 남았음 인식 |
| 2 | 다음 작업 파악 | Stable v1.0 선언 준비 |
| 3 | 3개 앱 Regression 상태 | PrintFlow/KTM/Dooly 모두 PASS |
| 4 | Generator 버전 | v3.9 |
| 5 | Feature Freeze 규칙 | Stable 이후 신규 기능 불허 인식 |
