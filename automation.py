import requests
import os

def run_hanafx(date_str: str, curCd: str):
    """하나은행 환율조회 페이지에서 '최초고시' 기준 엑셀 다운로드"""

    session = requests.Session()
    base = "https://www.kebhana.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
    }

    # 1️⃣ 메인 페이지 접속 (세션 쿠키 확보)
    session.get(f"{base}/easyone_foreign/exchange/exchangeRateList.do", headers=headers)

    # 2️⃣ 실제 조회 요청 (이 단계가 있어야 서버가 결과 context 생성)
    data = {
        "curCd": curCd,
        "pbldDvCd": "1",  # 최초고시
        "tmpInqStrDt": date_str
    }
    session.post(f"{base}/easyone_foreign/exchange/exchangeRateList.do", data=data, headers=headers)

    # 3️⃣ 엑셀 다운로드 요청 (이제 context가 존재함)
    excel_url = f"{base}/easyone_foreign/exchange/exchangeExcel.do"
    res = session.post(excel_url, data=data, headers=headers)

    if res.status_code != 200 or res.headers.get("Content-Type", "").find("excel") == -1:
        # 서버가 엑셀이 아니라 HTML 오류 페이지를 돌려줄 때
        raise Exception("하나은행 서버에서 유효한 엑셀 파일을 반환하지 않았습니다.")

    # 4️⃣ 파일 저장
    os.makedirs("downloads", exist_ok=True)
    file_name = f"환율조회_{curCd}_{date_str}_최초.xls"
    file_path = os.path.join("downloads", file_name)

    with open(file_path, "wb") as f:
        f.write(res.content)

    return file_path
