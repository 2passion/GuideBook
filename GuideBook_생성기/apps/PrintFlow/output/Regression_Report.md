---
Project: GuideBook Generator
App: PrintFlow
Generator: v3.8.1
Result: PASS
Generated: 2026-07-10 14:11

Inputs:
  guide_PrintFlow.md: 2026-07-10 12:41
  rule_PrintFlow.md: 2026-07-10 14:11
  faq_PrintFlow.md: 2026-07-06 22:11
  reference_PrintFlow.md: 2026-07-10 14:01
---

# Regression Report

생성일: 2026-07-10 14:11  |  Generator: v3.8.1  |  App: PrintFlow  |  Mode: both

---

## Core  ✅ PASS

✓ guide_PrintFlow.md 읽기
✓ rule_PrintFlow.md 읽기
✓ faq_PrintFlow.md 읽기
✓ reference_PrintFlow.md (optional)
✓ SOP HTML 생성
✓ SOP MD 생성
✓ Tutorial HTML 생성

---

## Renderer  ✅ PASS

✓ 코드블록 렌더링 (<pre><code>)
✓ 수평선 렌더링 (<hr>)
✓ H4 렌더링 (<h4>)
✓ 인라인 코드 렌더링 (<code>)

---

## App  ✅ PASS

✓ Sticky Tab
✓ PDF 버튼
✓ 탭 구조 (Guide)
✓ 탭 구조 (Rule)
✓ 탭 구조 (FAQ)

---

## Overall  ✅ PASS

---

## Summary

| 항목 | 수 |
|------|-----|
| ✓ PASS | 16 |
| ✗ FAIL | 0 |
| - N/A  | 0 |

---

## 다음 권장 작업

□ Phase A-3: PDF 전체 출력 개선 (14_작업지시서_v3.9)
□ Phase B:   PrintFlow 실사용 검증
□ Phase B:   KingTestMaker 실제 가이드북 생성
         python analyzer.py KingTestMaker "C:\Obsidian\복테메이커" "docs,electron,html,log"
□ Phase B:   Dooly 실제 가이드북 생성
         python analyzer.py Dooly "C:\Obsidian\Dooly" "00_System,01_Project,docs,api"
