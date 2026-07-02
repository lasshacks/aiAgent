# 04 MCP 직접 테스트 가이드

이 문서는 04_MCP 실습을 직접 복습하고 검증하기 위한 실행 가이드다.

04장의 완료 기준은 단순히 MCP Server와 Client를 만드는 것이 아니라, Agent가 MCP Tool을 호출하는 전체 흐름을 확인하는 것이다.

```text
User Prompt
  -> Local LLM Agent
  -> MCP Client
  -> MCP Server
  -> Tool 실행
  -> 결과 반환
```

## 1. 현재 구현 파일

```text
mcp_basic/
├── server.py        # MCP Server: hello, add_numbers Tool 제공
├── client.py        # LLM 없이 MCP Tool을 직접 호출하는 검증용 Client
├── agent_client.py  # LLM Agent가 MCP Tool을 선택해서 호출하는 통합 검증용 Client
└── requirements.txt
```

## 2. 환경 준비

WSL 기준:

```bash
cd /mnt/d/AI_Platform_Engineering_Lab
source .venv-wsl/bin/activate
python3 -m pip install -r mcp_basic/requirements.txt
python3 -m pip install -r agent_basic/requirements.txt
```

Windows PowerShell 기준:

```powershell
cd D:\AI_Platform_Engineering_Lab
.\.venv\Scripts\python.exe -m pip install -r mcp_basic\requirements.txt
.\.venv\Scripts\python.exe -m pip install -r agent_basic\requirements.txt
```

## 3. MCP 단독 테스트

이 단계는 LLM을 사용하지 않는다.

목적은 다음을 확인하는 것이다.

- MCP Server 실행
- initialize handshake
- tools/list
- tools/call
- structured result 반환

### hello Tool

```bash
python3 mcp_basic/client.py --tool hello --name iteyes
```

기대 결과:

```text
[MCP] server=ai-platform-study
[MCP] tools=['hello', 'add_numbers']
[Tool] hello -> {"result": "안녕하세요, iteyes!"}
```

### add_numbers Tool

```bash
python3 mcp_basic/client.py --tool add_numbers --a 12 --b 30
```

기대 결과:

```text
[MCP] server=ai-platform-study
[MCP] tools=['hello', 'add_numbers']
[Tool] add_numbers -> {"result": 42.0}
```

중간에 아래 로그가 보여도 정상이다.

```text
Processing request of type ListToolsRequest
Processing request of type CallToolRequest
```

이는 MCP Server가 요청을 처리했다는 로그이며 오류가 아니다.

## 4. Agent + MCP 통합 테스트

이 단계는 Qwen/Ollama를 사용한다.

```bash
python3 mcp_basic/agent_client.py "12와 30을 더해줘" --base-url http://172.30.236.141:11434
```

WSL에서 `localhost`가 정상 동작하면 아래도 가능하다.

```bash
python3 mcp_basic/agent_client.py "12와 30을 더해줘" --base-url http://localhost:11434
```

기대 결과:

```text
[MCP] server=ai-platform-study
[MCP] tools=['hello', 'add_numbers']
[MCP Tool] add_numbers -> {"result": 42.0}
[Agent] 계산 결과는 42.0입니다.
[Fallback] False
```

`[Fallback] False`는 모델이 native tool call을 정상 반환했다는 뜻이다.

`[Fallback] True`가 나와도 실패는 아니다. native tool call은 실패했지만 JSON Action fallback으로 Tool 실행에 성공했다는 뜻이다.

## 5. 테스트 의미

이번 테스트는 다음 구조가 실제로 동작함을 확인한다.

```text
Agent
  -> MCP Client
  -> MCP Server
  -> add_numbers Tool
```

각 구성 요소의 역할은 다음과 같다.

| 구성 요소 | 역할 |
|---|---|
| Agent | 사용자 요청을 해석하고 호출할 Tool을 선택 |
| MCP Client | Agent 쪽에서 MCP Server와 통신 |
| MCP Server | Tool 목록과 실행 기능을 표준 프로토콜로 제공 |
| Tool | 실제 작업 수행 |

## 6. 자주 발생하는 오류

### `ModuleNotFoundError: No module named 'mcp'`

현재 Python 환경에 MCP SDK가 설치되지 않은 것이다.

```bash
python3 -m pip install -r mcp_basic/requirements.txt
```

### Ollama 연결 실패

Ollama URL이 현재 실행 환경에서 접근 가능한지 확인한다.

```bash
curl http://172.30.236.141:11434/api/tags
curl http://localhost:11434/api/tags
```

VS Code/Windows 쪽에서는 `172.30.236.141`이 필요할 수 있고, WSL 내부에서는 `localhost`가 동작할 수 있다.

### Gemma 사용 시 Tool 오류

`gemma3:4b`는 현재 실습 기준에서 tool calling에 적합하지 않다.

Agent + MCP 테스트는 `qwen3:4b`로 진행한다.

## 7. Platform Mapping

- Layer: MCP Layer
- Domain: Tool Interface Standardization
- Agent: 향후 Planner Agent, Infra Agent, DB Agent
- 현재 구현: `mcp_basic`의 stdio MCP Server/Client와 Agent 통합 검증
- 향후 확장: `mcp/db-mcp`, `mcp/infra-mcp`, `mcp/developer-mcp`
- 호출 주체: User -> Agent -> MCP Client -> MCP Server -> Tool

## 8. 04장 완료 기준

- [x] MCP Server 생성
- [x] MCP Tool 등록
- [x] MCP Client에서 Tool discovery 확인
- [x] MCP Client에서 Tool call 확인
- [x] Agent가 MCP Tool을 호출하는 흐름 확인

따라서 04_MCP 기본 실습은 완료로 볼 수 있다.

