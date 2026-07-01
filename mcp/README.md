# MCP Layer

`mcp/`는 Tool을 MCP(Model Context Protocol) 서버로 표준화해서 Agent가 일관된 방식으로 호출할 수 있게 만드는 영역이다.

현재 `mcp_basic/`에서 stdio 기반 MCP server/client 선행 실험을 완료했다. 앞으로는 도메인별 MCP Server로 확장한다.

## Structure

```text
mcp/
├── infra-mcp/
├── db-mcp/
├── developer-mcp/
└── common-mcp/
```

## Role

- infra-mcp: Podman, Ansible, SSH, Kubernetes 관련 Tool 노출
- db-mcp: PostgreSQL 조회/진단 Tool 노출
- developer-mcp: filesystem, git, test runner Tool 노출
- common-mcp: 공통 유틸리티 Tool 노출

## Platform Mapping

- Layer: MCP Layer
- Domain: Tool Interface Standardization
- Agent: 모든 Domain Agent
- 현재 구현: `mcp_basic/` stdio MCP server/client
- 향후 확장: 도메인별 MCP Server
- 호출 주체: Planner Agent -> Domain Agent -> MCP Client -> MCP Server

