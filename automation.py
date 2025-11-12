import requests
import os

def run_hanafx(date_str: str, curCd: str):
    """
    하나은행 환율조회 페이지에서 '최초고시' 기준 엑셀 다운로드
    """

    session = requests.Session()

    # 1️⃣ 메인 페이지 먼저 방문 (세션 생성용)
    main_url = "https://www.kebhana.com/easyone_foreign/exchange/exchangeRateList.do"
    session.get(main_url, timeout=10)

    # 2️⃣ 엑셀 다운로드 요청
    excel_url = "https://www.kebhana.com/easyone_foreign/exchange/exchangeExcel.do"
    payload = {
        "curCd": curCd,
        "pbldDvCd": "1",  # 최초고시
        "tmpInqStrDt": date_str,
    }

    headers = {
        "Referer": main_url,
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
        ),
    }

    res = session.post(excel_url, data=payload, headers=headers)
    if "죄송합니다" in res.text or res.status_code != 200:
        raise Exception("하나은행 서버에서 유효한 엑셀 파일을 반환하지 않았습니다.")

    # 3️⃣ 파일 저장
    os.makedirs("downloads", exist_ok=True)
    file_name = f"환율조회_{curCd}_{date_str}_최초.xls"
    file_path = os.path.join("downloads", file_name)

    with open(file_path, "wb") as f:
        f.write(res.content)

    return file_path
