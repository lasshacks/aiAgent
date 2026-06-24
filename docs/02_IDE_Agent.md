# 02 IDE Agent

## 목표

VS Code에 로컬·원격 LLM을 연결하고 Chat, 코드 편집, Agent 도구 호출을 직접 검증한다. 단순 설치 여부가 아니라 실제 파일 생성, 실행 성공, 수정 횟수와 응답 시간을 비교한다.

## IDE Agent란?

IDE Agent는 코드 편집기 안에서 프로젝트 컨텍스트를 읽고 다음 작업을 수행하는 AI 도구다.

- 코드 생성과 수정
- 여러 파일 탐색과 변경
- 터미널 명령 실행
- 오류 분석과 테스트
- Git 및 외부 도구 연동

일반 Chat이 답변을 생성하는 데 집중한다면 Agent는 도구를 호출해 실제 프로젝트 상태를 변경한다.

## 실습 구성

```text
VS Code
├── Continue
│   ├── qwen3:4b  : Chat + Agent 후보
│   └── gemma3:4b : Chat 비교용
├── Cline         : 설치 완료, 비교 실습 예정
└── Codex         : 기준 구현 및 검증
        │
        ▼
Ollama API (172.30.236.141:11434)
```

## 도구 선택

| 도구 | 역할 | 현재 상태 |
|---|---|---|
| Continue | 여러 LLM을 연결하는 VS Code 확장 | Qwen3/Gemma3 연결 완료 |
| Cline | 파일·터미널 중심 IDE Agent | 설치 완료, Ollama 비교 예정 |
| Codex | 코드 구현·검증 기준 | 웹 앱 구현 및 Continue 결과 보정 완료 |
| Ollama | 로컬 모델 실행 API | 정상 동작 |

## 모델 역할

| 모델 | Ollama capabilities | 사용 범위 |
|---|---|---|
| `qwen3:4b` | completion, tools, thinking | Continue Chat 및 Agent |
| `gemma3:4b` | completion, vision | Continue Chat·코드 생성 비교 |

Gemma3 4B는 Ollama에서 tools를 지원하지 않으므로 `tool_use`를 강제로 선언하지 않는다. Agent 비교는 Qwen3를 기준으로 한다.

## 진행 결과

### 환경 구축

- [x] Continue 2.1.0 설치
- [x] Cline 3.89.2 설치
- [x] Ollama 0.30.10 연결
- [x] `qwen3:4b` 설치
- [x] `gemma3:4b` 설치
- [x] 스트리밍 응답 확인

### Continue 실습

- Qwen3 Chat 응답 확인
- Qwen3 Agent 모드가 소스와 명령을 대화로 제시하고 사용자가 복사·붙여넣기해 `continue_web_demo`의 파일 두 개를 생성·실행
- Agent가 파일 쓰기·터미널 도구를 직접 호출하지 않았고 응답도 느렸으며 수동 반영한 최초 구현은 실행 가능한 통합 상태가 아니었음
- 요구한 덧셈 대신 곱셈 앱을 생성해 요구사항 준수 문제가 확인됨
- Gemma3는 Chat 비교가 가능하지만 도구 호출은 지원하지 않음
- Cline에서 Gemma3 사용 시 tools 미지원 오류로 3회 자동 재시도 후 실패

### Codex 기준 구현

- `addition_app.py`와 `web/index.html`로 실행 가능한 덧셈 앱 구현
- 정적 화면, 덧셈 API, 오류 처리를 자동 검증
- Continue가 생성한 곱셈 앱의 서버·API·UI를 보정하고 포트 8001에서 검증

## 핵심 관찰

1. 로컬 4B 모델은 간단한 Chat과 코드 초안에는 사용할 수 있다.
2. Agent 작업은 모델의 `tools` capability가 반드시 필요하다.
3. 파일을 생성했다는 사실만으로 작업 성공을 판단할 수 없다.
4. 요구사항 준수, 실행 성공, 오류 처리까지 검증해야 한다.
5. 모델 메타데이터의 `tools` capability가 실제 구조화된 도구 호출 성공을 보장하지는 않는다.
6. 동시에 여러 Ollama 요청을 실행하면 대기열 때문에 벤치마크가 왜곡될 수 있다.
7. 로컬 모델은 크레딧 비용이 없지만 응답 시간과 수정 비용을 함께 고려해야 한다.

## 검증 기준

| 영역 | 확인 항목 |
|---|---|
| 연결 | 모델 목록과 응답 수신 여부 |
| Chat | 프롬프트 준수와 코드 문법 |
| Agent | 실제 파일 생성·수정 여부 |
| 통합 | 프론트엔드와 백엔드 연결 여부 |
| 실행 | HTTP 상태와 계산 결과 |
| 품질 | 오류 처리, 경로 분리, 하드코딩 여부 |
| 성능 | 첫 응답, 전체 시간, tokens/s |

## 다음 단계

- [x] Continue 요청을 모두 중단한 상태에서 Qwen3 단독 벤치마크 재실행
- [x] Continue Agent + Qwen3의 자동 파일 생성 검증(도구 미호출, 사용자 수동 반영)
- [ ] Gemma3 Chat에 동일한 코드 생성 프롬프트 적용
- [x] Cline + Qwen3로 동일 과제 수행(첫 응답 timeout)
- [x] Continue, Cline, Codex의 성공률·시간·수정 횟수 비교
- [ ] 실행 화면과 Agent 승인 과정 스크린샷 저장

## 기준 문서

- [Continue 사용 가이드](Continue_Usage_Guide.md)
- [Continue 로컬 LLM 벤치마크 보고서](Continue_Local_LLM_Benchmark_Report.md)
- [로컬 LLM 구축](01_Local_ChatGPT.md)
- [Agent 기본](03_Agent_Basic.md)
