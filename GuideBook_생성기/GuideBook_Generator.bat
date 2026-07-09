@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: ============================================================
:: 앱별 소스 경로 매핑 (소스 분석 기능용)
:: ============================================================
set "src_KingTestMaker=C:\Obsidian\복테메이커"
set "folders_KingTestMaker=docs,electron,html,log"
set "src_PrintFlow=C:\Obsidian\PrintFlow"
set "folders_PrintFlow=Archive,command,log,MVP,sync,WORK,배포"
set "src_Dooly=C:\Obsidian\Dooly"
set "folders_Dooly=00_System,01_Project,02_Claude_Project,03_Claude_Code,05_RAG,api,docs"

:MAIN_MENU
cls
echo ========================================
echo   GuideBook Generator v1.0
echo ========================================
echo.
echo   1. 가이드북 생성
echo   2. 앱 관리
echo   3. 설정
echo   4. 종료
echo.
set /p main_choice="선택 (1-4): "

if "%main_choice%"=="1" goto APP_SELECT
if "%main_choice%"=="2" goto APP_MANAGE
if "%main_choice%"=="3" goto SETTINGS
if "%main_choice%"=="4" exit
goto MAIN_MENU

:APP_SELECT
cls
echo ========================================
echo   가이드북 생성 — 앱 선택
echo ========================================
echo.

set count=0
for /d %%d in (apps\*) do (
    set /a count+=1
    set "app[!count!]=%%~nxd"
    echo   !count!. %%~nxd
)

if %count%==0 (
    echo   등록된 앱이 없습니다. 앱 관리에서 추가하세요.
    pause & goto MAIN_MENU
)

echo   0. 이전 메뉴
echo.
set /p app_choice="선택: "
if "%app_choice%"=="0" goto MAIN_MENU
set selected_app=!app[%app_choice%]!
if "!selected_app!"=="" goto APP_SELECT

:ACTION_MENU
cls
echo ========================================
echo   [!selected_app!] 작업 선택
echo ========================================
echo.
echo   1. A  업무 매뉴얼(SOP) 생성
echo   2. B  튜토리얼(HTML) 생성
echo   3. A+B 둘 다 생성
echo   ────────────────────────────────
echo   4. 소스 폴더 분석 - guide.md 자동 생성
echo   5. 소스 분석 + A+B 한번에
echo   ────────────────────────────────
echo   6. 입력 폴더 열기
echo   7. 출력 폴더 열기
echo   0. 이전 메뉴
echo.
set /p action_choice="선택 (0-7): "

if "%action_choice%"=="1" ( python generator.py "!selected_app!" sop & pause & goto ACTION_MENU )
if "%action_choice%"=="2" ( python generator.py "!selected_app!" tutorial & pause & goto ACTION_MENU )
if "%action_choice%"=="3" ( python generator.py "!selected_app!" both & pause & goto ACTION_MENU )
if "%action_choice%"=="4" ( call :DO_ANALYZE & pause & goto ACTION_MENU )
if "%action_choice%"=="5" ( call :DO_ANALYZE & python generator.py "!selected_app!" both & pause & goto ACTION_MENU )
if "%action_choice%"=="6" ( explorer "apps\!selected_app!\input" & goto ACTION_MENU )
if "%action_choice%"=="7" ( explorer "apps\!selected_app!\output" & goto ACTION_MENU )
if "%action_choice%"=="0" goto APP_SELECT
goto ACTION_MENU

:DO_ANALYZE
:: 앱별 소스 경로 자동 매핑
set "src_path="
set "src_folders="
if "!selected_app!"=="KingTestMaker" (
    set "src_path=!src_KingTestMaker!"
    set "src_folders=!folders_KingTestMaker!"
)
if "!selected_app!"=="PrintFlow" (
    set "src_path=!src_PrintFlow!"
    set "src_folders=!folders_PrintFlow!"
)
if "!selected_app!"=="Dooly" (
    set "src_path=!src_Dooly!"
    set "src_folders=!folders_Dooly!"
)
:: 매핑에 없는 앱은 직접 입력
if "!src_path!"=="" (
    echo.
    echo [!selected_app!] 소스 폴더 경로가 등록되어 있지 않습니다.
    set /p src_path="소스 루트 경로 입력 (예: C:\Obsidian\MyApp): "
    set /p src_folders="분석할 폴더 목록 입력 (쉼표 구분, 예: docs,src,log): "
)
echo.
echo [분석 시작] !selected_app!
echo   소스: !src_path!
echo   폴더: !src_folders!
python analyzer.py "!selected_app!" "!src_path!" "!src_folders!"
exit /b

:APP_MANAGE
cls
echo ========================================
echo   앱 관리
echo ========================================
echo.
echo   1. 새 앱 생성
echo   2. 앱 목록 보기
echo   3. 앱 폴더 열기
echo   0. 이전 메뉴
echo.
set /p manage_choice="선택 (0-3): "

if "%manage_choice%"=="1" (
    echo.
    set /p new_app_name="새 앱 이름 입력: "
    if not exist "apps\!new_app_name!" (
        mkdir "apps\!new_app_name!\input\images"
        mkdir "apps\!new_app_name!\output"
        (
            echo # !new_app_name! 가이드
            echo.
            echo ## 앱 개요
            echo 이 파일을 작성한 후 가이드북 생성을 실행하세요.
            echo.
            echo ## 업무 절차
            echo.
            echo ## 자주 하는 실수
        ) > "apps\!new_app_name!\input\guide_!new_app_name!.md"
        echo.
        echo [완료] apps\!new_app_name!\ 폴더가 생성되었습니다.
        echo [다음] apps\!new_app_name!\input\guide_!new_app_name!.md 파일을 작성하거나
        echo        소스 폴더 분석(메뉴 4번)을 실행하세요.
    ) else (
        echo [안내] 이미 존재하는 앱 이름입니다.
    )
    pause & goto APP_MANAGE
)
if "%manage_choice%"=="2" (
    echo.
    echo 등록된 앱 목록:
    for /d %%d in (apps\*) do echo   - %%~nxd
    echo.
    pause & goto APP_MANAGE
)
if "%manage_choice%"=="3" ( explorer apps & goto APP_MANAGE )
if "%manage_choice%"=="0" goto MAIN_MENU
goto APP_MANAGE

:SETTINGS
cls
echo ========================================
echo   설정
echo ========================================
echo.
echo   현재 경로: %cd%
echo.
echo   1. Python 버전 확인
echo   2. 전체 폴더 구조 보기
echo   0. 이전 메뉴
echo.
set /p settings_choice="선택 (0-2): "
if "%settings_choice%"=="1" ( python --version & pause & goto SETTINGS )
if "%settings_choice%"=="2" ( tree /f & pause & goto SETTINGS )
if "%settings_choice%"=="0" goto MAIN_MENU
goto SETTINGS
