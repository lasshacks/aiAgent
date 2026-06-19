# Continue vs Cline 설정 가이드

## 설치 현황 (2026-06-19)

### Continue ✅
- 설치: v2.0.0
- 설정: ~/.continue/config.json
- Ollama 연동: 완료 ✅

### Cline ✅
- 설치: v3.89.2
- 설정: VS Code UI 기반
- Ollama 연동: 진행 중

---

## Continue 설정 (완료)

### 파일 위치
```
~/.continue/config.json
```

### 설정 내용
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
  }
}
```

### 사용 방법

#### 1. Continue Chat 열기
```
Ctrl+L (또는 Cmd+L on Mac)
또는
View → Continue
```

#### 2. 모델 선택
- Chat 상단에서 "Qwen3 Local" 선택

#### 3. 사용 예
```
사용자: "Python으로 간단한 REST API 만들어줘"

Continue:
1. 모델 호출 (Ollama → Qwen3)
2. 코드 생성
3. 탭에 표시
```

---

## Cline 설정 (진행 중)

### 아키텍처
```
VS Code 
  ↓
Cline Extension
  ↓
MCP (Model Context Protocol)
  ↓
LLM (OpenAI / Anthropic / Custom)
  ↓
도구/파일 시스템 자동 접근
```

### Ollama 연동 방법

#### 방법 1: OpenRouter를 통한 간접 연동 (권장)
```
VS Code → Cline → OpenRouter API → Ollama
```

단점: 외부 API 의존

#### 방법 2: Custom Model 설정 (로컬 전용)
```
VS Code → Cline → Custom LLM endpoint → Ollama
```

장점: 완전 로컬

### Cline 설정 UI 사용법

#### 1. Cline 패널 열기
```
Ctrl+Shift+X (Extensions)
Cline 설정 아이콘 클릭
```

#### 2. 모델 설정
```
Settings → Models → Add Model
Name: Qwen3 Local
Type: Custom/Other
Endpoint: http://172.30.236.141:11434
Model: qwen3:4b
```

#### 3. 테스트
```
Cline Chat 오픈 → 모델 선택 → 테스트
```

---

## 주요 기능 비교

### Continue
```
사용 사례:
- 코드 자동 완성
- 간단한 코드 생성
- 코드 리뷰

장점:
✅ 설정이 간단
✅ 다양한 LLM 지원
✅ 좋은 자동 완성

단점:
❌ MCP 미지원
❌ 도구 자동화 약함
```

### Cline
```
사용 사례:
- 복잡한 프로젝트 분석
- 자동화된 작업 수행
- 파일/Git 자동 조작

장점:
✅ MCP 기반 도구 자동 발견
✅ 파일 시스템 직접 접근
✅ Git 자동 통합
✅ 고급 Agent 기능

단점:
❌ 설정이 복잡
❌ Custom LLM 설정 어려움
❌ 로컬 환경에서 API 키 필수
```

---

## 실습 계획

### Today (2026-06-19)
- [x] Continue 설치 및 설정
- [x] Cline 설치
- [ ] Cline Ollama 연동 테스트
- [ ] 두 도구 비교 실습

### 1단계: Continue 사용법 학습
```
Ctrl+L → "Spring Boot Controller 예제 보여줘"
```

### 2단계: Cline 설정 및 학습
```
VS Code → Cline Settings → Custom Model 설정
```

### 3단계: 고급 기능 활용
```
Cline: "@all 이 프로젝트 분석해서 README.md 만들어줘"
```

---

## 네트워크 설정

### WSL2 IP 주소
```
172.30.236.141 (변경 가능)
```

### 포트 매핑
```
Ollama API: 172.30.236.141:11434
Open WebUI: 172.30.236.141:3000
```

### 연결 테스트
```bash
curl http://172.30.236.141:11434/api/tags
```

---

## 다음 단계

1. Cline Custom Model 설정 테스트
2. Continue vs Cline 코드 생성 비교
3. 실제 프로젝트에 적용
4. Track 3: Agent Basic 진행
