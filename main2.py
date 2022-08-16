import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

st.map(df)