import requests
import os

def run_hanafx(date_str: str, curCd: str):
    """하나은행 환율조회 페이지에서 '최초 고시' 기준 엑셀 다운로드"""

    base = "https://www.kebhana.com"
    session = requests.Session()

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
        ),
        "Referer": f"{base}/easyone_foreign/exchange/exchangeRateList.do",
        "Origin": base,
    }

    # 1️⃣ 메인 페이지 방문 (세션 쿠키 확보)
    main_url = f"{base}/easyone_foreign/exchange/exchangeRateList.do"
    session.get(main_url, headers=headers, timeout=10)

    # 2️⃣ 조회 요청 (내부 상태 생성)
    search_payload = {
        "curCd": curCd,
        "pbldDvCd": "1",
        "tmpInqStrDt": date_str,
        "hid_key_data": "",
        "hid_enc_data": "",
    }

    session.post(main_url, headers=headers, data=search_payload)

    # 3️⃣ 엑셀 다운로드 요청
    excel_url = f"{base}/easyone_foreign/exchange/exchangeExcel.do"
    res = session.post(excel_url, headers=headers, data=search_payload)

    # 4️⃣ 검증
    content_type = res.headers.get("Content-Type", "")
    if not content_type or "excel" not in content_type.lower():
        with open("error_debug.html", "wb") as f:
            f.write(res.content)
        raise Exception("하나은행 서버에서 유효한 엑셀 파일을 반환하지 않았습니다. (error_debug.html 참조)")

    # 5️⃣ 파일 저장
    os.makedirs("downloads", exist_ok=True)
    file_name = f"환율조회_{curCd}_{date_str}_최초.xls"
    file_path = os.path.join("downloads", file_name)

    with open(file_path, "wb") as f:
        f.write(res.content)

    return file_path
