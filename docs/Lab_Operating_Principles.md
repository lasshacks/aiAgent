# Lab Operating Principles

이 Lab은 교육 내용을 그대로 복습하는 저장소가 아니라, AI Platform Engineering 관점에서 기술을 재해석하고 구현하는 설계 저장소다.

## 핵심 원칙

### 1. 교육은 출발점이고, Lab은 구조화된 구현이다

교육에서 `podman run`을 배웠다면 Lab에서는 다음까지 연결한다.

- Container Runtime
- OCI Image
- Rootless Container
- Namespace
- Cgroup
- Storage Driver
- Kubernetes와의 관계
- AI Platform에서 어떤 계층에 들어가는지

### 2. 모든 기술은 Platform Mapping을 남긴다

각 주제는 마지막에 반드시 `Platform Mapping`을 작성한다.

예시:

```markdown
## Platform Mapping

- Layer: Tool Layer
- Domain: Infrastructure
- Agent: Infra Agent
- 현재 구현: Python Tool
- 향후 확장: Infra MCP Server
- 호출 주체: Planner Agent -> Infra Agent
```

이 섹션이 누적되면 저장소 전체가 AI Platform 설계 문서가 된다.

### 3. Agent와 Tool을 구분한다

- Tool: 결정적인 실행 기능이다. 예: 파일 읽기, SQL 조회, Podman 실행, SSH 명령 실행
- MCP Server: Tool을 표준 프로토콜로 노출하는 서버다.
- Agent: LLM이 목표를 해석하고 Tool/MCP를 선택해 실행하는 주체다.
- LangGraph: 여러 Agent와 상태 전이를 엮는 Workflow/Orchestration 계층이다.

### 4. 먼저 Tool, 나중에 MCP, 마지막에 Agent로 확장한다

권장 구현 순서:

```text
Python Function
  -> CLI Tool
  -> MCP Server
  -> Agent Tool
  -> LangGraph Workflow
```

이 순서를 따르면 디버깅이 쉽고, 포트폴리오 설명도 명확해진다.

### 5. 실습 결과는 항상 검증 가능해야 한다

각 챕터는 다음을 남긴다.

- 실행 명령어
- 기대 결과
- 실제 결과
- 오류와 해결
- 다음 확장 방향

