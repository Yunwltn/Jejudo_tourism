import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_jejuEDA_app() :
    st.title('Welcome to JeJu-Do! EDA')
    tourism_df = pd.read_csv('jjtourism_2022.csv',index_col=0)
    restaurant_df = pd.read_csv('jjrestaurant_2022.csv',index_col=0)

    st.subheader('사용한 데이터 프레임 확인')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df)
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df)
    st.subheader('')

    st.subheader('기본 통계 데이터')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df.describe())
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df.describe())
    st.subheader('')

    st.subheader('최대 / 최소 데이터 확인하기')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df.loc[tourism_df['전체조회수'] == tourism_df['전체조회수'].max()])
    st.dataframe(tourism_df.loc[tourism_df['전체조회수'] == tourism_df['전체조회수'].min()])
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df.loc[restaurant_df['3개월전체매출수'] == restaurant_df['3개월전체매출수'].max()])
    st.dataframe(restaurant_df.loc[restaurant_df['3개월전체매출수'] == restaurant_df['3개월전체매출수'].min()])
    st.subheader('')

    st.subheader('상관 관계 분석')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df.corr())
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df.corr())
