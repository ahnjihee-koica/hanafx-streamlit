import os
os.system("pip install playwright && playwright install chromium")

import streamlit as st
import asyncio
import datetime
from automation import run_hanafx

st.set_page_config(page_title="하나은행 환율조회 자동화", page_icon="💱")
st.title("💱 하나은행 환율조회 자동화")

st.markdown("""
하나은행 환율조회 페이지에 접속해  
날짜와 통화를 선택하면 **최초 고시 기준 환율 엑셀 파일**을 자동으로 내려받습니다.
""")

currency = st.selectbox(
    "통화 선택",
    ["USD", "EUR", "JPY", "CNY", "GBP", "AUD", "UGX"]
)
date = st.date_input("조회 날짜", datetime.date.today())

if st.button("조회 및 엑셀 다운로드"):
    with st.spinner("조회 중입니다... (약 10~15초 소요)"):
        file_path = asyncio.run(run_hanafx(date.strftime("%Y-%m-%d"), currency))
        if file_path and os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(
                    label="📊 엑셀 다운로드",
                    data=f,
                    file_name=os.path.basename(file_path),
                    mime="application/vnd.ms-excel"
                )
            st.success("✅ 완료되었습니다! 파일을 다운로드하세요.")
        else:
            st.error("❌ 엑셀 다운로드 실패. 다시 시도해주세요.")
