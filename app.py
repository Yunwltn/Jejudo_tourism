import streamlit as st
from tourism import run_tourism_app
from jejuhome import run_jejuhome_app

def main() :
    menu = ['🌼 Home','🌼 Tourism','🌼 ??']
    img_url = 'https://blog.kakaocdn.net/dn/o1KIw/btqu9mflPY6/rGk1mM3iugV1c6jj9Z3E80/img.jpg'
    st.sidebar.image(img_url)

    st.sidebar.title(':palm_tree: Welcome to JeJu-Do! :palm_tree:')
    choice = st.sidebar.selectbox('MENU', menu)

    if choice == '🌼 Home' :
        run_jejuhome_app()

    elif choice == '🌼 Tourism' :
        run_tourism_app()

    elif choice == '🌼 ??' :
        pass

if __name__ == '__main__' :
    main()