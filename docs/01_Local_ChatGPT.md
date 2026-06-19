# 01_Local_ChatGPT

## 목표

로컬 환경에서 LLM(Large Language Model)을 직접 실행하여 AI 서비스의 기본 구조를 이해하고, 향후 Agent 및 AI Platform 구축을 위한 기반 환경을 확보한다.

최종 목표

* Local LLM 실행 환경 구축
* 모델 다운로드 및 관리 방법 습득
* LLM API 호출 구조 이해
* Chat UI 연동
* 향후 Agent 개발 기반 확보

---

## 학습 내용

### Local LLM이란?

클라우드(OpenAI, Anthropic 등)를 사용하지 않고 사용자의 PC 또는 서버에서 직접 LLM을 실행하는 방식이다.

장점

* 인터넷 없이 사용 가능
* 개인정보 외부 전송 없음
* 비용 절감
* 모델 교체 자유

단점

* GPU 자원 필요
* 성능 한계 존재
* 모델 관리 필요

---

### Ollama 이해

Ollama는 오픈소스 LLM을 로컬 환경에서 쉽게 실행할 수 있도록 지원하는 런타임이다.

주요 기능

* 모델 다운로드
* 모델 실행
* API 제공
* 모델 버전 관리

---

### 주요 오픈소스 모델

| 모델       | 특징          |
| -------- | ----------- |
| Qwen3    | 범용 성능 우수    |
| Gemma    | Google 오픈모델 |
| DeepSeek | 코딩 성능 우수    |
| Llama    | Meta 오픈모델   |
| Mistral  | 경량 모델       |

---

### Local ChatGPT 아키텍처

```text
사용자
    ↓
Chat UI
(Open WebUI)
    ↓
Ollama API
    ↓
LLM
(Qwen3/Gemma/DeepSeek)
    ↓
응답 반환
```

---

## 실습 절차

### 1. WSL2 환경 확인

```bash
wsl --status
```

확인 항목

* Ubuntu 설치 여부
* WSL2 활성화 여부

---

### 2. Ollama 설치

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

버전 확인

```bash
ollama --version
```

예상 결과

```text
ollama version 0.30.x
```

---

### 3. 모델 다운로드

Qwen3 4B

```bash
ollama pull qwen3:4b
```

Gemma

```bash
ollama pull gemma3:4b
```

DeepSeek

```bash
ollama pull deepseek-r1:8b
```

---

### 4. 모델 실행

```bash
ollama run qwen3:4b
```

예상 결과

```text
>>> Send a message
```

현재 상태

* 실습 완료
* 정상 실행 확인

---

### 5. 모델 목록 확인

```bash
ollama list
```

예상 결과

```text
NAME
qwen3:4b
gemma3:4b
```

---

### 6. API 호출 테스트

별도 터미널

```bash
curl http://localhost:11434/api/generate \
-d '{
  "model":"qwen3:4b",
  "prompt":"hello"
}'
```

확인 사항

* REST API 제공 여부
* Agent 연동 가능 여부

---

### 7. Open WebUI 연동

Docker 실행

```bash
docker run -d \
-p 3000:8080 \
--add-host=host.docker.internal:host-gateway \
-v open-webui:/app/backend/data \
ghcr.io/open-webui/open-webui:main
```

접속

```text
http://localhost:3000
```

---

---

## 환경 정보

### Host

* Windows 11 Pro
* Intel i7-10750H
* RAM 16GB

### WSL

* Ubuntu (WSL2)

### Container

* Docker Engine (WSL 내부)

---

## 설치 결과

### Ollama

설치 완료

버전

```bash
ollama --version
```

결과

```text
0.30.10
```

---

### 모델 설치

설치 모델

```bash
ollama pull qwen3:4b
ollama pull gemma3:4b
ollama pull deepseek-r1:8b
```

확인

```bash
ollama list
```

결과

```text
NAME            
qwen3:4b
gemma3:4b
deepseek-r1:8b
```

---

### 모델 실행 테스트

```bash
ollama run qwen3:4b
```

정상 응답 확인 ✅

---

## Open WebUI 구축

### 컨테이너 생성

```bash
docker run -d \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

---

## 발생 문제

### 문제 1: Open WebUI 연결 실패

에러

```text
Ollama: Network Problem
```

#### 원인

Ollama가 127.0.0.1:11434로만 바인딩되어 있음

Docker Container에서 접근 불가

#### 확인

```bash
ss -tlnp | grep 11434
```

결과

```text
127.0.0.1:11434
```

---

### 문제 2: Open WebUI 모델 조회 실패

에러

```text
Model Fetch Failed
```

#### 원인

Open WebUI → Ollama 연결 불가

---

## 해결 방법

### systemd override 적용

파일

```bash
/etc/systemd/system/ollama.service.d/override.conf
```

내용

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

#### 적용

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

#### 확인

```bash
ss -tlnp | grep 11434
```

결과

```text
*:11434
```

---

## WSL IP 확인

```bash
hostname -I
```

결과

```text
172.30.236.141
```

⚠️ 재부팅 시 변경 가능

---

## Open WebUI 연결 설정

### 기존 (실패)

```
http://host.docker.internal:11434
```

### 변경 (성공)

```
http://172.30.236.141:11434
```

---

## Open WebUI 접속

### Windows localhost (실패)

```
http://localhost:3000
```

#### 원인

Docker Desktop 미사용

WSL 내부 Docker 사용

### 성공 주소

```
http://172.30.236.141:3000
```

---

## 최종 아키텍처

```text
Windows Browser
        ↓
172.30.236.141:3000
        ↓
Open WebUI
        ↓
172.30.236.141:11434
        ↓
Ollama
        ↓
qwen3:4b
```

---

## 최종 상태

### Ollama

정상 ✅

```bash
systemctl status ollama
```

상태

```text
active (running)
```

---

### Port

```bash
ss -tlnp | grep 11434
```

결과

```text
*:11434
```

---

### Open WebUI

정상 ✅

---

### 모델

qwen3:4b 인식 성공 ✅

---

## 완료 체크리스트

* [x] WSL2 설치
* [x] Docker 사용 가능
* [x] Ollama 설치
* [x] qwen3:4b 설치
* [x] CLI 테스트
* [x] Open WebUI 설치
* [x] Ollama 연결
* [x] 모델 인식
* [x] Local ChatGPT 구축 완료

---

## TODO

### 실습

* [x] Ollama 설치
* [x] Qwen3 실행
* [x] Gemma 설치
* [x] DeepSeek 설치
* [x] Open WebUI 연동
* [x] API 호출 테스트

### 학습

* [ ] Ollama 구조 분석
* [ ] 모델 메모리 사용량 확인
* [ ] 모델 교체 실습

### 문서화

* [x] 설치 절차 기록
* [x] 트러블슈팅 기록
* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### 기능 검증

```bash
ollama run qwen3:4b
```

정상 응답 확인

---

### 프로세스 검증

```bash
ps -ef | grep ollama
```

또는

```bash
systemctl status ollama
```

---

### API 검증

```bash
curl http://localhost:11434/api/tags
```

정상 응답 확인

---

### 재현 검증

새 PC 또는 VM에서 동일 절차 수행 후 정상 실행 확인

---

## 결과물

### 코드

* Ollama 실행 스크립트
* API 테스트 스크립트

### 문서

* 설치 가이드
* 운영 가이드
* 트러블슈팅 문서

### 다이어그램

* Local ChatGPT Architecture
* Ollama Architecture

---

## 회고

### 배운 점

* LLM을 직접 실행하는 방법 이해
* Ollama 구조 이해
* 모델 다운로드 및 관리 방법 이해
* API 기반 서비스 구조 이해

### 개선점

* GPU 환경 구성 필요
* 모델 성능 비교 필요
* 응답 속도 측정 필요

### 다음 단계

* Open WebUI 구축
* IDE Agent 구축
* MCP 학습
* Agent 개발

---

## GitHub 업로드 기준

### 필수 포함

* README.md
* 설치 절차
* 실행 방법

### 권장 포함

* Ollama 버전 정보
* 모델 정보
* 테스트 결과

### 스크린샷

* Ollama 실행 화면
* 모델 목록
* API 호출 결과
* Open WebUI 화면

---

## 블로그 작성 포인트

### 문제 정의

왜 Local LLM 환경을 구축하려고 했는가?

* 비용 절감
* 개인정보 보호
* Agent 개발 환경 확보

---

### 구현 방법

* WSL2 설치
* Ollama 설치
* Qwen3 실행
* API 호출

---

### 트러블슈팅

예상 사례

* Ollama 설치 실패
* 모델 다운로드 실패
* 포트 충돌
* 메모리 부족

---

### 결과

* Local LLM 구축 완료
* API 호출 확인
* Agent 개발 기반 확보

---

## 면접 포인트

### 왜 Ollama를 사용했는가?

* 설치가 간단함
* 모델 관리가 쉬움
* REST API 제공
* 다양한 오픈모델 지원

---

### 왜 Qwen3를 선택했는가?

* 한국어 성능 우수
* 범용 성능 우수
* 비교적 적은 리소스 사용

---

### 대안은 무엇인가?

* vLLM
* LM Studio
* llama.cpp
* Text Generation WebUI

---

### Ollama와 vLLM 차이는?

| 구분    | Ollama | vLLM     |
| ----- | ------ | -------- |
| 목적    | 개인 개발  | 서비스 운영   |
| 설치    | 쉬움     | 상대적으로 복잡 |
| 성능    | 보통     | 높음       |
| 운영 환경 | 로컬     | 서버       |

---

### 운영 시 고려사항

* GPU 사용량
* 메모리 사용량
* 모델 버전 관리
* API 보안
* 모델 교체 전략

---

### AI Platform Engineer 관점 핵심 포인트

Local LLM은 최종 목표가 아니라 Agent, MCP, AI Platform 구축을 위한 기반 기술이다.

향후 구성 방향

```text
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
Kubernetes
    ↓
Observability
    ↓
AI Operations Platform
```
