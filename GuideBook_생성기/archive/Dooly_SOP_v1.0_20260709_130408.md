# Dooly 업무 매뉴얼 (SOP)
생성일: 2026-07-07 | 버전: v1.0

---

# Dooly 가이드
생성일: 2026-07-07
소스 경로: C:\Obsidian\Dooly
분석 폴더: 00_System, 01_Project, 02_Claude_Project, 03_Claude_Code, 05_RAG, api, docs
분석 파일 수: 117개

---

## 앱 개요

### faq_data.txt
[FAQ-1] 복사기가 종이를 먹었어요 | 카테고리: 복사기
종이가 구겨진 경우 ADF를 사용하지 말고 수동(평판) 스캔으로 진행하세요. 무리하게 ADF에 넣으면 용지 걸림이 발생합니다. 복사기/스캔 SOP를 확인하세요.

[FAQ-2] 학생이 복테를 못 찾겠어요 | 카테고리: 복테
복테 보관함 배치 순서를 확인하세요. X존(고등): 고3→고2→고1, Y존(초중): 초등→중3→중2→중1 순서입니다. 학년 내 A반/B반 섹션파일 앞부분을 확인하세요. 복테 보관함 운영 SOP를 참고하세요.

[FAQ-3] 오답기록표에 끝이라고 적혀있어요 | 카테고리: 오답노트
오답노트 제본을 진행해야 합니다. 교재 전체 오답기록표를 수집하고, 20mm 링으로 제본 후 첫 페이지에 만든날짜와 오답노트를 기입하여 학생에게 전달하세요. 오답노트 제본 SOP를 참고하세요.

[FAQ-4] 연습장이 부족해요 | 카테고리: 비품
연습장 보관함은 항상 5권을 유지해야 합니다. 5권 미만이면 즉시 제작하세요(50매 양식, 12mm 링 사용). 연습장이 없는 학생은 이면지 보관함에서 이면지를 사용하도록 안내하세요.

[FAQ-5] ADF 스캔과 수동 스캔 차이가 뭐예요 | 카테고리: 복사기
ADF(자동 원고 급지)는 깨끗하고 많은 양의 종이를 한 번에 스캔할 때 사용합니다. 수동(평판) 스캔은 종이가 얇거나 구겨진 경우에 사용합니다. 구겨진 종이를 ADF에 넣으면 용지 걸림이 발생하므로 반드시 수동으로 진행하세요.

[FAQ-6] 제본링 사이즈는 어떻게 선택해요 | 카테고리: 제본기
12mm 링: 연습장, 내신모의 10회분 등 얇은 자료에 사용
### sop_data.txt
[SOP-1] 복테 제출함 관리 SOP | 카테고리: 복테
학생 하원 즉시 제출함을 비운다. 내용물은 오답기록표와 복습테스트(복테)다. 오답기록표는 챙겨서 다음 등원용 복테 제작에 활용한다. 복테가 완료된 경우 점수 기록 후 스캔하여 학생 폴더에 저장한다. 복테가 미완료인 경우 복테 보관함으로 이동한다. 원칙: 학생이 하원하면 제출함은 반드시 비운다.

[SOP-2] 복테 제작 SOP | 카테고리: 복테
학생이 제출한 오답기록표를 확인한다. 오답기록표의 날짜/페이지/문제번호를 바탕으로 복테를 제작한다. 제작 완료 후 PC 저장 후 프린트하여 복테 보관함에 보관한다. 퇴근 30분 전에 학생별 복테 프린트 후 PC 저장, 작업완료 폴더에 저장한다. 복테는 다음 등원 시 학생에게 즉시 제공 가능해야 한다.

[SOP-3] 복테 보관함 운영 SOP | 카테고리: 복테
보관함 배치 규칙: X존(고등)은 고3, 고2, 고1 순서(위에서 아래). Y존(초중)은 초등 전체, 중3, 중2, 중1 순서(위에서 아래). 학년 칸 내 A반/B반 섹션파일로 구분한다. 앞부분에 복습테스트와 프린트물, 뒷부분에 오답기록표를 보관한다. 자료 찾기는 학년(X/Y존) 후 반(A/B) 순서로 확인한다.

[SOP-4] 복테 처리 및 폐기 SOP | 카테고리: 복테
완료된 복테는 스캔 후 학생 폴더에 저장한다. 스캔 완료된 문제지는 분리수거(폐기)한다. 빠른 정답지(뒷면 백지)는 이면지 보관함으로 이동한다. 미완료 복테는 복테 보관함에 보관하여 다음 시간에 재사용한다. 완료 기준: 모든 별표(★) 문제가 큰 세모(△)로 해결된 상태.

[SOP
### README.md
# README.md
# docs\ — King Assistant OS v2.0 운영 파일

작성일: 2026-06-30
프로젝트: King Assistant OS v2.0
배포: https://dooly-eight.vercel.app

---

## 이 폴더는 무엇인가?

Vercel이 서빙하는 현재 운영 중인 파일들이다.
GitHub에 push하면 Vercel이 자동으로 이 폴더를 배포한다.
Vercel Root Directory 설정: docs (공백 없이)

---

## 운영 구조

```
GitHub (코드 저장)
    ↓ git push → 자동 배포
Vercel (PWA 서빙 + API 프록시)
    ├── docs/api/gemini.js  → Gemini API 프록시
    └── docs/api/tasks.js   → Supabase Task API 프록시
        ↓
Supabase (Task DB — 기기간 동기화)
```

---

## 파일 목록 및 설명

### HTML 화면 파일

| 파일 | URL | 설명 |
|------|-----|------|
| index.html | /index.html | 홈 화면 (메인 진입점) |
| 02_Task_v1.html | /02_Task_v1.html | 업무 Task 관리 화면 (Supabase 연동) |
| 03_SOP_v1.html | /03_SOP_v1.html | SOP 조회 화면 |
| 04_FAQ_v1.html | /04_FAQ_v1.html | FAQ 조회 화면 |
| 05_Notice_v1.html | /05
### 02_Task_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>업무 관리</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  .sync-bar {
    background: #0b0f1a;
    padding: 6px 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 1px solid rgba(77,163,255,0.15);
    flex-shrink: 0;
  }

  header {
    background: #0b0f1a;
    border-bottom: 1px solid rgba(77,163,255,0.2);
    padding: 16px 20px;
    display: flex;
    align-it
### 03_SOP_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>SOP</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  header {
    background: #0b0f1a;
    border-bottom: 1px solid rgba(77,163,255,0.2);
    padding: 16px 20px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  header h1 { font-size: 18px; font-weight: 700; }

  main {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    padding-bottom: 8px;
  }

  .sear
### 04_FAQ_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>FAQ</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  header {
    background: #0b0f1a;
    border-bottom: 1px solid rgba(77,163,255,0.2);
    padding: 16px 20px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  header h1 { font-size: 18px; font-weight: 700; }

  main {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    padding-bottom: 8px;
  }

  .sear
### 05_Notice_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0;url=index.html">
<title>공지사항</title>
</head>
<body>
<script>location.replace('index.html');</script>
</body>
</html>
### 06_Dooly_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>둘리 (Dooly)</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  header {
    background: #0b0f1a;
    border-bottom: 1px solid rgba(77,163,255,0.2);
    padding: 16px 20px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
    flex-shrink: 0;
  }
  header h1 { font-size: 18px; font-weight: 700; }
  header p { font-size: 12px; opacity: 0.5; margin-top: 2px; }

  /* 채팅 영역
### 07_Settings_v1.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>설정 — KING Assistant OS</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  header {
    background: #0b0f1a;
    border-bottom: 1px solid rgba(77,163,255,0.2);
    padding: 16px 20px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  header h1 { font-size: 18px; font-weight: 700; color: #ffffff; }

  main {
    flex: 1;
    overflow-y: auto;
    padding: 20px 16p
### index.html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>KING Assistant OS</title>
<link rel="manifest" href="/Dooly/manifest.json">
<meta name="theme-color" content="#4da3ff">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="KING">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0b0f1a;
    color: #ffffff;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100dvh;
    max-width: 430px;
    margin: 0 auto;
  }

  header {
    background: #0b0f1a;
    b
### data.js
// cache-bust: 2026-06-28
// data.js
// King Assistant OS v1.0
// SOP + FAQ 공통 데이터 파일
// 수정 시 이 파일 1곳만 수정하면 SOP/FAQ/Dooly 전체 반영

var SOPS = [

  // ===== 복테 =====
  {
    id: 1, title: '복테 제출함 관리 SOP', category: '복테',
    keywords: ['복테', '제출함', '하원'],
    body: '1. 학생 하원 즉시 제출함을 비운다.\n2. 내용물: 오답기록표 + 복습테스트(복테).\n3. 오답기록표: 챙겨서 다음 등원용 복테 제작에 활용.\n4. 복테(완료): 점수 기록 후 스캔하여 학생 폴더에 저장.\n5. 복테(미완료): 복테 보관함으로 이동.\n6. 원칙: "학생이 하원하면 제출함은 반드시 비운다."'
  },
  {
    id: 2, title: '복테 제작 SOP', category: '복테',
    keywords: ['복테 제작', '복테 만들기', '오답기록표 제작'],
    body: '1. 학생이 제출한 오답기록표를 확인한다.\n2. 오답기록표의 날짜/페이지/문제번호를 바탕으로 복테를 제작한다.\n3. 제작 완료 후 PC 저장 → 프린트 → 복테 보관함에 보관.\n4. 퇴근 30분 전: 학생별 복테 프린트 → PC 저장 → 작업완료 폴더 저장.\n5. 복테는 다음 등원 시 학생에게 즉시 제공 가능해야 한다.'
  },
  {
    id: 3, title: '복테 보관함 운영 SOP', category: '복테'
### service-worker.js
// service-worker.js
// King Assistant OS v1.0 PWA

const CACHE_NAME = 'king-assistant-v3';
const URLS_TO_CACHE = [
  '/Dooly/',
  '/Dooly/index.html',
  '/Dooly/02_Task_v1.html',
  '/Dooly/03_SOP_v1.html',
  '/Dooly/04_FAQ_v1.html',
  '/Dooly/05_Notice_v1.html',
  '/Dooly/06_Dooly_v1.html',
  '/Dooly/07_Settings_v1.html',
  '/Dooly/data.js',
  '/Dooly/manifest.json',
  '/Dooly/icons/icon-192.png',
  '/Dooly/icons/icon-512.png'
];

// 설치: 모든 파일 캐시에 저장
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(URLS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// 활성화: 이전 캐시 삭제
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      re
### manifest.json
{
  "name": "Dooly",
  "short_name": "Dooly",
  "description": "킹수학 조교 AI 비서",
  "start_url": "/06_Dooly_v1.html",
  "display": "standalone",
  "background_color": "#0b0f1a",
  "theme_color": "#4da3ff",
  "icons": [
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}

---

## 주요 화면 및 메뉴
(html/jsx 파일에서 자동 추출됩니다)

---

## 업무 절차

### 00_SESSION_CLOSE_TEMPLATE.md
# 00_SESSION_CLOSE_TEMPLATE.md
# 세션 종료 Claude Code 프롬프트 템플릿
# ※ 매 세션 종료 시 이 템플릿을 복사해서 사용

---

## 📌 사용법
1. 아래 프롬프트에서 {버전}, {다음번호} 부분만 수정
2. Claude Code 입력창에 붙여넣기

---

## ✅ 세션 종료 Claude Code 프롬프트

```
아래 작업을 순서대로 실행해줘.

## 1. SESSION_HANDOVER 백업
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md 파일을
C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\{다음번호}_SESSION_HANDOVER_v{버전}.md 로 복사

## 2. SESSION_HANDOVER 업데이트
C:\Users\USER\Downloads\02_SESSION_HANDOVER_v{버전}.md 파일을
C:\Obsidian\Dooly\00_System\02
### 01_PROJECT_MASTER.md
# PROJECT_MASTER.md

# King Assistant OS v1.0

## 프로젝트 정보

프로젝트명

King Assistant OS v1.0

AI 비서

둘리(Dooly)

---

## 프로젝트 목적

학원 전체 운영 시스템이 아닌

조교 운영 시스템 구축을 목표로 한다.

원장의 반복 업무를 표준화하고 자동화하여
조교 교육 및 업무 운영 효율을 향상시킨다.

---

## 현재 단계

설계 단계 (Design Phase)

현재 상태

* 기획 완료
* MVP 범위 확정
* 문서 체계 확정
* Implementation Plan 작성 완료

---

## MVP 범위

* 업무 관리
* SOP 검색
* FAQ 검색
* 공지사항 조회
* 둘리 질의응답

---

## 핵심 DB

* Task DB
* Knowledge DB
* Log DB

---

## 핵심 문서

01_King_Assistant_OS_v1.0.md

02_SOP_v1.0.md

03_Exce
### 02_SESSION_HANDOVER.md
# 02_SESSION_HANDOVER.md v15.0

작성일: 2026-06-30
세션: 2026-06-30 (오후)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #55 완료 — 04_Runtime 아카이브 + README 작성

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 56번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git pu
### 03_DEVELOPMENT_RULE_v1.0.md
좋아. 이건 앞으로 프로젝트 전체 “규칙 엔진”이 되는 문서라서, 
**바로 Obsidian에 넣고 그대로 기준으로 써도 되는 완성본**으로 줄게.

---

# 📄 DEVELOPMENT_RULE_v1.0.md (완성본)

````md
# DEVELOPMENT_RULE_v1.0.md

# King Assistant OS v1.0
# Development Operating Rules (Dooly Project)

Version: v1.0  
Status: Active Rule Set  
Owner: Dooly System  

---

# 1. 목적 (Purpose)

본 문서는 King Assistant OS v1.0 개발 과정에서

- 파일 구조
- 버전 관리
- 작업 지시 방식
- 코드 생성 방식
- Git 운영 방식
- 문서 관리 방식

을 통합적으로 정의하는 **개발 운영 규칙(Development OS)** 이다.

---

# 2. 핵심 원칙 (Core Principles
### 04_PROJECT_GUIDE_v1.0.md
# KING Assistant OS — 프로젝트 전체 가이드
> 킹수학 조교 운영 시스템 구축 전체 과정
> 작성일: 2026-06-26
> 최신 커밋: 4ab9bd9 — feat: FastAPI static HTML serving for mobile access

---

## 1. 프로젝트 개요

### 1-1. 목적

킹수학 학원 조교의 반복 업무를 표준화하고, AI 비서 둘리(Dooly)를 통해 업무 운영 효율을 향상시킨다.
학원 전체 운영 시스템이 아닌, **조교 운영 시스템** 구축이 목표다.

#### MVP 구성

MVP 5개 기능:
- 업무 관리 (Task)
- SOP 검색
- FAQ 검색
- 공지사항 조회 (홈 통합)
- 둘리 질의응답 (RAG 기반 AI)

### 1-2. 기술 스택

#### 스택 구성 요약

| 영역 | 기술 |
|------|------|
| 프론트엔드 | Single-page HTML + localStorage (백엔드 없음) |
| AI 서버 | FastAPI + ChromaDB + Ol
### 05_WORKFLOW_GUIDE_v1.0.md
# 05_WORKFLOW_GUIDE_v1.0.md
# King Assistant OS v1.0
# 프로젝트 운영 워크플로우 가이드

Version: v1.0
Date: 2026-06-27

---

# 1. 역할 분담 (분업 원칙)

```
검토 · 설계 · 인수인계 작성
→ claude.ai (이 채팅창)

실행 · 파일 생성 · git push
→ VS Code 안의 Claude Code 입력창
```

| 작업 종류 | 도구 |
|---|---|
| 폴더 구조 검토 | claude.ai |
| 파일명 규칙 검토 | claude.ai |
| 작업지시서 md 작성 | claude.ai |
| 인수인계 md 작성 | claude.ai |
| 파일 생성 / 수정 | Claude Code |
| git add / commit / push | Claude Code |
| 서버 실행 / 테스트 | Claude Code or 직접 실행 |

---

# 2. 백업 체계 (이중 백업)

```
### 02_SESSION_HANDOVER.md
# SESSION_HANDOVER.md

작성일 : 2026-06-25

---

# 현재 상태

King Assistant OS v1.0

AI 비서 : 둘리(Dooly)

현재 단계 :

HTML Prototype Phase (Phase 0)

---

# 완료 작업

* 프로젝트 비전 정의
* MVP 범위 확정
* 역할 구조 정의
* SOP 구조 정리
* FAQ 구조 정리
* 문서 체계 정리
* Claude Project 구조 확정
* Claude Code 운영 방식 정리
* Implementation Plan 작성 완료
* UI Wireframe v1.0 완료
* HTML Prototype v1.0 생성 완료 (2026-06-25)
  - index.html (홈 + 달력)
  - 02_Task_v1.html (업무 관리)
  - 03_SOP_v1.html (SOP 검색)
  - 04_FAQ_v1.html (FAQ)
  - 05_Notice_v1.html (공지사항)
  - 
### 05_SESSION_HANDOVER_v1.md
# SESSION_HANDOVER.md

작성일: 2026-06-26

---

# 현재 상태

King Assistant OS v1.0
AI 비서: 둘리(Dooly)
현재 단계: Phase 6 완료 (자습실 PC 서버 구성 완료)

---

# 완료 작업 전체 목록

## Phase 0~5 (이전 세션 완료)
- HTML 프로토타입 7개 파일 생성
- SOP 22개, FAQ 22개, Dooly 키워드 23개
- RAG 서버 구축 (FastAPI + ChromaDB + Ollama)
- Dooly 모델 선택, 출처 태그, 대화 기록 유지
- 스마트폰 접속 구현

## 오늘 세션 완료 작업

### 32번 작업지시서 — 탭 404 오류 수정
- server.py에 리다이렉트 라우트 추가
- /{filename}.html → /app/{filename}.html 자동 리다이렉트
- 커밋: 355bc8e

### 33번 작업지시서 — 한국어 전용 답변
- server.py 시스템 프롬프트
### 06_SESSION_HANDOVER_v2.md
# SESSION_HANDOVER.md v2.0

작성일: 2026-06-26
세션: 2026-06-26 (오늘 세션)
프로젝트 버전: King Assistant OS v1.0
아키텍처 버전: AI OS v1.0
현재 마일스톤: Phase 6 완료 (자습실 PC 서버 구성 완료)

---

# 1. 현재 상태

## 완료 단계

| Phase | 내용 | 상태 |
|-------|------|------|
| Phase 0 | 환경 준비 | ✅ |
| Phase 1 | HTML 프로토타입 | ✅ |
| Phase 2 | 데이터 확장 (SOP/FAQ 22개) | ✅ |
| Phase 3 | UI 버그 수정 | ✅ |
| Phase 4 | RAG 서버 구축 | ✅ |
| Phase 5 | Dooly AI 고도화 | ✅ |
| Phase 6 | 자습실 PC 서버 구성 | ✅ |

---

# 2. 기술 스택

| 영역 | 기술 |
|------|------|
| Frontend | HTM
### 07_SESSION_HANDOVER_v3.md
# SESSION_HANDOVER.md v3.0

작성일: 2026-06-26
세션: 2026-06-26
프로젝트 버전: King Assistant OS v1.0
아키텍처 버전: AI OS v1.0
현재 마일스톤: Phase 6 완료 (자습실 PC 서버 구성 완료)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. SESSION_HANDOVER.md 읽기
2. 04_PROJECT_GUIDE_v1_0.md 읽기
3. 현재 마일스톤 파악
4. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
작업지시서 번호는 반드시 순서를 유지한다.

---

# 1. 프로젝트 철학

King Assistant OS는 킹수학 학원 조교 운영을 위한 AI 비서 시스템이다.
학원 전체 운영 시스템이 아닌, 조교 업무 표준화와 효율화가 목표다.

## 핵심 원칙

- HTML 우선: 별도 프레임워크 없이 HTML + Vanilla 
### 08_SESSION_HANDOVER_v4.0.md
# SESSION_HANDOVER.md

작성일 : 2026-06-25

---

# 현재 상태

King Assistant OS v1.0

AI 비서 : 둘리(Dooly)

현재 단계 :

HTML Prototype Phase (Phase 0)

---

# 완료 작업

* 프로젝트 비전 정의
* MVP 범위 확정
* 역할 구조 정의
* SOP 구조 정리
* FAQ 구조 정리
* 문서 체계 정리
* Claude Project 구조 확정
* Claude Code 운영 방식 정리
* Implementation Plan 작성 완료
* UI Wireframe v1.0 완료
* HTML Prototype v1.0 생성 완료 (2026-06-25)
  - index.html (홈 + 달력)
  - 02_Task_v1.html (업무 관리)
  - 03_SOP_v1.html (SOP 검색)
  - 04_FAQ_v1.html (FAQ)
  - 05_Notice_v1.html (공지사항)
  - 
### 09_SESSION_HANDOVER_v5.0.md
# SESSION_HANDOVER.md v4.0

작성일: 2026-06-27
세션: 2026-06-26 ~ 2026-06-27
프로젝트 버전: King Assistant OS v1.0
아키텍처 버전: AI OS v1.0
현재 마일스톤: Phase 6 완료 → Phase 7 (PWA) 진행 예정

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1_0.md 읽기
3. 현재 마일스톤 파악
4. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
작업지시서 번호는 반드시 순서를 유지한다. (현재 33번까지 완료)
다음 작업은 34번부터 시작한다.

---

# 1. 프로젝트 철학

King Assistant OS는 킹수학 학원 조교 운영을 위한 AI 비서 시스템이다.
학원 전체 운영 시스템이 아닌, 조교 업무 표준화와
### 09_SESSION_HANDOVER_v8.0.md
# 02_SESSION_HANDOVER.md v7.0

작성일: 2026-06-28
세션: 2026-06-28 (야간)
프로젝트 버전: King Assistant OS v1.0 → v2.0 전환 준비
현재 마일스톤: Phase 8 완료 준비 + v2.0 설계 확정

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 50번부터 시작한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push

### 10_SESSION_HANDOVER_v6.0.md
# SESSION_HANDOVER.md v5.0

작성일: 2026-06-28
세션: 2026-06-27 ~ 2026-06-28
프로젝트 버전: King Assistant OS v1.0
현재 마일스톤: Phase 7 완료 (PWA + GitHub Pages 배포)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
작업지시서 번호는 반드시 순서를 유지한다. (현재 45번까지 완료)
다음 작업은 46번부터 시작한다.

---

# 1. 프로젝트 철학

King Assistant OS는 킹수학 학원 조교 운영을 위한 AI 비서 시스템이다.
학원 전체 운영 시스템이 
### 11_SESSION_HANDOVER_v7.0.md
# 02_SESSION_HANDOVER.md v6.0

작성일: 2026-06-28
세션: 2026-06-28
프로젝트 버전: King Assistant OS v1.0
현재 마일스톤: Phase 8 진행 중 (Task API + 스마트폰 테스트)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
작업지시서 번호는 반드시 순서를 유지한다. (현재 48번까지 진행 중)
다음 작업은 49번부터 시작한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS 
### 12_SESSION_HANDOVER_v8.0.md
# 02_SESSION_HANDOVER.md v8.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v1.0 → v2.0 전환 진행 중
현재 마일스톤: Task #50 진행 중 (Claude API + Cloudflare Worker 연동)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 50번 이어서 진행한다 (Step 4부터).

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude C
### 14_SESSION_HANDOVER_v9.0.md
# 02_SESSION_HANDOVER.md v9.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v1.0 → v2.0 전환 진행 중
현재 마일스톤: Task #50 진행 중 (Gemini API + Cloudflare Worker 연동)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 50번 작업지시서 (v2.0) Step 1부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- C
### 15_SESSION_HANDOVER_v10.0.md
# 02_SESSION_HANDOVER.md v10.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v2.0 전환 진행 중
현재 마일스톤: Task #51 — Vercel 이전 (Gemini API 위치 문제 해결)

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 51번 작업지시서부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일
### 16_SESSION_HANDOVER_v11.0.md
# 02_SESSION_HANDOVER.md v11.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #51 완료 — Vercel + Gemini API 연동 성공

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 52번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push
### 17_SESSION_HANDOVER_v12.0.md
# 02_SESSION_HANDOVER.md v11.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #51 완료 — Vercel + Gemini API 연동 성공

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 52번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push
### 17_SESSION_HANDOVER_v13.0.md
# 02_SESSION_HANDOVER.md v12.0

작성일: 2026-06-29
세션: 2026-06-29 (주간)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #52 전체 완료 — PWA 아이콘 + Gemini UI 개선

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 53번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push
### 18_SESSION_HANDOVER_v14.0.md
# 02_SESSION_HANDOVER.md v13.0

작성일: 2026-06-30
세션: 2026-06-30 (주간)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #52 전체 완료 + 출처 태그 안정화

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 53번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push
- 인수인계 md 파일
### 18_SESSION_HANDOVER_v15.0.md
# 02_SESSION_HANDOVER.md v14.0

작성일: 2026-06-30
세션: 2026-06-30 (주간)
프로젝트 버전: King Assistant OS v2.0
현재 마일스톤: Task #53 완료 — Supabase Task 동기화

---

# 0. AI 인수인계 규칙

새 세션의 AI는 반드시 다음 순서로 시작한다.

1. 이 파일 (02_SESSION_HANDOVER.md) 읽기
2. 04_PROJECT_GUIDE_v1.0.md 읽기
3. 05_WORKFLOW_GUIDE_v1.0.md 읽기
4. 현재 마일스톤 파악
5. 작업지시서 번호 순서대로 작업 진행

이미 완료된 작업은 다시 구현하지 않는다.
다음 작업은 54번부터 진행한다.

---

# 1. 워크플로우 원칙 (반드시 준수)

- claude.ai: 검토 + 작업지시서 md 파일 생성 (다운로드 제공)
- Claude Code (VS Code): md 파일 읽고 실행 + git push
- 인수인계 
### iPhone_PWA_INSTALL_GUIDE.md
# 📱 아이폰 Dooly 설치 가이드

> 아이폰에서 Dooly를 홈 화면 앱으로 설치하는 방법입니다.
> **반드시 Safari 브라우저**를 사용해야 합니다.

---

## ✅ 설치 전 확인사항

- [ ] 아이폰 iOS 16.4 이상
- [ ] Safari 브라우저 사용 (Chrome, 네이버앱 불가)
- [ ] 인터넷(와이파이 또는 LTE) 연결 상태

---

## 📋 설치 순서

### Step 1 — Safari로 접속

Safari 주소창에 아래 URL 입력:

https://2passion.github.io/Dooly/

⚠️ Chrome이나 다른 브라우저로 열면 설치 버튼이 나오지 않습니다.
반드시 Safari로 열어야 합니다.

---

### Step 2 — 공유 버튼 탭

화면 하단 가운데의 공유 버튼(□↑)을 탭합니다.

---

### Step 3 — 홈 화면에 추가

공유 메뉴에서 스크롤을 내려
"홈 화면에 추가" 를 탭합니다.

---

### Ste
### SESSION_REPORT_20260629.md
# 📋 세션 요약 보고서
# King Assistant OS — 2026-06-29 작업 기록

---

## 1. 오늘 완료된 작업 전체

```
Task #52  ──────────────────────────────────────────────
  52-A   PWA 아이콘 파일 교체 (공룡 + 흰색 배경)        ✅
  52-B   manifest.json 아이콘 경로 수정                  ✅
  52-C   Gemini 출처 번호 표시 (시스템 프롬프트)         ✅
  52-D   질문 말풍선 텍스트 흰색으로 수정                ✅

Task #52-E ─────────────────────────────────────────────
  52-E1  서비스워커 v2 → v3 캐시 버전 업그레이드         ✅
  52-E2  Gemini 출처 FAQ 초록 / SOP 주황 태그 UI         ✅
  52-E3  Gemini 답변
### 01_King_Assistant_OS_v1.0.md
# King Assistant OS v1.0

AI 비서 : 둘리(Dooly)

## Vision

King Assistant OS v1.0은

조교 교육
업무 관리
SOP 관리

를 수행하는 조교 운영 시스템이다.
### 02_SOP_v1.0.md
# SOP

## 복테 관리

## 오답노트 관리

## 비품 관리

## 연습장 관리

## 제출함 관리

## 제본기 관리

## 복사기 관리
### 03_Exception_Manual_v1.0.md
# 예외상황 매뉴얼

## 파일 분실

## 인터넷 장애

## 복사기 오류

## 학생 자료 누락

## 연습장 부족

## 긴급 상황
### 04_FAQ_v1.0.md
# FAQ

Q.
복사기가 종이를 먹었어요

Q.
학생이 복테를 못 찾겠어요

Q.
오답기록표에 끝이라고 적혀있어요

Q.
연습장이 부족해요
### 06_Task_Management_v1.0.md
# Task 상태

Pending

In Progress

Review

Completed

Hold
### 08_King_Assistant_OS_v1.0_Implementation_Plan.md
# 08_King_Assistant_OS_v1.0_Implementation_Plan.md

---

# King Assistant OS v1.0 Implementation Plan

Version : v1.0
Status : Design Phase
AI Assistant : 둘리(Dooly)

---

# 1. 프로젝트 개요

## 1.1 프로젝트명

King Assistant OS v1.0

AI 비서

```text
둘리(Dooly)
```

---

## 1.2 프로젝트 목적

본 프로젝트는 학원 전체 운영 시스템이 아닌,

```text
조교 운영 시스템
```

구축을 목표로 한다.

원장이 반복적으로 수행하는 다음 업무를 표준화하고 자동화한다.

```text
조교 교육
업무 지시
업무 확인
업무 보고 확인
SOP 안내
FAQ 응답
공지 전달
```

이를 AI 비서 둘리(Dooly)가 지원하여 조교 운영 효율성을 향상시킨다.

---

# 2. MVP 범위

## 포함
### 09_UI_Wireframe_v1.0.md
📄 09_UI_Wireframe_v1.0.md (FULL FINAL)
# 09_UI_Wireframe_v1.0.md

# King Assistant OS v1.0
# UI Wireframe Specification

Version: v1.0  
Status: Design Freeze Candidate  
Device: Mobile First (Primary)

---

# 1. 문서 목적

본 문서는 King Assistant OS v1.0의 UI 구조를 정의하며,
HTML Prototype 및 이후 React/PWA 개발의 기준 설계도이다.

이 문서의 모든 구조는 실제 구현 기준이다.

---

# 2. 시스템 UI 철학

## 2.1 핵심 목표

- 모바일 우선 (Mobile First)
- 최소 클릭 구조
- 텍스트 중심 UI
- 업무 흐름 최적화
- 즉시 사용 가능 UX

---

## 2.2 UX 원칙

- 1탭 = 이동
- 2탭 = 실행
- 3클릭 이내 모든 기능 접근

### 10_HTML_Prototype_v1.0.md
# 📄 10_HTML_Prototype_v1.0.md (FULL FINAL)

````md id="htmlproto001"
# 10_HTML_Prototype_v1.0.md

# King Assistant OS v1.0
# HTML Prototype Specification

Version: v1.0  
Status: Prototype Phase  
Dependency: 09_UI_Wireframe_v1.0.md  
Target: Mobile First (PWA Ready)

---

# 1. 목적

본 문서는 King Assistant OS v1.0의 UI Wireframe을 기반으로
실제 동작 가능한 HTML 프로토타입을 생성하기 위한 설계 문서이다.

이 단계는 "디자인"이 아니라 "실사용 검증 단계"이다.

---

# 2. 핵심 목표

```text
1. 실제 클릭 가능한 UI 생성
2. 모바일에서 사용 가능
3. DB 없이 동작
4. 로컬 상태 기반 기능 구현
5. 사용자
### 11_Dooly_Architecture_Guide_v1.0.md
# Dooly 앱 구조 설명서 v1.0

작성일: 2026-06-29
프로젝트: King Assistant OS v2.0
문서 목적: Dooly 앱의 전체 구조, AI 답변 흐름, Task 동기화 흐름 설명

---

## 1. 전체 구조 개요

Dooly 앱은 5개 레이어로 구성된다.

```
┌─────────────────────────────────────────────────────┐
│  레이어 1 — 개발 환경 (킹스 작업 공간)               │
│  claude.ai (설계)  │  Claude Code (실행)  │  Obsidian │
└─────────────────────┬───────────────────────────────┘
                      │ git push
┌─────────────────────▼───────────────────────────────┐
│  레이어 2 — 배포 인프라                  
### 12 Dooly_User_Guide_v1.0.md
# Dooly 사용 가이드 v1.0
# King Assistant OS — 조교용

작성일: 2026-06-29

---

## Dooly란?

킹수학 학원 조교를 위한 AI 업무 도우미예요.
FAQ 검색, SOP 확인, 업무 관리를 도와줘요.

---

## 접속 방법

스마트폰 브라우저에서 아래 주소로 접속:

```
https://dooly-eight.vercel.app/06_Dooly_v1.html
```

**지원 브라우저:**
- Chrome ✅
- 삼성 브라우저 ✅
- 네이버 앱 ❌
- 카카오톡 인앱 ❌

---

## 화면 구성

| 탭 | 기능 |
|-----|------|
| 홈 | 업무 현황 + 캘린더 |
| 업무 | 업무 목록 관리 |
| SOP | 표준 운영 절차 검색 |
| FAQ | 자주 묻는 질문 |
| Dooly | AI 챗봇 질문 |
| 설정 | 환경 설정 |

---

## Dooly AI 사용법

### 모드 선택

| 모드 | 설명 | 인터넷 필
### 12_Dooly_Architecture_Guide_v2.0.md
# Dooly 앱 구조 설명서 v2.0

작성일: 2026-06-29
프로젝트: King Assistant OS v2.0
이전 버전: 11_Dooly_Architecture_Guide_v1.0.md
문서 목적: Dooly 앱의 전체 구조, AI 답변 흐름, Task 동기화 흐름 설명 (Vercel 이전 반영)

---

## ⚡ v1.0 → v2.0 주요 변경사항 요약

| 항목 | v1.0 (이전) | v2.0 (현재) | 변경 이유 |
|------|------------|------------|----------|
| PWA 서빙 | Cloudflare Pages | Vercel | 관리 통합 |
| API 프록시 | Cloudflare Worker | Vercel Function | 한국 서버 위치 차단 문제 |
| AI 모델 | gemini-1.5-flash | gemini-2.5-flash | 모델 업데이트 |
| 배포 URL | dooly-f4m.pages.dev | d
### 13_Dooly_User_Guide_v2.0.md
# 13_Dooly_User_Guide_v2.0.md
# 둘리(Dooly) 사용 가이드

작성일: 2026-06-30
버전: v2.0
대상: 킹수학 학원 조교

---

## Dooly란?

킹수학 학원 조교를 위한 AI 업무 도우미입니다.

- 복사기, 복테, 오답노트 등 업무 질문에 바로 답변
- SOP(표준 운영 절차) 검색
- FAQ 검색
- 업무(Task) 관리

접속 주소: **https://dooly-eight.vercel.app/06_Dooly_v1.html**

---

# B-1. 윈도우 컴퓨터 (PC / 노트북)

## 1. 접속 방법

1. Chrome 브라우저 열기
2. 주소창에 입력:
   ```
   https://dooly-eight.vercel.app/06_Dooly_v1.html
   ```
3. Enter

## 2. 바탕화면 바로가기 만들기 (선택)

1. Chrome에서 Dooly 페이지 접속
2. 오른쪽 상단 점 3개(⋮) 클릭
3. **저장 
### 05_Dooly_System_Prompt_v1.0.md
# King Assistant OS v1.0

AI 비서 : 둘리(Dooly)

## 역할

당신은 King Assistant OS의 AI 비서 둘리(Dooly)이다.

목표는 조교 교육, 업무 관리, SOP 관리, 운영 기록 관리를 지원하는 것이다.

---

# 핵심 원칙

1. 추측 금지

모르는 내용은 추측하지 않는다.

반드시

"확인이 필요합니다."

라고 답변한다.

---

2. SOP 우선

질문이 들어오면

FAQ
→ SOP
→ 공지사항

순으로 검색한다.

---

3. 최신 문서 우선

문서 충돌 시

최신 버전
최신 수정일

기준으로 답변한다.

---

4. 업무 누락 방지

업무가 완료되지 않았으면

반드시 상태를 확인한다.

상태

- Pending
- In Progress
- Review
- Completed
- Hold

---

5. 조교 지원 우선

주요 역할

- 신규 조교 교육
- 업무 안내
- FAQ 응답
- SOP 검색
- 업무 진행 지원

### 07_Claude_Code_Operation_v1.0.md
# Claude Code 운영 규칙

세션 종료

SESSION_HANDOVER.md 작성

↓

Git Commit

↓

Git Push

세션 시작

SESSION_HANDOVER.md 읽기

↓

PROJECT_MASTER.md 읽기

↓

작업 재개
### 11_Order_HTMLPrototype_v1.0.md
# 11_Order_HTMLPrototype_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-25

---

# 작업 시작 전 필수 확인

아래 파일을 순서대로 읽어라.

```
C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\00_System\03_DEVELOPMENT_RULE_v1.0.md
C:\Obsidian\Dooly\01_Project\09_UI_Wireframe_v1.0.md
C:\Obsidian\Dooly\01_Project\10_HTML_Prototype_v1.0.md
```

---

# 작업 목표

King Assistant OS v1.0 HTML Prototype 전체 생성.

10_HTML_Prototyp
### 12_Order_UI_v2.0.md
# 12_Order_UI_v2.0.md
# King Assistant OS — UI 수정 작업지시서

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html
C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html

---

# [수정 1] index.html — 홈 화면

## 업무 현황 카드
순서: 대기중(왼쪽) → 진행중(가운데) → 완료(오른쪽)
localStorage tasks 배열에서 각각 카운트:
- 대기중 = status === 'pending'
- 진행중 = status === 'in_progress'
- 완료   = status === 'completed'

## 빠른 실행 버튼 6개 전부 삭제

## 업무 현황 카드 아래에 "업무" 섹션 추가
- 섹션 제목: "업무"
- localStorage tasks 배열을 읽어서 카드로 표시
- 카드 구성: 제목 / 담당자 / 우선순위 신호등(urgent=🔴 to
### 13_Order_Data_v2.0.md
# 13_Order_Data_v2.0.md
# King Assistant OS — SOP/FAQ/Dooly 데이터 전면 교체 작업지시서

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html

HTML 구조/디자인은 건드리지 않는다.
JavaScript의 데이터 배열만 교체한다.

---

# [수정 1] 03_SOP_v1.html — SOP 데이터 전면 교체

## 카테고리 필터 변경
기존: ['전체', '업무', '예외', '비품', '복테', '오답노트']
변경: ['전체', '복테', '오답노트', '비품', '장비', '루틴']

## SOPS 배열 전면 교체 (기존 5개 → 13개)

```javascript
var SOPS = [

  // ===== 복테 ====
### 14_Order_Home_v3.0.md
# 14_Order_Home_v3.0.md
# King Assistant OS — 홈 화면 개편 + JSON 템플릿 기능

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html
C:\Obsidian\Dooly\04_Runtime\05_Notice_v1.html

---

# [수정 1] index.html — 홈 화면 전면 개편

## 변경 사항 요약
- 업무 현황 카드 클릭 시 02_Task_v1.html 이동
- 업무 섹션 삭제
- 공지 섹션을 05_Notice_v1.html과 동일한 데이터로 표시
  (아코디언 방식 그대로, 홈에서 바로 열림)
- Bottom Nav의 "공지" 탭은 유지 (index.html과 동일 데이터)

## 상세 구조

```
Header: King Assistant OS

인사말: 안녕하세요, 둘리(Dooly)입니다.

[업무 현황 카드] ← 전체 카드 클릭 시 02_Task_v1.html 이동
  대기중 N 
### 15_Order_UX_v1.0.md
# 15_Order_UX_v1.0.md
# KING Assistant OS — UX 전체 수정 작업지시서

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html
C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\05_Notice_v1.html

---

# [수정 1] 전체 파일 — "King" → "KING" 텍스트 수정

모든 HTML 파일에서:
- <title>King Assistant OS</title> → <title>KING Assistant OS</title>
- header h1: "King Assistant OS" → "KING Assistant OS"
- body 내 "King Assist
### 16_Order_Task_FAQ_v1.0.md
# 16_Order_Task_FAQ_v1.0.md
# KING Assistant OS — FAQ 태그 + 업무관리 개편

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html

---

# [수정 1] 04_FAQ_v1.html — 카테고리 태그 추가

## 카테고리 목록
['전체', '복사기', '복테', '오답노트', '비품', '제본기']

## 각 FAQ 항목에 category 필드 추가
기존 FAQS 배열에 category 추가:
```javascript
{ id: 1, question: '복사기가 종이를 먹었어요',         category: '복사기', answer: '...' },
{ id: 2, question: '학생이 복테를 못 찾겠어요',         category: '복테',   answer: '...' },
{ id: 3,
### 17_Order_Calendar_Settings_v1.0.md
# 17_Order_Calendar_Settings_v1.0.md
# KING Assistant OS — 홈 달력 + 설정 탭

---

# 수정/생성 대상
C:\Obsidian\Dooly\04_Runtime\index.html       (수정)
C:\Obsidian\Dooly\04_Runtime\07_Settings_v1.html  (신규 생성)
C:\Obsidian\Dooly\04_Runtime\*.html 전체       (네비게이션에 설정 탭 추가)

---

# [수정 1] index.html — 홈 달력 추가

## 달력 위치
업무 현황 카드 아래, 공지사항 섹션 위에 배치

## 달력 구조
```
[◀ 2026년 6월 ▶]

일  월  화  수  목  금  토
     1   2   3   4   5   6
 7   8   9  10  11  12  13
14  15  16  17  18  19  20
21  22  23  24  25  26  27
28  29  30
### 18_Order_SOP_v2.0.md
# 18_Order_SOP_v2.0.md
# KING Assistant OS — SOP 데이터 추가

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html

---

# 작업 방식
HTML 구조/디자인은 건드리지 않는다.
JavaScript의 SOPS 배열과 CATEGORIES 배열만 수정한다.

---

# [수정 1] CATEGORIES 배열 변경

기존:
```javascript
var CATEGORIES = ['전체', '복테', '오답노트', '비품', '장비', '루틴'];
```

변경:
```javascript
var CATEGORIES = ['전체', '복테', '오답노트', '채점', '비품', '장비', '루틴', '학생관리', '예외상황'];
```

---

# [수정 2] SOPS 배열에 아래 9개 항목 추가

기존 13개 배열 끝에 이어서 추가한다. id는 14번부터 시작.

```javascript
  //
### 19_Order_FAQ_Dooly_v2.0.md
# 19_Order_FAQ_Dooly_v2.0.md
# KING Assistant OS — FAQ 추가 + Dooly 키워드 추가

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html

---

# 작업 방식
HTML 구조/디자인은 건드리지 않는다.
JavaScript 데이터 배열만 수정한다.

---

# [수정 1] 04_FAQ_v1.html — CATEGORIES 배열 변경

기존:
```javascript
var CATEGORIES = ['전체', '복사기', '복테', '오답노트', '비품', '제본기'];
```

변경:
```javascript
var CATEGORIES = ['전체', '복테', '오답노트', '채점', '비품', '제본기', '복사기', '파일관리', '학생관리', '루틴'];
```

---

# [수정 2] 04_FA
### 20_Order_UI_Fix_v1.0.md
# 20_Order_UI_Fix_v1.0.md
# KING Assistant OS — UI 수정 3가지

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\07_Settings_v1.html

---

# 작업 방식
HTML 구조/디자인은 최소한으로 건드린다.
각 파일별 수정 범위를 정확히 지정하여 변경한다.

---

# [수정 1] 02_Task_v1.html — 체크박스 제거 + 업무진행상황 필터 추가

## 1-1. 체크박스 제거
- CSS에서 `.task-check` 관련 스타일 제거
- HTML 렌더링에서 `<input type="checkbox" class="task-check" ...>` 제거
- JS에서 `toggleCheck` 함수 제거
- task 객체에서 `checked: fals
### 21_Order_Fix_WeekNav_v1.0.md
# 21_Order_Fix_WeekNav_v1.0.md
# KING Assistant OS — 주간 달력 좌우 화살표 수정

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html

---

# 문제
주간 보기에서 ◀ ▶ 화살표를 클릭해도 주간이 이동하지 않음.
원인: prevMonth()/nextMonth() 함수에 `if (calView === 'week') return;` 이 있어서 주간 모드에서 아무 동작도 하지 않음.

---

# 수정 방법

index.html의 JS에서 prevMonth()와 nextMonth() 함수를 아래와 같이 교체한다.

## 기존 코드 (제거)
```javascript
  function prevMonth() {
    if (calView === 'week') return;
    calMonth--;
    if (calMonth < 0) { calMonth = 11; calYear--; }
    r
### 22_Order_Fix_SOPLink_v1.0.md
# 22_Order_Fix_SOPLink_v1.0.md
# KING Assistant OS — SOP 본문 URL 링크 클릭 가능하게 수정

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html

---

# 문제
SOP 상세 내용(body)에 URL이 일반 텍스트로 표시되어 클릭이 안 됨.
예: 신규 조교 온보딩 SOP의 http://crims.police.go.kr

---

# 수정 1: escHtml 후 URL을 링크로 변환하는 함수 추가

JS에서 기존 `escHtml` 함수 아래에 아래 함수를 추가한다:

```javascript
  function linkify(str) {
    return str.replace(/(https?:\/\/[^\s<>"]+)/g, function(url) {
      return '<a href="' + url + '" target="_blank" rel="noopener noreferre
### 23_Order_Fix_Combined_v1.0.md
# 23_Order_Fix_Combined_v1.0.md
# KING Assistant OS — 3가지 수정 한번에

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html

---

# [수정 1] index.html — 주간 달력 ◀▶ 화살표 버그 수정

## 문제
주간 보기에서 ◀ ▶ 클릭해도 주간이 이동하지 않음.
원인: prevMonth()/nextMonth() 함수에 `if (calView === 'week') return;` 이 있어서 주간 모드에서 아무 동작도 하지 않음.

## 1-1. 변수 선언 추가
`var selectedDate = null;` 바로 아래에 아래 줄 추가:
```javascript
  var weekOffset = 0;
```

## 1-2. prevM
### 24_Order_MergeNotice_v1.0.md
# 24_Order_MergeNotice_v1.0.md
# KING Assistant OS — 공지 탭을 홈으로 통합

---

# 작업 개요
- 홈(index.html) 공지사항 섹션에 JSON 다운로드/업로드 + 드래그 정렬 추가
- 전체 nav에서 공지 탭 제거 (7탭 → 6탭)
- 05_Notice_v1.html → 홈으로 리다이렉트

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\index.html
C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html
C:\Obsidian\Dooly\04_Runtime\03_SOP_v1.html
C:\Obsidian\Dooly\04_Runtime\04_FAQ_v1.html
C:\Obsidian\Dooly\04_Runtime\05_Notice_v1.html
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
C:\Obsidian\Dooly\04_Runtime
### 25_Order_RAG_Setup_v1.0.md
# 25_Order_RAG_Setup_v1.0.md
# KING Assistant OS — RAG 서버 구축 (FastAPI + Chroma + Ollama)

---

# 작업 개요
- 05_RAG 폴더에 필요한 파일 생성
- SOP/FAQ 데이터를 Chroma 벡터DB에 임베딩
- FastAPI 서버로 Dooly HTML과 연동
- SESSION_HANDOVER.md 및 PROJECT_MASTER.md 폴더 구조 업데이트

---

# 사전 확인
아래가 모두 완료된 상태에서 진행:
- Python 3.13.9 설치 완료
- Ollama 0.30.10 설치 완료
- qwen2.5:7b 모델 다운로드 완료
- fastapi, uvicorn, chromadb, sentence-transformers, ollama, PyPDF2 설치 완료
- C:\Obsidian\Dooly\05_RAG\db\ 폴더 존재
- C:\Obsidian\Dooly\05_RAG\docs\ 폴더 존재

---

#
### 26_Order_RAG_StartBat_v1.0.md
# 26_Order_RAG_StartBat_v1.0.md
# KING Assistant OS — RAG 서버 원클릭 실행 bat 파일 개선

---

# 작업 개요
현재 start.bat은 서버만 실행함.
아래 2개 bat 파일로 개선:
- run_embed.bat : 임베딩 전용 (데이터 변경 시 실행)
- run_server.bat : 서버 실행 전용 (매일 실행)

---

# 수정 대상
C:\Obsidian\Dooly\05_RAG\start.bat     ← 내용 교체
C:\Obsidian\Dooly\05_RAG\run_embed.bat ← 신규 생성
C:\Obsidian\Dooly\05_RAG\run_server.bat ← 신규 생성

---

# [작업 1] start.bat 내용 교체

기존 start.bat 전체 내용을 아래로 교체한다:

```bat
@echo off
chcp 65001 >nul
echo ===================================
### 27_Order_Fix_BatEncoding_v1.0.md
# 27_Order_Fix_BatEncoding_v1.0.md
# KING Assistant OS — bat 파일 한글 인코딩 오류 수정

---

# 문제
run_embed.bat, run_server.bat 실행 시
한글이 깨져서 명령어 오류 발생

# 원인
bat 파일 내 한글 문자열이 인코딩 충돌로 명령어로 인식됨

# 해결
한글 echo 문자열을 모두 영문으로 교체

---

# [수정 1] run_embed.bat 전체 교체

기존 파일 전체를 아래 내용으로 교체한다:

```bat
@echo off
cd /d C:\Obsidian\Dooly\05_RAG

echo ============================================
echo  Dooly Embedding Start
echo ============================================
echo.

python --version
if %errorlevel% neq 0 (
   
### 28_Order_Fix_Port_v1.0.md
# 28_Order_Fix_Port_v1.0.md
# KING Assistant OS — RAG 서버 포트 8000 → 8001 변경

---

# 문제
localhost:8000 을 다른 앱(SMART)이 사용 중
→ Dooly RAG 서버를 8001 포트로 변경

---

# 수정 대상
C:\Obsidian\Dooly\05_RAG\run_server.bat
C:\Obsidian\Dooly\05_RAG\README_RAG.txt
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html

---

# [수정 1] run_server.bat — 포트 변경

기존:
```bat
python -m uvicorn server:app --host 0.0.0.0 --port 8000
```

변경:
```bat
python -m uvicorn server:app --host 0.0.0.0 --port 8001
```

상단 echo도 변경:
기존:
```bat
echo
### 29_Order_Dooly_ModelSource_v1.0.md
# 29_Order_Dooly_ModelSource_v1.0.md
# KING Assistant OS — Dooly 모델 선택 + 출처 표시

---

# 작업 개요
1. Dooly 헤더에 모델 선택 드롭다운 추가 (모델 A/B/C 이름으로 표시)
2. 답변 하단에 구체적 출처 표시 (예: FAQ Q1 / SOP 2)
3. server.py에서 모델을 동적으로 받고 출처 정보를 상세하게 반환

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
C:\Obsidian\Dooly\05_RAG\server.py

---

# [수정 1] server.py — 모델 동적 수신 + 출처 상세 반환

## 1-1. ChatRequest 모델에 model 필드 추가

기존:
```python
class ChatRequest(BaseModel):
    message: str
```

변경:
```python
class ChatRequest(B
### 30_Order_Dooly_ChatHistory_v1.0.md
# 30_Order_Dooly_ChatHistory_v1.0.md
# KING Assistant OS — Dooly 대화 기록 유지 (localStorage)

---

# 문제
Dooly 탭을 벗어나면 대화 내용이 사라짐

# 해결
대화 내용을 localStorage에 저장
→ 탭 이동 후 돌아와도 대화 기록 유지
→ 브라우저 새로고침 후에도 유지

---

# 수정 대상
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html

---

# [수정 1] JS에 대화 기록 저장/불러오기 함수 추가

기존 `escHtml` 함수 바로 위에 아래 코드 추가:

```javascript
  /* ── 대화 기록 저장/불러오기 ── */
  var CHAT_STORAGE_KEY = 'dooly_chat_history';

  function saveChatHistory() {
    var area = document.getElementById('chatArea'
### 31_Order_RAG_StaticServe_v1.0.md
# 31_Order_RAG_StaticServe_v1.0.md
# KING Assistant OS — FastAPI에서 HTML 파일 서빙 (스마트폰 접속)

---

# 작업 개요
현재 server.py는 /chat API만 제공
스마트폰에서 HTML 앱 전체를 사용하려면
FastAPI에서 HTML 파일도 서빙해야 함

---

# 수정 대상
C:\Obsidian\Dooly\05_RAG\server.py
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html

---

# [수정 1] server.py — HTML 정적 파일 서빙 추가

## 1-1. import 추가

기존:
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from chromadb.utils i
### 32_Order_ProjectSummary_v1.0.md
# 32_Order_ProjectSummary_v1.0.md
# KING Assistant OS — 프로젝트 전체 가이드 문서 생성

---

# 작업 개요
지금까지 진행한 전체 작업을 빠짐없이, 중복없이 정리하여
나중에 처음부터 따라할 수 있는 단계별 가이드 문서를 생성한다.

---

# 읽을 파일 목록 (순서대로 모두 읽기)
1. C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
2. C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
3. C:\Obsidian\Dooly\00_System\03_DEVELOPMENT_RULE_v1.0.md
4. C:\Obsidian\Dooly\03_Claude_Code\ 폴더 전체 파일 목록 확인
5. C:\Obsidian\Dooly\04_Runtime\ 폴더 전체 파일 목록 확인
6. C:\Obsidian\Dooly\05_RAG\ 폴더 전체 파일 목록 확인
7. C:
### 32_Order_ServerRedirect_v1.0.md

# 32_Order_ServerRedirect_v1.0.md

## 작업 개요
server.py에 리다이렉트 라우트 추가
/02_Task_v1.html → /app/02_Task_v1.html 형태로 자동 리다이렉트

## 수정 대상 파일
C:\Obsidian\Dooly\05_RAG\server.py

## 작업 내용
기존 라우트 아래에 아래 코드 추가:

from fastapi.responses import RedirectResponse

@app.get("/{filename}.html")
async def redirect_html(filename: str):
    return RedirectResponse(url=f"/app/{filename}.html")

## 작업 완료 후 git 명령어
git add .
git commit -m "fix: redirect /{filename}.html to /app/{filename}.html"
git push
### 33_Order_KoreanOnly_v1.0.md
# 33_Order_KoreanOnly_v1.0.md

## 작업 개요
server.py 시스템 프롬프트에 한국어 전용 지시 추가
qwen 모델이 답변 마지막에 중국어를 붙이는 문제 수정

## 수정 대상 파일
C:\Obsidian\Dooly\05_RAG\server.py

## 작업 내용
server.py 내 시스템 프롬프트 문자열에 아래 내용 추가:

기존:
system_prompt = """당신은 킹수학 학원의 AI 비서 둘리입니다.
...existing content...
"""

변경:
system_prompt = """당신은 킹수학 학원의 AI 비서 둘리입니다.
...existing content...

반드시 한국어로만 답변하라.
중국어, 영어, 일본어 등 한국어 이외의 언어는 절대 사용하지 마라.
답변 마지막에 다른 언어로 된 문장을 추가하지 마라.
"""

## 작업 완료 후 git 명령어
git add .
git commit -m "fix: enforce Korea
### 34_Order_SystemCleanup_PWA_v1.0.md
# 34_Order_SystemCleanup_PWA_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 순서대로 읽어라.

```
C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\00_System\03_DEVELOPMENT_RULE_v1.0.md
```

---

# 작업 목표

1. 파일명 버전 표기 통일 (v1_0 → v1.0)
2. 인수인계 파일 최신화 및 히스토리 보관
3. PWA 전환 1단계 (manifest.json) 생성

작업은 반드시 아래 순서대로 진행한다.
한 STEP 완료 후 다음 STEP으로 넘어간다.

---

# STEP 1 — 파일명 버전 표기 
### 35_Order_GitIgnore_WorkflowGuide_v1.0.md
# 35_Order_GitIgnore_WorkflowGuide_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 순서대로 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\00_System\05_WORKFLOW_GUIDE_v1.0.md
```

---

# 작업 목표

1. .gitignore 항목 추가 (보안 + 불필요 파일 제외)
2. 05_WORKFLOW_GUIDE_v1.0.md git 등록
3. 전체 커밋 및 push

작업은 반드시 아래 순서대로 진행한다.

---

# STEP 1 — .gitignore 업데이트

## 수정 대상 파일

```
C:\Obsidian\Dooly\.gitignore
```

## 현재 내용 (변경 금
### 36_Order_GitIgnore_WorkflowGuide_v1.0.md
# 36_Order_GitIgnore_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 순서대로 읽어라.

```
C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\00_System\05_WORKFLOW_GUIDE_v1.0.md
```

---

# 작업 목표

.gitignore 항목 추가 (보안 + 불필요 파일 제외)

※ 05_WORKFLOW_GUIDE_v1.0.md 는 34번 작업 중 이미 git push 완료됨 → 별도 작업 불필요

---

# STEP 1 — .gitignore 업데이트

## 수정 대상 파일

```
C:\Obsidian\Dooly\.giti
### 37_Order_DataJS_v1.0.md
# 37_Order_DataJS_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 순서대로 읽어라.

```
C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
```

---

# 작업 목표

방법 A 적용: SOP/FAQ 데이터를 공통 data.js로 분리

1. data.js 신규 생성 (SOP 23개 + FAQ 22개 배열)
2. 03_SOP_v1.html 수정 (data.js 연결 + 기존 배열 삭제)
3. 04_FAQ_v1.html 수정 (data.js 연결 + 기존 배열 삭제)
4. 06_Dooly_v1.html 수정 (data.js 연결 + mockResponse 고도화)

작업은 반드시 아
### 38_Order_MockFallback_v1.0.md
# 38_Order_MockFallback_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
```

---

# 작업 목표

RAG 서버 연결 실패 시 자동으로 Mock 모드로 전환

현재 문제:
```
서버 없을 때
→ "RAG 서버에 연결할 수 없습니다. run_server.bat을 실행해주세요." 출력
→ 대화 종료
```

수정 후:
```
서버 없을 때
→ Mock 모드 자동 전환
→ data.js 기반 FAQ/SOP 내용 답변
→ 답변 하단에 "[Mock 모드]" 표시
```

---

# STEP 1 — 06_Dooly_v1.h
### 39_Order_MockModel_v1.0.md
# 39_Order_MockModel_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
```

---

# 작업 목표

모델 드롭다운에 Mock 옵션 추가 + 기본값으로 설정

현재 문제:
```
RAG 서버 모드가 기본값
→ "복사기 종이 먹었어요" 질문에 복테 관련 답변 출력
→ RAG 검색 품질이 낮아 엉뚱한 답변 발생
```

수정 후:
```
Mock 모드가 기본값
→ data.js 키워드 매칭으로 정확한 FAQ/SOP 답변
→ 서버 불필요, 오프라인 동작
→ RAG는 드롭다운에서 수동 선택 시만 사용
```

---

# STEP
### 40_Order_MockUI_v1.0.md
# 40_Order_MockUI_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
```

---

# 작업 목표

1. Mock 모드 답변에 출처 태그 추가 (색깔 구별)
2. 모든 메시지에 날짜/시간 표시 추가

---

# STEP 1 — 날짜/시간 포맷 함수 추가

## 추가 위치

06_Dooly_v1.html 의 `<script>` 태그 안 맨 위 (다른 함수들 위)에 추가한다.

## 추가할 코드

```javascript
function getNow() {
  var d = new Date();
  var mm = String(
### 41_Order_MockMultiResult_v1.0.md
# 41_Order_MockMultiResult_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
C:\Obsidian\Dooly\04_Runtime\06_Dooly_v1.html
```

---

# 작업 목표

Mock 모드에서 키워드 매칭 결과를 전체 목록으로 표시
클릭하면 내용이 펼쳐지는 아코디언 방식 적용

현재:
```
"복테" 입력 → 첫 번째 매칭 1개만 답변
```

수정 후:
```
"복테" 입력 → 관련 FAQ/SOP 전체 목록 표시
              제목 클릭 시 내용 펼치기/접기
```

---

# STEP 1 — CSS 추가 (아코디언 스타일)

## 추가 위치

`<style>` 태그 안
### 42_Order_GitHubPages_v1.0.md
# 42_Order_GitHubPages_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-27

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
```

---

# 작업 목표

GitHub Pages 배포 설정
→ server.py 없이 HTML 파일을 직접 서빙
→ 24시간 항상 접속 가능
→ 자습실 PC, ngrok 불필요

---

# 배경 설명

현재 구조:
```
04_Runtime\
├── index.html
├── 02_Task_v1.html
├── 03_SOP_v1.html
├── 04_FAQ_v1.html
├── 05_Notice_v1.html
├── 06_Dooly_v1.html
├── 07_Settings_v1.html
├── data.js
├── man
### 43_Order_PWA_ServiceWorker_v1.0.md
# 43_Order_PWA_ServiceWorker_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-28

---

# 작업 시작 전 필수 확인

아래 파일을 읽어라.

```
C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
```

---

# 작업 목표

PWA 완성: service-worker.js + 아이콘 생성
→ 갤럭시/아이폰 홈 화면에 앱 설치 가능

---

# 배경

현재 상태:
```
docs\manifest.json ✅ (42번에서 완료)
docs\icons\ 폴더  ✅ (비어있음)
service-worker.js  ❌ (없음)
아이콘 PNG 파일    ❌ (없음)
```

이번 작업:
```
docs\service-worker.js  ← 신규 생성
docs\icons\icon-192.png ← 신규 생성 (Python으로 
### 44_Order_PWA_Icon_Dooly_v1.0.md
# 44_Order_PWA_Icon_Dooly_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-28

---

# 작업 배경

43번 작업이 STEP 2까지 완료됨.
- service-worker.js 생성 완료 ✅
- icon-192.png, icon-512.png 임시 생성 완료 ✅
- docs/index.html SW 등록 코드 추가 미완료 ❌

이번 작업:
1. 아이콘을 공룡(Dooly) 스타일로 교체
2. 앱 이름 KING → Dooly로 수정
3. docs/index.html SW 등록 코드 추가 (43번 미완료 부분)
4. 04_Runtime 동기화
5. git push

---

# STEP 1 — 공룡 아이콘 생성 (Python)

## 실행 위치

```
cd C:\Obsidian\Dooly
```

## 실행 명령어

```python
python -c "
impor
### 45_Order_PWA_Icon_Update_v1.0.md
# 45_Order_PWA_Icon_Update_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-28

---

# 작업 목표

공룡 이미지를 원형 + 흰색 배경 아이콘으로 변환
→ icon-192.png, icon-512.png 교체

---

# 작업 시작 전 필수 준비 (직접 진행)

원본 이미지 파일을 아래 경로에 저장한다.
```
C:\Obsidian\Dooly\99_Archive\dooly_source.png
```

---

# STEP 1 — Pillow 설치

```
pip install Pillow
```

---

# STEP 2 — 원형 아이콘 생성 (Python)

## 실행 위치

```
cd C:\Obsidian\Dooly
```

## 실행 명령어

```python
python -c "
from PIL import Image, ImageDraw
import
### 46_Order_SessionHandover_v5_v1.0.md
# 46_Order_SessionHandover_v5_v1.0.md
# King Assistant OS v1.0
# Claude Code 작업지시서

Version: v1.0
Date: 2026-06-28

---

# 작업 목표

SESSION_HANDOVER v5.0 저장 및 업데이트

---

# STEP 1 — 현재 인수인계 파일을 히스토리로 복사

```
Copy-Item "C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md" "C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\09_SESSION_HANDOVER_v5.0.md"
```

기존 02_SESSION_HANDOVER.md 는 수정하지 않는다.

---

# STEP 2 — 02_SESSION_HANDOVER.md 최신 내용으로 덮어쓰기

아래 내용으로 C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md 를
### 47_Order_iPhone_PWA_Guide_v1.0.md
# 47_Order_iPhone_PWA_Guide_v1.0.md
# King Assistant OS v1.0
# 작업지시서 #47 — 아이폰 PWA 설치 가이드 문서 생성

작성일: 2026-06-28
우선순위: 높음

---

## 1. 작업 개요

아이폰(iOS) 사용자(조교A, B)가 Dooly를 홈 화면에 설치할 수 있도록
PWA 설치 가이드 Markdown 파일을 생성한다.

생성 목적:
- 조교가 스스로 설치할 수 있도록 단계별 안내
- 아이폰 Safari 전용 설치 흐름 안내 (iOS는 Safari에서만 PWA 설치 가능)
- GitHub Pages URL 기준으로 안내 (인터넷 연결만 있으면 설치 가능)

---

## 2. 생성할 파일

경로: C:\Obsidian\Dooly\00_System\iPhone_PWA_INSTALL_GUIDE.md

---

## 3. 파일 내용

아래 내용을 그대로 작성할 것.

---

```
# 📱 아이폰 Dooly 설치 가이드

>
### 48B_Order_Task_API_PWA_v1.0.md
# 48B_Order_Task_API_PWA_v1.0.md
# King Assistant OS v1.0
# 작업지시서 #48B — PWA Task 화면 FastAPI 연동

작성일: 2026-06-28
실행 위치: 노트북(화이트) Claude Code
우선순위: 높음
선행 작업: 48A 완료 ✅

---

## 1. 작업 개요

PWA Task 화면(02_Task_v1.html)을 수정한다.
기존 localStorage 방식에서 FastAPI 연동 방식으로 변경한다.

핵심 기능:
- 🟢 온라인 / 🔴 오프라인 상태 표시
- 온라인: FastAPI에서 Task 실시간 조회/추가/수정/삭제
- 오프라인: localStorage에 임시 저장
- [🔄 동기화] 버튼: 오프라인 상태일 때만 활성화

현재 접속 방식: 학원 내부 와이파이 전용
향후 계획: 외부 접속은 50번(Cloudflare Tunnel)에서 추가 예정

---

## 2. 환경 정보

| 항목 | 내용 |
|------|
### 48B_Order_Task_API_PWA_v1.1.md
# 48B_Order_Task_API_PWA_v1.1.md
# King Assistant OS v1.0
# 작업지시서 #48B 수정 — PWA Task API IP 주소 수정

작성일: 2026-06-28
실행 위치: 노트북(화이트) Claude Code
우선순위: 높음

---

## 1. 작업 개요

02_Task_v1.html 안의 API_BASE IP 주소를 수정한다.

| 항목 | 내용 |
|------|------|
| 수정 전 | http://192.168.219.100:8001 |
| 수정 후 | http://192.168.0.10:8001 |

---

## 2. 수정 파일

- C:\Obsidian\Dooly\04_Runtime\02_Task_v1.html
- C:\Obsidian\Dooly\docs\02_Task_v1.html

---

## 3. 작업 내용

### Step 1 — 04_Runtime\02_Task_v1.html 수정

아래 한 줄을 찾아서 교체
### 49_Order_Claude_API_Worker_v1.0.md
# 50_Order_Claude_API_Worker_v1.0.md
# King Assistant OS v2.0
# 작업: Claude API + Cloudflare Workers 연동 (Dooly 챗봇 실제 AI 답변)

작성일: 2026-06-29
작업번호: 50
우선순위: 높음

---

## 목표

현재 Dooly 챗봇은 Mock 모드(data.js 기반 정적 답변)로 동작 중이다.
이번 작업에서 Claude API를 연동하여 실제 AI 답변으로 업그레이드한다.

### 아키텍처 (A안 — Cloudflare Workers 프록시)

```
PWA (Cloudflare Pages)
    ↓ fetch POST
Cloudflare Worker (프록시)
    ↓ API 키 주입
Claude API (claude-sonnet-4-6)
    ↓ 응답
PWA 챗봇 화면
```

**선택 이유:**
- API 키가 프론트엔드 코드에 노출되지 않음
- CORS 문제 없음 (Worke
### 50_Order_Gemini_API_Worker_v2.0.md
# 50_Order_Gemini_API_Worker_v2.0.md

작성일: 2026-06-29
작업: Task #50 — Gemini API + Cloudflare Worker 연동 (v2.0)
변경 이유: Claude API → Gemini API (하단 시행착오 참고)

---

# 배경

원래 Task #50은 Claude API 연동으로 계획됐으나,
Anthropic Console에서 크레딧 구매 버튼이 비활성화되는 문제로
기존에 발급된 Gemini API로 변경하여 진행한다.

---

# 현재 완료된 상태

- ✅ Cloudflare Worker 생성 완료
  - Worker 이름: `dooly-claude-proxy`
  - URL: `https://dooly-claude-proxy.2davidpassion.workers.dev`
- ✅ Worker에 Claude API 프록시 코드 배포 완료 (Gemini용으로 교체 필요)
- ❌ API 키 환경변수 미설정

---

### 51_Order_Vercel_Migration_v1.0.md
# 51_Order_Vercel_Migration_v1.0.md

작성일: 2026-06-29
작업: Cloudflare Pages/Worker → Vercel 완전 이전
이유: Cloudflare Worker에서 Gemini API 호출 시 한국 서버 위치로 인한 차단 문제

---

# 배경

Cloudflare Worker가 아시아/한국 서버에서 실행되면서
Gemini API가 "User location is not supported" 오류로 차단됨.
Vercel은 미국 서버 기반이라 Gemini API 차단 없음.

---

# 변경 구조

```
변경 전:
GitHub → Cloudflare Pages (PWA 서빙)
              ↓
       Cloudflare Worker (프록시) → Gemini API (차단)

변경 후:
GitHub → Vercel (PWA 서빙 + 프록시)
              ↓
         Gemini API (미국 서버
### 52_Order_PWA_Icon_Gemini_Fix_v1.0.md
# 52_Order_PWA_Icon_Gemini_Fix_v1.0.md
# Task #52 — PWA 아이콘 교체 + Gemini 출처 번호 + 말풍선 색상 수정

작성일: 2026-06-29
작업자: Claude Code
우선순위: 높음

---

## 1. 작업 개요

| 번호 | 항목 | 내용 |
|------|------|------|
| 52-A | PWA 아이콘 교체 | 새 공룡 아이콘(흰색 배경)으로 교체 |
| 52-B | manifest.json 경로 수정 | Vercel Root Directory(docs/) 기준으로 아이콘 경로 수정 |
| 52-C | Gemini 출처 번호 표시 | 시스템 프롬프트 수정 → FAQ Q1, SOP 10 형식 출처 표시 |
| 52-D | 질문 말풍선 텍스트 색상 | 파란 배경 + 파란 텍스트 → 파란 배경 + 흰색 텍스트 |

---

## 2. 수정 대상 파일 경로

```
C:\Obsidian\Dooly\
├── docs\
│ 
### 52E_Order_SW_Cache_Gemini_UI_v1.0.md
# 52E_Order_SW_Cache_Gemini_UI_v1.0.md
# Task #52-E — 서비스워커 캐시 갱신 + Gemini 출처 태그 UI 개선

작성일: 2026-06-29
작업자: Claude Code
우선순위: 높음

---

## 1. 작업 개요

| 번호 | 항목 | 내용 |
|------|------|------|
| 52-E1 | 서비스워커 캐시 버전 업그레이드 | king-assistant-v2 → king-assistant-v3 |
| 52-E2 | Gemini 출처 태그 UI 개선 | 텍스트 출처 → FAQ 초록 / SOP 주황 태그로 변환 |
| 52-E3 | Gemini 답변 줄바꿈 처리 | 번호 목록마다 줄바꿈 적용 |

---

## 2. 수정 대상 파일 경로

```
C:\Obsidian\Dooly\
└── docs\
    ├── service-worker.js     ← 52-E1: 캐시 버전 수정
    └── 06_Dooly_v1.html
### 52F_Order_Manifest_Link_v1.0.md
# 52F_Order_Manifest_Link_v1.0.md
# Task #52-F — manifest.json 링크 태그 추가 (PWA 아이콘 수정)

작성일: 2026-06-29
작업자: Claude Code
우선순위: 높음

---

## 1. 작업 개요

| 번호 | 항목 | 내용 |
|------|------|------|
| 52-F | manifest 링크 태그 추가 | 06_Dooly_v1.html `<head>`에 manifest 연결 태그 추가 |

### 원인
F12 → Application → Manifest에서 "No manifest detected" 확인.
`06_Dooly_v1.html`의 `<head>` 안에 manifest.json 연결 태그가 없어서
브라우저가 PWA manifest를 인식하지 못하고 기본 아이콘(V)을 표시함.

---

## 2. 수정 대상 파일

```
C:\Obsidian\Dooly\docs\06_Dooly_v1.html
```
### 52G_Order_Gemini_Source_Number_v1.0.md
# 52G_Order_Gemini_Source_Number_v1.0.md

작성일: 2026-06-30
작업 번호: Task #52-G
작업명: Gemini 출처 번호 표시 수정
대상 파일: docs/06_Dooly_v1.html
선행 조건: Task #52-F 완료 (커밋 9a24c94)

---

## 목표

Gemini AI 답변 하단에 출처 태그가 표시될 때
번호 없이 카테고리명만 나오는 문제를 수정한다.

### 현재 (문제)
```
FAQ Q: 복사기가 종이를 먹었어요
SOP 복사기/스캔 SOP
```

### 목표 (수정 후)
```
FAQ Q1
SOP 1
```

---

## 수정 내용

### 1. 시스템 프롬프트 수정

`docs/06_Dooly_v1.html` 안에서 Gemini에게 전달하는 시스템 프롬프트를 찾는다.
아래와 같이 출처 형식 지시를 명확하게 수정한다.

**찾을 텍스트 (기존 출처 지시 부분):**
```
출처를 표시할 때는 [FAQ Q1], [
### 52H_Order_Source_Tag_Fix_v1.0.md
# 52H_Order_Source_Tag_Fix_v1.0.md

작성일: 2026-06-30
작업 번호: Task #52-H
작업명: AI 답변 잘림 수정
대상 파일: docs/api/gemini.js, docs/06_Dooly_v1.html
선행 조건: Task #52-G 완료 (커밋 ed8f884)

---

## 수정 범위

Mock 모드 출처 태그는 현재 정상 동작 중 → 수정하지 않음
AI(Gemini) 모드 답변이 중간에 잘리는 문제만 수정한다.

---

## 문제 — AI 모드 답변이 중간에 잘림

### 현재 (문제)
```
"복사기 종이"에 대해 어떤 점이 궁금하신가요?
만약 복사기 종이를 먹었거나 종이 걸림이 발생했다면, 구
```
"구" 에서 답변이 끊김.

### 원인
`docs/api/gemini.js` 의 `maxOutputTokens` 값이 너무 낮거나
응답 파싱 시 텍스트를 자르는 코드가 있을 가능성.

---

## 수정 1 — docs/api/gem
### 52I_Order_Gemini_Response_Fix_v1.0.md
# 52I_Order_Gemini_Response_Fix_v1.0.md

작성일: 2026-06-30
작업 번호: Task #52-I
작업명: Gemini 응답 잘림 정확한 원인 수정
대상 파일: docs/api/gemini.js, docs/06_Dooly_v1.html
선행 조건: Task #52-H 완료 (커밋 8f6eccf)

---

## 상황

- maxOutputTokens 1000 → 2048 올렸더니 속도만 느려지고 여전히 잘림
- maxOutputTokens는 1000으로 복원
- 잘림 원인은 다른 곳에 있음 → 정확히 찾아서 수정

---

## 수정 1 — maxOutputTokens 복원

**api/gemini.js 와 docs/api/gemini.js 두 파일 모두:**

```javascript
maxOutputTokens: 2048  →  maxOutputTokens: 1000
```

---

## 수정 2 — 잘림 원인 찾기 및 수정

`docs/06
### 52X_Order_Rollback_to_52F_v1.0.md
# 52X_Order_Rollback_to_52F_v1.0.md

작성일: 2026-06-30
작업 번호: Task #52-X (롤백)
작업명: 52-G 이전 상태로 롤백
대상 파일: docs/06_Dooly_v1.html, api/gemini.js, docs/api/gemini.js
롤백 목표 커밋: 9a24c94 (52-F 완료 상태)

---

## 롤백 이유

52-G 이후 3개 작업(52-G, 52-H, 52-I)을 거쳤으나
AI 응답 속도 10초, 답변 잘림 문제가 해결되지 않고 악화됨.
52-F 상태(커밋 9a24c94)는 정상 동작했으므로 해당 시점으로 롤백.

---

## 작업 — git revert 방식으로 롤백

아래 명령을 순서대로 실행한다.

```
cd C:\Obsidian\Dooly

# 52-F 커밋(9a24c94) 상태의 3개 파일을 현재 브랜치에 복원
git checkout 9a24c94 -- docs/06_Dooly_v1.html
git check
### 52Y_Order_Rollback_to_52E_v1.0.md
# 52Y_Order_Rollback_to_52E_v1.0.md

작성일: 2026-06-30
작업 번호: Task #52-Y (롤백)
작업명: 52-E 상태로 롤백 (출처 태그 복원)
대상 파일: docs/06_Dooly_v1.html, api/gemini.js, docs/api/gemini.js
롤백 목표 커밋: d98cfb9 (52-E 완료 상태)

---

## 롤백 이유

현재 상태(52-F 롤백, 커밋 5281c6e)는 출처 태그가 없음.
52-E(커밋 d98cfb9)는 출처 태그(FAQ Q:, SOP) 정상 표시 + 답변 정상 상태.
52-G에서 출처 번호 수정 시도가 오히려 성능 저하를 일으켰으므로
52-E 상태로 되돌린다.

---

## 작업

```
cd C:\Obsidian\Dooly

git checkout d98cfb9 -- docs/06_Dooly_v1.html
git checkout d98cfb9 -- docs/api/gemini.js
git checko
### 53_Order_Supabase_Task_Sync_v1.0.md
# 53_Order_Supabase_Task_Sync_v1.0.md

작성일: 2026-06-30
작업 번호: Task #53
작업명: Supabase Task 동기화
대상 파일: docs/06_Dooly_v1.html, docs/api/tasks.js (신규), Vercel 환경변수
선행 조건: Task #52-Y 완료 (커밋 35f7576)

---

## 0. 사전 준비 (수동 작업 — Claude Code 실행 전)

아래 3단계는 브라우저에서 직접 수행한다.

### Step 0-1. Supabase 프로젝트 생성

1. https://supabase.com 접속 → 신규 가입
2. New Project 생성
   - Name: dooly
   - Region: Northeast Asia (Seoul) 권장

### Step 0-2. tasks 테이블 생성

Supabase 대시보드 → SQL Editor → 아래 쿼리 실행:

```sql
create table tasks
### 54_Order_Dooly_Manifest_ErrorHandling_v1.0.md
# 54_Order_Dooly_Manifest_ErrorHandling_v1.0.md
# Task #54 — manifest 링크 태그 추가 + Gemini 에러 한국어 처리

작성일: 2026-06-30
대상 파일: C:\Obsidian\Dooly\docs\06_Dooly_v1.html

---

# 작업 개요

| 항목 | 내용 |
|------|------|
| 작업 번호 | Task #54 |
| 작업명 | manifest 링크 태그 추가 + Gemini 에러 한국어 처리 |
| 대상 파일 | docs/06_Dooly_v1.html |
| 작업 유형 | HTML 수정 |
| 예상 소요 | 5분 이내 |

---

# 작업 1 — manifest 링크 태그 추가

## 원인
06_Dooly_v1.html의 <head>에 manifest 링크 태그가 없어
PWA 설치 버튼이 나타나지 않고 "No manifest detected" 오류 발생.

## 수정 위치
C:\Obsidian
### 55_Order_Archive_Runtime_v1.0.md
# 55_Order_Archive_Runtime_v1.0.md
# Task #55 — 04_Runtime 아카이브 + README 작성

작성일: 2026-06-30
작업자: Claude Code

---

# 작업 개요

| 항목 | 내용 |
|------|------|
| 작업 번호 | Task #55 |
| 작업명 | 04_Runtime 아카이브 + README 작성 |
| 작업 유형 | 폴더 이동 + 문서 작성 |
| 예상 소요 | 5분 이내 |

## 작업 배경
- v1.0 시절 로컬 FastAPI 서버용 파일들이 04_Runtime에 남아있음
- v2.0 Vercel 배포로 마이그레이션 완료 후 구버전 파일 미정리 상태
- 현재 운영 파일은 docs\ 폴더에만 있음
- 혼동 방지를 위해 04_Runtime을 99_Archive로 이동하고 README로 설명 남김

---

# 작업 1 — 04_Runtime 폴더 아카이브 이동

## 실행 명령어

```powershell
### 56_Order_GitHubPages_Update_v1.0.md
# 56_Order_GitHubPages_Update_v1.0.md
# King Assistant OS v2.0
# 작업지시서 #56 — GitHub Pages 최신버전 업데이트

작성일: 2026-06-30
우선순위: 낮음
전제조건: Task #53 완료 (커밋 82d593a)

---

## 1. 작업 개요

### 목적
GitHub Pages가 구버전 상태로 방치되어 있어 현재 Vercel 운영 버전과 동기화한다.

### 배경
- 운영 URL: https://dooly-eight.vercel.app (Vercel — 최신)
- Pages URL: https://2passion.github.io/Dooly (GitHub Pages — 구버전)
- Vercel 이전(Task #51) 이후 GitHub Pages 설정이 갱신되지 않은 상태

### 작업 범위
1. GitHub Pages 현재 설정 확인
2. Pages 빌드 소스를 `main` 브랜치 `docs/` 폴더로 지정
3.
### 57_Order_TaskFilter_Sync_v1.0.md
# 57_Order_TaskFilter_Sync_v1.0.md
# King Assistant OS v2.0
# 작업지시서 #57 — Task 화면 담당자 필터 동기화 확인

작성일: 2026-06-30
우선순위: 보통
전제조건: Task #53 완료 (Supabase Task 동기화, 커밋 82d593a)

---

## 1. 작업 개요

### 목적
Task #53에서 Supabase 연동을 완료했으나, 담당자 필터 기능이 기기 간에 정상적으로 동기화되는지 검증하고 문제가 있으면 수정한다.

### 확인 항목 3가지

| 번호 | 항목 | 설명 |
|------|------|------|
| A | 필터 쿼리 정확성 | Supabase에 담당자별 where절이 올바르게 전달되는지 |
| B | 기기 간 실시간 동기화 | 기기 A에서 Task 추가/변경 시 기기 B에 즉시 반영되는지 |
| C | 필터 상태 유지 | 새로고침 후에도 선택된 필터가 유지되는지 |

---

## 2. 
### README_RAG.txt
=============================================
  Dooly RAG 시스템 사용 방법
=============================================

[처음 설치 후]
1. run_embed.bat 더블클릭 → 임베딩 완료 대기
2. run_server.bat 더블클릭 → 서버 실행
3. 브라우저에서 index.html 열기 → Dooly 탭

[매일 사용할 때]
1. run_server.bat 더블클릭
2. 브라우저에서 index.html 열기 → Dooly 탭

[SOP/F
### embed.py
# embed.py — SOP/FAQ 문서를 Chroma 벡터DB에 임베딩

import os
import chromadb
from chromadb.utils import embedding_functions

# 경로 설정
DOCS_DIR = r"C:\Obsidian\Dooly\05_RAG\docs"
DB_DIR   = r"C:\Obsidian\Dooly\05_RAG\db"

# 임베딩 함수 (로컬 모델, 인터넷 불필요)
emb_fn = embedding_functions.SentenceTransformerEmbeddingFunct
### server.py
# server.py — FastAPI + Chroma + Ollama RAG 서버

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
import chromadb
from chromadb.utils i
### run_embed.bat
@echo off
cd /d C:\Obsidian\Dooly\05_RAG

echo ============================================
echo  Dooly Embedding Start
echo ============================================
echo.

python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python not found.
    pause
    exit /b 1
)

echo.
echo [Running]
### run_server.bat
@echo off
cd /d C:\Obsidian\Dooly\05_RAG

echo ============================================
echo  Dooly RAG Server Start
echo  URL: http://localhost:8001
echo  Stop: Close this window or Ctrl+C
echo ============================================
echo.

echo [Check] Ollama running...
curl -s http://loc
### start.bat
@echo off
echo ============================================
echo  Dooly RAG System
echo ============================================
echo.
echo  First time or data changed:
echo    run_embed.bat
echo.
echo  Daily use:
echo    run_server.bat
echo.
echo ============================================
pau
### gemini.js
export const config = {
  runtime: 'edge',
};

export default async function handler(request) {
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-
### gemini.js
export const config = {
  runtime: 'edge',
};

export default async function handler(request) {
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-
### tasks.js
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY;

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS');
  res.

---

## 주의사항 및 오류
(log/ 파일에서 자동 추출됩니다)

---

## 자주 하는 실수
| 증상 | 원인 | 해결 |
|------|------|------|
| (log 분석 후 추가 예정) | | |

---

## FAQ
Q. (docs 분석 후 추가 예정)
A.

---

## 분석 파일 목록 (117개)
- C:\Obsidian\Dooly\00_System\00_SESSION_CLOSE_TEMPLATE.md
- C:\Obsidian\Dooly\00_System\01_PROJECT_MASTER.md
- C:\Obsidian\Dooly\00_System\02_SESSION_HANDOVER.md
- C:\Obsidian\Dooly\00_System\03_DEVELOPMENT_RULE_v1.0.md
- C:\Obsidian\Dooly\00_System\04_PROJECT_GUIDE_v1.0.md
- C:\Obsidian\Dooly\00_System\05_WORKFLOW_GUIDE_v1.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\02_SESSION_HANDOVER.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\05_SESSION_HANDOVER_v1.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\06_SESSION_HANDOVER_v2.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\07_SESSION_HANDOVER_v3.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\08_SESSION_HANDOVER_v4.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\09_SESSION_HANDOVER_v5.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\09_SESSION_HANDOVER_v8.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\10_SESSION_HANDOVER_v6.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\11_SESSION_HANDOVER_v7.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\12_SESSION_HANDOVER_v8.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\14_SESSION_HANDOVER_v9.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\15_SESSION_HANDOVER_v10.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\16_SESSION_HANDOVER_v11.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\17_SESSION_HANDOVER_v12.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\17_SESSION_HANDOVER_v13.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\18_SESSION_HANDOVER_v14.0.md
- C:\Obsidian\Dooly\00_System\HANDOVER_HISTORY\18_SESSION_HANDOVER_v15.0.md
- C:\Obsidian\Dooly\00_System\iPhone_PWA_INSTALL_GUIDE.md
- C:\Obsidian\Dooly\00_System\SESSION_REPORT_20260629.md
- C:\Obsidian\Dooly\01_Project\01_King_Assistant_OS_v1.0.md
- C:\Obsidian\Dooly\01_Project\02_SOP_v1.0.md
- C:\Obsidian\Dooly\01_Project\03_Exception_Manual_v1.0.md
- C:\Obsidian\Dooly\01_Project\04_FAQ_v1.0.md
- C:\Obsidian\Dooly\01_Project\06_Task_Management_v1.0.md
- C:\Obsidian\Dooly\01_Project\08_King_Assistant_OS_v1.0_Implementation_Plan.md
- C:\Obsidian\Dooly\01_Project\09_UI_Wireframe_v1.0.md
- C:\Obsidian\Dooly\01_Project\10_HTML_Prototype_v1.0.md
- C:\Obsidian\Dooly\01_Project\11_Dooly_Architecture_Guide_v1.0.md
- C:\Obsidian\Dooly\01_Project\12 Dooly_User_Guide_v1.0.md
- C:\Obsidian\Dooly\01_Project\12_Dooly_Architecture_Guide_v2.0.md
- C:\Obsidian\Dooly\01_Project\13_Dooly_User_Guide_v2.0.md
- C:\Obsidian\Dooly\02_Claude_Project\05_Dooly_System_Prompt_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\07_Claude_Code_Operation_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\11_Order_HTMLPrototype_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\12_Order_UI_v2.0.md
- C:\Obsidian\Dooly\03_Claude_Code\13_Order_Data_v2.0.md
- C:\Obsidian\Dooly\03_Claude_Code\14_Order_Home_v3.0.md
- C:\Obsidian\Dooly\03_Claude_Code\15_Order_UX_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\16_Order_Task_FAQ_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\17_Order_Calendar_Settings_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\18_Order_SOP_v2.0.md
- C:\Obsidian\Dooly\03_Claude_Code\19_Order_FAQ_Dooly_v2.0.md
- C:\Obsidian\Dooly\03_Claude_Code\20_Order_UI_Fix_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\21_Order_Fix_WeekNav_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\22_Order_Fix_SOPLink_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\23_Order_Fix_Combined_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\24_Order_MergeNotice_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\25_Order_RAG_Setup_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\26_Order_RAG_StartBat_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\27_Order_Fix_BatEncoding_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\28_Order_Fix_Port_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\29_Order_Dooly_ModelSource_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\30_Order_Dooly_ChatHistory_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\31_Order_RAG_StaticServe_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\32_Order_ProjectSummary_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\32_Order_ServerRedirect_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\33_Order_KoreanOnly_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\34_Order_SystemCleanup_PWA_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\35_Order_GitIgnore_WorkflowGuide_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\36_Order_GitIgnore_WorkflowGuide_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\37_Order_DataJS_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\38_Order_MockFallback_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\39_Order_MockModel_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\40_Order_MockUI_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\41_Order_MockMultiResult_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\42_Order_GitHubPages_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\43_Order_PWA_ServiceWorker_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\44_Order_PWA_Icon_Dooly_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\45_Order_PWA_Icon_Update_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\46_Order_SessionHandover_v5_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\47_Order_iPhone_PWA_Guide_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\48B_Order_Task_API_PWA_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\48B_Order_Task_API_PWA_v1.1.md
- C:\Obsidian\Dooly\03_Claude_Code\49_Order_Claude_API_Worker_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\50_Order_Gemini_API_Worker_v2.0.md
- C:\Obsidian\Dooly\03_Claude_Code\51_Order_Vercel_Migration_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52_Order_PWA_Icon_Gemini_Fix_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52E_Order_SW_Cache_Gemini_UI_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52F_Order_Manifest_Link_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52G_Order_Gemini_Source_Number_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52H_Order_Source_Tag_Fix_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52I_Order_Gemini_Response_Fix_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52X_Order_Rollback_to_52F_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\52Y_Order_Rollback_to_52E_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\53_Order_Supabase_Task_Sync_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\54_Order_Dooly_Manifest_ErrorHandling_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\55_Order_Archive_Runtime_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\56_Order_GitHubPages_Update_v1.0.md
- C:\Obsidian\Dooly\03_Claude_Code\57_Order_TaskFilter_Sync_v1.0.md
- C:\Obsidian\Dooly\05_RAG\docs\faq_data.txt
- C:\Obsidian\Dooly\05_RAG\docs\sop_data.txt
- C:\Obsidian\Dooly\05_RAG\README_RAG.txt
- C:\Obsidian\Dooly\05_RAG\embed.py
- C:\Obsidian\Dooly\05_RAG\server.py
- C:\Obsidian\Dooly\05_RAG\run_embed.bat
- C:\Obsidian\Dooly\05_RAG\run_server.bat
- C:\Obsidian\Dooly\05_RAG\start.bat
- C:\Obsidian\Dooly\api\gemini.js
- C:\Obsidian\Dooly\docs\README.md
- C:\Obsidian\Dooly\docs\02_Task_v1.html
- C:\Obsidian\Dooly\docs\03_SOP_v1.html
- C:\Obsidian\Dooly\docs\04_FAQ_v1.html
- C:\Obsidian\Dooly\docs\05_Notice_v1.html
- C:\Obsidian\Dooly\docs\06_Dooly_v1.html
- C:\Obsidian\Dooly\docs\07_Settings_v1.html
- C:\Obsidian\Dooly\docs\index.html
- C:\Obsidian\Dooly\docs\api\gemini.js
- C:\Obsidian\Dooly\docs\api\tasks.js
- C:\Obsidian\Dooly\docs\data.js
- C:\Obsidian\Dooly\docs\service-worker.js
- C:\Obsidian\Dooly\docs\manifest.json


---

# Dooly 업무 규칙

(추후 작성)

---

# Dooly FAQ

(추후 작성)