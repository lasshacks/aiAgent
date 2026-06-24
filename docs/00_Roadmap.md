# 00_Roadmap

## 목표

현재 보유한 Backend/Cloud Native 역량을 기반으로 AI 기술을 결합하여 AI Platform Engineer 역량을 확보한다.

최종적으로 다음 역량을 확보하는 것을 목표로 한다.

* Local LLM 환경 구축
* AI Agent 개발 및 운영
* MCP(Model Context Protocol) 활용
* Kubernetes 기반 AI 플랫폼 운영
* Observability 기반 AI 서비스 모니터링
* Multi-Agent 시스템 설계
* AI Operations Platform 구축

---

## 학습 내용

### Phase 1. Local AI 환경 구축

#### 01_Local_ChatGPT

학습 목표

* Local LLM 실행 환경 구축
* 오픈소스 모델 실행
* API 기반 호출 이해

주요 기술

* Ollama
* Qwen
* Gemma
* DeepSeek
* Open WebUI

---

### Phase 2. 개발 생산성 향상

#### 02_IDE_Agent

학습 목표

* AI 기반 개발 환경 구축
* 코드 생성 및 리뷰 자동화

주요 기술

* GitHub Copilot
* Codex
* Cursor
* VS Code

---

### Phase 3. Agent 기초

#### 03_Agent_Basic

학습 목표

* LLM 기반 Agent 개발
* Tool Calling 이해
* Memory 이해

주요 기술

* OpenAI SDK
* LangChain
* Prompt Engineering

---

### Phase 4. MCP

#### 04_MCP

학습 목표

* MCP 구조 이해
* MCP Server 구축
* MCP Client 연동

주요 기술

* MCP
* Python
* FastAPI

---

### Phase 5. Kubernetes Agent

#### 05_Kubernetes_Agent

학습 목표

* Kubernetes 운영 Agent 구축
* Pod 상태 분석
* 로그 조회 및 장애 진단

주요 기술

* Kubernetes API
* MCP
* Agent

---

### Phase 6. Database Agent

#### 06_Database_Agent

학습 목표

* PostgreSQL 운영 Agent 구축
* SQL 생성 및 분석
* 운영 지원 자동화

주요 기술

* PostgreSQL
* Vector Search
* Agent

---

### Phase 7. Observability

#### 07_Observability

학습 목표

* AI 서비스 관측성 확보
* Trace / Metric / Log 분석

주요 기술

* OpenTelemetry
* Prometheus
* Grafana
* Jaeger

---

### Phase 8. Multi-Agent

#### 08_Multi_Agent

학습 목표

* Agent 협업 구조 설계
* 역할 기반 Agent 구성

예시

* Kubernetes Agent
* DBA Agent
* Developer Agent
* Reviewer Agent

주요 기술

* LangGraph
* CrewAI

---

### Phase 9. AI Operations Platform

#### 09_AI_Operations_Platform

학습 목표

* AI 기반 운영 자동화 플랫폼 구축

구성 요소

* Chat Interface
* Agent Layer
* MCP Layer
* Tool Layer
* Kubernetes
* Database
* Monitoring

---

## 실습 절차

### STEP 1. 환경 구축

* WSL2
* Docker
* VS Code
* Ollama

### STEP 2. 모델 실행

```bash
ollama run qwen3:4b
```

### STEP 3. Agent 개발

* Prompt 작성
* Tool 연동
* Memory 구현

### STEP 4. MCP 연동

* MCP Server 구축
* Tool 연결
* Database 연결
* Kubernetes 연결

### STEP 5. 운영 플랫폼 구축

* Dashboard
* Monitoring
* Logging
* Alerting

---

## TODO

### 학습 목표

* [ ] Local ChatGPT 구축
* [ ] IDE Agent 구축
* [x] Agent 기초 학습
* [ ] MCP 구축
* [ ] Kubernetes Agent 구축
* [ ] Database Agent 구축
* [ ] Observability 구축
* [ ] Multi-Agent 구축
* [ ] AI Operations Platform 구축

### 포트폴리오

* [ ] GitHub 정리
* [ ] 기술 블로그 작성
* [ ] 아키텍처 다이어그램 작성

---

## 검증 방법

### 기능 검증

* 모델 정상 응답
* Agent 정상 동작
* Tool 정상 호출

### 운영 검증

* 로그 수집 확인
* Trace 확인
* Metric 확인

### 플랫폼 검증

* 장애 재현 가능
* Agent 자동 대응 가능
* 운영 자동화 가능

---

## 결과물

### 코드

* Python Source
* MCP Server
* Agent Source

### 문서

* 구축 가이드
* 운영 가이드
* 트러블슈팅 문서

### 다이어그램

* AI Platform Architecture
* MCP Architecture
* Multi-Agent Architecture

---

## 회고

### 배운 점

* LLM 구조 이해
* Agent 동작 원리 이해
* MCP 활용 방법 이해

### 개선점

* Prompt 최적화
* Agent 응답 품질 향상
* 운영 자동화 확대

### 다음 단계

* RAG
* Vector Database
* AI Gateway
* Enterprise AI Platform

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* Architecture Diagram
* Screenshot
* Troubleshooting

### 저장소 구조 예시

```text
AI_Platform_Engineering_Lab/

README.md
decision-log.md
weekly-review.md
portfolio.md

docs/
├── 00_Roadmap.md
├── 01_Local_ChatGPT.md
├── 02_IDE_Agent.md
├── 03_Agent_Basic.md
├── 04_MCP.md
├── 05_Kubernetes_Agent.md
├── 06_Database_Agent.md
├── 07_Observability.md
├── 08_Multi_Agent.md
└── 09_AI_Operations_Platform.md
```

---

## 블로그 작성 포인트

### 문제 정의

* 왜 AI Platform Engineer를 목표로 했는가

### 구현 방법

* 환경 구성
* 아키텍처 설계
* 기술 선택 이유

### 트러블슈팅

* 설치 오류
* 연동 오류
* 성능 이슈

### 결과

* 구축 결과
* 배운 점
* 개선 방향

---

## 면접 포인트

### AI

* LLM과 Agent의 차이
* RAG란 무엇인가
* MCP란 무엇인가

### 플랫폼

* Kubernetes를 사용하는 이유
* Agent 운영 시 고려사항
* Observability가 필요한 이유

### 운영

* 장애 발생 시 대응 방법
* AI 서비스 모니터링 방법
* 비용 최적화 방안

### 실무 적용

* 기존 MSA 운영 경험과 AI Agent의 접목 방안
* Kubernetes 운영 자동화 사례
* Database 운영 자동화 사례
