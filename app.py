import streamlit as st
from tourism import run_tourism_app
from jejuhome import run_jejuhome_app
from restaurant import run_restaurant_app
import pandas as pd
import numpy as np

def main() :
    menu = ['🌼 Home','🌼 Tourism','🌼 Restaurant']
    img_url = 'https://blog.kakaocdn.net/dn/o1KIw/btqu9mflPY6/rGk1mM3iugV1c6jj9Z3E80/img.jpg'
    st.sidebar.image(img_url)

    st.sidebar.title(':palm_tree: Welcome to JeJu-Do! :palm_tree:')
    
    choice = st.sidebar.selectbox('MENU', menu)
    st.sidebar.write('')

    tourism_input = st.sidebar.text_input('간편 관광지명으로 주소 검색하기')
    df = pd.read_csv('jjtourism_2022.csv',index_col=0)
    if len(tourism_input) != 0 :
        my_tourism = df.loc[ df['관광지명'].str.contains(tourism_input, case=False) ]
        st.sidebar.dataframe(my_tourism[['관광지명','주소']])
        if st.sidebar.button('다른 관광지 더 살펴보기 :car:') :
            run_tourism_app()
    else :
        st.sidebar.dataframe(df[['관광지명','주소']])


    if choice == '🌼 Home' :
        run_jejuhome_app()

    elif choice == '🌼 Tourism' :
        run_tourism_app()

    elif choice == '🌼 Restaurant' :
        run_restaurant_app()


if __name__ == '__main__' :
    main()