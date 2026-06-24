# Agent Basic 실습

프레임워크 없이 Ollama API와 Python 표준 라이브러리만 사용해 Chat과 Tool Calling의 차이를 확인한다.

## 구조

- `ollama_client.py`: Ollama `/api/chat` 클라이언트
- `chat_demo.py`: 도구가 없는 일반 Chat 호출
- `basic_agent.py`: Native tool call과 JSON Action fallback을 Python 함수 실행으로 연결하는 Agent loop
- `memory_agent.py`: 최근 대화를 JSON으로 저장하고 다음 요청에 전달하는 Agent

## 실행

Windows PowerShell:

```powershell
python .\agent_basic\chat_demo.py --model gemma3:4b
python .\agent_basic\basic_agent.py "12와 30을 더해줘"
python .\agent_basic\memory_agent.py "12와 30을 더해줘"
python .\agent_basic\memory_agent.py "그 결과에 8을 더해줘"
```

WSL에서 고정 Ollama 주소를 사용할 경우:

```bash
export OLLAMA_BASE_URL=http://172.30.236.141:11434
python3 agent_basic/chat_demo.py --model gemma3:4b
python3 agent_basic/basic_agent.py "12와 30을 더해줘"
python3 agent_basic/memory_agent.py "12와 30을 더해줘"
python3 agent_basic/memory_agent.py "그 결과에 8을 더해줘"
```

## 기대 결과

- Gemma3 Chat: 일반 텍스트 응답
- Gemma3 Agent: tools 미지원 오류
- Qwen3 Agent: native tool call로 Python 함수 실행
- Native 호출에는 `/no_think`, 단일 영어 도구 스키마, 최대 512 출력 토큰 적용
- Native 호출 실패 시 JSON Schema로 Action을 강제하고 검증 후 실행
- 허용 목록에 없는 도구나 잘못된 인자는 실행하지 않음
- 모델이 동일한 호출을 중복 반환하면 한 번으로 정규화하고 서로 다른 다중 호출은 차단

Memory 확인과 초기화:

```bash
python agent_basic/memory_agent.py --show
python agent_basic/memory_agent.py --clear
```

## 현재 파일 역할

- `agent_core.py`: Tool schema, native tool call, fallback, 검증 및 실행을 담당하는 공통 엔진
- `basic_agent.py`: 메모리를 저장하지 않는 단발성 실행 예제이자 공통 엔진 점검용 CLI
- `memory_agent.py`: 공통 엔진에 JSON 대화 이력을 결합한 상태 유지 CLI
- `langchain_agent.py`: 같은 작업을 LangChain `bind_tools`로 구현한 비교 예제

`basic_agent.py`는 실무 대화 서비스의 진입점이라기보다, 메모리 문제와 Tool Calling 문제를
분리해서 검사하는 최소 재현 도구로 유지한다.

## LangChain 비교 실습

WSL에서는 Windows용 `.venv`를 재사용하지 말고 별도 환경을 만든다.

```bash
cd /mnt/d/AI_Platform_Engineering_Lab
python3 -m venv .venv-wsl
source .venv-wsl/bin/activate
python3 -m pip install -r agent_basic/requirements.txt
export OLLAMA_BASE_URL=http://172.30.236.141:11434
python3 agent_basic/langchain_agent.py "12와 30을 더해줘"
```

예상 결과:

```text
[Agent] LangChain bind_tools 호출 실패. structured output fallback을 사용합니다.
[Tool] add_numbers -> {"result": 42}
[Agent] 계산 결과는 42입니다.
[Framework] LangChain structured_output_fallback
```

동일 프롬프트 비교 벤치마크:

```bash
python3 agent_basic/compare_agents.py "12와 30을 더해줘"
```

각 구현의 실행시간, 종료코드, native/fallback 경로와 최종 결과를 함께 출력한다.
