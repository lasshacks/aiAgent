# VS Code Continue 실행 가이드 (실시간)

## 🎯 목표
VS Code Continue와 Ollama를 사용하여 실시간 코드 생성 테스트

## 📋 체크리스트

### 사전 준비 (터미널)
- [x] Ollama 설치 (v0.30.10)
- [x] Qwen3 4B 다운로드
- [x] systemd override 설정 (OLLAMA_HOST=0.0.0.0:11434)
- [x] Ollama 서비스 재시작
- [x] Continue v2.0.0 설치
- [x] ~/.continue/config.json 설정

### VS Code 준비
- [ ] VS Code 실행 (이미 열려있음)
- [ ] Continue Tab 확인 (좌측 Sidebar)
- [ ] Chat 열기 준비 (Ctrl+L)

---

## 📖 Step-by-Step 실행 가이드

### Step 1: Continue Chat 열기 ⏱️ 1초

**액션:**
```
VS Code에서 Ctrl+L 누르기
(또는 Cmd+L on Mac)
```

**확인 사항:**
```
좌측 Sidebar에 Continue 아이콘
또는 상단에 "Continue Chat" 탭 나타남
```

**스크린샷 예상:**
```
┌─────────────────────────────────────┐
│ VS Code                             │
├─────────────────────────────────────┤
│ File Edit View ... Ctrl+L           │
│ ┌─ Continue Chat ───────────────────┤
│ │                                   │
│ │ [Chat input box]                 │
│ │                                   │
│ └───────────────────────────────────┤
```

---

### Step 2: 모델 선택 ⏱️ 1초

**액션:**
```
Continue Chat 상단의 드롭다운 클릭
→ "Qwen3 Local" 선택
```

**확인:**
```
"Qwen3 Local" 모델이 선택됨 (표시됨)
```

---

### Step 3: 첫 번째 테스트 프롬프트 ⏱️ 20-30초

**액션:**
아래 프롬프트를 복사해서 Chat에 붙여넣기:

```
Python으로 간단한 함수를 만들어줘.
함수명: add_numbers
기능: 두 개의 숫자를 더해서 반환
주석: 달아줘
```

**예상 결과:**
```python
def add_numbers(a, b):
    """
    두 개의 숫자를 더해서 반환하는 함수
    
    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자
    
    Returns:
        두 숫자의 합
    """
    return a + b
```

**버튼:**
- "Insert": 현재 파일에 코드 삽입
- "Copy": 클립보드로 복사
- "Stop": 생성 중단 (필요시)

---

### Step 4: 두 번째 테스트 (클래스 생성) ⏱️ 25-35초

**액션:**
Chat을 지우고 새 프롬프트 입력:

```
Python Student 클래스를 만들어줘.
- 속성: name, age, grade
- 메서드: get_info() - "이름: {name}, 나이: {age}, 등급: {grade}" 형식으로 반환
- __init__ 생성자 포함
- 주석 달아줘
```

**예상 결과:**
```python
class Student:
    """학생 정보를 관리하는 클래스"""
    
    def __init__(self, name, age, grade):
        """
        초기화 메서드
        
        Args:
            name: 학생 이름
            age: 학생 나이
            grade: 학생 등급
        """
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        """학생 정보 반환"""
        return f"이름: {self.name}, 나이: {self.age}, 등급: {self.grade}"
```

---

### Step 5: 세 번째 테스트 (Flask API) ⏱️ 30-40초

**액션:**
```
Python Flask REST API를 만들어줘.
- GET /hello 엔드포인트
- 응답: {"message": "Hello, World!"}
- Flask import 포함
- if __name__ == '__main__': app.run()
```

**예상 결과:**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    """
    Hello 엔드포인트
    
    Returns:
        JSON 응답
    """
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run()
```

---

## 🔄 Tab Autocomplete 테스트 (선택사항)

**액션:**
```
새 파일 만들기
파일에 다음 입력:

def calculate_
```

**기대:**
```
자동 완성 제안 나타남 (예: calculate_sum, calculate_average 등)
Tab 키로 수용
```

---

## 📊 성능 지표 기록

### Test 1: add_numbers 함수
```
입력 길이: 약 25자
응답 시간: ___초
생성된 라인: ___줄
품질 평가: ___/5.0
```

### Test 2: Student 클래스
```
입력 길이: 약 60자
응답 시간: ___초
생성된 라인: ___줄
품질 평가: ___/5.0
```

### Test 3: Flask API
```
입력 길이: 약 50자
응답 시간: ___초
생성된 라인: ___줄
품질 평가: ___/5.0
```

---

## ✅ 테스트 체크리스트

완료 후 체크:

- [ ] Step 1: Continue Chat 열기
- [ ] Step 2: 모델 선택
- [ ] Step 3: 첫 번째 함수 생성
- [ ] Step 4: 클래스 생성
- [ ] Step 5: Flask API 생성
- [ ] Tab Autocomplete 테스트
- [ ] 성능 지표 기록

---

## 🆘 문제 해결

### Continue Chat이 안 열려요

**해결:**
```
Option 1: Ctrl+Shift+X → Continue 검색 → Enable 확인
Option 2: View → Command Palette → "Continue: Open" 검색
Option 3: VS Code 재시작
```

### 모델이 보이지 않아요

**해결:**
```
1. ~/.continue/config.json 확인
2. Ollama가 실행 중인지 확인
   systemctl status ollama
3. API 테스트
   curl http://172.30.236.141:11434/api/tags
4. VS Code 재시작
```

### 응답이 매우 느려요

**해결:**
```
- Ollama 메모리 확인: systemctl status ollama
- 다른 프로세스 확인: top
- Gemma3:4b로 전환 (더 빠름)
- 프롬프트 길이 줄이기
```

### "Connection refused" 에러

**해결:**
```
1. WSL IP 확인:
   hostname -I
2. ~/.continue/config.json에서 
   apiBase를 실제 IP로 변경
3. 방화벽 확인
```

---

## 📝 실시간 메모

테스트하면서 여기에 메모하세요:

```
시간: ___
테스트: ___
결과: ___
문제: ___
해결: ___
```

---

## 🎬 다음 단계

테스트 완료 후:
1. [ ] 결과 스크린샷 저장
2. [ ] 성능 분석 문서 작성
3. [ ] Cline 테스트 (Decision-003)
4. [ ] Continue vs Cline 비교표 작성
5. [ ] Track 3 시작 준비

---

## 📚 참고 문서

- Continue_Usage_Guide.md
- Continue_Test_Results.md
- 02_IDE_Agent_Setup_Guide.md
