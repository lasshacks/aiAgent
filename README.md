# AI Platform Engineering Lab

로컬 LLM, IDE Agent, MCP, 데이터베이스, Kubernetes와 관측 가능성을 단계별로 실습하는 AI Platform Engineering 저장소입니다.

## 학습 문서

| 단계 | 문서 |
|---|---|
| 00 | [로드맵](docs/00_Roadmap.md) |
| 01 | [로컬 LLM 구축](docs/01_Local_ChatGPT.md) |
| 02 | [IDE Agent](docs/02_IDE_Agent.md) |
| 03 | [Agent 기본](docs/03_Agent_Basic.md) |
| 04 | [MCP](docs/04_MCP.md) |
| 05 | [Kubernetes Agent](docs/05_Kubernetes_Agent.md) |
| 06 | [Database Agent](docs/06_Database_Agent.md) |
| 07 | [Observability](docs/07_Observability.md) |
| 08 | [Multi Agent](docs/08_Multi_Agent.md) |
| 09 | [AI Operations Platform](docs/09_AI_Operations_Platform.md) |

## Continue 실습

- [Continue 사용 가이드](docs/Continue_Usage_Guide.md)
- [로컬 LLM 벤치마크 보고서](docs/Continue_Local_LLM_Benchmark_Report.md)

## 실습 코드

- `addition_app.py`, `web/`: Codex가 구현한 덧셈 앱
- `continue_web_demo/`: Continue Agent 응답을 수동 반영하고 보정한 곱셈 앱
- `benchmarks/`: Ollama 모델 비교 스크립트
- `agent_basic/`: 직접 구현 및 LangChain Tool Calling Agent
- `mcp_basic/`: stdio MCP Server와 Client 기본 실습
