# AI Platform Engineer Portfolio

## 소개

Backend Engineer에서 AI Platform Engineer로 전환하기 위해 수행한 학습 및 프로젝트 포트폴리오입니다.

기존 경험

* Spring Boot
* PostgreSQL
* Kafka
* Kubernetes
* OpenTelemetry
* MSA 전환 사업

을 기반으로 AI Agent, MCP, Multi-Agent, AI Operations Platform 영역까지 확장하는 것을 목표로 진행하였습니다.

---

# 목표

## 최종 목표

AI 기반 운영 자동화 플랫폼 구축

### 구현 범위

* Local LLM 구축
* AI Agent 개발
* MCP 구축
* Kubernetes Agent 구축
* Database Agent 구축
* Observability Agent 구축
* Multi-Agent 구축
* AI Operations Platform 구축

---

# 기술 스택

## AI / LLM

* Ollama (Local LLM Runtime)
* Qwen3 4B
* Gemma 2B/3B
* DeepSeek-R1 8B
* Open WebUI (개발 예정)

---

# 01. Local ChatGPT (완료 ✅)

## 목표

로컬 환경에서 LLM을 직접 실행하여 AI 서비스의 기본 구조 이해 및 향후 Agent 개발 기반 확보

## 완료 내용

### 1. 환경 구축

- WSL2 Ubuntu에서 Ollama 설치 (v0.30.10)
- 3개 LLM 모델 다운로드 완료 (Qwen3, Gemma, DeepSeek)
- 모델 실행 및 정상 작동 확인
- Open WebUI 설치 및 연동 완료

### 2. 학습 요소

- Local LLM의 개념과 장단점
- Ollama 런타임의 기능 및 API 구조
- 오픈소스 LLM 모델 비교 분석
- REST API 기반 LLM 호출
- WSL2 내 Docker 네트워크 구조

### 3. 기술 검증

- ✅ Ollama 설치 성공 (v0.30.10)
- ✅ 모델 다운로드 성공 (3개)
- ✅ CLI 테스트 성공
- ✅ API 호출 성공
- ✅ Open WebUI 연동 성공
- ✅ 성능 확인 (Qwen3 4B 기준)

### 4. 발생 문제 및 해결

**문제 1**: Open WebUI → Ollama 연결 실패
- 원인: Ollama가 127.0.0.1:11434로만 바인딩
- 해결: systemd override로 0.0.0.0:11434로 변경

**문제 2**: Windows에서 서비스 접근 실패
- 원인: WSL2 내부 Docker 사용으로 localhost 불가
- 해결: WSL2 IP (172.30.236.141) 기반 접근

### 5. 최종 아키텍처

```
Windows Browser
    ↓
172.30.236.141:3000
    ↓
Open WebUI
    ↓
172.30.236.141:11434
    ↓
Ollama
    ↓
qwen3:4b
```

### 6. 완료 체크리스트

- [x] WSL2 설치
- [x] Docker 사용 가능
- [x] Ollama 설치
- [x] 모델 다운로드
- [x] CLI 테스트
- [x] Open WebUI 설치
- [x] Ollama 연결
- [x] 모델 인식
- [x] Local ChatGPT 구축 완료

### 7. 다음 단계

- [ ] Open WebUI 고급 기능 학습
- [ ] Python API 클라이언트 작성
- [ ] Agent 프레임워크 연동

---

# 02. IDE Agent (예정)

## 목표

VSCode에서 AI Agent를 활용하여 코드 작성 보조

## 기술 스택 후보

- Continue
- Cline
- RooCode

---

# 03. Agent Basic (예정)

## 목표

AI Agent의 기본 개념 및 구현 학습

## 학습 대상

- Tool Calling
- Agent Workflow
- Multi-Agent Patterns

---

---

## Agent

* LangChain
* LangGraph
* MCP

---

## Backend

* Python
* Spring Boot

---

## Database

* PostgreSQL

---

## Platform

* Docker
* Kubernetes

---

## Observability

* OpenTelemetry
* Prometheus
* Grafana
* Jaeger

---

# 프로젝트 진행 현황

| 단계 | 프로젝트                   | 상태 | 완료일 |
| -- | ---------------------- | -- | --- |
| 01 | Local ChatGPT          | ⬜  |     |
| 02 | IDE Agent              | ⬜  |     |
| 03 | Agent Basic            | ⬜  |     |
| 04 | MCP                    | ⬜  |     |
| 05 | Kubernetes Agent       | ⬜  |     |
| 06 | Database Agent         | ⬜  |     |
| 07 | Observability          | ⬜  |     |
| 08 | Multi-Agent            | ⬜  |     |
| 09 | AI Operations Platform | ⬜  |     |

---

# 프로젝트 상세

## Project 01. Local ChatGPT

### 목표

로컬 환경에서 LLM 실행

### 기술

* Ollama
* Qwen3
* Open WebUI

### 결과

* Local LLM 구축

### 관련 문서

* docs/01_Local_ChatGPT.md

### GitHub

* 링크 작성

---

## Project 02. IDE Agent

### 목표

AI 개발 환경 구축

### 기술

* Cursor
* Codex
* Copilot

### 결과

* 코드 생성 자동화
* 리뷰 자동화

### 관련 문서

* docs/02_IDE_Agent.md

### GitHub

* 링크 작성

---

## Project 03. Agent Basic

### 목표

Tool Calling Agent 구축

### 기술

* LangChain
* Ollama

### 결과

* Agent 구현
* Memory 구현

### 관련 문서

* docs/03_Agent_Basic.md

---

## Project 04. MCP

### 목표

MCP Server 구축

### 기술

* MCP SDK
* Python

### 결과

* MCP Server 구축

### 관련 문서

* docs/04_MCP.md

---

## Project 05. Kubernetes Agent

### 목표

Kubernetes 운영 자동화

### 기술

* Kubernetes API
* MCP

### 결과

* Pod 조회 Agent
* 로그 분석 Agent

### 관련 문서

* docs/05_Kubernetes_Agent.md

---

## Project 06. Database Agent

### 목표

Database 운영 자동화

### 기술

* PostgreSQL
* MCP

### 결과

* 자연어 SQL
* 운영 분석

### 관련 문서

* docs/06_Database_Agent.md

---

## Project 07. Observability

### 목표

관측성 기반 장애 분석

### 기술

* OpenTelemetry
* Grafana
* Jaeger

### 결과

* Trace 분석
* Metric 분석

### 관련 문서

* docs/07_Observability.md

---

## Project 08. Multi-Agent

### 목표

Agent 협업 구조 구축

### 기술

* LangGraph
* CrewAI

### 결과

* Coordinator Agent
* 협업 Workflow

### 관련 문서

* docs/08_Multi_Agent.md

---

## Project 09. AI Operations Platform

### 목표

AI 기반 운영 자동화 플랫폼 구축

### 기술

* Multi-Agent
* MCP
* Kubernetes
* PostgreSQL
* OpenTelemetry

### 결과

* 자연어 기반 운영 플랫폼

### 관련 문서

* docs/09_AI_Operations_Platform.md

---

# 핵심 의사결정

| 항목              | 결정            |
| --------------- | ------------- |
| Local LLM       | Ollama        |
| 기본 모델           | Qwen3         |
| Agent Framework | LangChain     |
| Workflow        | LangGraph     |
| Tool 표준         | MCP           |
| DB              | PostgreSQL    |
| Platform        | Kubernetes    |
| Observability   | OpenTelemetry |

자세한 내용은 decision-log.md 참고

---

# 트러블슈팅

## 주요 이슈

| 날짜 | 내용 | 해결 |
| -- | -- | -- |
|    |    |    |
|    |    |    |
|    |    |    |

---

# 최종 아키텍처

```text
사용자
    ↓

Open WebUI

    ↓

Coordinator Agent

    ↓

Database Agent
Kubernetes Agent
Observability Agent

    ↓

MCP

    ↓

PostgreSQL
Kubernetes
OpenTelemetry
```

---

# 핵심 역량

## AI

* Local LLM 구축
* Agent 개발
* MCP 개발
* Multi-Agent 설계

---

## Platform

* Kubernetes 운영
* Docker 운영
* AI 플랫폼 설계

---

## Observability

* OpenTelemetry
* Prometheus
* Grafana
* Jaeger

---

## Database

* PostgreSQL 운영
* SQL 최적화
* Database Agent 구축

---

# 향후 계획

## 단기

* AI Operations Platform 완성
* GitHub 공개

## 중기

* RAG 구축
* Vector Database 구축

## 장기

* Enterprise AI Platform 구축
* AI Platform Engineer 전환

---

# 참고 문서

* README.md
* decision-log.md
* weekly-review.md
* docs/00_Roadmap.md

```
```
