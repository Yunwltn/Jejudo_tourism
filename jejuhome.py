import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_jejuhome_app() :
    st.title('Welcome to JeJu-Do!')
    st.write('환영합니다 Welcome to JeJu-Do! 는 제주도의 관한 관광지 정보를')
    st.write('관광지 조회수, 음식점 카드 매출수 등의 정보를 통계해 순위를 보여주는 앱입니다')
    image_url = 'http://www.grandmerjeju.com/data/editor/1610/thumb-4c97623c9cb60df276a4dc448a48316c_1476762657_11_1000x598.jpg'
    st.image(image_url, use_column_width=True)