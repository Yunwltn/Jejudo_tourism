import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_restaurant_app() :
    df = pd.read_csv('jjrestaurant_2022.csv',index_col=0)
    image_url = 'https://static.wixstatic.com/media/a1f07c_7d16726d07c7480fbd1ff46dc614d51f~mv2.jpg/v1/fill/w_640,h_394,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/a1f07c_7d16726d07c7480fbd1ff46dc614d51f~mv2.jpg'
    
    # 페이지 설명과 이미지, 사용한 데이터 프레임 삽입
    st.title('제주도 음식점 데이터')
    st.write('최근 3개월 카드매출 데이터로 제주도 내 음식점 순위 데이터를 보여드립니다')
    st.info('2022년 8, 9, 10월달의 신한카드 제주도 내 음식점별 매출 파일을 사용했습니다')
    st.image(image_url, use_column_width=True)
    st.dataframe(df)
    st.subheader('')

    # 8, 9, 10월의 전체 매출수 순서대로 차트와 데이터 프레임 보여주기
    st.subheader('3개월간 매출이 가장 많은 음식점 TOP20')
    df = df.sort_values('3개월전체매출수', ascending=False)
    df_top20 = df.head(20)

    fig1 = px.bar(df_top20, y= '음식점명', x='3개월전체매출수', height=600)
    # 정렬
    fig1.update_layout(yaxis = dict(autorange='reversed'))
    st.plotly_chart(fig1)

    st.dataframe(df_top20[['음식점명','시군구명','행정동명','지역명','중분류','소분류','3개월전체매출수']])
    st.subheader('')

    # 라디오 버튼으로 현지인/외지인 소비별 매출 많은 음식점 데이터 차트와 데이터 프레임 보여주기
    st.subheader('현지인/외지인 소비가 가장 많은 음식점 TOP10')
    status = st.radio('선택하세요', ['현지인 소비가 많은 음식점','외지인 소비가 많은 음식점'])

    if status == '현지인 소비가 많은 음식점' :
        df = df.sort_values('현지인매출금액비율', ascending=False)
        df_top10 = df.head(10)
        fig2 = px.bar(df_top10, x= '음식점명', y='현지인매출금액비율', height=600)
        st.plotly_chart(fig2)
        st.dataframe(df[['음식점명','시군구명','행정동명','지역명','중분류','소분류','현지인매출수비율','3개월전체매출수']].head(20))

    elif status == '외지인 소비가 많은 음식점' :
        df = df.sort_values('외지인매출금액비율', ascending=False)
        df_top10 = df.head(10)
        fig3 = px.bar(df_top10, x= '음식점명', y='외지인매출금액비율', height=600)
        st.plotly_chart(fig3)
        st.dataframe(df[['음식점명','시군구명','행정동명','지역명','중분류','소분류','외지인매출수비율','3개월전체매출수']].head(20))
    st.subheader('')
    
    # 중분류별 소비순위 데이터 프레임 보여주기
    st.subheader('음식점 분류별 소비순위')

    df_list1 = df['중분류'].unique()
    df_list1 = sorted(df_list1)
    my_choice1 = st.selectbox('음식점 중분류를 선택해주세요', df_list1)

    choice_df = df.loc[ (df['중분류'] == my_choice1) ]
    choice_df = choice_df.sort_values('3개월전체매출수',ascending=False)
    choice_df_max = choice_df.loc[choice_df['3개월전체매출수'] == choice_df['3개월전체매출수'].max()]
    choice_df_max = choice_df_max['음식점명'].tolist()[0]
    st.info('중분류 : ' + my_choice1 + '의 매출이 가장 많은 곳은 ' + choice_df_max + ' 입니다')
    st.dataframe(choice_df[['음식점명','시군구명','행정동명','지역명','중분류','소분류','3개월전체매출수']])

    # 체크박스 선택시 해당 중분류에 소분류까지 나눠서 데이터 프레임 보여주기
    if st.checkbox('소분류 구분해서 보기') :
        df_list2 = df.loc[ df['중분류'] == my_choice1 ]
        df_list2 = df_list2['소분류'].unique().tolist()
        df_list2 = sorted(df_list2)
        my_choice2 = st.selectbox('음식점 소분류를 선택해주세요', df_list2)

        choice_df = df.loc[ (df['중분류'] == my_choice1) & (df['소분류'] == my_choice2) ]
        choice_df = choice_df.sort_values('3개월전체매출수',ascending=False)
        choice_df_max = choice_df.loc[choice_df['3개월전체매출수'] == choice_df['3개월전체매출수'].max()]
        choice_df_max = choice_df_max['음식점명'].tolist()[0]
        st.info(my_choice1 + ' / 소분류 : ' + my_choice2 + '의 매출이 가장 많은 곳은 ' + choice_df_max + ' 입니다')
        st.dataframe(choice_df[['음식점명','시군구명','행정동명','지역명','중분류','소분류','3개월전체매출수']])



