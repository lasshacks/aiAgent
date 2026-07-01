# Podman

Podman은 컨테이너를 실행하고 관리하는 OCI 호환 Container Runtime 도구다.

이 Lab에서는 Podman을 단순히 `podman run` 명령어 수준에서 끝내지 않고, AI Platform에서 모델 런타임과 운영 도구를 격리 실행하는 기반으로 다룬다.

## 문서 구성

- [practice.md](practice.md): 실습 기록
- [commands.md](commands.md): 명령어 모음
- [troubleshooting.md](troubleshooting.md): 오류와 해결
- [architecture.md](architecture.md): 내부 구조와 Platform 연결
- `images/`: 실행 결과 스크린샷

## Platform Mapping

- Layer: Tool Layer
- Domain: Infrastructure
- Agent: Infra Agent
- 현재 구현: 예정
- 향후 확장: Infra MCP Server
- 호출 주체: Planner Agent -> Infra Agent

