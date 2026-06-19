# 08_Multi_Agent

## 목표

여러 Agent가 협업하여 복잡한 업무를 수행하는 Multi-Agent 시스템을 구축하고, 운영 자동화 플랫폼의 핵심 구조를 설계한다.

최종 목표

* Multi-Agent 개념 이해
* Agent 역할 분리
* Agent 간 협업 구조 구현
* LangGraph 활용
* CrewAI 활용
* 운영 자동화 Workflow 구축

---

## 학습 내용

### Multi-Agent란?

하나의 Agent가 모든 업무를 수행하는 것이 아니라 역할별 Agent가 협업하여 문제를 해결하는 구조이다.

---

### Single Agent 구조

```text id="singleagent1"
사용자
    ↓
Agent
    ↓
DB 조회
    ↓
Kubernetes 조회
    ↓
로그 분석
    ↓
응답
```

문제점

* 역할 과다
* Prompt 복잡도 증가
* 유지보수 어려움

---

### Multi-Agent 구조

```text id="multiagent1"
사용자
    ↓
Coordinator Agent
    ↓
┌─────────────┬─────────────┬─────────────┐
│             │             │
DB Agent   K8s Agent   Obs Agent
│             │             │
└─────────────┴─────────────┘
              ↓
           응답
```

---

### Multi-Agent가 필요한 이유

실제 운영 업무는 여러 전문가가 협업한다.

예시

```text id="realworld1"
장애 발생
 ↓
DBA
 ↓
인프라 담당자
 ↓
개발자
 ↓
원인 분석
```

Agent도 동일한 방식 적용

---

### Agent 역할 분리

#### Coordinator Agent

역할

* 요청 분석
* 작업 분배
* 결과 취합

---

#### Database Agent

역할

* SQL 생성
* 데이터 조회
* 성능 분석

---

#### Kubernetes Agent

역할

* Pod 조회
* 로그 조회
* 이벤트 조회

---

#### Observability Agent

역할

* Metric 분석
* Log 분석
* Trace 분석

---

#### Developer Agent

역할

* 코드 분석
* 코드 생성
* 코드 리뷰

---

### Multi-Agent 아키텍처

```text id="multiarch1"
사용자
    ↓
Coordinator Agent
    ↓
Agent Router
    ↓
─────────────────────
DB Agent
K8s Agent
Obs Agent
Developer Agent
─────────────────────
    ↓
MCP
    ↓
Tool
```

---

### Agent 협업 예시

질문

```text id="question81"
서비스가 느린 원인 알려줘
```

---

처리 흐름

```text id="workflow81"
Coordinator
    ↓
K8s Agent
    ↓
CPU 확인

Coordinator
    ↓
DB Agent
    ↓
Slow Query 확인

Coordinator
    ↓
Obs Agent
    ↓
Trace 분석

결과 통합
    ↓
최종 응답
```

---

## 실습 절차

### 1. Multi-Agent Framework 설치

LangGraph

```bash id="multi81"
pip install langgraph
```

CrewAI

```bash id="multi82"
pip install crewai
```

---

### 2. Coordinator Agent 생성

역할

* 요청 수신
* Agent 선택

예제

```python id="coord81"
def route_request():
    pass
```

---

### 3. Database Agent 생성

기능

* SQL 생성
* 데이터 조회

---

### 4. Kubernetes Agent 생성

기능

* Pod 조회
* 로그 분석

---

### 5. Observability Agent 생성

기능

* Metric 분석
* Trace 분석

---

### 6. Agent Router 구현

예제

```text id="router81"
DB 질문
 ↓
Database Agent

Kubernetes 질문
 ↓
Kubernetes Agent
```

---

### 7. Agent 협업 구현

예제

```text id="cooperate81"
장애 원인 알려줘
```

호출

```text id="cooperate82"
K8s Agent
+
DB Agent
+
Obs Agent
```

---

### 8. LangGraph Workflow 구현

구성

```text id="langgraph81"
START
 ↓
Coordinator
 ↓
Agent
 ↓
END
```

---

### 9. MCP 연동

구성

```text id="mcp81"
Agent
 ↓
MCP
 ↓
Tool
```

---

### 10. Multi-Agent 구축

최종 기능

* Agent 협업
* 결과 통합
* 운영 분석

---

## TODO

### 환경 구축

* [ ] LangGraph 설치
* [ ] CrewAI 설치

### 실습

* [ ] Coordinator Agent
* [ ] Database Agent
* [ ] Kubernetes Agent
* [ ] Observability Agent

### Workflow

* [ ] Agent Router
* [ ] 협업 Workflow

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### 단일 Agent 검증

각 Agent 정상 동작 확인

---

### Router 검증

질문별 올바른 Agent 호출 확인

---

### 협업 검증

예제

```text id="verify81"
서비스가 느린 원인 알려줘
```

확인

```text id="verify82"
K8s Agent
+
DB Agent
+
Obs Agent
```

---

### Workflow 검증

LangGraph 실행 결과 확인

---

### 재현 검증

다른 환경에서 동일 결과 확인

---

## 결과물

### 코드

* Coordinator Agent
* Database Agent
* Kubernetes Agent
* Observability Agent

### 문서

* 구축 가이드
* Workflow 설명서
* 운영 가이드

### 다이어그램

* Multi-Agent Architecture
* Workflow Diagram

---

## 회고

### 배운 점

* Multi-Agent 구조 이해
* Agent 협업 이해
* Workflow 설계 방법 이해

### 개선점

* Agent 정확도 향상
* Workflow 최적화
* Agent 간 충돌 방지

### 다음 단계

* AI Operations Platform

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* Workflow Diagram
* Agent 설명
* Prompt 예제

### 스크린샷

* Agent 실행 화면
* Workflow 결과
* 협업 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 Single Agent만으로는 부족한가?

복잡한 운영 업무는 여러 전문가의 협업이 필요하기 때문이다.

---

### 구현 방법

* 역할 정의
* Agent 구현
* Router 구현
* Workflow 구현

---

### 트러블슈팅

예상 사례

* Agent 선택 오류
* Context 공유 문제
* 응답 충돌
* Workflow Loop

---

### 결과

* Multi-Agent 구축
* 협업 자동화
* 운영 분석 자동화

---

## 면접 포인트

### Multi-Agent란?

여러 Agent가 역할을 나누어 협업하는 구조이다.

---

### Single Agent와 차이는?

| 항목   | Single Agent | Multi-Agent |
| ---- | ------------ | ----------- |
| 구조   | 단일           | 다중          |
| 유지보수 | 어려움          | 쉬움          |
| 확장성  | 제한적          | 우수          |
| 전문성  | 낮음           | 높음          |

---

### Coordinator Agent 역할은?

* 요청 분석
* Agent 선택
* 결과 통합

---

### LangGraph란?

Agent Workflow를 그래프 형태로 구성하는 프레임워크이다.

---

### CrewAI란?

역할 기반 Multi-Agent 협업 프레임워크이다.

---

### MCP와 어떤 관계가 있는가?

Agent는 MCP를 통해 Tool을 사용한다.

```text id="relation81"
Agent
 ↓
MCP
 ↓
Tool
```

---

### 대안은 무엇인가?

* AutoGen
* Semantic Kernel
* 직접 구현

---

### 운영 시 고려사항

* Agent 권한 분리
* Context 공유 정책
* 비용 관리
* 무한 루프 방지
* Agent 응답 충돌 방지

---

### AI Platform Engineer 관점 핵심 포인트

지금까지 만든 Agent들을 하나의 운영 조직처럼 연결하는 단계이다.

```text id="org81"
DBA
 ↓
DB Agent

SRE
 ↓
Obs Agent

Platform Engineer
 ↓
K8s Agent
```

---

### 실무 적용 포인트

현재 경험과 직접 연결 가능

* PostgreSQL 운영 자동화
* Kubernetes 운영 자동화
* OpenTelemetry 분석 자동화
* 장애 분석 자동화

---

### 최종 운영 시나리오

질문

```text id="scenario81"
현재 서비스 장애 원인 알려줘
```

수행

```text id="scenario82"
Coordinator
 ↓
K8s Agent
 ↓
DB Agent
 ↓
Obs Agent
 ↓
결과 통합
 ↓
응답
```

---

### 최종 목표

```text id="final81"
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
Database Agent
    ↓
Kubernetes Agent
    ↓
Observability Agent
    ↓
Multi-Agent
    ↓
AI Operations Platform
```
