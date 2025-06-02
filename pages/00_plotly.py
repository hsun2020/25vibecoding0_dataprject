import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="서울시 인구 시각화")

st.title("서울특별시 연령별 인구 시각화 (2025년 5월)")

# CSV 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (남녀 구분 포함된 파일)", type="csv")

if uploaded_file:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file, encoding='cp949')
    df_seoul = df[df['행정구역'].str.contains("서울특별시")].copy()

    # 연령별 남녀 컬럼 추출
    male_cols = [c for c in df_seoul.columns if '남_' in c and '세' in c]
    female_cols = [c for c in df_seoul.columns if '여_' in c and '세' in c]
    ages = [col.split('_')[-1].replace('세', '').replace('100세 이상', '100+') for col in male_cols]

    # 숫자 정제
    male_vals = df_seoul[male_cols].iloc[0].fillna(0).astype(str).str.replace(",", "").astype(int) * -1
    female_vals = df_seoul[female_cols].iloc[0].fillna(0).astype(str).str.replace(",", "").astype(int)
    total_vals = male_vals.abs() + female_vals

    # 인구 피라미드
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(y=ages, x=male_vals, name="남성", orientation="h", marker_color="steelblue"))
    fig1.add_trace(go.Bar(y=ages, x=female_vals, name="여성", orientation="h", marker_color="lightcoral"))
    fig1.update_layout(
        title="인구 피라미드",
        barmode="relative",
        xaxis=dict(title="인구수", tickvals=[-50000, -25000, 0, 25000, 50000],
                   ticktext=["50,000", "25,000", "0", "25,000", "50,000"]),
        yaxis=dict(title="연령"),
        height=700
    )

    # 전체 인구 막대그래프
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=ages, y=total_vals, marker_color="mediumseagreen"))
    fig2.update_layout(
        title="연령별 전체 인구",
        xaxis=dict(title="연령"),
        yaxis=dict(title="인구수"),
        height=500
    )

    # 두 그래프 나란히 배치
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("먼저 CSV 파일을 업로드하세요.")
