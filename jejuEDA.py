import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_jejuEDA_app() :
    # 앱에 사용된 데이터 불러오기
    tourism_df = pd.read_csv('jjtourism_2022.csv',index_col=0)
    restaurant_df = pd.read_csv('jjrestaurant_2022.csv',index_col=0)

    # 사용한 데이터 프레임
    st.subheader('사용한 데이터 프레임 확인 :open_file_folder:')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df)
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df)
    st.subheader('')

    # 사용한 데이터 프레임 기본 통계
    st.subheader('기본 통계 데이터 :clipboard:')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df.describe())
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df.describe())
    st.subheader('')

     # 사용한 데이터 프레임별로 최대, 최소값 확인할 수 있게 셀렉트박스 사용
    st.subheader('최대 / 최소 데이터 확인하기 :bookmark_tabs:')
    tourism_column_list = tourism_df.columns[3:]
    seleced_column = st.selectbox('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터 컬럼을 선택하세요', tourism_column_list)
    st.write('최대값')
    st.dataframe(tourism_df.loc[tourism_df[seleced_column] == tourism_df[seleced_column].max()])
    st.write('최소값')
    st.dataframe(tourism_df.loc[tourism_df[seleced_column] == tourism_df[seleced_column].min()])

    restaurant_df_column_list = restaurant_df.columns[6:]
    seleced_column = st.selectbox('신한카드 제주도 내 음식점별 매출 변화량 데이터 컬럼을 선택하세요', restaurant_df_column_list)
    st.write('최대값')
    st.dataframe(restaurant_df.loc[restaurant_df[seleced_column] == restaurant_df[seleced_column].max()])
    st.write('최소값')
    st.dataframe(restaurant_df.loc[restaurant_df[seleced_column] == restaurant_df[seleced_column].min()])
    st.subheader('')
    
    # 사용한 데이터의 상관관계를 보여주는 데이터 프레임
    st.subheader('상관 관계 분석 :mag:')
    st.write('제주관광공사 비짓제주 홈페이지 내 관광지 검색 로그데이터')
    st.dataframe(tourism_df.corr())
    st.write('신한카드 제주도 내 음식점별 매출 변화량 데이터')
    st.dataframe(restaurant_df.corr())

    # 사용한 데이터 URL
    st.write('')
    st.write('사용한 데이터 주소 ')
    st.info('https://www.bigdata-culture.kr/bigdata/user/data_market/agency/detail.do?id=ijto_org')
