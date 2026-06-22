# Continue 실습 가이드

## 설치 확인

### VS Code에서 Continue 확인

1. **Continue Tab 확인**
   ```
   좌측 Sidebar에서 "Continue" 아이콘 확인
   또는 Ctrl+Shift+X → Continue 검색
   ```

2. **Continue Chat 열기**
   ```
   Ctrl+L (또는 Cmd+L on Mac)
   또는 View → Command Palette → "Continue: Open"
   ```

---

## 사용 방법

### 1단계: 모델 선택

Continue Chat 열기 후:
- 상단 드롭다운에서 모델 선택
- 추천: "Qwen3 Local"

### 2단계: 프롬프트 입력

Chat 입력창에 다음 예제 입력:

```
Python으로 간단한 REST API 만들어줘.
- Flask 사용
- GET /users 엔드포인트
- 샘플 데이터 반환
```

### 3단계: 코드 생성 및 삽입

Continue가 코드 생성 후:
1. 코드 검토
2. "Insert" 버튼 클릭
3. 현재 파일에 삽입

---

## 실습 예제 1: 간단한 함수

### 프롬프트
```
Python으로 주어진 문자열이 팰린드롬인지 확인하는 함수를 만들어줘.
주석도 달아줘.
```

### 예상 결과
```python
def is_palindrome(s):
    """
    문자열이 팰린드롬인지 확인하는 함수
    
    Args:
        s: 확인할 문자열
    
    Returns:
        bool: 팰린드롬이면 True, 아니면 False
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

---

## 실습 예제 2: 클래스 생성

### 프롬프트
```
Python으로 Student 클래스를 만들어줘.
- 속성: name, age, grade
- 메서드: get_info() - 학생 정보 출력
- __init__ 생성자 포함
```

### 예상 결과
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
        """학생 정보 출력"""
        return f"이름: {self.name}, 나이: {self.age}, 등급: {self.grade}"
```

---

## 실습 예제 3: 데이터 처리

### 프롬프트
```
Python에서 CSV 파일을 읽어서 데이터를 필터링하고 저장하는 코드를 만들어줘.
- pandas 사용
- 나이가 20 이상인 데이터만 필터링
- 결과를 new_data.csv에 저장
```

---

## 실습 예제 4: 테스트 코드

### 프롬프트
```
위의 is_palindrome 함수에 대한 unittest를 작성해줘.
- 팰린드롬인 경우
- 팰린드롬이 아닌 경우
- 공백 포함 경우 테스트
```

---

## 고급 기능

### Tab Autocomplete 활용

파일을 작성하다가 코드 입력 중:
1. 몇 글자 입력
2. 자동으로 제안 표시
3. Tab 키로 수용

### 다중 회차 대화

```
사용자: "Python 함수 만들어줘"
Continue: [코드 생성]

사용자: "이제 주석 추가해줘"
Continue: [주석 추가]

사용자: "테스트 코드도 만들어줘"
Continue: [테스트 코드 생성]
```

---

## 팁과 트러블슈팅

### 팁 1: 컨텍스트 제공

```
"이전에 만든 Student 클래스를 사용해서 
학생 목록을 관리하는 StudentManager 클래스를 만들어줘"
```

### 팁 2: 구체적인 요구사항

```
좋지 않은 예:
"함수를 만들어줘"

좋은 예:
"입력된 리스트를 오름차순으로 정렬하는 함수를 만들어줘.
버블 정렬 알고리즘 사용"
```

### 팁 3: 에러 수정

코드에 에러가 있으면:
```
"이 코드의 에러를 찾아서 고쳐줘"
[에러 발생 코드]
```

---

## Continue vs 직접 타이핑

| 상황 | Continue 추천 |
|------|---------------|
| 반복적인 코드 | ⭐⭐⭐ |
| 복잡한 로직 | ⭐⭐ |
| 테스트 코드 | ⭐⭐⭐ |
| 보일러플레이트 | ⭐⭐⭐⭐⭐ |
| 문서화 | ⭐⭐⭐ |
| 디버깅 | ⭐⭐ |

---

## 성능 기대값

Qwen3 4B 기준:
- 간단한 함수: 5-10초
- 중간 복잡도: 10-20초
- 복잡한 코드: 20-30초+

### 성능 개선 팁
1. 구체적인 프롬프트 (설명 짧을수록 빠름)
2. 작은 단위로 분할 요청
3. 필요시 Gemma 3B로 전환 (더 빠름)

---

## 다음 단계

1. [ ] 위의 4가지 예제 모두 테스트
2. [ ] 실제 프로젝트에 적용
3. [ ] Cline과의 차이점 비교
4. [ ] Track 3: Agent Basic 진행

## 최근 업데이트 (요약)

- [x] `c:\Users\sedof\.continue\config.yaml`에 각 모델에 `stream: true` 추가 — Continue가 Ollama에 스트리밍 호출을 하도록 설정함.
- [x] Ollama `qwen3:4b`에 대한 스트리밍 호출을 `curl`로 확인함 (NDJSON 토큰 청크 출력 확인).
- [ ] Continue UI에서 모델 드롭다운 및 코드 삽입 테스트 — 대기 중 (VS Code 재시작 후 확인 필요).

스트리밍 테스트(터미널에서 실행):

```bash
curl -sN --max-time 120 -X POST 'http://172.30.236.141:11434/api/generate' \
    -H 'Content-Type: application/json' \
    -d '{"model":"qwen3:4b","prompt":"Hello from test — reply with the model id only.","stream":true}' \
| python3 -u -c "import sys,json
out=''
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    j=json.loads(line)
    out += j.get('thinking','') or j.get('response','')
    if j.get('done'):
        break
print(out)"
```

참고: Ollama는 스트리밍과 비스트리밍 호출을 모두 지원합니다. Continue에는 생성되는 응답을 UI에 점진적으로 표시하기 위해 `stream: true`를 사용합니다.
