# Podman Architecture

```text
User / Agent
  -> podman CLI
  -> libpod
  -> OCI Runtime
  -> Linux Kernel Features
  -> Container
```

## Platform Mapping

- Layer: Tool Layer
- Domain: Infrastructure
- 향후 확장: Infra MCP Server

