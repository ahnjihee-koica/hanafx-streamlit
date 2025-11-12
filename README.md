# 💱 하나은행 환율조회 자동화 (Lite Fixed3)

이 버전은 **하나은행 서버의 보안 정책(Referer, Origin, Session 검증)** 을 완벽히 반영했습니다.

## 기능
- 날짜와 통화를 선택하면 자동으로 “최초 고시” 기준 환율 엑셀 파일을 다운로드합니다.
- 서버 오류 시, `error_debug.html` 파일이 자동 저장되어 원인 확인 가능

## 구성
| 파일 | 설명 |
|------|------|
| app.py | Streamlit UI |
| automation.py | 서버 세션 기반 requests 로직 |
| requirements.txt | Streamlit Cloud 의존성 |
| README.md | 사용 안내 |

## 배포 방법
1️⃣ GitHub에 이 파일들을 업로드  
2️⃣ [Streamlit Cloud](https://share.streamlit.io) 접속  
3️⃣ “New app” → `app.py` 선택  
4️⃣ ✅ 바로 배포 (추가 설정 불필요)
