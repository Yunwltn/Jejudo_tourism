import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_tourism_app() :
    df = pd.read_csv('jjtourism_2022.csv',index_col=0)
    image_url = 'https://cdn.pixabay.com/photo/2016/11/18/07/46/seopjikoji-1833560_960_720.jpg'

    # 페이지 설명과 이미지, 사용한 데이터 프레임 삽입
    st.title('제주도 관광지 데이터')
    st.write('최근 3개월 조회수 데이터로 제주도 관광지의 순위 데이터를 보여드립니다')
    st.info('2022년 8, 9, 10월달의 제주도 관광지 조회수 파일을 사용했습니다')
    st.image(image_url, use_column_width=True)
    df = df.sort_values('관광지명', ascending=False)
    st.dataframe(df[['분류','관광지명','주소']])
    st.subheader('')

    # 전체 조회수로 정렬해서 데이터 프레임과 차트 보여주기
    st.subheader('3개월간 조회수가 가장 높은 관광지 종합 TOP10')
    df = df.sort_values('전체조회수', ascending=False)
    df_top10 = df.head(10)

    fig1 = px.bar(df_top10, x= '관광지명', y=['8월','9월','10월','전체조회수'], barmode='group', height=600)
    st.plotly_chart(fig1)

    st.dataframe(df_top10[['분류','관광지명','주소','전체조회수']])
    st.subheader('')

    # 셀렉트박스로 월별 선택해서 차트로 조회수 순위로 10개 표시
    st.subheader('월별 조회수가 많은 관광지 종합 TOP10')

    my_choice = st.selectbox('조회수 데이터를 보고싶은 달을 선택해주세요', ['8월', '9월', '10월'])

    if my_choice == '8월' :
        df_8 = df.loc[ df['8월'] == df['8월'].max() ]
        st.info(my_choice + '의 조회수가 가장 많은 관광지는 ' + df_8['관광지명'].tolist()[0] + '입니다')
        
        df = df.sort_values('8월', ascending=False)
        df_8_top10 = df.head(10)
        fig2 = px.bar(df_8_top10, x= '관광지명', y='8월', height=600)
        st.plotly_chart(fig2)
        st.dataframe(df_8_top10[['분류','관광지명','주소','8월']])

    elif my_choice == '9월' :
        df_8 = df.loc[ df['9월'] == df['9월'].max() ]
        st.info(my_choice + '의 조회수가 가장 많은 관광지는 ' + df_8['관광지명'].tolist()[0] + '입니다')
        
        df = df.sort_values('9월', ascending=False)
        df_9_top10 = df.head(10)
        fig3 = px.bar(df_9_top10, x= '관광지명', y='9월', height=600)
        st.plotly_chart(fig3)
        st.dataframe(df_9_top10[['분류','관광지명','주소','9월']])

    elif my_choice == '10월' :
        df_8 = df.loc[ df['10월'] == df['10월'].max() ]
        st.info(my_choice + '의 조회수가 가장 많은 관광지는 ' + df_8['관광지명'].tolist()[0] + '입니다')
        
        df = df.sort_values('10월', ascending=False)
        df_10_top10 = df.head(10)
        fig4 = px.bar(df_10_top10, x= '관광지명', y='10월', height=600)
        st.plotly_chart(fig4)
        st.dataframe(df_10_top10[['분류','관광지명','주소','10월']])
        st.subheader('')

    # 셀렉트박스로 분류 선택하면 해당 분류의 데이터 프레임 보여주기
    st.subheader('관광지 분류별로 조회하기')
    division_list = df['분류'].unique().tolist()
    my_choice = st.selectbox('분류를 선택하세요', division_list)
    df = df.sort_values('전체조회수', ascending=False)

    choice_df = df.loc[ df['분류'] == my_choice ]

    # 선택한 분류의 1순위
    choice_df_max = choice_df.loc[ choice_df['전체조회수'] == choice_df['전체조회수'].max() ]
    choice_df_max = choice_df_max['관광지명'].tolist()[0]

    st.info(my_choice + '의 조회수 1위는 ' + choice_df_max + ' 입니다')
    st.dataframe(choice_df[['분류','관광지명','주소','전체조회수','평균조회수']])

    # 체크박스 클릭시 해당분류의 조회수 높은 순서대로 관광지를 차트로 나타내기
    if st.checkbox('해당 분류 관광지 차트로 보기') :
        choice_count = st.slider('차트로 확인할 갯수를 선택하세요', 2, 30, value=15)
        fig5 = px.bar(choice_df.head(choice_count), x='관광지명', y='전체조회수', height=600, text='전체조회수')
        fig5.update_traces(textfont_size=14,textposition='auto')
        st.plotly_chart(fig5)

        