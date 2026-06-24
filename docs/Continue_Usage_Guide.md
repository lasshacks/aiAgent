# Continue 사용 가이드

## 1. 현재 구성

| 항목 | 값 |
|---|---|
| Continue | 2.1.0 |
| Ollama | `http://172.30.236.141:11434` |
| Agent 모델 | `qwen3:4b` |
| Chat 비교 모델 | `gemma3:4b` |
| 프로젝트 설정 | `.continue/config.json` |
| 사용자 설정 | `C:\Users\sedof\.continue\config.yaml` |

## 2. 연결 확인

브라우저에서 다음 주소를 열거나 터미널에서 API를 호출한다.

```text
http://172.30.236.141:11434
```

```bash
curl http://172.30.236.141:11434/api/tags
```

현재 모델 목록에는 다음 두 모델이 있어야 한다.

```text
qwen3:4b
gemma3:4b
```

## 3. 사용자 설정

```yaml
name: Local Config
version: 1.0.0
schema: v1
models:
  - name: qwen3-local
    provider: ollama
    model: qwen3:4b
    apiBase: http://172.30.236.141:11434
    stream: true
    capabilities:
      - tool_use
  - name: gemma3-local
    provider: ollama
    model: gemma3:4b
    apiBase: http://172.30.236.141:11434
    stream: true
```

`qwen3:4b`는 Ollama에서 tools를 지원하므로 Agent에 사용한다. `gemma3:4b`는 tools를 지원하지 않으므로 Chat 모드에서만 비교한다.

## 4. Chat 사용

1. VS Code의 Continue 패널을 연다.
2. 모델에서 `qwen3-local` 또는 `gemma3-local`을 선택한다.
3. Mode Selector에서 `Chat`을 선택한다.
4. 프롬프트를 입력한다.
5. 생성된 코드가 필요하면 Apply를 사용하거나 직접 파일에 반영한다.

간단한 확인 프롬프트:

```text
두 숫자를 더하는 Python 함수 add_numbers를 작성해줘.
타입 힌트와 한국어 docstring을 포함해줘.
```

## 5. Agent 사용

1. Continue 입력창 아래 Mode Selector의 `Chat`을 클릭한다.
2. `Agent`를 선택한다.
3. 모델이 `qwen3-local`인지 확인한다.
4. 파일을 실제 생성하라는 요구사항을 포함해 프롬프트를 전송한다.
5. 파일 변경이나 명령 실행 승인 창을 검토한 뒤 허용한다.
6. 완료 후 생성 파일과 실행 결과를 직접 확인한다.

멀티파일 확인 프롬프트:

```text
현재 프로젝트에 별도 폴더를 만들고 간단한 덧셈 웹 앱을 구현해줘.

요구사항:
- Python 표준 라이브러리만 사용
- backend.py에서 HTTP 서버와 덧셈 API 제공
- static/index.html에 숫자 두 개를 입력하는 화면 구현
- 계산 버튼을 누르면 API를 호출해 결과 표시
- WSL에서 python3 backend.py로 실행 가능
- 필요한 파일을 실제로 생성하고 실행 방법도 알려줘
```

## 6. 결과 검증

Agent가 완료했다고 답하더라도 다음 항목을 확인한다.

- 요청한 연산과 파일명이 맞는가?
- 입력값을 실제로 파싱하는가?
- 결과가 하드코딩되어 있지 않은가?
- 브라우저 GET 요청으로 정적 화면을 제공하는가?
- API 경로를 구분하는가?
- 잘못된 입력에 적절한 상태 코드를 반환하는가?
- 실행 명령이 실제로 성공하는가?

## 7. 실습 앱 실행

Codex 기준 덧셈 앱:

```bash
python3 addition_app.py
```

```text
http://localhost:8000
```

Continue 생성 후 보정한 곱셈 앱:

```bash
python3 continue_web_demo/backend.py
```

```text
http://localhost:8001
```

## 8. 벤치마크

Continue의 실행 중인 요청을 모두 중지한 다음 측정한다. 요청이 남아 있으면 Ollama 대기열 때문에 결과가 왜곡될 수 있다.

```bash
python3 benchmarks/ollama_model_benchmark.py
```

기록 항목:

- 첫 응답 시간
- 전체 완료 시간
- 출력 토큰과 tokens/s
- 문법 정상 여부
- 요구사항 충족 여부
- 도구 호출 여부
- 생성 파일 수와 수정 횟수

## 9. 문제 해결

### 모델이 보이지 않음

- `config.yaml`의 YAML 문법을 확인한다.
- 모델명이 `qwen3:4b`, `gemma3:4b`인지 확인한다.
- `Developer: Reload Window`를 실행한다.
- `/api/tags`에서 모델 설치 여부를 확인한다.

### Agent가 보이지 않거나 도구를 사용하지 못함

- Qwen3 설정에 `capabilities: [tool_use]`가 적용됐는지 확인한다.
- Gemma3 4B는 도구 호출 모델로 사용하지 않는다.
- Mode Selector에서 Chat이 아닌 Agent를 선택한다.

### 응답이 지나치게 느림

- Continue의 이전 요청을 Stop으로 종료한다.
- 동시에 여러 모델 요청을 실행하지 않는다.
- Ollama `/api/ps`에서 로드된 모델을 확인한다.
- 작은 프롬프트로 API 응답을 먼저 검사한다.

### 스키마 경로 오류

VS Code `settings.json`의 `yaml.schemas`에서 삭제된 Continue 버전 경로를 제거하고 현재 설치 버전만 남긴다.

## 10. 관련 문서

- [IDE Agent 개요](02_IDE_Agent.md)
- [실측 및 비교 결과](Continue_Local_LLM_Benchmark_Report.md)
