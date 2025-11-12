import asyncio
import os
from playwright.async_api import async_playwright

async def run_hanafx(date_str: str, curCd: str, token: str):
    """Browserless.io를 통해 원격으로 하나은행 환율 페이지에서 엑셀 다운로드"""
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    async with async_playwright() as p:
        ws_url = f"wss://chrome.browserless.io?token={token}"
        browser = await p.chromium.connect_over_cdp(ws_url)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        url = "https://www.kebhana.com/easyone_foreign/exchange/exchangeRateList.do"
        await page.goto(url, timeout=60000)

        # 통화 선택
        await page.select_option("#curCd", curCd)
        await page.wait_for_timeout(1000)

        # 날짜 입력
        await page.fill("input[name='tmpInqStrDt']", date_str)
        await page.click("#searchBtn")
        await page.wait_for_timeout(3000)

        # 최초 고시회차 선택
        await page.click("label[for='pbldDvCd_1']")
        await page.wait_for_timeout(1000)

        # 엑셀 다운로드
        async with page.expect_download() as download_info:
            await page.click("a.btnTxt.excel")
        download = await download_info.value

        new_filename = f"환율조회_{curCd}_{date_str}_최초.xls"
        new_filepath = os.path.join(download_dir, new_filename)
        await download.save_as(new_filepath)

        await browser.close()
        return new_filepath
