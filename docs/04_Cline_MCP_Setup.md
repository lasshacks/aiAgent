# 04 Cline MCP 등록 가이드

이 문서는 `mcp_basic/server.py`를 Cline의 MCP Server로 등록해서 IDE 안에서 Tool처럼 호출하는 방법을 정리한다.

공식 Cline 문서 기준으로 IDE 확장에서는 MCP Servers 화면의 Configure 탭에서 MCP 설정 JSON을 열고, `mcpServers` 아래에 local STDIO server를 등록한다.

참고: https://docs.cline.bot/mcp/mcp-overview

## 1. 목표

지금까지는 우리가 직접 Python 명령어를 실행했다.

```bash
python3 mcp_basic/client.py --tool add_numbers --a 12 --b 30
```

Cline에 MCP Server를 등록하면 흐름이 이렇게 바뀐다.

```text
Cline
  -> MCP 설정 읽기
  -> mcp_basic/server.py 자동 실행
  -> tools/list
  -> tools/call
  -> 결과 반환
```

즉, `client.py`는 테스트용이고, 실제 IDE 연동에서는 Cline이 MCP Client/Host 역할을 한다.

## 2. 먼저 단독 실행 확인

WSL:

```bash
cd /mnt/d/AI_Platform_Engineering_Lab
source .venv-wsl/bin/activate
python3 mcp_basic/client.py --tool add_numbers --a 12 --b 30
```

Windows PowerShell:

```powershell
cd D:\AI_Platform_Engineering_Lab
.\.venv\Scripts\python.exe mcp_basic\client.py --tool add_numbers --a 12 --b 30
```

기대 결과:

```text
[MCP] server=ai-platform-study
[MCP] tools=['hello', 'add_numbers']
[Tool] add_numbers -> {"result": 42.0}
```

## 3. Cline MCP 설정 열기

1. VS Code에서 Cline 패널을 연다.
2. 상단의 MCP Servers 아이콘을 클릭한다.
3. Configure 탭으로 이동한다.
4. Configure MCP Servers 버튼을 클릭한다.
5. 열린 JSON 파일의 `mcpServers` 아래에 설정을 추가한다.

## 4. Windows VS Code인 경우

VS Code와 Cline 확장이 Windows 쪽에서 실행 중이면 이 설정을 사용한다.

예시 파일:

- `mcp_basic/cline_mcp_config.windows.json`

```json
{
  "mcpServers": {
    "ai-platform-study": {
      "command": "D:\\AI_Platform_Engineering_Lab\\.venv\\Scripts\\python.exe",
      "args": [
        "D:\\AI_Platform_Engineering_Lab\\mcp_basic\\server.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 5. WSL Remote인 경우

VS Code가 WSL Remote로 열려 있고 Cline 확장도 WSL 안에서 실행된다면 이 설정을 사용한다.

예시 파일:

- `mcp_basic/cline_mcp_config.wsl.json`

```json
{
  "mcpServers": {
    "ai-platform-study": {
      "command": "python3",
      "args": [
        "/mnt/d/AI_Platform_Engineering_Lab/mcp_basic/server.py"
      ],
      "env": {
        "PYTHONPATH": "/mnt/d/AI_Platform_Engineering_Lab"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 6. 등록 후 확인

Cline MCP 화면에서 다음 Tool이 보여야 한다.

```text
hello
add_numbers
```

테스트 프롬프트:

```text
MCP tool add_numbers를 사용해서 12와 30을 더해줘.
```

기대 동작:

```text
Cline이 ai-platform-study MCP Server의 add_numbers Tool 호출을 제안
사용자가 승인
결과 42 반환
```

## 7. 문제 해결

### Tool이 보이지 않는 경우

- Cline이 Windows에서 실행 중인지 WSL Remote에서 실행 중인지 먼저 확인한다.
- Windows Cline이면 Windows 경로를 사용한다.
- WSL Remote Cline이면 `/mnt/d/...` 경로를 사용한다.
- 해당 Python 환경에 `mcp` 패키지가 설치되어 있어야 한다.

### `ModuleNotFoundError: No module named 'mcp'`

Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install -r mcp_basic\requirements.txt
```

WSL:

```bash
source .venv-wsl/bin/activate
python3 -m pip install -r mcp_basic/requirements.txt
```

### 서버가 계속 켜져 있어야 하나?

아니다.

STDIO MCP Server는 일반 웹 서버처럼 미리 켜두는 방식이 아니다. Cline이 필요할 때 설정된 command와 args로 서버 프로세스를 실행하고, 표준 입출력으로 JSON-RPC 메시지를 주고받는다.

## 8. Platform Mapping

- Layer: MCP Layer
- Domain: Tool Interface Standardization
- Agent: Cline / 향후 Planner Agent / Infra Agent / DB Agent
- 현재 구현: Cline MCP Host가 `mcp_basic/server.py`를 local STDIO server로 실행
- 향후 확장: `mcp/infra-mcp`, `mcp/db-mcp`, `mcp/developer-mcp`
- 호출 주체: Cline -> MCP Server -> Tool

