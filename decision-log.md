# Decision Log

## 목적

AI Platform Engineering Lab 진행 중 발생한 기술 선택,
아키텍처 결정, 시행착오, 트러블슈팅을 기록한다.

목표는 단순 학습 기록이 아닌

- 기술 선택 근거 확보
- 아키텍처 의사결정 기록
- 트러블슈팅 자산화
- 면접 답변 자료 확보

이다.

---

# 기록 규칙

## 상태

- Proposed
- In Progress
- Accepted
- Rejected
- Deprecated

---

# Decision-001

## 날짜

2026-06-19

## 상태

Accepted

## 제목

Local LLM 런타임으로 Ollama 선택

## 배경

Local ChatGPT 환경 구축 필요

## 검토 대안

- Ollama
- LM Studio
- vLLM
- llama.cpp

## 결정

Ollama 선택

## 결정 이유

- 설치 간단
- Linux 환경 친화적
- API 제공
- MCP 연계 용이
- 학습 자료 많음

## Trade-off

장점

- 빠른 구축 가능

단점

- 대규모 서비스 운영에는 부적합

## 결과

WSL2 Ubuntu 환경에서 정상 구동

## 관련 문서

- docs/01_Local_ChatGPT.md

## 관련 명령어

```bash
# Ollama 설치
curl -fsSL https://ollama.com/install.sh | sh

# 모델 다운로드
ollama pull qwen3:4b
ollama pull gemma3:4b
ollama pull deepseek-r1:8b

# 모델 실행
ollama run qwen3:4b

# 모델 목록 확인
ollama list

# API 호출 테스트
curl http://localhost:11434/api/generate \
-d '{"model":"qwen3:4b","prompt":"hello"}'
```

---

# Decision-002

## 날짜

2026-06-19

## 상태

Accepted

## 제목

Ollama HOST 바인딩 문제 - systemd override 적용

## 배경

Open WebUI에서 Ollama 연결 실패

Ollama가 127.0.0.1:11434로만 바인딩되어 Docker Container에서 접근 불가

## 검토 대안

1. OLLAMA_HOST 환경변수 변경
2. systemd override 적용
3. Docker 네트워크 분석

## 결정

systemd override + WSL IP 기반 네트워크 연결

## 결정 이유

- WSL2 내부 Docker 구조의 특성 고려
- 재현 가능한 permanent 해결책
- 다른 모델, 도구 확장에도 적용 가능

## Trade-off

장점

- Open WebUI 연동 성공
- 모든 모델 인식 가능

단점

- WSL IP 변경 시 수동 업데이트 필요

## 결과

Open WebUI 정상 연동, Qwen3 모델 인식 성공

## 관련 문서

- docs/01_Local_ChatGPT.md

## 관련 명령어

```bash
# systemd override 적용
sudo systemctl daemon-reload
sudo systemctl restart ollama

# 포트 확인
ss -tlnp | grep 11434

# WSL IP 확인
hostname -I
```

---

# Decision-003

## 날짜

2026-06-19

## 상태

Accepted

## 제목

IDE Agent 도구로 Continue + Cline 선택

## 배경

AI 기반 개발 생산성 향상을 위해 IDE Agent 도구 필요

## 검토 대안

1. GitHub Copilot (API 기반, 클라우드만)
2. Continue (다중 LLM, 범용)
3. Cline (MCP 기반, 고급 자동화)
4. Cursor (전용 에디터, 비용 있음)

## 결정

Continue + Cline 병행 사용

## 결정 이유

**Continue**:
- Ollama와의 연동이 가장 간단
- 다양한 LLM 제공자 지원
- 커뮤니티 크고 자료 많음
- 코드 자동 완성 우수

**Cline**:
- MCP 기반 최신 기술
- 파일/Git 자동 조작 가능
- 고급 Agent 기능
- 프로젝트 분석 강력

## Trade-off

장점

- 두 도구의 장점 모두 활용
- 상황에 맞는 도구 선택 가능
- 확장성 높음

단점

- 설정 복잡도 증가
- 학습 곡선 가파름

## 결과

두 도구 모두 설치 완료, Ollama 연동 설정 진행 중

## 관련 문서

- docs/02_IDE_Agent.md
- docs/Continue_Usage_Guide.md
- docs/Continue_Local_LLM_Benchmark_Report.md

## 관련 명령어

```bash
# Continue 설치
code --install-extension Continue.continue

# Cline 설치
code --install-extension saoudrizwan.claude-dev

# Ollama API 테스트
curl http://172.30.236.141:11434/api/tags
```
