# MCP Basic

Python MCP SDK의 stdio transport로 Server와 Client를 연결하는 최소 실습이다.

```text
client.py
  -> MCP initialize
  -> tools/list
  -> tools/call
  -> server.py
  -> hello / add_numbers
```

## WSL 설치

기존 `.venv-wsl`을 활성화한 뒤 설치한다.

```bash
source .venv-wsl/bin/activate
python3 -m pip install -r mcp_basic/requirements.txt
```

## 테스트

Server는 Client가 자식 프로세스로 자동 실행하므로 터미널을 따로 열 필요가 없다.

```bash
python3 mcp_basic/client.py --tool hello --name "iteyes"
python3 mcp_basic/client.py --tool add_numbers --a 12 --b 30
```

예상 출력:

```text
[MCP] server=ai-platform-study
[MCP] tools=['hello', 'add_numbers']
[Tool] add_numbers -> {"result": 42.0}
```
