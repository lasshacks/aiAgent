# Platform Layer

`platform/`은 AI Platform의 기반 실행 환경을 담는 영역이다.

여기에는 모델 런타임, 모델 라우터, 프롬프트, 설정처럼 Agent가 사용하기 전에 먼저 준비되어야 하는 기반 요소가 들어간다.

## Structure

```text
platform/
├── model-runtime/
│   ├── llama.cpp/
│   ├── gguf/
│   └── openai-api/
├── model-router/
├── prompt/
└── config/
```

## Platform Mapping

- Layer: Platform Layer
- Domain: Model Serving / Runtime
- Agent: 모든 Agent의 기반 런타임
- 현재 구현: Ollama, llama.cpp, GGUF, OpenAI-compatible API 학습 예정
- 향후 확장: Model Router, Runtime Health Check, Provider Abstraction
- 호출 주체: Developer Agent, Planner Agent, IDE Agent

