# 23 — Generator archive Git 추적 제외

작업 루트:
C:\Obsidian\GuideBook

---

## 작업 원칙

- 로컬 archive 파일은 절대 삭제하지 않는다.
- Git 추적만 해제한다.
- generator.py / analyzer.py 수정 금지.
- 콘텐츠 파일 변경 금지.

---

## 작업 내용

1. .gitignore 수정
   C:\Obsidian\GuideBook\.gitignore 파일에 아래 내용을 추가한다.

   ```
   # Generator archive (실행 직전 자동 백업 — Git 제외)
   GuideBook_생성기/archive/*
   !GuideBook_생성기/archive/.gitkeep
   ```

2. 이미 추적 중인 archive 파일 추적 해제
   로컬 파일은 삭제하지 않고 Git 추적만 해제한다.

   ```bash
   git rm -r --cached GuideBook_생성기/archive
   ```

3. commit & push

   ```bash
   git add .gitignore
   git commit -m "chore: ignore generator archive"
   git push
   ```

4. 최종 확인

   ```bash
   git status
   ```

   archive 파일이 목록에 나타나지 않으면 성공.

---

## 완료 후 보고 형식

1. .gitignore 추가 내용 확인
2. git rm --cached 결과 (추적 해제된 파일 목록)
3. commit 결과 (해시, 변경 파일 수)
4. push 결과 (branch, remote)
5. git status 최종 확인
6. 특이사항
