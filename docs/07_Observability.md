# 07_Observability

## 목표

Observability(관측성) 플랫폼을 구축하고 AI Agent와 연계하여 시스템 상태를 실시간으로 분석하고 장애를 진단할 수 있는 역량을 확보한다.

최종 목표

* OpenTelemetry 이해
* Metric 수집
* Log 수집
* Trace 수집
* Grafana 시각화
* AI 기반 장애 분석 Agent 구축

---

## 학습 내용

### Observability란?

시스템 내부 상태를 외부 데이터로 파악할 수 있는 능력이다.

기존 Monitoring

```text id="monitor1"
CPU
Memory
Disk
```

---

Observability

```text id="obs1"
Metric
+
Log
+
Trace
```

---

### 왜 Observability가 필요한가?

MSA 환경에서는 서비스가 많아지기 때문에 장애 원인을 찾기 어렵다.

예시

```text id="obs2"
API 호출
 ↓
Gateway
 ↓
Service A
 ↓
Kafka
 ↓
Service B
 ↓
PostgreSQL
```

장애 발생 시 전체 흐름 추적 필요

---

### Observability 3대 요소

#### Metrics

수치 데이터

예시

* CPU
* Memory
* Request Count
* Error Rate

---

#### Logs

이벤트 기록

예시

```text id="log71"
2026-06-19 ERROR DB Connection Fail
```

---

#### Traces

요청 흐름 추적

예시

```text id="trace71"
Gateway
 ↓
User Service
 ↓
Payment Service
 ↓
PostgreSQL
```

---

### OpenTelemetry

관측성 데이터 수집 표준

구성

```text id="otel1"
Application
 ↓
OTEL SDK
 ↓
OTEL Collector
 ↓
Backend
```

---

### 주요 구성요소

#### OpenTelemetry SDK

애플리케이션 계측

---

#### OTEL Collector

데이터 수집 및 전송

---

#### Prometheus

Metric 저장

---

#### Jaeger

Trace 저장

---

#### Grafana

시각화

---

### Observability 아키텍처

```text id="obsarch1"
Spring Boot
    ↓
OpenTelemetry SDK
    ↓
OTEL Collector
    ↓
Prometheus
    ↓
Grafana

Spring Boot
    ↓
OpenTelemetry SDK
    ↓
OTEL Collector
    ↓
Jaeger
```

---

### 현재 실무 경험 연결

이미 경험 보유

* OpenTelemetry
* Spring Boot
* Kubernetes
* MSA 전환 사업

이번 단계 목표

```text id="obsgoal1"
운영
 ↓
관측
 ↓
분석
 ↓
AI Agent
```

---

## 실습 절차

### 1. Docker 환경 준비

확인

```bash id="obsdocker1"
docker ps
```

---

### 2. OpenTelemetry Collector 실행

Docker Compose 예제

```yaml id="obsyaml1"
otel-collector:
  image: otel/opentelemetry-collector
```

---

### 3. Prometheus 구성

확인

```text id="prom71"
http://localhost:9090
```

---

### 4. Grafana 구성

확인

```text id="graf71"
http://localhost:3000
```

---

### 5. Jaeger 구성

확인

```text id="jaeger71"
http://localhost:16686
```

---

### 6. Spring Boot 계측

Gradle

```gradle id="gradle71"
implementation 'io.opentelemetry:opentelemetry-api'
```

---

### 7. Metric 수집

확인 항목

* Request Count
* Error Count
* Response Time

---

### 8. Trace 수집

테스트

```text id="trace72"
API 호출
```

확인

```text id="trace73"
Gateway
 ↓
Service
 ↓
DB
```

---

### 9. Log 수집

수집 항목

* Application Log
* Exception Log
* Audit Log

---

### 10. Grafana Dashboard 구성

대시보드

* API 현황
* Error 현황
* JVM 현황
* PostgreSQL 현황

---

### 11. Observability Agent 구축

예제

```text id="obsagent1"
현재 장애 원인 알려줘
```

Agent

```text id="obsagent2"
Metric
 ↓
Trace
 ↓
Log
 ↓
분석
```

---

## TODO

### 환경 구축

* [ ] OpenTelemetry 설치
* [ ] Collector 설치
* [ ] Prometheus 설치
* [ ] Grafana 설치
* [ ] Jaeger 설치

### 실습

* [ ] Metric 수집
* [ ] Log 수집
* [ ] Trace 수집
* [ ] Dashboard 구성

### Agent

* [ ] Observability Agent 구축
* [ ] MCP 연동

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### Metric 검증

Prometheus 확인

```text id="verify71"
http_server_requests
```

---

### Log 검증

에러 로그 발생 후 확인

---

### Trace 검증

Jaeger에서 호출 흐름 확인

---

### Dashboard 검증

Grafana Dashboard 확인

---

### 재현 검증

새 환경에서 동일 구성 후 정상 동작 확인

---

## 결과물

### 코드

* Spring Boot 계측 코드
* Collector 설정
* Dashboard 설정

### 문서

* 구축 가이드
* 운영 가이드
* 장애 분석 가이드

### 다이어그램

* Observability Architecture
* Trace Flow Diagram

---

## 회고

### 배운 점

* Observability 이해
* OpenTelemetry 구조 이해
* Trace 분석 방법 이해

### 개선점

* Alert 구성 필요
* Dashboard 고도화 필요
* AI 분석 정확도 향상 필요

### 다음 단계

* Multi-Agent
* AI Operations Platform

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* Collector 설정
* Dashboard JSON
* 테스트 데이터

### 스크린샷

* Grafana Dashboard
* Jaeger Trace
* Prometheus Metric

---

## 블로그 작성 포인트

### 문제 정의

왜 Monitoring만으로는 부족한가?

MSA 환경에서는 장애 원인을 찾기 어렵기 때문이다.

---

### 구현 방법

* OpenTelemetry 적용
* Collector 구성
* Prometheus 구성
* Grafana 구성

---

### 트러블슈팅

예상 사례

* Trace 누락
* Metric 누락
* Collector 설정 오류
* Dashboard 데이터 미표시

---

### 결과

* Observability 플랫폼 구축
* Trace 기반 분석 가능
* 장애 분석 자동화 기반 확보

---

## 면접 포인트

### Observability란?

시스템 내부 상태를 Metric, Log, Trace를 통해 파악하는 능력이다.

---

### Monitoring과 차이는?

| 구분    | Monitoring | Observability        |
| ----- | ---------- | -------------------- |
| 목적    | 상태 확인      | 원인 분석                |
| 데이터   | Metric 중심  | Metric + Log + Trace |
| 장애 분석 | 제한적        | 가능                   |

---

### OpenTelemetry란?

관측성 데이터 수집을 위한 표준 프레임워크이다.

---

### OpenTelemetry 구성 요소는?

* SDK
* Collector
* Exporter

---

### OTLP란?

OpenTelemetry Protocol

Collector로 데이터를 전달하기 위한 표준 프로토콜

예시

* OTLP gRPC
* OTLP HTTP

---

### 왜 OTEL Collector를 사용하는가?

장점

* 중앙 수집
* 데이터 변환
* 멀티 백엔드 지원

---

### Trace가 중요한 이유는?

MSA 환경에서 요청 흐름을 추적할 수 있기 때문이다.

예시

```text id="traceinterview1"
Gateway
 ↓
Service A
 ↓
Kafka
 ↓
Service B
 ↓
DB
```

---

### 대안은 무엇인가?

* Datadog
* Dynatrace
* New Relic
* Elastic APM

---

### 운영 시 고려사항

* Trace 샘플링 정책
* 저장 비용
* 개인정보 마스킹
* 로그 보존 정책
* Collector 이중화

---

### AI Platform Engineer 관점 핵심 포인트

현재까지 학습한 내용을 모두 연결하는 단계이다.

```text id="obsflow1"
Spring Boot
 ↓
OpenTelemetry
 ↓
Collector
 ↓
Prometheus
 ↓
Grafana
```

---

### 실무 적용 포인트

현재 경험과 직접 연결 가능

* OpenTelemetry 적용 경험
* MSA Trace 분석
* Kafka Trace 추적
* PostgreSQL 성능 분석
* Kubernetes 관측성 확보

---

### Agent 확장 방향

```text id="obsflow2"
Metric
 +
Log
 +
Trace
        ↓
Observability Agent
        ↓
장애 진단
        ↓
원인 분석
        ↓
대응 방안 제시
```

---

### 최종 목표

```text id="obsflow3"
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
Kubernetes Agent
    ↓
Database Agent
    ↓
Observability Agent
    ↓
AI Operations Platform
```
