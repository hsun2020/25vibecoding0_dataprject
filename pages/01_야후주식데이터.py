import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Global Top 10 Stocks", layout="wide")

st.title("🌍 글로벌 시가총액 TOP 10 기업 - 최근 1년 주가 변화")

# 시가총액 기준 글로벌 TOP 10 기업 티커 목록 (2025년 기준 추정)
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

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 가져오기
@st.cache_data
def get_data():
    df_list = []
    for name, ticker in tickers.items():
        data = yf.download(ticker, start=start_date, end=end_date)
        data["Company"] = name
        data["Date"] = data.index
        df_list.append(data[["Date", "Close", "Company"]])
    return pd.concat(df_list)

df = get_data()

# Plotly로 시각화
fig = px.line(df, x="Date", y="Close", color="Company",
              title="📈 글로벌 TOP 10 기업의 최근 1년 주가 변화",
              labels={"Close": "Stock Price (USD)", "Date": "Date"})

fig.update_layout(hovermode="x unified", height=600)

st.plotly_chart(fig, use_container_width=True)
