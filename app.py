import streamlit as st
import datetime
import os
from automation import run_hanafx

st.set_page_config(page_title="하나은행 환율조회 자동화 (Lite)", page_icon="💱")
st.title("💱 하나은행 환율조회 자동화 (Lite)")

st.markdown("""
하나은행 환율조회 페이지에서  
**날짜와 통화를 선택**하면  
자동으로 “최초 고시 기준” 환율 엑셀을 다운로드합니다.
""")

currency = st.selectbox(
    "통화 선택",
    ["USD", "EUR", "JPY", "CNY", "GBP", "AUD", "UGX"]
)
date = st.date_input("조회 날짜", datetime.date.today())

if st.button("조회 및 엑셀 다운로드"):
    with st.spinner("조회 중입니다... (1~2초 소요)"):
        try:
            file_path = run_hanafx(date.strftime("%Y-%m-%d"), currency)
            with open(file_path, "rb") as f:
                st.download_button(
                    label="📊 엑셀 다운로드",
                    data=f,
                    file_name=os.path.basename(file_path),
                    mime="application/vnd.ms-excel"
                )
            st.success("✅ 완료되었습니다! 파일을 다운로드하세요.")
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
