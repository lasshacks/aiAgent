# 05_Kubernetes_Agent

## 목표

Kubernetes 환경을 AI Agent와 연계하여 클러스터 상태 조회, 로그 분석, 장애 진단 및 운영 자동화를 수행할 수 있는 Kubernetes Agent를 구축한다.

최종 목표

* Kubernetes Agent 구축
* Kubernetes API 활용
* Pod 상태 조회 자동화
* 로그 분석 자동화
* 장애 진단 자동화
* MCP 기반 Kubernetes Tool 구축

---

## 학습 내용

### Kubernetes Agent란?

Kubernetes 운영 업무를 수행하는 AI Agent이다.

예시

```text id="k8sagent1"
사용자
 ↓
현재 장애 있는 Pod 알려줘
 ↓
Agent
 ↓
Kubernetes 조회
 ↓
결과 분석
 ↓
응답
```

---

### 왜 Kubernetes Agent가 필요한가?

기존 운영 방식

```text id="oldk81"
운영자
 ↓
kubectl 입력
 ↓
로그 확인
 ↓
원인 분석
 ↓
조치
```

---

Agent 방식

```text id="newk81"
운영자
 ↓
Agent
 ↓
Kubernetes API
 ↓
로그 분석
 ↓
원인 진단
 ↓
응답
```

---

### Kubernetes Agent 활용 사례

#### Pod 상태 조회

```text id="podcase1"
현재 장애 Pod 알려줘
```

---

#### 로그 분석

```text id="logcase1"
payment-service 오류 원인 알려줘
```

---

#### 리소스 분석

```text id="resource1"
CPU 사용률 높은 Pod 알려줘
```

---

#### 장애 원인 분석

```text id="trouble1"
CrashLoopBackOff 원인 분석해줘
```

---

### Kubernetes Agent 아키텍처

```text id="k8sarch1"
사용자
    ↓
Agent
    ↓
MCP
    ↓
Kubernetes Tool
    ↓
Kubernetes API
    ↓
Cluster
```

---

### Kubernetes 운영 자동화 범위

| 기능      | 자동화 가능 |
| ------- | ------ |
| Pod 조회  | O      |
| Node 조회 | O      |
| 로그 조회   | O      |
| 이벤트 조회  | O      |
| 장애 진단   | O      |
| 배포 수행   | O      |
| 스케일링    | O      |

---

## 실습 절차

### 1. Kubernetes 환경 준비

선택

* Minikube
* Kind
* K3s
* 실제 Kubernetes Cluster

---

### 2. Kubectl 설치 확인

```bash id="kubectl1"
kubectl version --client
```

---

### 3. 클러스터 연결 확인

```bash id="kubectl2"
kubectl get nodes
```

정상 결과 확인

---

### 4. Python Kubernetes SDK 설치

```bash id="k8spkg1"
pip install kubernetes
```

---

### 5. Kubernetes API 호출

예제

```python id="k8scode1"
from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

for pod in pods.items:
    print(pod.metadata.name)
```

---

### 6. Pod 조회 Tool 생성

예제

```python id="tool51"
def get_pods():
    pass
```

Agent 호출

```text id="tool52"
Pod 목록 보여줘
```

---

### 7. 로그 조회 Tool 생성

예제

```python id="tool53"
def get_logs(pod_name):
    pass
```

Agent 호출

```text id="tool54"
payment-service 로그 보여줘
```

---

### 8. 장애 진단 Tool 생성

예제

```python id="tool55"
def analyze_pod():
    pass
```

분석 대상

* CrashLoopBackOff
* OOMKilled
* ImagePullBackOff
* Pending

---

### 9. MCP 연동

구성

```text id="mcpk81"
Agent
 ↓
MCP
 ↓
Kubernetes Tool
 ↓
Cluster
```

---

### 10. Kubernetes Agent 구축

최종 기능

* Pod 조회
* Node 조회
* 로그 조회
* 이벤트 조회
* 장애 진단

---

## TODO

### 환경 구축

* [ ] Kubernetes Cluster 준비
* [ ] Kubectl 설치
* [ ] Python SDK 설치

### 실습

* [ ] Pod 조회 Tool
* [ ] Node 조회 Tool
* [ ] 로그 조회 Tool
* [ ] 이벤트 조회 Tool
* [ ] 장애 진단 Tool

### Agent

* [ ] MCP 연동
* [ ] Kubernetes Agent 구축

### 문서화

* [ ] GitHub 업로드
* [ ] 블로그 작성

---

## 검증 방법

### 클러스터 검증

```bash id="verify51"
kubectl get nodes
```

---

### Pod 조회 검증

```bash id="verify52"
kubectl get pods -A
```

Agent 결과와 비교

---

### 로그 조회 검증

```bash id="verify53"
kubectl logs POD_NAME
```

Agent 결과와 비교

---

### 장애 진단 검증

테스트 케이스

* CrashLoopBackOff
* OOMKilled
* Pending

분석 결과 확인

---

### 재현 검증

다른 클러스터에서 동일 기능 수행

---

## 결과물

### 코드

* Kubernetes Tool
* MCP Tool
* Kubernetes Agent

### 문서

* 구축 가이드
* 운영 가이드
* 장애 분석 가이드

### 다이어그램

* Kubernetes Agent Architecture
* MCP Integration Architecture

---

## 회고

### 배운 점

* Kubernetes API 이해
* Kubernetes 운영 자동화 이해
* Agent 활용 방법 이해

### 개선점

* 진단 정확도 향상 필요
* 이벤트 분석 강화 필요
* 자동 조치 기능 추가 필요

### 다음 단계

* Database Agent
* Observability Agent
* Multi-Agent

---

## GitHub 업로드 기준

### 필수

* README.md
* 설치 방법
* 실행 방법

### 권장

* 테스트 환경 정보
* Kubernetes 버전 정보
* MCP 설정 정보

### 스크린샷

* Pod 조회 결과
* 로그 조회 결과
* 장애 분석 결과

---

## 블로그 작성 포인트

### 문제 정의

왜 Kubernetes Agent가 필요한가?

운영자가 반복적으로 수행하는 조회 및 장애 분석 작업을 자동화하기 위함이다.

---

### 구현 방법

* Kubernetes API 연동
* Tool 구현
* MCP 연동
* Agent 구축

---

### 트러블슈팅

예상 사례

* kubeconfig 오류
* 권한 문제
* API 연결 실패
* 로그 조회 실패

---

### 결과

* Kubernetes Agent 구축
* 장애 진단 자동화
* 운영 효율 향상

---

## 면접 포인트

### Kubernetes Agent란?

Kubernetes 운영 업무를 수행하는 AI Agent이다.

---

### Kubernetes Agent가 수행할 수 있는 작업은?

* Pod 조회
* Node 조회
* 로그 조회
* 이벤트 조회
* 장애 분석

---

### Kubernetes API를 사용하는 이유는?

kubectl 명령어 대신 프로그래밍 방식으로 클러스터 정보를 조회할 수 있기 때문이다.

---

### MCP와 Kubernetes를 왜 연결하는가?

Agent가 Kubernetes를 Tool 형태로 사용할 수 있도록 하기 위함이다.

---

### CrashLoopBackOff란?

컨테이너가 반복적으로 종료되고 재시작되는 상태이다.

주요 원인

* 애플리케이션 오류
* 설정 오류
* 환경 변수 누락

---

### OOMKilled란?

메모리 부족으로 인해 컨테이너가 종료된 상태이다.

---

### 대안은 무엇인가?

* Kubectl Plugin
* Lens
* K9s
* Rancher

하지만 이들은 조회 도구이며 Agent 기반 자동화와는 목적이 다르다.

---

### 운영 시 고려사항

* RBAC 권한 관리
* API 접근 제어
* 로그 보안
* Agent 오작동 방지
* 자동 조치 범위 제한

---

### AI Platform Engineer 관점 핵심 포인트

현재 보유한 Kubernetes 운영 경험을 AI Agent로 자동화하는 단계이다.

기존 방식

```text id="compare51"
운영자
 ↓
kubectl
 ↓
분석
```

AI 방식

```text id="compare52"
운영자
 ↓
Agent
 ↓
Kubernetes API
 ↓
분석
 ↓
응답
```

---

### 실무 적용 포인트

현재 경험과 직접 연결 가능

* Pod 장애 분석
* Deployment 상태 확인
* Kafka 상태 확인
* OpenTelemetry Collector 상태 확인
* Prometheus 상태 확인

즉, Kubernetes 운영 업무를 자연어 기반으로 수행할 수 있도록 만드는 실습이다.

---

### 최종 목표

```text id="k8sflow1"
Local LLM
    ↓
Agent
    ↓
MCP
    ↓
Kubernetes Agent
    ↓
Observability
    ↓
AI Operations Platform
```
