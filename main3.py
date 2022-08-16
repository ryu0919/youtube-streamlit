from curses import use_default_colors
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit入門')

st.write('ブログレスバー')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('こんにちは')
expander2.write('解答')
#text = st.text_input('あなたの趣味を教えてください')
#condtion = st.slider('あなたの今の調子は？',0, 100, 50)

#'趣味：',text, 'です。'
#'コンディション:',condtion

#option = st.selectbox(
    #'あなたの好きな数字を教えてください',
    #list(range(1, 11))
#)
#'あなたの好きな数字は、',option, 'です。'

#if st.checkbox('Show Image'):
    #img = Image.open('sample.jpg')
    #st.image(img, caption='きゅうり', use_column_width=True)
   