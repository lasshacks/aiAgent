# 02_IDE_Agent

## 목표

AI 기반 개발 도구를 활용하여 개발 생산성을 향상시키고, Agent 기반 개발 방식(Agentic Development)을 이해한다.

최종 목표

* AI 코딩 Assistant 활용
* 코드 생성 자동화
* 코드 리뷰 자동화
* 문서 생성 자동화
* Agent 기반 개발 방식 이해
* AI 개발 워크플로우 구축

---

## 학습 내용

### IDE Agent란?

IDE 내부에서 동작하며 개발자의 작업을 지원하는 AI Agent를 의미한다.

주요 기능

* 코드 생성
* 코드 수정
* 리팩토링
* 테스트 코드 생성
* 문서 생성
* 코드 리뷰

---

### AI 코딩 도구 비교

| 도구             | 특징            |
| -------------- | ------------- |
| GitHub Copilot | 가장 대중적        |
| Cursor         | Agent 기능 강력   |
| Codex          | CLI 기반 개발 지원  |
| Cline          | VS Code Agent |
| Roo Code       | MCP 연동 가능     |

---

### Agentic Development

기존 개발 방식

```text id="olddev1"
개발자
 ↓
설계
 ↓
코딩
 ↓
테스트
```

AI 활용 개발 방식

```text id="newdev1"
개발자
 ↓
AI Agent
 ↓
코드 생성
 ↓
테스트 생성
 ↓
리뷰
 ↓
개선
```

---

### IDE Agent 아키텍처

```text id="archdev1"
개발자
   ↓
VS Code
   ↓
AI Agent
(Copilot/Cursor/Codex)
   ↓
LLM
(OpenAI/Ollama)
   ↓
코드 생성
```

---

## Track 2 진행 현황

### 2026-06-19 - Continue 설치

#### 1. Continue VS Code Extension 설치

설치 완료

```bash
code --install-extension Continue.continue
```

결과

```text
Extension 'continue.continue' v2.0.0 was successfully installed.
```

✅ 설치 완료

---

#### 2. Continue 설정 파일 생성

경로

```text
~/.continue/config.json
```

설정 내용

```json
{
  "models": [
    {
      "title": "Qwen3 Local",
      "provider": "ollama",
      "model": "qwen3:4b",
      "apiBase": "http://172.30.236.141:11434"
    },
    {
      "title": "Gemma Local",
      "provider": "ollama",
      "model": "gemma3:4b",
      "apiBase": "http://172.30.236.141:11434"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Qwen3 Tab Complete",
    "provider": "ollama",
    "model": "qwen3:4b",
    "apiBase": "http://172.30.236.141:11434"
  },
  "allowAnonymousTelemetry": false,
  "userEmail": "user@local",
  "temperature": 0.7
}
```

✅ 설정 완료

---

#### 3. Ollama 연동 확인

Ollama 상태

```bash
systemctl status ollama
```

결과

```text
● ollama.service - Ollama Service
   Active: active (running)
   Memory: 896.0M
```

✅ Ollama 정상 실행

---

#### 4. Ollama API 테스트

모델 목록 조회

```bash
curl http://172.30.236.141:11434/api/tags
```

결과

```json
{
  "models": [
    {
      "name": "qwen3:4b",
      "model": "qwen3:4b",
      "size": 2497293931,
      "details": {
        "parameter_size": "4.0B",
        "context_length": 262144
      }
    }
  ]
}
```

✅ API 정상 작동

---

## 실습 절차

### 1. Continue 사용법

VS Code에서 Continue 탭 열기

```text
Ctrl+Shift+X → Continue 확인
또는
Ctrl+L (Continue Chat 오픈)
```

주요 기능

* Chat: `Ctrl+L`
* Tab Autocomplete: 코드 입력 시 자동 제안
* Command Palette: `Cmd+Shift+P` → "Continue"

---

#### 5. LLM 응답 테스트

코드 생성 테스트

```bash
curl -s http://172.30.236.141:11434/api/generate \
-d '{
  "model": "qwen3:4b",
  "prompt": "Python으로 간단한 Hello World 프로그램을 만들어줘",
  "stream": false
}'
```

✅ LLM 응답 정상

---

### 5. Cline VS Code Extension 설치

설치 완료

```bash
code --install-extension saoudrizwan.claude-dev
```

결과

```text
Extension 'saoudrizwan.claude-dev' v3.89.2 was successfully installed.
```

✅ 설치 완료

---

### 6. Cline 아키텍처

```text
VS Code
  ↓
Cline Extension (MCP 기반)
  ↓
도구 및 리소스 자동 발견
  ↓
LLM 호출
  ↓
파일/Git 자동 조작
```

---

### 7. Cline vs Continue 비교

| 항목 | Continue | Cline |
|------|----------|-------|
| 설정 난이도 | ⭐ 쉬움 | ⭐⭐ 중간 |
| 코드 자동 완성 | ✅ 우수 | ⚠️ 제한적 |
| 프로젝트 분석 | ⭐ 기본 | ⭐⭐⭐ 강력 |
| 파일 자동 조작 | ❌ 없음 | ✅ 있음 |
| Git 통합 | ❌ 없음 | ✅ 있음 |
| MCP 지원 | ⚠️ 제한적 | ✅ 완벽 |
| 로컬 LLM | ✅ 우수 | ⚠️ 복잡 |

---

## 실습 절차

### 1. Continue 사용법

VS Code에서 Continue 탭 열기

```text
Ctrl+Shift+X → Continue 확인
또는
Ctrl+L (Continue Chat 오픈)
```

주요 기능

* Chat: `Ctrl+L`
* Tab Autocomplete: 코드 입력 시 자동 제안
* Command Palette: `Cmd+Shift+P` → "Continue"

---

### 2. Cline 설정 및 사용법

VS Code에서 Cline 패널 열기

```text
View → Command Palette → "Cline: Open"
또는
좌측 Sidebar 아이콘
```

Ollama 연동 설정

```text
Cline Settings → Models → Custom/Other
Endpoint: http://172.30.236.141:11434
Model: qwen3:4b
```

---

### 3. 코드 생성 실습 (Continue)

사용자 프롬프트

```text
"Spring Boot REST API로 간단한 CRUD 만들어줘"
```

결과

```
- Controller 생성
- Service 생성  
- Repository 생성
- DTO 생성
```

---

### 4. 프로젝트 분석 (Cline)

사용자 프롬프트

```text
"@all 이 프로젝트의 구조를 분석해서 README.md 만들어줘"
```

Cline 자동 수행

```
1. 파일 시스템 스캔
2. 프로젝트 구조 분석
3. README.md 생성
4. Git 커밋
```

---

## 다음 단계

Track 3: Agent Basic (LangChain/LangGraph 학습)

- [ ] Tool Calling 이해
- [ ] Agent Workflow 학습
- [ ] Multi-Agent Pattern 실습

---

### 5. Local LLM 연동

Ollama 실행

```bash id="ollama11"
ollama run qwen3:4b
```

목표

* 로컬 모델 기반 AI 개발 환경 구성

---

### 6. Spring Boot 프로젝트 분석

대상

* 현재 업무 프로젝트
* 개인 프로젝트

실습

```text id="analysis11"
프로젝트 구조 설명해줘
```

```text id="analysis12"
Controller 구조 분석해줘
```

```text id="analysis13"
개선 포인트 알려줘
```

---

### 7. 코드 생성 실습

예제

```text id="codegen11"
Spring Boot CRUD 생성
```

생성 항목

* Controller
* Service
* Repository
* DTO

---

### 8. 테스트 코드 생성

예제

```text id="testgen11"
JUnit 테스트 코드 생성
```

생성 항목

* Unit Test
* Integration Test

---

### 9. 코드 리뷰 실습

예제

```text id="review11"
이 코드 리뷰해줘
```

확인 항목

* 성능
* 보안
* 가독성
* 유지보수성

---

## TODO

### 환경 구축

* [ ] VS Code 설치
* [ ] GitHub Copilot 설치
* [ ] Cursor 설치
* [ ] Codex 설치

### 실습

* [ ] 코드 생성
* [ ] 테스트 코드 생성
* [ ] 코드 리뷰
* [ ] 문서 생성
* [ ] Local LLM 연동

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### 기능 검증

AI를 통해

* Controller 생성
* Service 생성
* SQL 생성

가능 여부 확인

---

### 품질 검증

직접 작성 코드와 비교

비교 항목

* 가독성
* 생산성
* 유지보수성

---

### 생산성 검증

측정 항목

* 코드 작성 시간
* 테스트 작성 시간
* 문서 작성 시간

---

### 재현 검증

동일 프롬프트 입력 시

* 동일 결과 생성 여부
* 품질 유지 여부

확인

---

## 결과물

### 코드

* AI 생성 코드
* 테스트 코드
* 리팩토링 코드

### 문서

* 코드 리뷰 결과
* 개발 가이드
* 프롬프트 모음

### 다이어그램

* IDE Agent Architecture
* Agentic Development Flow

---

## 회고

### 배운 점

* AI 기반 개발 방식 이해
* Agent 활용 방법 이해
* 코드 생성 자동화 경험

### 개선점

* 프롬프트 품질 향상 필요
* 검증 프로세스 정립 필요
* 코드 리뷰 기준 정립 필요

### 다음 단계

* MCP 연동
* Tool Calling
* Agent 개발

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 사용 방법

### 권장

* Prompt 예제
* 코드 생성 결과
* 테스트 결과

### 스크린샷

* VS Code
* Copilot
* Cursor
* Codex
* 코드 생성 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 IDE Agent를 사용하려고 했는가?

* 생산성 향상
* 반복 작업 감소
* 코드 품질 향상

---

### 구현 방법

* VS Code 설치
* Copilot 설치
* Cursor 설치
* Local LLM 연동

---

### 트러블슈팅

예상 사례

* Extension 충돌
* 모델 연결 실패
* 응답 속도 문제
* 컨텍스트 부족

---

### 결과

* 코드 생성 자동화
* 테스트 자동화
* 문서 생성 자동화

---

## 면접 포인트

### IDE Agent란 무엇인가?

개발자의 작업을 지원하는 AI 기반 개발 Assistant이다.

주요 역할

* 코드 생성
* 코드 리뷰
* 테스트 생성
* 문서 생성

---

### 왜 Cursor를 사용하는가?

장점

* Agent 기능 강력
* 프로젝트 전체 분석 가능
* 코드 수정 능력 우수
* AI Native IDE

---

### 왜 Codex를 사용하는가?

장점

* CLI 환경 지원
* 코드 생성 자동화
* 문서 생성 자동화
* 반복 작업 자동화

---

### GitHub Copilot과 Cursor 차이는?

| 항목       | Copilot | Cursor |
| -------- | ------- | ------ |
| 코드 자동완성  | 강점      | 지원     |
| Agent 기능 | 제한적     | 강력     |
| 프로젝트 분석  | 제한적     | 가능     |
| 코드 수정    | 일부      | 우수     |

---

### 대안은 무엇인가?

* Cline
* Roo Code
* Continue
* JetBrains AI Assistant

---

### 운영 시 고려사항

* 소스코드 보안
* 개인정보 포함 여부
* 비용 관리
* 프롬프트 관리
* 생성 코드 검증

---

### AI Platform Engineer 관점 핵심 포인트

IDE Agent는 단순한 코딩 도구가 아니라 향후 구축할 Agent 시스템의 가장 쉬운 입문 사례이다.

학습 흐름

```text id="agentflow1"
IDE Agent
    ↓
Tool Calling
    ↓
MCP
    ↓
Kubernetes Agent
    ↓
Multi-Agent
    ↓
AI Operations Platform
```

---

### 실무 적용 포인트

현재 보유 기술 스택에 적용 가능

* Spring Boot 코드 생성
* PostgreSQL SQL 생성
* Kafka 연계 코드 생성
* Kubernetes YAML 생성
* OpenTelemetry 설정 생성

즉, 기존 백엔드 개발자를 AI 기반 플랫폼 엔지니어로 전환하는 첫 단계라고 볼 수 있다.
