# llama.cpp

`llama.cpp`는 GGUF 모델을 로컬 CPU/GPU 환경에서 실행하기 위한 경량 모델 런타임이다.

이 챕터는 교육 내용을 그대로 따라 하는 것이 아니라, AI Platform의 Model Runtime 관점에서 `llama.cpp`가 어떤 역할을 하는지 이해하고 구현하는 것을 목표로 한다.

## 문서 구성

- [practice.md](practice.md): 실습 기록
- [commands.md](commands.md): 명령어 모음
- [troubleshooting.md](troubleshooting.md): 오류와 해결
- [architecture.md](architecture.md): 내부 구조와 Platform 연결
- `images/`: 실행 결과 스크린샷

## Platform Mapping

- Layer: Platform Layer
- Domain: Model Runtime
- Agent: 모든 Agent의 로컬 모델 실행 기반
- 현재 구현: 예정
- 향후 확장: OpenAI-compatible API server, Model Router
- 호출 주체: IDE Agent, Developer Agent, Planner Agent

