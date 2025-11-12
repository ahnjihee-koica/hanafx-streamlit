import requests
import os

def run_hanafx(date_str: str, curCd: str):
    """하나은행 환율조회 페이지에서 최초고시 기준 엑셀 다운로드"""
    url = "https://www.kebhana.com/easyone_foreign/exchange/exchangeExcel.do"
    params = {
        "curCd": curCd,
        "pbldDvCd": "1",  # 최초고시
        "tmpInqStrDt": date_str
    }

    res = requests.post(url, params)
    if res.status_code != 200:
        raise Exception("엑셀 파일을 불러오지 못했습니다.")

    os.makedirs("downloads", exist_ok=True)
    file_name = f"환율조회_{curCd}_{date_str}_최초.xls"
    file_path = os.path.join("downloads", file_name)

    with open(file_path, "wb") as f:
        f.write(res.content)

    return file_path
