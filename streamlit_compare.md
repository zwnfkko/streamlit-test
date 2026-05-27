# Streamlit Cloud vs GitHub Pages (stlite) 배포 비교

## 한 줄 요약

| | Streamlit Cloud | GitHub Pages + stlite |
|---|---|---|
| 실행 위치 | **서버** (Streamlit 서버) | **브라우저** (WebAssembly) |
| 현재 방식 | ❌ 미사용 | ✅ 사용 중 |

---

## 1. 아키텍처

### Streamlit Cloud
```
사용자 브라우저  ←──HTTP──→  Streamlit Cloud 서버  ←──→  Python 런타임
                              (Anthropic 인프라)         (서버에서 실행)
```
- Python이 **클라우드 서버**에서 실행됨
- 브라우저는 렌더링 결과만 수신 (WebSocket 통신)

### GitHub Pages + stlite (현재 방식)
```
사용자 브라우저  ←──HTTP──→  GitHub CDN (정적 파일)
       │
       └──→  Pyodide (WebAssembly)로 Python을 브라우저 내에서 직접 실행
```
- Python이 **사용자 브라우저** 안에서 실행됨
- 서버가 전혀 없음 (100% 정적)

---

## 2. 항목별 상세 비교

| 항목 | Streamlit Cloud | GitHub Pages + stlite |
|---|---|---|
| **실행 환경** | 클라우드 서버 (Python) | 브라우저 내 WebAssembly (Pyodide) |
| **서버 비용** | 무료 tier 존재 (제한 있음) | **무료** (GitHub Pages) |
| **초기 로딩** | 빠름 (1~3초) | 느림 (10~30초, Pyodide 다운로드) |
| **이후 로딩** | 빠름 | 빠름 (캐시됨) |
| **Python 라이브러리** | pip 설치 가능 (거의 모두) | Pyodide 지원 패키지만 가능 |
| **파일 I/O** | 서버 파일시스템 접근 가능 | 불가 (브라우저 샌드박스) |
| **DB 연결** | 가능 (PostgreSQL, MySQL 등) | 불가 (네트워크 제한) |
| **API 호출** | 가능 | CORS 정책에 따라 제한 |
| **보안** | 서버 측 처리 (안전) | 코드가 브라우저에 노출됨 |
| **GitHub 연동** | 자동 배포 (push 시 자동) | 수동 또는 Actions 구성 필요 |
| **커스텀 도메인** | 지원 | 지원 |
| **앱 절전 모드** | 비활성 시 슬립 (무료 tier) | 없음 (정적 파일) |
| **동시 접속 제한** | 무료 tier 제한 있음 | **제한 없음** |
| **배포 방법** | share.streamlit.io UI | GitHub API / git push |

---

## 3. 지원 라이브러리 차이

### Streamlit Cloud → 제한 없음
```
pandas, numpy, scikit-learn, tensorflow, pytorch,
sqlalchemy, requests, selenium, playwright, ...
```

### GitHub Pages + stlite → Pyodide 지원 패키지만 가능
```
✅ pandas, numpy, matplotlib, plotly, scikit-learn, pillow
✅ 현재 앱 (streamlit만 사용) → 문제 없음
❌ sqlalchemy, psycopg2, selenium, torch (대용량 패키지)
```

---

## 4. 언제 어떤 걸 써야 할까?

### GitHub Pages + stlite가 유리한 경우
- 포트폴리오, 자기소개 등 **정적 콘텐츠** 위주
- DB / 외부 API 연결이 **없는** 앱
- **비용 0원**으로 무제한 트래픽이 필요할 때
- 서버 관리 없이 빠르게 배포하고 싶을 때

### Streamlit Cloud가 유리한 경우
- DB 연결, 파일 저장, 외부 API 호출이 필요할 때
- 무거운 ML 라이브러리 (torch, tensorflow) 사용할 때
- 팀 협업 / 사내 대시보드 등 **실서비스** 수준의 앱
- 빠른 초기 로딩이 중요할 때

---

## 5. 현재 프로젝트 평가

현재 `이지원 자기소개` 앱은 순수 Streamlit UI만 사용하므로
**GitHub Pages + stlite 방식이 최적**입니다.

```
✅ 서버 비용 없음
✅ 무제한 트래픽
✅ https://zwnfkko.github.io/streamlit-test/ 으로 즉시 접속
⚠️  첫 로딩 10~20초 (Pyodide 초기화) — 자기소개 페이지 특성상 허용 범위
```

만약 향후 **DB 연동, 로그인, 실시간 데이터** 등이 추가된다면
그때 Streamlit Cloud 또는 별도 서버로 전환을 권장합니다.
