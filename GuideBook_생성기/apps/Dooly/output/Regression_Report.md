---
Project: GuideBook Generator
App: Dooly
Generator: v3.8.1
Result: PASS
Generated: 2026-07-10 20:57

Inputs:
  guide_Dooly.md: 2026-07-10 20:51
  rule_Dooly.md: 2026-07-10 20:55
  faq_Dooly.md: 2026-07-10 20:55
  reference_Dooly.md: 파일 없음
---

# Regression Report

생성일: 2026-07-10 20:57  |  Generator: v3.8.1  |  App: Dooly  |  Mode: both

---

## Core  ✅ PASS

✓ guide_Dooly.md 읽기
✓ rule_Dooly.md 읽기
✓ faq_Dooly.md 읽기
- reference_Dooly.md (optional) (reference 없음 → N/A)
✓ SOP HTML 생성
✓ SOP MD 생성
✓ Tutorial HTML 생성

---

## Renderer  ✅ PASS

- 코드블록 렌더링 (<pre><code>) (입력 원문에 코드블록(```) 없음)
✓ 수평선 렌더링 (<hr>)
- H4 렌더링 (<h4>) (입력 원문에 H4(####) 없음)
- 인라인 코드 렌더링 (<code>) (입력 원문에 인라인코드(`...`) 없음)

---

## App  ✅ PASS

✓ PDF 버튼
✓ 탭 구조 (Guide)
✓ 탭 구조 (Rule)
✓ 탭 구조 (FAQ)

---

## Overall  ✅ PASS (N/A 포함)

---

## Summary

| 항목 | 수 |
|------|-----|
| ✓ PASS | 11 |
| ✗ FAIL | 0 |
| - N/A  | 4 |

---

## 다음 권장 작업

□ Phase A-3: PDF 전체 출력 개선 (14_작업지시서_v3.9)
□ Phase B:   PrintFlow 실사용 검증
□ Phase B:   KingTestMaker 실제 가이드북 생성
         python analyzer.py KingTestMaker "C:\Obsidian\복테메이커" "docs,electron,html,log"
□ Phase B:   Dooly 실제 가이드북 생성
         python analyzer.py Dooly "C:\Obsidian\Dooly" "00_System,01_Project,docs,api"
