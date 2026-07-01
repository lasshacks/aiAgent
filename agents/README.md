# Agent Layer

`agents/`는 LLM이 목표를 해석하고 Tool/MCP를 선택해 작업을 수행하는 실행 주체를 담는 영역이다.

현재 `agent_basic/`에서 Agent loop, tool calling, memory, LangChain 비교 실험을 먼저 수행했다. 앞으로는 이 경험을 바탕으로 도메인별 Agent를 분리한다.

## Structure

```text
agents/
├── planner-agent/
├── developer-agent/
├── db-agent/
├── infra-agent/
└── observability-agent/
```

## Role

- Planner Agent: 작업을 분해하고 적절한 Domain Agent를 선택
- Developer Agent: 코드/파일/Git 작업 지원
- DB Agent: PostgreSQL 상태 조회, 쿼리 분석, 장애 진단
- Infra Agent: Podman, Ansible, SSH, Kubernetes 작업 지원
- Observability Agent: 로그, 메트릭, 트레이스 분석

## Platform Mapping

- Layer: Agent Layer
- Domain: AI Operations
- 현재 구현: `agent_basic/` 선행 실험
- 향후 확장: Domain Agent + LangGraph orchestration
- 호출 주체: 사용자, IDE, Planner Agent

