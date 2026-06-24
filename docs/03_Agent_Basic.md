# 03_Agent_Basic

## 목표

LLM 기반 Agent의 기본 개념을 이해하고, Tool Calling, Memory, Prompt Engineering을 활용하여 실제 Agent를 구현할 수 있는 역량을 확보한다.

최종 목표

* Agent와 Chatbot의 차이 이해
* Tool Calling 구현
* Memory 구현
* Agent Workflow 이해
* 프레임워크 없는 Agent loop 구현
* 이후 LangChain 기반 구현과 비교
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

### 1. 환경 확인

- Python 3.11.5
- Ollama 0.30.10
- `qwen3:4b`, `gemma3:4b`
- 외부 Python 패키지 없음

LangChain을 먼저 사용하지 않고 HTTP 요청, messages, tools, tool result의 실제 구조를 표준 라이브러리로 확인한다.

### 2. Ollama Chat 호출

```bash
python agent_basic/chat_demo.py --model gemma3:4b
```

2026-06-24 측정 결과:

```text
응답: 네, 무엇을 도와드릴까요?
시간: 42.37초
출력: 9토큰
```

### 3. Tool Calling Agent loop

`agent_basic/basic_agent.py`는 다음 순서로 동작한다.

```text
사용자 요청
  → Ollama에 tools 스키마 전달
  → 모델의 native tool_calls 검사
  → 실패하면 JSON Schema Action fallback
  → 허용된 Python 함수 실행
  → tool 결과를 messages에 추가
  → 모델에 최종 응답 요청
```

등록 도구:

- `add_numbers(a, b)`
- `get_current_time()`

실행:

```bash
python agent_basic/basic_agent.py "12와 30을 더한 결과를 알려줘."
```

2026-06-24 최초 Qwen3 결과:

- 약 85.9초 소요
- 도구를 사용해야 한다는 설명은 생성
- 구조화된 `tool_calls`는 반환하지 않음
- Python 도구 함수는 실행되지 않음

이는 Agent 실행기의 도구 등록과 모델의 도구 선택이 서로 다른 단계임을 보여준다. 모델 메타데이터의 tools 지원만으로 실제 호출 성공이 보장되지는 않는다.

프롬프트를 명확히 하고 모델에 노출하는 도구를 하나로 제한한 뒤 JSON Schema fallback을 추가했다.

```text
[Agent] Native tool call 실패. JSON Action fallback을 사용합니다.
[Tool] add_numbers -> {"result": 42}
[Agent] 계산 결과는 42입니다.
```

- 개선 후 전체 실행: 36.8초
- Native `tool_calls`: 여전히 실패
- JSON Action 생성 및 검증: 성공
- Python 도구 실행: 성공
- 최종 결과 반환: 성공

이후 native 호출 자체를 해결하기 위해 다음을 적용했다.

- system/user prompt에 `/no_think` 추가
- “설명 없이 즉시 함수 호출”을 영어로 명시
- 모델에 노출하는 도구를 하나로 제한
- 도구 설명과 JSON Schema를 짧은 영어로 통일
- native 출력 한도를 96에서 512토큰으로 증가
- 동일한 native 호출이 중복될 경우 한 번으로 정규화

최종 결과:

```text
[Tool] add_numbers -> {"result": 42}
[Agent] 계산 결과는 42입니다.
```

- 영어 요청 native 호출: 성공, 약 27.97초
- 한국어 요청 native 호출: 성공
- 동일 호출 중복 반환: 안전하게 한 번으로 정규화
- JSON Action fallback: native 실패 시에만 사용하는 안전망으로 유지

### 4. 도구 실행기 단위 검증

모델과 무관한 다음 항목은 통과했다.

- Python 파일 문법
- `add_numbers(12, 30) == 42`
- 도구 이름 허용 목록
- JSON 객체 인자 처리

### 5. Memory 실습

`agent_basic/memory_agent.py`는 최근 사용자·Agent 메시지를 `memory.json`에 저장하고 다음 요청의 컨텍스트로 전달한다.

```bash
python agent_basic/memory_agent.py "12와 30을 더해줘"
python agent_basic/memory_agent.py "그 결과에 8을 더해줘"
```

검증 결과:

```text
첫 요청: 12 + 30 = 42
후속 요청: 그 결과 + 8 = 50
```

- JSON 저장과 불러오기 성공
- 이전 결과 42 참조 성공
- 후속 도구 인자 `42`, `8` 생성 성공
- 최종 계산 결과 50 반환
- 첫 요청과 후속 요청 모두 native tool call 사용(`fallback=False`)
- 최근 10개 메시지만 유지

---

### 6. 다음 Agent 개선

- Qwen3 native tool call 추가 개선
- 짧은 컨텍스트와 출력 제한 비교
- 같은 loop를 LangChain으로 구현해 차이 비교

---

## TODO

### 환경 구축

* [x] Python 설치
* [x] LangChain 설치
* [x] Ollama 연동

### 실습

* [x] LLM 호출
* [x] Prompt 실습
* [x] Tool Calling 실행기 구현
* [x] Qwen3의 구조화된 tool call 성공
* [x] Memory 구현
* [x] 최소 Agent loop 구현

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### LLM 검증

Gemma3 Chat에서 정상 응답을 확인했다. `chat_demo.py`는 모델, 시간, 출력 토큰을 표시한다.

---

### Tool 검증

도구 함수와 디스패처 단위 테스트에 성공했다. Qwen3 native 호출도 `/no_think`, 단일 영어 도구 스키마, 512 출력 토큰을 적용한 뒤 성공했다. JSON Action fallback은 native 실패 시의 안전망으로 유지한다.

예시

```text id="toolcheck1"
현재 시간을 알려줘
```

---

### Memory 검증

첫 계산 결과 42를 저장한 뒤 “그 결과에 8을 더해줘”라는 후속 요청이 50을 반환하는 것을 확인했다. 저장 파일의 한글도 UTF-8 Unicode 코드 포인트로 검증했다.

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

* `agent_basic/ollama_client.py`: Ollama API 클라이언트
* `agent_basic/chat_demo.py`: LLM 호출 코드
* `agent_basic/basic_agent.py`: Native + JSON fallback Tool Calling Agent loop
* `agent_basic/memory_agent.py`: JSON 기반 대화 Memory

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

---

## 2026-06-24 구조 개선 및 LangChain 비교

실무 역할에 맞춰 코드를 다음과 같이 분리했다.

- `agent_core.py`: 모델 호출, tool call 검증, allowlist 실행, JSON fallback을 담당하는 공통 엔진
- `basic_agent.py`: 상태를 저장하지 않는 단발 실행·장애 분리용 CLI
- `memory_agent.py`: 공통 엔진에 JSON 단기 메모리를 결합한 대화형 CLI
- `langchain_agent.py`: LangChain `ChatOllama.bind_tools()` 비교 구현

핵심은 메모리가 없는 Agent가 무조건 불필요한 것이 아니라는 점이다. 독립 배치 요청과
Tool Calling 단위 검증에는 단발 실행기가 유용하고, 연속 대화에는 메모리 계층이 필요하다.

LangChain 비교 구현에서는 tool schema 변환과 메시지 객체 구성을 프레임워크가 담당한다.
반면 실제 도구의 권한 검사, 실행, 결과 검증 및 메모리 정책은 애플리케이션 코드가 여전히
책임져야 한다. 프레임워크 사용이 로컬 모델의 추론 속도 자체를 높여주지는 않는다.

검증 상태:

- 프로젝트 `.venv`에 `langchain-core 1.4.8`, `langchain-ollama 1.1.0` 설치
- 전체 Python import 및 문법 검사 통과
- Windows 환경의 LangChain 실제 Qwen 호출은 2분 이상 응답이 없어 중단
- WSL 재검증에서 native `bind_tools`는 실패했으나 structured output fallback으로 42 반환 성공

WSL 실행:

```bash
python3 -m venv .venv-wsl
source .venv-wsl/bin/activate
python3 -m pip install -r agent_basic/requirements.txt
export OLLAMA_BASE_URL=http://172.30.236.141:11434
python3 agent_basic/langchain_agent.py "12와 30을 더해줘"
```

### Memory 참조 오류 보강

여러 계산 이력이 있는 상태에서 Qwen3 4B가 `그 결과`를 최신 값이 아닌 과거 값으로
해석하여 `42 + 8` 대신 `8 + 8 = 16`을 반환한 사례가 발생했다. 대화 전문을 모델에
전달하는 것만으로는 상태의 정확성을 보장할 수 없다는 사례다.

`agent_core.resolve_result_reference()`가 assistant 메시지를 역순으로 탐색하여 가장 최근
계산 결과를 찾고, `그 결과`를 해당 숫자로 확정한 뒤 모델을 호출하도록 개선했다. 중요한
업무 상태는 LLM의 문맥 추론에만 맡기지 않고 구조화된 방식으로 결정해야 한다.

표현 변화 재검증 결과(2026-06-24):

```text
"30에 12를 보태줘"                   -> 42, native, fallback=False
"이 결과에다가 8을 추가해줘"         -> 50, 최신 결과 치환, fallback=False
"방금 나온 값에 10을 더하면 얼마야?" -> 60, JSON Action, fallback=True
```

세 요청은 모두 기능적으로 성공했으며 전체 실행시간은 약 153.6초였다. `방금 나온 값`은
현재 결정적 참조 치환 목록에는 없으므로 모델의 문맥 해석과 fallback에 의존한다.

### LangChain bind_tools 실패 보강

WSL에서 `langchain_agent.py`를 실행했을 때 연결은 성공했지만
`AIMessage.tool_calls`가 빈 배열로 반환됐다.

```text
LangChain Agent 실행 실패: 도구 호출 하나가 필요하지만 0개를 받았습니다: []
```

설치된 `langchain-ollama 1.1.0`의 `ChatOllama.bind_tools()` 구현을 확인한 결과,
Ollama가 강제 도구 선택을 지원하지 않아 `tool_choice` 인자가 현재 무시된다. 즉,
`bind_tools`는 도구 스키마를 전달하지만 모델이 반드시 도구를 호출하도록 보장하지 않는다.

이를 보완하기 위해 native tool call이 없으면 LangChain의
`with_structured_output(method="json_schema")`으로 Action을 강제한 뒤 기존 allowlist
실행기로 검증·실행하도록 개선했다.

WSL 최종 재검증 결과:

```text
[Agent] LangChain bind_tools 호출 실패. structured output fallback을 사용합니다.
[Tool] add_numbers -> {"result": 42}
[Agent] 계산 결과는 42입니다.
[Framework] LangChain structured_output_fallback
```

따라서 LangChain 연동, structured output 생성, Action 검증 및 실제 Python 도구 실행은
성공했다. native `bind_tools` 성공 여부와 Agent 작업 전체의 성공 여부는 분리해서 판단한다.

### 직접 구현과 LangChain 비교

| 항목 | 직접 구현 | LangChain 구현 |
|---|---|---|
| 주요 코드 | `ollama_client.py` 59줄 + `agent_core.py` 263줄 | `langchain_agent.py` 141줄 |
| 외부 의존성 | 없음(표준 라이브러리) | `langchain-core`, `langchain-ollama` |
| Tool schema 전달 | 직접 JSON 구성 | `@tool`, `bind_tools()`가 변환 |
| 동일 요청 native 결과 | 성공 사례 확인 | `tool_calls=[]` 실패 |
| fallback | 직접 JSON Schema Action | `with_structured_output(json_schema)` |
| 실행 제어·검증 | 모두 직접 구현 | allowlist와 실행 검증은 여전히 직접 구현 |
| 디버깅 투명성 | 높음 | 추상화 계층 때문에 상대적으로 낮음 |
| 확장성 | 작은 실습에 적합 | 다양한 모델·체인 연계에 유리 |

현재 Qwen3 4B + Ollama 조합에서는 직접 구현이 더 단순하고 native 성공 사례도 확인됐다.
LangChain은 코드량과 스키마 변환 부담을 줄이지만 Tool Calling 성공률이나 모델 속도를 자동으로
개선하지 않는다. 따라서 학습용 핵심 엔진은 직접 구현을 유지하고, 이후 복잡한 workflow와
통합이 필요할 때 LangChain/LangGraph를 선택하는 것이 적절하다.

동일 환경의 실행시간 비교:

```bash
python3 agent_basic/compare_agents.py "12와 30을 더해줘"
```

즉, 지금까지 수행한 운영 업무를 Agent로 자동화하기 위한 가장 중요한 기초 단계이다.
