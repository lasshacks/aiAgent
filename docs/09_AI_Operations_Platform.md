# 09_AI_Operations_Platform

## 목표

지금까지 구축한 Local LLM, MCP, Kubernetes Agent, Database Agent, Observability Agent를 통합하여 AI 기반 운영 자동화 플랫폼(AI Operations Platform)을 구축한다.

최종 목표

* 자연어 기반 운영 플랫폼 구축
* Multi-Agent 기반 운영 자동화
* 장애 분석 자동화
* 운영 지원 자동화
* AI Platform Engineer 포트폴리오 완성

---

## 프로젝트 개요

### 프로젝트명

AI Operations Platform

### 목적

기존 운영자가 수행하던 반복 업무를 AI Agent가 대신 수행할 수 있도록 플랫폼을 구축한다.

예시

```text
현재 장애 원인 알려줘

→ Kubernetes 조회
→ PostgreSQL 조회
→ Trace 분석
→ 로그 분석
→ 원인 도출
→ 대응 방안 제시
```

---

## 전체 아키텍처

```text
사용자
    ↓

Web Chat UI
(Open WebUI)

    ↓

Coordinator Agent

    ↓

────────────────────────────

Database Agent

Kubernetes Agent

Observability Agent

Developer Agent

────────────────────────────

    ↓

MCP Layer

    ↓

────────────────────────────

PostgreSQL

Kubernetes

OpenTelemetry

Prometheus

Grafana

Jaeger

────────────────────────────
```

---

## 학습 내용

### Layer 1. Interface

사용자와 상호작용

구성

* Open WebUI
* Chat Interface

역할

* 질문 입력
* 결과 확인

---

### Layer 2. Agent

운영 업무 수행

구성

* Coordinator Agent
* Database Agent
* Kubernetes Agent
* Observability Agent

역할

* 작업 분배
* 결과 분석
* 응답 생성

---

### Layer 3. MCP

Tool 표준화 계층

구성

* Database MCP
* Kubernetes MCP
* Observability MCP

역할

* Tool 연결
* 권한 관리
* 인터페이스 표준화

---

### Layer 4. Platform

실제 운영 환경

구성

* PostgreSQL
* Kubernetes
* Prometheus
* Grafana
* Jaeger

---

## 주요 기능

### 기능 1. 자연어 기반 운영 조회

예시

```text
현재 장애 있는 Pod 알려줘
```

수행

```text
Kubernetes Agent
 ↓
MCP
 ↓
Kubernetes API
```

---

### 기능 2. Database 조회

예시

```text
오늘 가입한 회원 수 알려줘
```

수행

```text
Database Agent
 ↓
SQL 생성
 ↓
PostgreSQL 조회
```

---

### 기능 3. 장애 분석

예시

```text
서비스가 느린 원인 알려줘
```

수행

```text
Coordinator
 ↓
K8s Agent
 ↓
DB Agent
 ↓
Obs Agent
 ↓
결과 통합
```

---

### 기능 4. 운영 보고서 생성

예시

```text
오늘 장애 현황 정리해줘
```

결과

```text
장애 건수
영향 범위
원인 분석
조치 결과
```

---

### 기능 5. AI 운영 어시스턴트

예시

```text
OOMKilled 원인 알려줘
```

예상 응답

```text
메모리 제한 512Mi
실사용량 780Mi

조치 권장

- Limit 증가
- Heap 설정 확인
```

---

## 실습 절차

### 1단계

Local LLM 준비

```bash
ollama run qwen3:4b
```

확인

* 모델 실행

---

### 2단계

MCP Server 구성

구성

* Database MCP
* Kubernetes MCP
* Observability MCP

---

### 3단계

Agent 구성

구성

* Coordinator Agent
* Database Agent
* Kubernetes Agent
* Observability Agent

---

### 4단계

Open WebUI 연결

목표

* Chat Interface 제공

---

### 5단계

운영 시나리오 테스트

테스트 예시

```text
현재 장애 있는 서비스 알려줘
```

---

### 6단계

통합 테스트

테스트 항목

* Agent 호출
* MCP 호출
* DB 조회
* K8s 조회
* Trace 조회

---

## TODO

### 플랫폼

* [ ] Open WebUI 구축
* [ ] MCP Server 구축
* [ ] Multi-Agent 구축

### Agent

* [ ] Database Agent
* [ ] Kubernetes Agent
* [ ] Observability Agent

### 운영

* [ ] 장애 분석 자동화
* [ ] 운영 리포트 자동화
* [ ] 자연어 조회 기능

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성
* [ ] 아키텍처 다이어그램 작성

---

## 검증 방법

### 기능 검증

질문

```text
현재 장애 있는 Pod 알려줘
```

정상 응답 여부 확인

---

### Agent 검증

확인 항목

* Agent 선택
* Tool 호출
* 결과 반환

---

### MCP 검증

확인 항목

* DB 조회
* Kubernetes 조회
* Observability 조회

---

### 통합 검증

확인 항목

* Multi-Agent 협업
* 장애 분석
* 보고서 생성

---

### 재현 검증

새 환경에서 동일 구축 후 정상 동작 확인

---

## 결과물

### 코드

* MCP Server
* Multi-Agent
* Database Agent
* Kubernetes Agent
* Observability Agent

### 문서

* 구축 가이드
* 운영 가이드
* 트러블슈팅 문서

### 다이어그램

* AI Operations Platform Architecture
* Multi-Agent Workflow
* MCP Architecture

---

## 회고

### 배운 점

* AI Agent 구조 이해
* MCP 활용 방법 이해
* Multi-Agent 설계 방법 이해
* 운영 자동화 방법 이해

### 개선점

* Agent 정확도 향상
* Prompt 최적화
* 자동 조치 기능 추가

### 다음 단계

* RAG
* Vector Database
* Enterprise AI Platform
* AIOps 고도화

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법
* 아키텍처 설명

### 권장

* 시연 영상
* Prompt 예제
* MCP 설정 예제

### 스크린샷

* Open WebUI
* Agent 실행 화면
* 장애 분석 결과
* Dashboard 화면

---

## 블로그 작성 포인트

### 문제 정의

왜 AI Operations Platform이 필요한가?

운영자가 반복적으로 수행하는 조회, 분석, 진단 업무를 자동화하기 위해서이다.

---

### 구현 방법

* Local LLM 구축
* MCP 구축
* Agent 구축
* Multi-Agent 구축
* 운영 시스템 연동

---

### 트러블슈팅

예상 사례

* MCP 연결 실패
* Agent 선택 오류
* Context 부족
* Tool 권한 문제

---

### 결과

* 자연어 기반 운영 플랫폼 구축
* 운영 자동화 구현
* 장애 분석 자동화 구현

---

## 면접 포인트

### AI Operations Platform이란?

AI Agent를 활용하여 운영 업무를 자동화하는 플랫폼이다.

---

### 기존 운영 방식과 차이는?

기존

```text
운영자
 ↓
조회
 ↓
분석
 ↓
조치
```

AI 기반

```text
운영자
 ↓
질문
 ↓
AI Agent
 ↓
분석
 ↓
응답
```

---

### 왜 Multi-Agent 구조를 사용했는가?

역할 분리를 통해

* 확장성 확보
* 유지보수성 향상
* 전문성 강화

를 달성하기 위함이다.

---

### MCP를 사용하는 이유는?

Agent와 외부 시스템 연결을 표준화하기 위해서이다.

---

### 실무 적용 사례는?

* PostgreSQL 운영 자동화
* Kubernetes 운영 자동화
* OpenTelemetry 분석 자동화
* 장애 원인 분석 자동화

---

### 운영 시 고려사항

* 권한 관리
* 감사 로그
* 비용 관리
* Agent 오작동 방지
* 개인정보 보호

---

## 포트폴리오 핵심 메시지

### Before

```text
Spring Boot 개발자
+
MSA 운영 경험
+
Kubernetes 운영 경험
```

### After

```text
AI Platform Engineer

- Local LLM 구축
- MCP 구축
- Kubernetes Agent 구축
- Database Agent 구축
- Observability Agent 구축
- Multi-Agent 구축
- AI Operations Platform 구축
```

---

## 최종 완성 로드맵

```text
01 Local ChatGPT
        ↓
02 IDE Agent
        ↓
03 Agent Basic
        ↓
04 MCP
        ↓
05 Kubernetes Agent
        ↓
06 Database Agent
        ↓
07 Observability
        ↓
08 Multi-Agent
        ↓
09 AI Operations Platform
        ↓
AI Platform Engineer
```
