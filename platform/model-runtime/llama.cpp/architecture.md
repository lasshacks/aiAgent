# llama.cpp Architecture

```text
GGUF Model
  -> llama.cpp Runtime
  -> Local Inference
  -> API / CLI
  -> Agent or Application
```

## Platform Mapping

- Layer: Platform Layer
- Domain: Model Runtime
- 향후 확장: OpenAI-compatible API, Model Router

