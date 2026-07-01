# Podman Practice

## 1. 교육 내용 요약

## 2. 개념 설명: 기초에서 심화까지

### Container Runtime

### OCI

### Rootless Container

### Namespace / Cgroup

### Storage Driver

### Pod

### Kubernetes와의 관계

## 3. 내부 동작 원리

```text
podman command
  -> libpod
  -> OCI runtime
  -> Linux namespace/cgroup/storage
  -> container process
```

## 4. AI Platform에서의 역할

## 5. 실습

## 6. 결과 검증

## 7. 오류 및 해결

## 8. GitHub 문서화

## 9. 면접 포인트

## 10. Platform Mapping

- Layer: Tool Layer
- Domain: Infrastructure
- Agent: Infra Agent
- 현재 구현:
- 향후 확장: Infra MCP Server
- 호출 주체: Planner Agent -> Infra Agent

