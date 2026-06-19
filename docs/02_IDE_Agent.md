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

## 실습 절차

### 1. VS Code 설치

확인 사항

* 최신 버전 설치
* Extension 사용 가능 여부 확인

---

### 2. GitHub Copilot 설치

VS Code Extension

```text id="copilot1"
GitHub Copilot
```

로그인 후 활성화

---

### 3. Cursor 설치

공식 사이트 다운로드

주요 기능

* Agent Mode
* Chat
* Code Generation
* Code Review

---

### 4. Codex 설치

설치 확인

```bash id="codex11"
codex --version
```

예상 학습 내용

* 코드 생성
* 프로젝트 분석
* 문서 생성

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
