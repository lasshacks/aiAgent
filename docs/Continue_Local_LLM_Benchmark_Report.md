# Continue 로컬 LLM 연동 및 IDE Agent 실습 보고서

## 1. 실습 개요

- 실습 기간: 2026-06-19 ~ 2026-06-23
- 목표: VS Code의 Continue를 로컬 Ollama 모델과 연결하고 Chat 및 Agent 기반 코드 생성을 검증한다.
- 비교 대상: Continue + Qwen3, Continue + Gemma3, Codex
- 주요 산출물: 단순 함수, 덧셈 웹 앱, 곱셈 웹 앱, Ollama 모델 벤치마크

## 2. 환경

| 구분 | 구성 |
|---|---|
| IDE | Visual Studio Code |
| Continue | 2.1.0 |
| Cline | 3.89.2, 설치 완료·연동 비교 미실시 |
| Ollama | 0.30.10 |
| Ollama API | `http://172.30.236.141:11434` |
| 기본 모델 | `qwen3:4b` |
| 비교 모델 | `gemma3:4b` |
| 실행 환경 | Windows + WSL 터미널 |

Ollama 루트 주소와 `/api/tags`를 통해 서버와 모델 연결을 확인했다. Continue 설정에는 응답을 UI에 점진적으로 표시하기 위해 `stream: true`를 사용했다. Ollama의 스트리밍 및 비스트리밍 API 호출은 모두 정상 동작했다.

## 3. 모델 설치 및 설정

### 설치 모델

| 모델 | 저장 크기 | 파라미터 | 양자화 | Ollama capabilities |
|---|---:|---:|---|---|
| `qwen3:4b` | 약 2.33GB | 4.0B | Q4_K_M | completion, tools, thinking |
| `gemma3:4b` | 약 3.11GB | 4.3B | Q4_K_M | completion, vision |

Gemma3는 다음 명령에 해당하는 Ollama API 작업으로 설치했으며 약 1분 37초가 걸렸다.

```bash
ollama pull gemma3:4b
```

프로젝트 설정과 사용자 Continue 설정의 모델명을 `gemma3:4b`로 통일했다. 기존 사용자 설정의 `gemma:3b`는 잘못된 모델명이었다.

Gemma3 4B는 Ollama 메타데이터상 `tools` capability가 없다. 따라서 설정에서 Gemma의 `tool_use` 강제 선언을 제거했으며, Continue Chat 비교에는 사용할 수 있지만 Agent의 파일 조작 모델로 평가하지 않는다.

## 4. Continue + Qwen3 실습

### 단순 코드 생성

다음 요구사항으로 Python 함수를 생성했다.

```text
두 숫자를 더하는 Python 함수 add_numbers를 작성해줘.
타입 힌트와 한국어 docstring을 포함해줘.
```

생성 결과는 `continue_add_numbers.py`에 저장했고 `add_numbers(2, 3) == 5`를 확인했다. 단, 이 파일의 실제 생성과 삽입은 Codex가 수행했으므로 Continue의 `Insert at Cursor` 검증 결과에는 포함하지 않는다.

### Agent 모드 멀티파일 코드 생성

Continue Agent 모드에 Python 표준 라이브러리 기반 웹 앱과 프론트엔드 생성을 요청했다. Qwen3는 파일 쓰기나 터미널 도구를 직접 호출하지 않고 대화 기록에 소스 코드와 실행 명령을 제시했다. 사용자가 이를 복사·붙여넣기해 다음 파일을 만들고 직접 실행했다.

- `continue_web_demo/backend.py`
- `continue_web_demo/static/index.html`

Agent 모드의 코드 응답은 받았지만 자동 파일 생성은 수행되지 않았고 시간이 오래 걸렸다. 사용자가 파일에 반영한 최초 결과에는 다음 문제가 있었다.

- 덧셈 앱 요구사항을 곱셈 앱으로 구현함
- 사용자가 입력한 숫자를 파싱하지 않고 `5 * 3 = 15`를 고정 반환함
- `BaseHTTPRequestHandler`만 사용하여 정적 HTML을 제공하지 못함
- 모든 POST 경로를 구분 없이 처리함
- 입력 검증과 오류 응답이 없음
- 프론트엔드와 백엔드가 실행 가능한 하나의 앱으로 연결되지 않음

Continue Agent 대화가 중간에 제안한 다음 형태의 코드도 올바르지 않았다.

```python
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler):
    http.server.SimpleHTTPRequestHandler.serve_forever()
```

`serve_forever()`는 Handler 클래스가 아니라 생성된 서버 객체에서 호출해야 한다.

```python
with socketserver.TCPServer(("", PORT), Handler) as server:
    server.serve_forever()
```

## 5. Codex 구현 및 보정

### Codex 기준 앱

Codex는 다음 구조의 덧셈 앱을 구현했다.

- `continue_add_numbers.py`: 덧셈 함수
- `addition_app.py`: 정적 화면과 `/api/add` API를 제공하는 멀티스레드 서버
- `web/index.html`: 반응형 덧셈 계산기 화면

검증 결과는 다음과 같다.

- 정적 화면 GET: 성공
- `2 + 3 = 5` API: 성공
- Python 문법 검사: 성공
- 잘못된 입력 처리: HTTP 400

실행 방법:

```bash
python3 addition_app.py
```

브라우저 주소:

```text
http://localhost:8000
```

### Continue Agent 결과 보정

Continue Agent 대화의 응답을 사용자가 붙여넣어 만든 곱셈 앱은 다음과 같이 수정했다.

- `SimpleHTTPRequestHandler`를 상속해 `static/index.html` 제공
- `/multiply` 경로만 POST API로 처리
- URL 인코딩된 `num1`, `num2`를 파싱해 실제 곱셈 수행
- 숫자 유효성 검사와 HTTP 400 응답 추가
- `ThreadingHTTPServer` 적용
- 덧셈 앱과 동시에 실행할 수 있도록 포트 `8001` 사용
- 덧셈 계산기와 동일한 다크 그라데이션 UI 적용

검증 결과:

- 정적 화면 GET: 성공
- `5 × 3 = 15` API: 성공
- 잘못된 입력: HTTP 400 성공
- 반응형 디자인 제공: 성공

실행 방법:

```bash
python3 continue_web_demo/backend.py
```

브라우저 주소:

```text
http://localhost:8001
```

## 6. Qwen3와 Gemma3 API 벤치마크

벤치마크는 `benchmarks/ollama_model_benchmark.py`로 수행했다. 동일한 Python 코드 생성 요청과 구조화된 도구 호출 요청을 사용했다.

### 측정 결과

| 항목 | Qwen3 4B | Gemma3 4B |
|---|---|---|
| 코드 생성 | 28.68초 | 69.45초 |
| 모델 로드 시간 | 12.01초 | 40.19초 |
| 출력 토큰 | 128 | 128 |
| 생성 속도 | 8.53 tokens/s | 4.91 tokens/s |
| Python 문법 | 코드 미생성 | 정상 |
| 요구 함수 포함 | 미포함 | 포함 |
| 5개 테스트 포함 | 미포함 | 미포함 |
| 도구 호출 | 11.40초, 구조화된 호출 실패 | 모델 미지원 오류 |

최초 Qwen3 측정은 Continue Agent의 장시간 요청과 겹쳐 180초를 초과했으므로 폐기했다. 2026-06-23에 모든 모델을 언로드하고 Qwen3만 단독으로 다시 측정한 결과가 위 표의 수치다.

Qwen3는 Gemma3보다 토큰 생성 속도가 빨랐지만 128토큰을 문제 설명에 사용하고 실제 Python 코드를 출력하지 못했다. 도구 호출 요청에서도 `tool_calls`를 반환하지 않고 도구 사용 방법을 설명하는 일반 텍스트를 반환했다. Ollama 메타데이터에 `tools` capability가 있어도 이 모델 크기와 프롬프트 조건에서 실제 구조화된 호출 성공을 보장하지 않는다는 결과다.

Gemma3는 코드를 반환했지만 128토큰 제한 내에서 테스트 코드를 완성하지 못했다. 또한 Ollama는 도구 호출 요청에 다음 오류를 반환했다.

```text
registry.ollama.ai/library/gemma3:4b does not support tools
```

벤치마크 재실행:

```bash
python3 benchmarks/ollama_model_benchmark.py
```

## 7. Cline + Qwen3 진행 기록

2026-06-23에 Cline 3.89.2의 Act 모드에서 로컬 Ollama `qwen3:4b`를 사용해 멀티파일 웹 앱 생성을 요청했다.

| 시각 | 상태 |
|---|---|
| 15:16:47 | 작업 생성 및 체크포인트 생성 |
| 15:17:00 | Ollama API 요청 시작 |
| 15:26:04 | `Ollama request timed out after 180 seconds` 기록 |
| 15:26:06 | 최대 3회 중 첫 번째 자동 재시도 시작 |
| 15:46 확인 | 입력·출력 토큰 0, 생성 파일 0, 재시도 진전 없음 |
| 15:48 | 사용자가 작업 취소, `cline_web_demo` 미생성 확인 |

확인 당시 Qwen3는 약 5.1GB 메모리로 로드되어 있었지만 `cline_web_demo` 폴더는 생성되지 않았다. 직전의 단순 `안녕` 작업도 입력 15,399토큰과 출력 3,119토큰을 사용했다. 짧은 인사에도 Cline의 Agent 컨텍스트와 Qwen3의 thinking 출력이 매우 크게 소비된다는 점을 확인했다.

실행 프롬프트에는 첫 줄의 “곱셈 웹 앱”과 세부 조건의 “덧셈 API”가 함께 있어 요구사항도 일치하지 않았다. 공정한 재시험에서는 연산을 하나로 통일해야 한다.

최종 판정:

- Cline과 로컬 Ollama 연결: 성공
- Qwen3 기본 응답과 파일 읽기: 성공
- 멀티파일 생성 요청: 첫 요청 timeout
- 자동 재시도: 장시간 무응답
- 실제 파일 생성: 실패
- 사용자 취소 후 Qwen3 언로드 및 Ollama 캐시 정리 완료

### Cline + Gemma3 호환성 확인

Cline에서 `gemma3:4b`를 선택했을 때 Ollama는 다음 오류를 반환했다.

```text
registry.ollama.ai/library/gemma3:4b does not support tools
```

Cline은 같은 요청을 3회 자동 재시도했지만 모두 실패했다. 이는 생성 속도 문제가 아니라 Cline Agent 요청이 tools를 포함하는 반면 Gemma3 4B가 Ollama tools capability를 제공하지 않아서 발생한 호환성 오류다.

- 모델 추론 시작: 실패
- 도구 호출 capability 검사: 실패
- 자동 재시도: 3회 모두 실패
- 파일 변경: 없음
- 판정: Gemma3 4B는 Cline Plan/Act 모델로 사용 불가

Gemma3 코드 품질 비교는 도구를 요구하지 않는 Continue Chat 또는 Ollama API에서 수행해야 한다.

## 8. 비교 평가

| 평가 항목 | Continue + Qwen3 | Cline + Qwen3 | Continue + Gemma3 | Codex |
|---|---|---|---|---|
| 일반 Chat | 성공 | Qwen3 성공, 과도한 thinking 사용 | 사용 가능, UI 실측 필요 | 성공 |
| 파일 생성 | Agent 모드였으나 사용자가 수동 반영 | timeout, 생성 파일 0 | Agent 도구 호출 미지원 | 성공 |
| 멀티파일 완성도 | 수동 반영한 최초 결과 미완성 | 작업 시작 실패 | 평가 대상 아님 | 실행 가능한 형태로 완성 |
| 요구사항 준수 | 덧셈을 곱셈으로 구현 | 평가 불가, 프롬프트도 상충 | 추가 실측 필요 | 준수 |
| 실행 검증 | 사용자 및 Codex 보정 필요 | 실행 파일 없음 | 추가 실측 필요 | 자동 검증 완료 |
| 로컬 실행 비용 | OpenAI 크레딧 없음 | OpenAI 크레딧 없음 | OpenAI 크레딧 없음 | OpenAI 사용량 발생 |

## 9. 결론

1. Continue와 Ollama 연결 및 로컬 모델 선택은 정상 동작한다.
2. Qwen3 4B는 Continue Agent 모드에서 소스와 명령을 응답했지만 파일 반영과 실행은 사용자가 직접 수행했으므로 자동 편집 성공으로 볼 수 없다.
3. 단독 API 테스트에서는 실제 코드와 구조화된 도구 호출을 생성하지 못했고, Agent 대화 산출물의 요구사항 준수와 통합 완성도도 낮았다.
4. Gemma3 4B는 코드 생성 비교에는 의미가 있지만 Ollama에서 tools를 지원하지 않으므로 Continue Agent 비교 모델로는 적합하지 않다.
5. Cline은 단순 인사에도 큰 Agent 컨텍스트와 thinking 토큰을 사용했고 멀티파일 작업은 첫 응답 전에 timeout됐다.
6. Cline에서 Gemma3를 사용하면 tools 미지원 오류가 발생해 모델 추론 자체가 시작되지 않는다.
7. Codex는 같은 범위의 멀티파일 앱을 더 완성된 형태로 생성하고 자동 검증까지 수행했다.
8. 로컬 4B 모델은 비용 없는 간단한 Chat·코드 초안에 유용하지만, 복잡한 IDE Agent 작업에는 성능과 신뢰성 한계가 있다.

## 10. 다음 단계

- [x] Continue의 진행 중 요청을 모두 종료한 뒤 Qwen3 단독 벤치마크 재실행
- [x] Continue Agent + Qwen3의 자동 파일 생성 검증(도구 미호출, 사용자 수동 반영)
- [ ] Gemma3를 Continue Chat 모드에서 동일 프롬프트로 코드 품질 비교
- [ ] Qwen3 Agent의 파일 변경 승인 과정과 실행 결과 스크린샷 저장
- [x] Cline + Qwen3 연동 및 동일 과제 수행(첫 응답 timeout으로 종료)
- [x] Continue, Cline, Codex의 시간·성공률·수정 횟수 비교표 완성
- [ ] CPU, GPU, RAM 사용량과 토큰 생성 속도 함께 기록

## 11. 관련 파일

- `.continue/config.json`: 프로젝트 Continue 설정
- `continue_add_numbers.py`: 기본 덧셈 함수
- `addition_app.py`: Codex 덧셈 앱 백엔드
- `web/index.html`: Codex 덧셈 앱 화면
- `continue_web_demo/backend.py`: Continue Agent 응답을 수동 반영 후 보정한 곱셈 앱 백엔드
- `continue_web_demo/static/index.html`: Continue Agent 응답을 수동 반영 후 보정한 곱셈 앱 화면
- `benchmarks/ollama_model_benchmark.py`: Ollama 모델 비교 스크립트
- `docs/02_IDE_Agent.md`: IDE Agent 개요와 진행 현황
- `docs/Continue_Usage_Guide.md`: 최신 Continue 설정 및 사용 가이드
