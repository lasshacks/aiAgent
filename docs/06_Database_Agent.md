# 06_Database_Agent

## 목표

데이터베이스 운영 및 분석 업무를 AI Agent로 자동화하고, 자연어 기반 SQL 생성 및 데이터 조회가 가능한 Database Agent를 구축한다.

최종 목표

* PostgreSQL Agent 구축
* 자연어 기반 SQL 생성
* 데이터 조회 자동화
* 운영 점검 자동화
* 성능 분석 자동화
* MCP 기반 Database Tool 구축

---

## 학습 내용

### Database Agent란?

데이터베이스와 연동되어 조회, 분석, 운영 지원을 수행하는 AI Agent이다.

예시

```text id="dbagent1"
사용자
 ↓
오늘 가입한 회원 수 알려줘
 ↓
Agent
 ↓
SQL 생성
 ↓
DB 조회
 ↓
결과 반환
```

---

### 왜 Database Agent가 필요한가?

기존 방식

```text id="olddb1"
사용자
 ↓
운영자
 ↓
SQL 작성
 ↓
DB 조회
 ↓
결과 전달
```

---

Agent 방식

```text id="newdb1"
사용자
 ↓
Agent
 ↓
SQL 생성
 ↓
DB 조회
 ↓
결과 반환
```

---

### Database Agent 활용 사례

#### 데이터 조회

```text id="dbcase1"
오늘 신규 회원 수 알려줘
```

---

#### SQL 생성

```text id="dbcase2"
최근 30일 로그인 사용자 조회 SQL 만들어줘
```

---

#### 성능 분석

```text id="dbcase3"
느린 쿼리 찾아줘
```

---

#### 운영 지원

```text id="dbcase4"
현재 접속 세션 수 알려줘
```

---

### Database Agent 아키텍처

```text id="dbarch1"
사용자
    ↓
Agent
    ↓
MCP
    ↓
Database Tool
    ↓
PostgreSQL
```

---

### 운영 자동화 범위

| 기능     | 자동화 가능 |
| ------ | ------ |
| SQL 생성 | O      |
| 데이터 조회 | O      |
| 통계 조회  | O      |
| 세션 조회  | O      |
| 인덱스 분석 | O      |
| 성능 분석  | O      |
| 리포트 생성 | O      |

---

## 실습 절차

### 1. PostgreSQL 환경 준비

대상

* Local PostgreSQL
* Docker PostgreSQL
* 운영 유사 환경

---

### 2. PostgreSQL 연결 확인

```bash id="psql1"
psql -U postgres
```

---

### 3. Python PostgreSQL 라이브러리 설치

```bash id="psql2"
pip install psycopg2-binary
```

또는

```bash id="psql3"
pip install sqlalchemy
```

---

### 4. DB 연결 실습

예제

```python id="dbconnect1"
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="study",
    user="postgres",
    password="postgres"
)
```

---

### 5. SQL 실행 Tool 생성

예제

```python id="tool61"
def execute_sql(query):
    pass
```

---

### 6. 테이블 정보 조회 Tool

예제

```python id="tool62"
def get_tables():
    pass
```

실행 예시

```text id="tool63"
현재 테이블 목록 보여줘
```

---

### 7. 자연어 → SQL 변환

예제

```text id="sqlgen1"
오늘 가입한 회원 수 알려줘
```

변환

```sql id="sqlgen2"
SELECT COUNT(*)
FROM member
WHERE join_date = CURRENT_DATE;
```

---

### 8. 운영 점검 Tool 생성

조회 항목

* 세션 수
* Lock 상태
* Long Running Query
* Slow Query

---

### 9. MCP 연동

구성

```text id="dbmcp61"
Agent
 ↓
MCP
 ↓
Database Tool
 ↓
PostgreSQL
```

---

### 10. Database Agent 구축

최종 기능

* SQL 생성
* 데이터 조회
* 통계 조회
* 운영 점검
* 성능 분석

---

## TODO

### 환경 구축

* [ ] PostgreSQL 준비
* [ ] Python 라이브러리 설치
* [ ] DB 연결 확인

### 실습

* [ ] SQL Tool
* [ ] 테이블 조회 Tool
* [ ] 자연어 SQL 생성
* [ ] 운영 점검 Tool
* [ ] 성능 분석 Tool

### Agent

* [ ] MCP 연동
* [ ] Database Agent 구축

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### DB 연결 검증

```sql id="verify61"
SELECT 1;
```

정상 응답 확인

---

### SQL 생성 검증

질문

```text id="verify62"
회원 수 알려줘
```

생성 SQL 검증

---

### 데이터 조회 검증

직접 실행 결과와 비교

---

### 운영 점검 검증

확인 항목

* 세션 수
* Lock 정보
* Slow Query

---

### 재현 검증

다른 DB 환경에서 동일 기능 수행

---

## 결과물

### 코드

* Database Tool
* SQL Generator
* Database Agent

### 문서

* 구축 가이드
* SQL 예제 모음
* 운영 가이드

### 다이어그램

* Database Agent Architecture
* MCP Integration Architecture

---

## 회고

### 배운 점

* 자연어 SQL 변환 이해
* Database Agent 구조 이해
* 운영 자동화 방법 이해

### 개선점

* SQL 정확도 향상
* 권한 제어 강화
* 성능 분석 기능 확대

### 다음 단계

* Observability
* Multi-Agent
* AI Operations Platform

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* 샘플 데이터
* SQL 예제
* 테스트 결과

### 스크린샷

* SQL 생성 결과
* 데이터 조회 결과
* 운영 점검 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 Database Agent가 필요한가?

반복적인 데이터 조회 및 운영 점검 업무를 자동화하기 위함이다.

---

### 구현 방법

* PostgreSQL 연결
* Tool 구현
* SQL 생성
* MCP 연동

---

### 트러블슈팅

예상 사례

* DB 연결 실패
* 권한 부족
* SQL 생성 오류
* 결과 해석 오류

---

### 결과

* Database Agent 구축
* SQL 자동 생성
* 운영 점검 자동화

---

## 면접 포인트

### Database Agent란?

데이터베이스를 대상으로 조회, 분석, 운영 지원을 수행하는 AI Agent이다.

---

### 자연어 SQL 생성이란?

사용자의 자연어 요청을 SQL로 변환하여 실행하는 기능이다.

예시

```text id="interview61"
회원 수 알려줘
```

↓

```sql id="interview62"
SELECT COUNT(*) FROM member;
```

---

### 왜 PostgreSQL을 선택했는가?

현재 실무 경험이 가장 많으며 AI Agent 실습에 적합하기 때문이다.

---

### Database Agent가 수행할 수 있는 작업은?

* 데이터 조회
* SQL 생성
* 세션 조회
* Lock 조회
* 성능 분석

---

### MCP와 Database를 왜 연결하는가?

Agent가 Database를 Tool 형태로 활용하기 위해서이다.

---

### 대안은 무엇인가?

* BI Tool
* Query Tool
* Admin Tool

예시

* pgAdmin
* DBeaver
* DataGrip

하지만 자연어 기반 Agent 자동화는 제공하지 않는다.

---

### 운영 시 고려사항

* DB 계정 권한 최소화
* SQL Injection 방지
* 조회 범위 제한
* 감사 로그 기록
* 운영 DB 직접 변경 금지

---

### AI Platform Engineer 관점 핵심 포인트

현재 실무에서 수행하는 PostgreSQL 운영 업무를 AI Agent로 자동화하는 단계이다.

기존 방식

```text id="compare61"
운영자
 ↓
SQL 작성
 ↓
조회
```

AI 방식

```text id="compare62"
운영자
 ↓
Agent
 ↓
SQL 생성
 ↓
조회
 ↓
분석
```

---

### 실무 적용 포인트

현재 경험과 직접 연결 가능

* PostgreSQL 운영
* Kafka 메타데이터 조회
* Data Mart 분석
* CDC 상태 조회
* PMS 데이터 조회

---

### 확장 방향

#### 현재

```text id="dbfuture1"
Agent
 ↓
PostgreSQL
```

#### 확장

```text id="dbfuture2"
Agent
 ↓
MCP
 ↓
PostgreSQL
 ↓
Vector DB
 ↓
Data Mart
 ↓
Analytics
```

---

### 최종 목표

```text id="dbflow1"
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
Database Agent
    ↓
Kubernetes Agent
    ↓
Observability
    ↓
AI Operations Platform
```
