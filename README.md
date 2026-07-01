# AI Platform Engineering Lab

이 저장소는 단순한 교육 복습 저장소가 아니라, AI Platform Engineer 관점에서 로컬 모델 런타임, 도구, Agent, MCP, 운영 자동화 구조를 설계하고 구현하는 Lab입니다.

핵심 흐름은 다음과 같습니다.

```text
Education
  -> Lab Implementation
  -> AI Platform Architecture
  -> GitHub Documentation
  -> Portfolio
```

## Lab Architecture

```text
AI_Platform_Engineering_Lab/
├── platform/       # 모델 실행, 라우팅, 프롬프트, 설정
├── tools/          # filesystem, git, postgres, ansible, podman, k8s, ssh 등 실행 도구
├── agents/         # planner, developer, db, infra, observability agent
├── mcp/            # 향후 MCP server 구현 영역
├── docs/           # 학습/설계/회고 문서
├── experiments/    # 비교 실험, PoC, 임시 검증
├── agent_basic/    # 03장에서 만든 Agent loop 선행 실험
└── mcp_basic/      # 04장에서 만든 MCP server/client 선행 실험
```

## Current Direction

앞으로 교육에서 다루는 기술은 그대로 따라 적는 것이 아니라, AI Platform 안에서 어느 계층에 속하는지까지 연결합니다.

예를 들어:

- Podman: `tools/podman/`
- llama.cpp: `platform/model-runtime/llama.cpp/`
- GGUF: `platform/model-runtime/gguf/`
- OpenAI-compatible API: `platform/model-runtime/openai-api/`
- Ansible: `tools/ansible/`
- SSH: `tools/ssh/`
- DB Tool: `tools/postgres/`
- DB MCP: `mcp/db-mcp/`
- DB Agent: `agents/db-agent/`

## Documentation Rule

각 주제는 가능하면 아래 형식으로 정리합니다.

1. 교육 내용 요약
2. 개념 설명: 기초에서 심화까지
3. 내부 동작 원리
4. AI Platform에서의 역할
5. LangGraph / Agent / Tool / MCP 중 어디에 해당하는지
6. 현업 아키텍처
7. 실습: 명령어와 코드
8. 결과 검증
9. 발생 가능한 오류 및 해결
10. GitHub 문서화
11. 면접 포인트
12. 다음 단계와 확장 방향
13. Platform Mapping

공통 템플릿은 [docs/Lab_Chapter_Template.md](docs/Lab_Chapter_Template.md)를 사용합니다.

## Learning Documents

| Step | Document |
|---|---|
| 00 | [Roadmap](docs/00_Roadmap.md) |
| 01 | [Local ChatGPT](docs/01_Local_ChatGPT.md) |
| 02 | [IDE Agent](docs/02_IDE_Agent.md) |
| 03 | [Agent Basic](docs/03_Agent_Basic.md) |
| 04 | [MCP](docs/04_MCP.md) |
| 05 | [Kubernetes Agent](docs/05_Kubernetes_Agent.md) |
| 06 | [Database Agent](docs/06_Database_Agent.md) |
| 07 | [Observability](docs/07_Observability.md) |
| 08 | [Multi Agent](docs/08_Multi_Agent.md) |
| 09 | [AI Operations Platform](docs/09_AI_Operations_Platform.md) |

## Existing Practice Code

- `agent_basic/`: 직접 구현한 Agent loop, memory, LangChain 비교 실험
- `mcp_basic/`: stdio MCP server/client 기본 실습
- `benchmarks/`: Ollama 모델 비교 실험
- `continue_web_demo/`: Continue/Cline IDE Agent 실습 결과물
- `addition_app.py`, `web/`: 간단 웹 앱 구현 검증

