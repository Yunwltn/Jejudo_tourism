import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_tourism_app() :
    df = pd.read_csv('jjtourism_2022.csv',index_col=0)
    image_url = 'https://cdn.pixabay.com/photo/2016/11/18/07/46/seopjikoji-1833560_960_720.jpg'

    st.title('제주도 관광지 데이터')
    st.write('최근 3개월 조회수 데이터로 제주도 관광지의 순위 데이터를 보여주는 앱입니다')
    st.info('2022년 8, 9, 10월달의 제주도 관광지 조회수 파일을 사용했습니다')
    st.image(image_url, use_column_width=True)
    df = df.sort_values('관광지명', ascending=False)
    st.dataframe(df[['분류','관광지명','주소']])
    st.subheader('')

    st.subheader('3개월간 조회수가 가장 높은 관광지 TOP10')
    df = df.sort_values('전체조회수', ascending=False)
    df_top10 = df.head(10)
    st.dataframe(df_top10[['분류','관광지명','주소','전체조회수']])
    fig1 = px.bar(df_top10, x= '관광지명', y=['8월','9월','10월','전체조회수'], barmode='group', height=600)
    st.plotly_chart(fig1)