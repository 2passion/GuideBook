# 42_작업지시서 — GuideBook_배포 구조 전환

파일명: 42_작업지시서_GuideBook_배포_구조전환_v1.2.md
작성일: 2026-07-12
이전 버전: v1.1 (STEP4 스테이징 전 기준 수정 / untracked 허용 / exit→throw 수정)
목적: 루트 배포 폴더(01~03)를 GuideBook_배포\ 아래로 이동하여 생성기/배포 역할 분리

---

## 배경

현재 구조:
```
GuideBook\
├── 01_KingTestMaker\
├── 02_PrintFlow\
├── 03_Dooly\
├── GuideBook_생성기\
└── 99_공통\
```

목표 구조:
```
GuideBook\
├── GuideBook_배포\
│   ├── 01_KingTestMaker\
│   ├── 02_PrintFlow\
│   └── 03_Dooly\
├── GuideBook_생성기\
└── 99_공통\
```

역할 분리 원칙:
```
GuideBook_생성기\  = 개발 영역 (SSOT + Generator)
GuideBook_배포\    = 배포 영역 (사용자용 HTML)
99_공통\           = 운영 문서
```

---

## STEP 0 — 현재 구조 확인

### 0-1. 루트 구조 및 폴더 존재 확인
```powershell
"=== GuideBook 루트 ==="
Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook" |
    Select-Object Name, @{n='Type';e={if($_.PSIsContainer){'DIR'}else{'FILE'}}} |
    Format-Table -AutoSize

"=== GuideBook_배포 존재 여부 ==="
Test-Path -LiteralPath "C:\Obsidian\GuideBook\GuideBook_배포"

"=== 이동 대상 폴더 존재 여부 ==="
"01_KingTestMaker: $(Test-Path -LiteralPath 'C:\Obsidian\GuideBook\01_KingTestMaker')"
"02_PrintFlow:     $(Test-Path -LiteralPath 'C:\Obsidian\GuideBook\02_PrintFlow')"
"03_Dooly:         $(Test-Path -LiteralPath 'C:\Obsidian\GuideBook\03_Dooly')"
```

### 0-2. 이동 대상 배포 폴더 내부 파일 확인 (이동 전 기록용)
```powershell
foreach ($app in @("01_KingTestMaker","02_PrintFlow","03_Dooly")) {
    "=== $app 내부 ==="
    Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook\$app" -Recurse |
        Select-Object Name, Length | Format-Table -AutoSize
}
```

### 0-3. Git 상태 확인 (STEP 4 비교용 기준선)
```powershell
cd C:\Obsidian\GuideBook
git -c core.quotepath=false status --short
```

완료 후 보고 형식:
```
1. GuideBook 루트 현재 구조
2. GuideBook_배포 존재 여부
3. 이동 대상 3개 폴더 존재 여부
4. 각 배포 폴더 내부 파일 목록 (이동 전 기록)
5. Git 상태 (STEP 4 비교 기준선)
6. 진행 가능 여부
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 1 — GuideBook_배포\ 폴더 생성

```powershell
New-Item -ItemType Directory -Path "C:\Obsidian\GuideBook\GuideBook_배포" -Force
"GuideBook_배포 생성: $(Test-Path -LiteralPath 'C:\Obsidian\GuideBook\GuideBook_배포')"
```

완료 후 보고 형식:
```
1. 생성 결과 (True여야 정상)
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 2 — 배포 폴더 이동 (복사 아닌 이동)

### 2-1. 목적지 충돌 확인 (이동 전 필수)
```powershell
$dst = "C:\Obsidian\GuideBook\GuideBook_배포"
$targets = "01_KingTestMaker", "02_PrintFlow", "03_Dooly"
foreach ($name in $targets) {
    $targetPath = Join-Path $dst $name
    if (Test-Path -LiteralPath $targetPath) {
        throw "이동 중단 — 목적지 폴더가 이미 존재합니다: $targetPath"
    }
}
"목적지 충돌 없음 — 이동 진행"
```

목적지에 같은 이름 폴더가 있으면 중단하고 보고한다.

### 2-2. 폴더 이동
```powershell
$src = "C:\Obsidian\GuideBook"
$dst = "C:\Obsidian\GuideBook\GuideBook_배포"

Move-Item -LiteralPath (Join-Path $src "01_KingTestMaker") -Destination $dst
Move-Item -LiteralPath (Join-Path $src "02_PrintFlow")     -Destination $dst
Move-Item -LiteralPath (Join-Path $src "03_Dooly")         -Destination $dst

"=== 이동 후 루트 구조 ==="
Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook" | Select-Object Name | Format-Table -AutoSize

"=== GuideBook_배포 내부 ==="
Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook\GuideBook_배포" | Select-Object Name | Format-Table -AutoSize
```

완료 후 보고 형식:
```
1. 목적지 충돌 확인 결과
2. 루트에서 01/02/03 폴더 사라졌는지 확인
3. GuideBook_배포\ 내부에 01/02/03 존재하는지 확인
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 3 — 구조 검증

```powershell
"=== GuideBook 루트 최종 ==="
Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook" |
    Select-Object Name, @{n='Type';e={if($_.PSIsContainer){'DIR'}else{'FILE'}}} |
    Format-Table -AutoSize

"=== GuideBook_배포 내부 파일 확인 ==="
foreach ($app in @("01_KingTestMaker","02_PrintFlow","03_Dooly")) {
    "--- $app ---"
    Get-ChildItem -LiteralPath "C:\Obsidian\GuideBook\GuideBook_배포\$app" -Recurse |
        Select-Object Name, Length | Format-Table -AutoSize
}
```

확인 기준:
```
루트 필수 폴더:
  GuideBook_생성기\
  GuideBook_배포\
  99_공통\

루트 허용 파일:
  .gitignore

루트에 01_KingTestMaker\, 02_PrintFlow\, 03_Dooly\가 없어야 한다.

배포 폴더 내부:
  각 앱 폴더에 SOP.html + 튜토리얼.html 존재
```

완료 후 중지하고 다음 지시를 기다린다.

---

## STEP 4 — Git 상태 확인 (스테이징 전)

```powershell
cd C:\Obsidian\GuideBook
git -c core.quotepath=false status --short
git -c core.quotepath=false diff --name-status
```

스테이징 전 정상 판단 기준:
```
정상:
  기존 루트의 01~03 파일 → D (삭제로 인식)
  새 GuideBook_배포\01~03 파일 → ?? (untracked)
  git diff --name-status에는 추적 파일 삭제(D)만 나타날 수 있음

허용:
  기존부터 존재한 untracked 구버전 문서 (37/38/40/41번 구버전)
  → STEP 0 Git 상태와 동일하면 정상

비정상:
  STEP 0 대비 42번 작업 외 새로운 예상 외 변경

참고:
  R100 또는 D+A 판정은 이후 git add 후
  git diff --cached --name-status에서 확인한다.
```

완료 후 보고 형식:
```
1. git status --short 결과
2. git diff --name-status 결과
3. D 파일 목록 (기존 01~03 위치)
4. ?? 파일 목록 (새 GuideBook_배포 위치)
5. STEP 0 대비 새로운 예상 외 변경 여부
6. 커밋 진행 가능 여부
```

완료 후 중지하고 다음 지시를 기다린다.

---

## 전체 완료 후 예상 구조

```
GuideBook\
├── GuideBook_배포\
│   ├── 01_KingTestMaker\
│   │   ├── KingTestMaker_SOP_v1.0.html
│   │   └── KingTestMaker_튜토리얼_v1.0.html
│   ├── 02_PrintFlow\
│   │   ├── PrintFlow_SOP_v1.0.html
│   │   └── PrintFlow_튜토리얼_v1.0.html
│   └── 03_Dooly\
│       ├── Dooly_SOP_v1.0.html
│       └── Dooly_튜토리얼_v1.0.html
├── GuideBook_생성기\
└── 99_공통\
```

---

## 제약

- GuideBook_생성기\ 이동 금지
- 99_공통\ 이동 금지
- .gitignore 수정 금지
- generator.py 수정 금지
- analyzer.py 수정 금지
- Move-Item은 -LiteralPath 사용
- 목적지 충돌 시 throw로 중단
- 각 STEP 완료 후 반드시 중지하고 다음 지시를 기다린다
