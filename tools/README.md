# Tool Layer

`tools/`는 Agent가 실제 작업을 수행하기 위해 호출할 수 있는 실행 기능을 담는 영역이다.

Tool은 아직 Agent가 아니다. Tool은 결정적인 기능이고, Agent는 상황을 판단해서 어떤 Tool을 호출할지 결정하는 주체다.

## Structure

```text
tools/
├── filesystem/
├── git/
├── postgres/
├── ansible/
├── podman/
├── kubernetes/
└── ssh/
```

## 확장 순서

```text
Python Function
  -> CLI Tool
  -> MCP Server
  -> Agent Tool
  -> LangGraph Workflow
```

## Platform Mapping

- Layer: Tool Layer
- Domain: Infrastructure / Developer Productivity / Data
- Agent: Infra Agent, DB Agent, Developer Agent
- 현재 구현: 개별 CLI/Python Tool 예정
- 향후 확장: MCP Server로 표준화
- 호출 주체: Planner Agent -> Domain Agent

