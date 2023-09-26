import streamlit as st

st.image('./pic/1.jpg')
col1,col2 = st.columns(2)

with col1:
    st.header('วิริยะ เหมมาลา')
with col2:
    st.subheader('สาขาวิทยาการข้อมูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

st.header('Wiriya Hemmala')