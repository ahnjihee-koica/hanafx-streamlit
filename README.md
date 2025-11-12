# 💱 하나은행 환율조회 자동화 (Streamlit Cloud Ready)

이 앱은 하나은행 환율조회 페이지에서  
날짜와 통화를 선택하면 **자동으로 “최초 고시” 기준 환율 엑셀**을 다운로드합니다.

## ✅ Streamlit Cloud 호환 버전

- Playwright 자동설치 (pip & chromium)
- Headless Chrome 실행 시 sandbox, GPU, SHM 제한 자동 회피
- Streamlit Cloud에서 별도 설정 없이 작동

## 📦 파일 구성

| 파일 | 설명 |
|------|------|
| `app.py` | Streamlit 앱 (자동설치 포함) |
| `automation.py` | Playwright 자동화 로직 |
| `requirements.txt` | Python 의존성 |
| `apt.txt` | Cloud에서 필요한 시스템 패키지 |
| `README.md` | 사용 설명서 |

## 🚀 배포 방법

1️⃣ GitHub 저장소 생성  
2️⃣ 이 파일들 업로드  
3️⃣ Streamlit Cloud에서 새 앱 배포 (`app.py`) 선택  
4️⃣ 별도 pre-run script 불필요  
5️⃣ 자동으로 playwright + chromium 설치 후 정상 실행

