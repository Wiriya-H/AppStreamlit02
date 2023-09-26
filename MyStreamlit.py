import streamlit as st

st.image('./pic/1.jpg')
col1,col2 = st.columns(2)

with col1:
    st.header('วิริยะ เหมมาลา')
with col2:
    st.subheader('สาขาวิทยาการข้อมูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

html_1 = """
<div style="background-color:97FFF4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้เบื้องต้น</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))
st.button('Show bar chart')