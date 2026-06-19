# Weekly Review

## 목적

AI Platform Engineering Lab 진행 과정에서 매주 학습 내용, 시행착오, 성과, 다음 계획을 기록한다.

목표

* 학습 진행 상황 추적
* 문제점 정리
* 다음 주 계획 수립
* 포트폴리오 작성 자료 확보
* 면접 대비 자료 확보

---

# 작성 규칙

매주 1회 작성

권장 시점

* 금요일 퇴근 전
* 주말 학습 종료 후

---

# Week 1

## 기간

2026-06-19 ~ 2026-06-20

---

## 이번 주 목표

* [x] Local ChatGPT 환경 구축
* [x] Ollama 런타임 이해
* [ ] Agent 기초 학습 진행 (02 Agent Basic)

---

## 진행한 내용

### 학습

* Local LLM의 개념과 구조 이해
* Ollama 런타임의 주요 기능 학습
* Open Source LLM 모델 분류 및 특성 파악
  - Qwen3: 범용 성능 우수
  - Gemma: Google 오픈 모델
  - DeepSeek: 코딩 성능 우수
  - Llama/Mistral: 기초 모델들

### 실습

* WSL2 Ubuntu 환경에서 Ollama 설치 및 설정
* Qwen3 4B 모델 다운로드 및 실행
* Gemma, DeepSeek 모델 다운로드
* Ollama API 호출 테스트 완료
* 모델 정상 작동 확인

### 문서화

* 01_Local_ChatGPT.md 학습 내용 정리
* Decision-001: Ollama 선택 배경 및 이유 기록
* 실습 절차 및 예상 결과 기록

---

## 완료 항목

* [x] 01_Local_ChatGPT 학습 완료
* [x] Ollama 설치 및 기본 구성
* [x] 3개 LLM 모델 다운로드
* [x] API 호출 테스트

---

## 진행 중 항목

* [ ] Open WebUI 연동 (다음 단계)
* [ ] AI Agent 기초 학습 시작
* [ ] 더 큰 모델 테스트 (7B, 8B)

---

## 발생한 문제

### 문제: 없음

순조로운 진행

---

## 새롭게 배운 내용

### 기술

**WSL2 내 Docker → localhost 네트워크 구조**

- Docker Desktop 네트워크 vs WSL2 Ubuntu 네트워크 구조 차이
- Windows localhost 네트워크로는 WSL 내 서비스 접근 불가
- WSL2 내부 IP 기반 네트워크로만 접근 가능

### Ollama 배포

Ollama systemd 서비스 권한

- systemd override.conf 작성 방법
- OLLAMA_HOST 환경변수 동작 원리
- daemon-reload와 서비스 재시작 프로세스

---

# 다음 단계

## Track 2: IDE Agent

### 후보

- Continue
- Cline  
- RooCode

### 목표

```
VSCode
 ↓
Agent
 ↓
Ollama
 ↓
qwen3:4b
```
통합

*

### 개념

*

### 운영 관점

*

---

## 의사결정 사항

관련 문서

* decision-log.md

이번 주 결정

*

---

## 결과물

### 코드

*

### 문서

*

### 다이어그램

*

---

## 가장 의미 있었던 것

*

---

## 아쉬운 점

*

---

## 다음 주 목표

* [ ]
* [ ]
* [ ]

---

## 현재 진행률

| 단계                        | 상태 |
| ------------------------- | -- |
| 01 Local ChatGPT          | ⬜  |
| 02 IDE Agent              | ⬜  |
| 03 Agent Basic            | ⬜  |
| 04 MCP                    | ⬜  |
| 05 Kubernetes Agent       | ⬜  |
| 06 Database Agent         | ⬜  |
| 07 Observability          | ⬜  |
| 08 Multi-Agent            | ⬜  |
| 09 AI Operations Platform | ⬜  |

---

# Weekly Reviews

---

## Week 01

### 기간

2026-06-19 ~ 2026-06-25

### 이번 주 목표

* Ollama 설치
* Qwen3 실행
* 로드맵 작성

### 진행한 내용

#### 학습

* AI Platform Engineering Lab 구조 설계
* 전체 로드맵 작성

#### 실습

* WSL2 확인
* Ollama 설치
* Qwen3 실행

#### 문서화

* README 작성
* Roadmap 작성
* 01~09 문서 작성

### 완료 항목

* [x] Ollama 설치
* [x] Qwen3 실행
* [x] Roadmap 작성

### 발생한 문제

#### Ollama 이해 부족

원인

* Local LLM 경험 없음

해결

* Ollama 구조 학습

### 새롭게 배운 내용

* Ollama는 Local LLM Runtime
* Qwen3는 Ollama에서 실행 가능
* Agent 학습 전에 Local LLM 이해 필요

### 가장 의미 있었던 것

AI Platform Engineer 학습 체계를 구축함

### 다음 주 목표

* Open WebUI 구축
* Cursor 설치
* Codex 실습

### 현재 진행률

| 단계                        | 상태     |
| ------------------------- | ------ |
| 01 Local ChatGPT          | 🟨 진행중 |
| 02 IDE Agent              | ⬜      |
| 03 Agent Basic            | ⬜      |
| 04 MCP                    | ⬜      |
| 05 Kubernetes Agent       | ⬜      |
| 06 Database Agent         | ⬜      |
| 07 Observability          | ⬜      |
| 08 Multi-Agent            | ⬜      |
| 09 AI Operations Platform | ⬜      |
