# 37_재작업 + Regression + Git 수정

작성일: 2026-07-10
버전: v1.1 (STEP3 git add 지정 파일 방식으로 수정)
목적: rule_Dooly.md 수정 → Regression → 커밋 반영

---

## 배경

커밋 0175c29에 rule_Dooly.md가 포함되어 있으나,
아래 4개 항목이 미확정 규칙으로 판명되어 삭제가 필요하다.

삭제 대상:
- JSON 파일은 당일 업무 시작 전 반드시 업로드합니다.
- 조교는 JSON 파일을 임의로 수정하지 않습니다.
- 완료 처리 없이 다음 조교에게 넘기지 않습니다.
- AI 답변은 참고용이며, 최종 판단은 SOP/FAQ를 우선합니다.

---

## STEP 1 — rule_Dooly.md 수정

※ STEP 1은 이미 완료됨. 확인 후 STEP 2로 진행한다.

대상 파일:
C:\Obsidian\GuideBook\GuideBook_생성기\apps\Dooly\input\rule_Dooly.md

수정 완료 후 최종 구조 (확인용):

```markdown
# Dooly 업무 규칙

## JSON 규칙

- JSON 파일은 덮어쓰지 않고 날짜별로 보관합니다.

## 업무 처리 규칙

- 업무는 반드시 Dooly 앱에서 완료 처리합니다.
- 업무 목록이 비어 있으면 JSON 업로드를 먼저 실행합니다.

## AI 챗봇 사용 규칙

- 기본 모드는 Mock 모드(오프라인)입니다.
- 실시간 AI 답변이 필요할 때만 Gemini 모드로 전환합니다.

## 설정 규칙

- 담당자 추가/관리는 설정 탭에서 최초 1회 실행합니다.
- DB 폴더 경로는 최초 설정 후 임의로 변경하지 않습니다.
```

완료 후 중지한다.
확인 후 STEP 2 진행을 지시하면 이어서 실행한다.

---

## STEP 2 — Regression 실행

아래 명령을 실행한다.

```
cd C:\Obsidian\GuideBook\GuideBook_생성기
python generator.py Dooly both
```

완료 후 아래 형식으로 보고한다.

1. Core 결과
2. Renderer 결과
3. App 결과
4. Overall 결과
5. PASS / FAIL / N/A Summary
6. 특이사항

기준선: PASS 11 / FAIL 0 / N/A 4

PASS 확인 후 중지한다.
확인 후 STEP 3 진행을 지시하면 이어서 실행한다.

---

## STEP 3 — Git 커밋 (신규 커밋)

아래 순서대로 실행한다.

### 3-1. 지정 파일만 스테이징

```
cd C:\Obsidian\GuideBook
git add "GuideBook_생성기/apps/Dooly/input/rule_Dooly.md"
git add "GuideBook_생성기/apps/Dooly/output/"
```

### 3-2. 스테이징 확인

```
git diff --cached --name-status
```

스테이징된 파일이 아래와 일치하는지 확인한다.

예상 스테이징 파일:
- GuideBook_생성기/apps/Dooly/input/rule_Dooly.md
- GuideBook_생성기/apps/Dooly/output/Dooly_SOP_v1.0.md
- GuideBook_생성기/apps/Dooly/output/Dooly_SOP_v1.0.html
- GuideBook_생성기/apps/Dooly/output/Dooly_튜토리얼_v1.0.html
- GuideBook_생성기/apps/Dooly/output/Regression_Report.md

일치하면 커밋 진행.
일치하지 않으면 중단하고 보고한다.

### 3-3. 커밋

```
git commit -m "fix: remove unconfirmed rules from rule_Dooly and regenerate output"
git rev-parse HEAD
```

### 3-4. 최종 확인

```
git status --short
git log --oneline -5
```

완료 후 아래 형식으로 보고한다.

1. 커밋 해시
2. 스테이징 파일 목록 (git diff --cached --name-status 결과)
3. git log --oneline -5 결과
4. 워킹트리 상태 (git status --short)
5. 특이사항

---

## 제약

- generator.py 수정 금지
- analyzer.py 수정 금지
- SSOT 원칙 유지
- 각 STEP 완료 후 반드시 중지하고 다음 지시를 기다린다
