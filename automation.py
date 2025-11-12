import asyncio
import os
from playwright.async_api import async_playwright

async def run_hanafx(date_str: str, curCd: str):
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--single-process",
                "--disable-software-rasterizer"
            ]
        )
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
        try:
            await page.click("label[for='pbldDvCd_1']")
        except:
            await page.evaluate("""
                var radio = document.getElementById('pbldDvCd_1');
                radio.checked = true;
                var event = new Event('change', { bubbles: true });
                radio.dispatchEvent(event);
            """)
        await page.wait_for_timeout(2000)

        # 엑셀 다운로드
        async with page.expect_download() as download_info:
            await page.click("a.btnTxt.excel")
        download = await download_info.value

        new_filename = f"환율조회_{date_str}_{curCd}_최초.xls"
        new_filepath = os.path.join(download_dir, new_filename)
        await download.save_as(new_filepath)

        await browser.close()
        return new_filepath
