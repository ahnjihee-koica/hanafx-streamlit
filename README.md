# 💱 하나은행 환율조회 자동화 (Lite)

이 버전은 **Playwright 없이 작동하는 Streamlit Cloud 완전 호환 버전**입니다.

## 기능
- 날짜와 통화를 선택하면 자동으로 “최초 고시” 기준 환율 엑셀 파일을 다운로드합니다.
- 실행 환경: Streamlit Cloud, 로컬

## 구성
| 파일 | 설명 |
|------|------|
| app.py | Streamlit UI |
| automation.py | requests 기반 자동화 로직 |
| requirements.txt | Streamlit Cloud 자동 설치용 |
| README.md | 사용 안내 |

## 배포 방법
1️⃣ GitHub에 이 파일들을 업로드  
2️⃣ [Streamlit Cloud](https://share.streamlit.io) 접속  
3️⃣ “New app” → `app.py` 선택  
4️⃣ ✅ 바로 배포 (추가 설정 불필요)
