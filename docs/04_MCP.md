# 04_MCP

## 목표

MCP(Model Context Protocol)의 개념과 구조를 이해하고, AI Agent가 외부 시스템과 표준화된 방식으로 연동할 수 있는 MCP Server를 직접 구축한다.

최종 목표

* MCP 개념 이해
* MCP Server 구축
* MCP Client 연동
* Tool 표준화
* Agent + MCP 연계
* Kubernetes 및 Database Agent 확장 기반 확보

---

## 학습 내용

### MCP란?

MCP(Model Context Protocol)는 LLM과 외부 시스템을 연결하기 위한 표준 프로토콜이다.

쉽게 말하면

```text id="mcp1"
USB-C
=
장치 연결 표준

MCP
=
LLM Tool 연결 표준
```

---

### MCP가 필요한 이유

기존 방식

```text id="oldmcp1"
Agent
 ↓
직접 API 개발
 ↓
DB 연결
 ↓
Kubernetes 연결
 ↓
파일 시스템 연결
```

시스템마다 별도 구현 필요

---

MCP 방식

```text id="newmcp1"
Agent
 ↓
MCP Client
 ↓
MCP Server
 ↓
Tool
```

표준 인터페이스 사용

---

### MCP 구성 요소

#### MCP Client

Agent 측

예시

* Claude Desktop
* Cursor
* OpenAI Agent
* Custom Agent

---

#### MCP Server

Tool 제공

예시

* PostgreSQL
* Kubernetes
* File System
* GitHub

---

#### Tool

실제 기능 수행

예시

* SQL 조회
* Pod 조회
* 파일 읽기

---

### MCP 아키텍처

```text id="mcparch1"
Agent
    ↓
MCP Client
    ↓
MCP Protocol
    ↓
MCP Server
    ↓
Tool
    ↓
DB / Kubernetes / File
```

---

### MCP 활용 사례

#### Database MCP

```text id="dbmcp1"
사용자
 ↓
DB 상태 알려줘
 ↓
Agent
 ↓
MCP
 ↓
PostgreSQL 조회
 ↓
결과 반환
```

---

#### Kubernetes MCP

```text id="k8smcp1"
사용자
 ↓
Pod 상태 알려줘
 ↓
Agent
 ↓
MCP
 ↓
Kubernetes API
 ↓
결과 반환
```

---

## 실습 절차

### 1. Python 환경 구성

가상환경 생성

```bash id="mcppy1"
python -m venv venv
```

활성화

```bash id="mcppy2"
source venv/bin/activate
```

---

### 2. MCP SDK 설치

```bash id="mcppkg1"
pip install mcp
```

버전 확인

```bash id="mcppkg2"
pip show mcp
```

---

### 3. 첫 번째 MCP Server 생성

예제

```python id="mcpserver1"
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("study")

@mcp.tool()
def hello():
    return "Hello MCP"

mcp.run()
```

---

### 4. MCP Server 실행

```bash id="mcpserver2"
python server.py
```

확인

* 정상 기동 여부
* Tool 등록 여부

---

### 5. MCP Client 연결

Cursor 또는 Claude Desktop 설정

예제

```json id="mcpjson1"
{
  "mcpServers": {
    "study": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

---

### 6. Tool 호출 테스트

예제

```text id="mcptest1"
hello 실행해줘
```

예상 결과

```text id="mcptest2"
Hello MCP
```

---

### 7. File System Tool 추가

예제

```python id="filetool1"
@mcp.tool()
def read_file(path:str):
    ...
```

실습 목표

* 파일 읽기
* 파일 목록 조회

---

### 8. PostgreSQL Tool 추가

예제

```python id="dbtool1"
@mcp.tool()
def execute_sql(query:str):
    ...
```

실습 목표

* SQL 조회
* 결과 반환

---

### 9. Agent 연동

구성

```text id="agentmcp1"
Agent
 ↓
MCP
 ↓
Tool
 ↓
결과 반환
```

---

## TODO

### 환경 구축

* [ ] MCP SDK 설치
* [ ] MCP Server 구축

### 실습

* [ ] Hello Tool
* [ ] File Tool
* [ ] PostgreSQL Tool
* [ ] Agent 연동

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### MCP Server 검증

정상 기동 여부 확인

```bash id="mcpcheck1"
python server.py
```

---

### Tool 검증

등록된 Tool 호출

예시

```text id="toolcheck41"
hello
```

---

### Agent 연동 검증

Agent가 Tool을 호출 가능한지 확인

---

### 재현 검증

다른 PC에서 동일 절차 수행 후 정상 동작 확인

---

## 결과물

### 코드

* MCP Server
* Tool 구현 코드
* PostgreSQL Tool

### 문서

* 구축 가이드
* 설정 가이드
* 트러블슈팅 문서

### 다이어그램

* MCP Architecture
* Agent + MCP Architecture

---

## 회고

### 배운 점

* MCP 구조 이해
* Tool 표준화 이해
* Agent 연동 구조 이해

### 개선점

* Tool 확장 필요
* 인증 기능 추가 필요
* 에러 처리 강화 필요

### 다음 단계

* Kubernetes MCP
* Database MCP
* Multi-Agent

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* MCP 설정 파일
* Tool 예제
* PostgreSQL 예제

### 스크린샷

* MCP 실행 화면
* Tool 호출 결과
* Agent 연동 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 MCP가 필요한가?

Agent가 외부 시스템과 연동하기 위한 표준 방식이 필요하기 때문이다.

---

### 구현 방법

* MCP SDK 설치
* MCP Server 생성
* Tool 등록
* Agent 연동

---

### 트러블슈팅

예상 사례

* MCP 연결 실패
* Tool 등록 실패
* JSON 설정 오류
* Python 환경 문제

---

### 결과

* MCP Server 구축 완료
* Agent 연동 완료
* Tool 표준화 완료

---

## 면접 포인트

### MCP란 무엇인가?

LLM과 외부 시스템을 연결하기 위한 표준 프로토콜이다.

---

### MCP가 왜 필요한가?

기존에는 시스템마다 개별 API를 개발해야 했지만 MCP는 표준 인터페이스를 제공한다.

---

### MCP 구성 요소는?

* MCP Client
* MCP Server
* Tool

---

### MCP와 REST API 차이는?

| 항목    | REST API | MCP        |
| ----- | -------- | ---------- |
| 목적    | 시스템 연동   | AI 연동      |
| 호출 주체 | 애플리케이션   | Agent      |
| 표준화   | 일반 API   | AI Tool 표준 |
| 사용 대상 | 개발자      | Agent      |

---

### 대안은 무엇인가?

* 직접 API 개발
* LangChain Tool
* OpenAI Function Calling

---

### 운영 시 고려사항

* 인증 및 권한 관리
* Tool 접근 제어
* 로깅 및 감사
* 장애 처리
* 버전 관리

---

### AI Platform Engineer 관점 핵심 포인트

MCP는 AI 플랫폼의 API Gateway 역할과 유사하다.

기존 경험과 비교

```text id="comparemcp1"
Spring Boot
    ↓
REST API
    ↓
Frontend

Agent
    ↓
MCP
    ↓
Tool
```

---

### 실무 적용 포인트

현재 경험과 직접 연결 가능

* PostgreSQL 조회 MCP
* Kubernetes 운영 MCP
* Kafka 조회 MCP
* OpenTelemetry 조회 MCP

즉, 기존 운영 업무를 AI Agent가 수행하도록 연결하는 핵심 기술이다.

---

### 최종 목표

```text id="mcpflow1"
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
PostgreSQL
    ↓
Kubernetes
    ↓
Observability
    ↓
AI Operations Platform
```
