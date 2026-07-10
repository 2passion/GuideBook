# 38_작업지시서 — Dooly Phase B Git 커밋 및 Push

파일명: 38_작업지시서_Dooly_Git_커밋_v1.1.md
작성일: 2026-07-10
저장 위치: C:\Obsidian\GuideBook\99_공통\

---

## 배경

Dooly Phase B 작업이 완료되었다.
아래 커밋이 로컬에 대기 중이며, 추가 커밋 2개와 Push가 필요하다.

```
68b393a  fix: remove unconfirmed rules from rule_Dooly and regenerate output
6cd9678  docs: add Dooly Phase B work orders
0175c29  feat: complete Dooly Phase B document set
```

---

## 커밋 1 — 작업지시서

### 1-1. 스테이징

```
cd C:\Obsidian\GuideBook
git add "99_공통/37_재작업_및_Regression_v1.1.md"
git add "99_공통/38_작업지시서_Dooly_Git_커밋_v1.1.md"
```

### 1-2. 스테이징 검증

```
git diff --cached --name-status
```

스테이징된 파일이 아래와 일치하는지 확인한다.

```
A  99_공통/37_재작업_및_Regression_v1.1.md
A  99_공통/38_작업지시서_Dooly_Git_커밋_v1.1.md
```

일치하면 커밋 진행.
일치하지 않으면 커밋하지 말고 이유를 보고한다.

### 1-3. 커밋

```
git commit -m "docs: add Dooly fix and Git work orders"
git log --oneline -3
```

### 1-4. Push

```
git push origin main
git status --short
```

완료 후 아래 형식으로 보고한다.

1. 커밋 해시
2. 스테이징 검증 결과
3. git log --oneline -3
4. push 결과 (원격 기준 여러 커밋이 함께 올라갈 수 있음 — 정상)
5. 워킹트리 상태

완료 후 중지하고 다음 지시를 기다린다.

---

## 커밋 2 — 운영 문서

### 2-1. 스테이징

```
cd C:\Obsidian\GuideBook
git add "99_공통/13_채팅시작_프롬프트_v1.0.md"
git add "99_공통/33_ClaudeCode_Dooly_PhaseB.md"
```

### 2-2. 스테이징 검증

```
git diff --cached --name-status
```

스테이징된 파일이 아래와 일치하는지 확인한다.

```
A  99_공통/13_채팅시작_프롬프트_v1.0.md
A  99_공통/33_ClaudeCode_Dooly_PhaseB.md
```

일치하면 커밋 진행.
일치하지 않으면 커밋하지 말고 이유를 보고한다.

### 2-3. 커밋

```
git commit -m "docs: add Dooly Phase B operational docs"
git log --oneline -3
```

### 2-4. Push

```
git push origin main
git status --short
git log --oneline -5
```

완료 후 아래 형식으로 보고한다.

1. 커밋 해시
2. 스테이징 검증 결과
3. git log --oneline -3
4. push 결과
5. 워킹트리 상태
6. git log --oneline -5 (HANDOVER 작성용)

완료 후 중지하고 대기한다.

---

## 제약

- generator.py 수정 금지
- analyzer.py 수정 금지
- 37_재작업_및_Regression_v1.0.md 는 커밋하지 않는다
- 각 STEP 완료 후 반드시 중지하고 다음 지시를 기다린다
