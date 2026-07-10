# 24_구현계획서_Automation_Hooks_v1.0.md
# GuideBook Automation Hooks — 설계 문서

작성일: 2026-07-10
상태: 설계 완료 / 구현 보류 (v2.x에서 구현)
분류: Developer Productivity Tool (Generator와 독립)

---

## 결정 사항

```
지금  : 설계만 완료
Phase B: 콘텐츠 작업 집중 (구현하지 않음)
v2.x  : Automation Hooks 구현
```

이유:
- Generator / Documentation과 독립된 개발 생산성 도구
- Feature Freeze 원칙 유지
- Phase B 집중력 유지
- 좋은 아이디어를 Roadmap으로 보존

---

## 목적

현재 운영 문서(시행착오_기록, 워크플로우_가이드, HANDOVER)는
사람이 직접 요청해야 업데이트된다.

```
현재
작업 완료 → 사용자 "시행착오 기록 추가해줘" → AI 작성 → 저장

목표
작업 완료 → 완료 보고 자동 파싱 → Markdown 자동 생성 → 저장
```

---

## 아키텍처

```
GuideBook
│
├── Generator        (읽기 → 생성, 현재 Stable)
├── Claude Code      (구현 공간)
│
└── Automation Hooks (v2.x 구현 예정)
      │
      ├── log_hook.py       시행착오_기록.md 자동 업데이트
      ├── workflow_hook.py  워크플로우_가이드.md 자동 업데이트
      ├── handover_hook.py  HANDOVER 자동 생성
      └── commit_hook.py    Commit 메시지 자동 생성
```

저장 위치 (예정):
```
GuideBook_생성기/hooks/
  ├── log_hook.py
  ├── workflow_hook.py
  ├── handover_hook.py
  └── commit_hook.py
```

---

## Hook 종류 및 역할

### 1. log_hook.py — 시행착오 자동 기록

트리거:
- Regression FAIL 발생 시
- Generator 수정 발생 시
- 완료 보고에 "수정 파일" 항목 존재 시

동작:
```
완료 보고 파싱
    ↓
번호 자동 증가
분류 자동 결정 (버그 / 설계 / 운영)
관련 파일 자동 추출
    ↓
시행착오_기록.md append
```

출력 형식:
```
### #{번호} — {제목}
| 항목 | 내용 |
날짜 / 분류 / 상태

문제 / 원인 / 해결
관련 파일
재발 방지
교훈
```

---

### 2. workflow_hook.py — 워크플로우 자동 업데이트

트리거:
- 작업지시서에 새로운 단계 추가 감지 시
- 워크플로우 변경 키워드 포함 완료 보고 시

동작:
```
완료 보고 파싱
    ↓
워크플로우 변경 감지
    ↓
버전 자동 증가 (v1.4 → v1.5)
변경 이력 행 추가
상세 기록 섹션 추가
    ↓
워크플로우_가이드.md 덮어쓰기
```

---

### 3. handover_hook.py — HANDOVER 자동 생성

트리거:
- 세션 종료 요청 시
- "인수인계 만들어줘" 키워드 감지 시

동작:
```
현재 세션 완료 항목 수집
    ↓
다음 세션 첫 작업 자동 추출
    ↓
{순번}_HANDOVER_v{버전}.md 생성
```

출력 형식 (5섹션):
```
1. 세션 요약
2. 완료 작업
3. 문제와 해결
4. 되돌리지 말아야 할 결정
5. 다음 세션 첫 작업
```

---

### 4. commit_hook.py — Commit 메시지 자동 생성

트리거:
- Regression PASS 후 Git Commit 단계 진입 시

동작:
```
완료 보고 파싱
    ↓
변경 파일 분류
    ↓
prefix 자동 결정
  feat: 신규 기능
  fix:  버그 수정
  docs: 문서 변경
  chore: 설정 변경
    ↓
커밋 메시지 제안
```

예시 출력:
```
docs: finalize KingTestMaker content baseline
```

---

## 예상 Workflow (v2.x 이후)

```
작업지시서 실행
    ↓
Claude Code 구현
    ↓
완료 보고 생성
    ↓
┌─────────────────────────────┐
│  Automation Hooks           │
│  log_hook      → 시행착오   │
│  workflow_hook → 워크플로우  │
│  commit_hook   → 커밋 메시지 │
└─────────────────────────────┘
    ↓
Git Commit & Push
    ↓
handover_hook → HANDOVER 생성
    ↓
다음 세션
```

---

## 구현 원칙 (v2.x 적용)

```
1. Generator / analyzer.py 수정 금지
   Hook은 독립 도구로 운영

2. 완료 보고 파싱 기반
   Claude Code 출력 형식 활용

3. Append 방식
   기존 파일 덮어쓰지 않고 내용 누적

4. 실패해도 안전
   Hook 실패 시 기존 수동 방식으로 fallback
```

---

## GuideBook 로드맵

```
v1.1   Generator Stable              ✅ 완료
Phase B 콘텐츠 고도화                 ▶ 진행 중
v1.2   Content Complete              예정
v2.x   Automation Hooks              설계 완료 / 구현 보류
       SSOT Auto Classification      설계 완료 / 구현 보류
```

---

## 다음 Action

```
Phase B 완료 후
    ↓
v2.x 작업지시서 작성
    ↓
hooks/ 폴더 생성
    ↓
log_hook.py 구현 (우선순위 1)
    ↓
handover_hook.py 구현 (우선순위 2)
    ↓
workflow_hook.py / commit_hook.py (우선순위 3)
```
