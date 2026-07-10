# 29_Git_Commit_Workflow_v1.0
GuideBook Git 커밋 운영 표준
작성일: 2026-07-10 | 버전: v1.0

---

## 개요

GuideBook Phase B Git 운영 표준이다.
모든 앱(PrintFlow / KingTestMaker / Dooly / CheckFlow)에서 동일하게 재사용한다.

---

## 커밋 구조 (앱 단위 완료 시)

```
Commit 1  앱 콘텐츠
          GuideBook_생성기/apps/{AppName}/input/
          GuideBook_생성기/apps/{AppName}/output/

Commit 2  작업지시서
          99_공통/{번호}_작업지시서_v*.md

Commit 3  운영 문서
          99_공통/시행착오_기록.md
          99_공통/워크플로우_가이드.md

Commit 4  시스템 기준 (변경 시에만)
          99_공통/8_SYSTEM_PROMPT_v*.md

Commit 5  HANDOVER
          99_공통/{번호}_HANDOVER_v*.md
```

---

## Claude Code 전달 프롬프트 템플릿

```
아래 순서대로 커밋 N개를 순차 실행해줘.

중요:
- 한 번에 모두 실행하지 않는다.
- 각 커밋을 실행한 뒤 완료 보고를 출력하고 중지한다.
- 내가 확인하고 다음 커밋 진행을 요청하면 이어서 실행한다.
- 지정된 파일 외에는 스테이징하지 않는다.
- 커밋 전에 staged 파일 목록을 확인한다.
- 빈 커밋은 만들지 않는다.

---

# Commit N — {목적}

cd "C:/Obsidian/GuideBook"

git add \
  "{파일 경로 1}" \
  "{파일 경로 2}"

git diff --cached --name-status
스테이징된 파일이 작업지시와 일치하는지 확인한다.
일치하면 commit을 진행한다.
일치하지 않으면 commit하지 말고 이유를 보고한다.

git commit -m "{커밋 메시지}"
git push

완료 보고:
1. 커밋 hash
2. 스테이징·커밋된 파일 목록
3. commit 메시지
4. push 결과(branch, remote, range)
5. 특이사항

완료 보고 후 중지하고 다음 지시를 기다린다.
```

---

## 커밋 메시지 규칙

```
feat:  앱 콘텐츠 완료
       feat: complete {AppName} Phase B document set

docs:  문서 변경
       docs: add {AppName} Phase B work orders
       docs: update GuideBook workflow and knowledge base
       docs: finalize GuideBook system baseline v{버전}
       docs: add {AppName} Phase B milestone handover

chore: 설정 변경
       chore: ignore generator archive
```

---

## 실행 흐름

```
작업 완료
↓
git add
↓
staged 파일 검증 (git diff --cached --name-status)
↓
작업지시와 비교
↓
일치 → commit → push → 보고
불일치 → commit 중단 → 이유 보고
↓
사용자 승인
↓
다음 commit
```

---

## 주의사항

```
- 앱 콘텐츠와 99_공통 파일을 같은 커밋에 섞지 않는다
- SYSTEM_PROMPT는 단독 커밋한다 (시스템 기준선 변경 추적)
- archive/ 파일은 Git 제외 (.gitignore)
- HANDOVER는 마지막 커밋 (최신 hash 반영 후 작성)
- LF→CRLF 경고는 Windows 정상 동작, 오류 아님
```

---

## 적용 이력

| 앱 | 적용 커밋 | 날짜 |
|----|----------|------|
| PrintFlow | cd0b337 | 2026-07-10 |
| KingTestMaker | f43ad16 | 2026-07-10 |
| Dooly | — | — |
| CheckFlow | — | — |
