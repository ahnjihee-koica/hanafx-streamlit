# 💱 하나은행 환율조회 자동화 (Browserless + Streamlit Cloud)

이 앱은 하나은행 환율조회 페이지에 접속해  
**Browserless.io의 원격 브라우저**를 이용해 엑셀 파일을 자동 다운로드합니다.

## ⚙️ 환경 설정
1️⃣ [browserless.io](https://www.browserless.io) 가입 및 API token 복사  
2️⃣ Streamlit Cloud → “Advanced settings → Secrets” → 다음 내용 추가:

```
BROWSERLESS_TOKEN="YOUR_API_TOKEN_HERE"
```

3️⃣ GitHub에 업로드 후 Streamlit Cloud에서 “New app” → `app.py` 선택 → Deploy

✅ 완료! 이제 직원들이 날짜/통화만 선택해 바로 엑셀을 받을 수 있습니다.
