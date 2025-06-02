import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Global Top 10 Stocks", layout="wide")

st.title("🌍 글로벌 시가총액 TOP 10 기업 - 최근 1년 주가 변화")

tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "Eli Lilly": "LLY",
    "TSMC": "TSM"
}

end_date = datetime.today()
start_date = end_date - timedelta(days=365)

@st.cache_data
def get_data():
    df_list = []
    for name, ticker in tickers.items():
        t
