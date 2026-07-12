# 40_작업지시서 — images 표준화

파일명: 40_작업지시서_images_표준화_v1.1.md
작성일: 2026-07-12
목적: 배포 폴더의 screenshots\ 제거 및 input\images\ 표준 확정

---

## 배경

현재 상태:
- 02_PrintFlow\ 배포 폴더에 screenshots\ 폴더 존재
- GuideBook_생성기\apps\PrintFlow\input\ 에 images\ 폴더 존재
- 두 폴더가 같은 목적처럼 보여 혼동 발생

확정된 표준:
```
이미지 저장 위치  → apps\{App}\input\images\ (유일)
배포 폴더        → HTML 파일만 (이미지 폴더 없음)
```

---

## images 표준

```
Generator (개발 영역)
apps\{App}\input\
    ├── guide.md
    ├── rule.md
    ├── faq.md
    ├── reference.md  (optional)
    └── images\
        ├── .gitkeep
        └── README.txt       ← 유일한 이미지 저장 위치

배포 영역
0X_{App}\
    ├── {App}_SOP_v1.0.html
    └── {App}_튜토리얼_v1.0.html
    (이미지 폴더 없음)
```

---

## 대상 경로

```
배포 폴더: C:\Obsidian\GuideBook\
생성기:    C:\Obsidian\GuideBook\GuideBook_생성기\apps\
```

---

## STEP 1 — screenshots\ 내용 확인 및 삭제

### 1-1. 내용 확인
```
C:\Obsidian\GuideBook\02_PrintFlow\screenshots\
```
안에 있는 파일 목록을 출력한다.
실제 이미지 파일(png/jpg 등)이 있으면 중단하고 보고한다.
.gitkeep, README.txt 같은 메타 파일만 있으면 삭제 진행한다.

### 1-2. screenshots\ 폴더 삭제
내용 확인 후 삭제 진행:
```
Remove-Item -LiteralPath "C:\Obsidian\GuideBook\02_PrintFlow\screenshots" -Recurse -Force
```

### 1-3. 삭제 확인
```
02_PrintFlow\ 폴더 목록 출력
```

완료 후 보고 형식:
```
1. screenshots\ 내부 파일 목록
2. 삭제 결과
3. 02_PrintFlow\ 최종 파일 목록
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 2 — 각 앱 input\images\ 현황 확인

아래 3개 앱의 input\ 폴더를 확인한다.

```
C:\Obsidian\GuideBook\GuideBook_생성기\apps\KingTestMaker\input\
C:\Obsidian\GuideBook\GuideBook_생성기\apps\PrintFlow\input\
C:\Obsidian\GuideBook\GuideBook_생성기\apps\Dooly\input\
```

각 앱별로:
- images\ 폴더 존재 여부
- images\ 내부 파일 목록 (있으면)
- images\ 없으면 "생성 필요" 표시

완료 후 보고 형식:
```
앱명 | images\ 존재 여부 | 내부 파일 수 | 조치 필요
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 3 — 모든 앱 images\ 표준 구조 완성

STEP 2 결과를 기준으로 아래 3개 앱 모두를 확인한다.

- images\ 폴더가 없으면 생성한다.
- .gitkeep이 없으면 생성한다.
- README.txt가 없으면 생성한다.
- 기존 이미지 파일은 이동·수정·삭제하지 않는다.
- 기존 README.txt가 있으면 덮어쓰지 않고 내용을 보고한다.

대상 앱:
```
KingTestMaker / PrintFlow / Dooly
```

실행 기준 (각 앱별 반복):
```powershell
$imgDir = "...\input\images"
New-Item -ItemType Directory -LiteralPath $imgDir -Force

$gitkeep = Join-Path $imgDir ".gitkeep"
if (-not (Test-Path -LiteralPath $gitkeep)) {
    New-Item -ItemType File -LiteralPath $gitkeep -Force
}

$readme = Join-Path $imgDir "README.txt"
if (-not (Test-Path -LiteralPath $readme)) {
    Set-Content -LiteralPath $readme `
      -Value "GuideBook Standard`r`n이미지는 이 폴더(input/images/)만 사용합니다." `
      -Encoding UTF8
} else {
    "README.txt 이미 존재 — 내용 확인 필요:"
    Get-Content -LiteralPath $readme
}
```

완료 후 보고 형식:
```
앱명 | 조치 내용 | 최종 images\ 구조
KingTestMaker | 생성/기존 | .gitkeep / README.txt
PrintFlow     | 생성/기존 | .gitkeep / README.txt
Dooly         | 생성/기존 | .gitkeep / README.txt
```

완료 후 중지하고 다음 지시를 기다린다.

---

## 전체 완료 후 예상 구조

```
배포 폴더:
02_PrintFlow\
    ├── PrintFlow_SOP_v1.0.html
    └── PrintFlow_튜토리얼_v1.0.html
    (screenshots\ 없음)

Generator:
apps\KingTestMaker\input\
    ├── guide_KingTestMaker.md
    ├── rule_KingTestMaker.md
    ├── faq_KingTestMaker.md
    └── images\
        ├── .gitkeep
        └── README.txt

apps\PrintFlow\input\
    ├── guide_PrintFlow.md
    ├── rule_PrintFlow.md
    ├── faq_PrintFlow.md
    ├── reference_PrintFlow.md
    └── images\
        ├── .gitkeep
        └── README.txt

apps\Dooly\input\
    ├── guide_Dooly.md
    ├── rule_Dooly.md
    ├── faq_Dooly.md
    └── images\
        ├── .gitkeep
        └── README.txt
```

---

## 제약

- generator.py 수정 금지
- analyzer.py 수정 금지
- apps\input\ Markdown 파일 수정 금지
- apps\output\ 수정 금지
- screenshots\ 안에 실제 이미지 있으면 삭제 중단
- Remove-Item 은 반드시 -LiteralPath 사용
- 기존 images\ 내부 이미지 파일은 이동·수정·삭제하지 않는다
- 기존 README.txt는 자동 덮어쓰지 않고 내용 보고 후 대기한다
- 파일 생성과 수정에는 가능하면 -LiteralPath를 사용한다
- 각 STEP 완료 후 반드시 중지하고 다음 지시를 기다린다
