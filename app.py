import streamlit as st
import pandas as pd
import numpy as np
from tourism import run_tourism_app
from jejuhome import run_jejuhome_app
from restaurant import run_restaurant_app

def main() :
    # 사이드바 이미지와 타이틀 작성
    img_url = 'https://blog.kakaocdn.net/dn/o1KIw/btqu9mflPY6/rGk1mM3iugV1c6jj9Z3E80/img.jpg'
    st.sidebar.image(img_url)
    st.sidebar.title(':palm_tree: Welcome to JeJu-Do! :palm_tree:')
    
    # 사이드바 메뉴 생성
    menu = ['🌼 Home','🌼 Tourism','🌼 Restaurant']
    choice = st.sidebar.selectbox('MENU', menu)
    st.sidebar.write('')

    # 관광지명을 검색하면 관광지명과 데이터 프레임이 나오게하기
    tourism_input = st.sidebar.text_input('간편 관광지명으로 주소 검색하기')
    df = pd.read_csv('jjtourism_2022.csv',index_col=0)

    my_tourism = df.loc[ df['관광지명'].str.contains(tourism_input, case=False) ]
    st.sidebar.dataframe(my_tourism[['관광지명','주소']])
    st.sidebar.info('다른 관광지 정보를 더 보고싶다면 상단의 Tourism 를 클릭해주세요 :mag:')


    if choice == '🌼 Home' :
        run_jejuhome_app()

    elif choice == '🌼 Tourism' :
        run_tourism_app()

    elif choice == '🌼 Restaurant' :
        run_restaurant_app()


if __name__ == '__main__' :
    main()