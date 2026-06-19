# 03_Agent_Basic

## 목표

LLM 기반 Agent의 기본 개념을 이해하고, Tool Calling, Memory, Prompt Engineering을 활용하여 실제 Agent를 구현할 수 있는 역량을 확보한다.

최종 목표

* Agent와 Chatbot의 차이 이해
* Tool Calling 구현
* Memory 구현
* Agent Workflow 이해
* LangChain 기반 Agent 구축
* MCP 학습을 위한 기반 확보

---

## 학습 내용

### Agent란?

Agent는 단순히 질문에 답변하는 LLM이 아니라 목표를 달성하기 위해 스스로 판단하고 도구를 사용하는 시스템이다.

기존 ChatGPT

```text id="chat1"
사용자 질문
    ↓
LLM
    ↓
응답
```

Agent

```text id="agent1"
사용자 질문
    ↓
Agent
    ↓
판단
    ↓
Tool 실행
    ↓
결과 수집
    ↓
응답
```

---

### Chatbot과 Agent 차이

| 항목        | Chatbot | Agent |
| --------- | ------- | ----- |
| 응답 생성     | 가능      | 가능    |
| Tool 사용   | 불가      | 가능    |
| 외부 시스템 연동 | 제한적     | 가능    |
| 작업 수행     | 불가      | 가능    |
| 자동화       | 제한적     | 가능    |

---

### Agent 핵심 구성요소

#### LLM

의사결정 엔진

예시

* GPT
* Claude
* Qwen
* Gemma

---

#### Prompt

Agent 행동 정의

예시

```text id="prompt1"
당신은 Kubernetes 운영 전문가입니다.
```

---

#### Tool

외부 기능 호출

예시

* DB 조회
* API 호출
* 파일 읽기
* Kubernetes 조회

---

#### Memory

대화 및 상태 기억

예시

```text id="memory1"
사용자 이름 기억
이전 질문 기억
```

---

#### Workflow

작업 흐름 정의

예시

```text id="workflow1"
질문
 ↓
판단
 ↓
Tool 실행
 ↓
응답 생성
```

---

### Agent 아키텍처

```text id="agentarch1"
사용자
    ↓
Agent
    ↓
Planner
    ↓
Tool
    ↓
LLM
    ↓
응답
```

---

## 실습 절차

### 1. Python 환경 구성

가상환경 생성

```bash id="pyenv1"
python -m venv venv
```

활성화

```bash id="pyenv2"
source venv/bin/activate
```

---

### 2. 패키지 설치

```bash id="pkg1"
pip install langchain
pip install langchain-community
pip install langchain-ollama
```

---

### 3. Ollama 실행

```bash id="ollama31"
ollama run qwen3:4b
```

확인

```bash id="ollama32"
ollama list
```

---

### 4. LLM 호출 실습

예제

```python id="llm1"
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:4b")

result = llm.invoke("안녕하세요")
print(result.content)
```

---

### 5. Prompt Engineering 실습

예제

```python id="prompt2"
prompt = """
당신은 PostgreSQL 전문가입니다.
"""
```

확인 항목

* 역할 지정
* 응답 품질 변화

---

### 6. Tool Calling 실습

예제

```python id="tool1"
def get_time():
    return "현재 시간 조회"
```

Agent가 Tool 호출 가능 여부 확인

---

### 7. Memory 실습

예제

```text id="memory2"
내 이름은 Dabin이다.
```

이후

```text id="memory3"
내 이름이 뭐야?
```

정상 기억 여부 확인

---

### 8. Agent 구현

예제

```text id="agentexample1"
질문
 ↓
Agent
 ↓
Tool 호출
 ↓
응답 생성
```

---

## TODO

### 환경 구축

* [ ] Python 설치
* [ ] LangChain 설치
* [ ] Ollama 연동

### 실습

* [ ] LLM 호출
* [ ] Prompt 실습
* [ ] Tool Calling
* [ ] Memory 구현
* [ ] Agent 구현

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### LLM 검증

질문 입력 시 정상 응답 여부 확인

---

### Tool 검증

Agent가 Tool 호출 가능한지 확인

예시

```text id="toolcheck1"
현재 시간을 알려줘
```

---

### Memory 검증

이전 정보 기억 여부 확인

---

### Workflow 검증

질문

```text id="workflowcheck1"
DB 상태를 조회해줘
```

확인

```text id="workflowcheck2"
Agent
 ↓
Tool
 ↓
결과
 ↓
응답
```

---

### 재현 검증

동일 환경에서 재실행 후 동일 동작 여부 확인

---

## 결과물

### 코드

* LLM 호출 코드
* Tool Calling 코드
* Memory 코드
* Agent 코드

### 문서

* Agent 구축 가이드
* Prompt 모음
* 트러블슈팅 문서

### 다이어그램

* Agent Architecture
* Agent Workflow

---

## 회고

### 배운 점

* Agent 구조 이해
* Tool Calling 이해
* Memory 이해
* Prompt Engineering 이해

### 개선점

* Tool 종류 확대 필요
* Prompt 최적화 필요
* Memory 고도화 필요

### 다음 단계

* MCP
* LangGraph
* Kubernetes Agent

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* Prompt 예제
* Tool 예제
* Memory 예제

### 스크린샷

* Agent 실행 화면
* Tool 호출 결과
* Memory 테스트 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 Agent가 필요한가?

기존 Chatbot은 응답만 가능하지만 Agent는 실제 작업 수행이 가능하다.

---

### 구현 방법

* Ollama 구성
* LangChain 구성
* Tool 구현
* Memory 구현

---

### 트러블슈팅

예상 사례

* Tool 호출 실패
* Prompt 오류
* Context 부족
* Memory 관리 문제

---

### 결과

* Agent 구축 완료
* Tool Calling 구현
* Memory 구현

---

## 면접 포인트

### Agent란 무엇인가?

LLM을 활용하여 목표를 달성하기 위해 스스로 판단하고 Tool을 사용하는 시스템이다.

---

### Tool Calling이란?

Agent가 외부 기능을 호출하는 방식이다.

예시

* DB 조회
* API 호출
* 파일 읽기
* Kubernetes 조회

---

### Memory란?

Agent가 이전 상태나 대화 내용을 기억하는 기능이다.

종류

* Short-Term Memory
* Long-Term Memory

---

### Prompt Engineering이 중요한 이유는?

Agent 행동을 결정하기 때문이다.

동일 모델이라도 Prompt에 따라 결과 품질이 달라진다.

---

### LangChain을 사용하는 이유는?

장점

* Tool Calling 지원
* Memory 지원
* Agent Framework 제공

---

### 대안은 무엇인가?

* LangGraph
* CrewAI
* AutoGen
* Semantic Kernel

---

### 운영 시 고려사항

* Prompt 관리
* Memory 관리
* Tool 권한 관리
* 비용 관리
* 응답 품질 관리

---

### AI Platform Engineer 관점 핵심 포인트

Agent는 AI Platform의 핵심 실행 단위이다.

향후 학습 흐름

```text id="agentflow31"
LLM
    ↓
Prompt
    ↓
Tool Calling
    ↓
Memory
    ↓
Agent
    ↓
MCP
    ↓
Multi-Agent
    ↓
AI Operations Platform
```

---

### 실무 적용 포인트

현재 경험과 연결 가능

* PostgreSQL 운영 Agent
* Kubernetes 운영 Agent
* Kafka 운영 Agent
* OpenTelemetry 분석 Agent

즉, 지금까지 수행한 운영 업무를 Agent로 자동화하기 위한 가장 중요한 기초 단계이다.
