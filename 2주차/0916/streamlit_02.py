#1부터 100사이의 데이터
import random
datas = [random.randint(1,100) for i in range(10)]
print(datas)

import streamlit as st
st.write('막대 그래프')
st.bar_chart(datas)

st.write('선 그래프')
st.line_chart(datas)
st.write('영역 그래프')
st.area_chart(datas)
st.write('1 x 2 layout 구성')
col1, col2 = st.columns(2)
with col1:
    st.write('막대 그래프')
    st.bar_chart(datas)
#col1.bar_chart(datas) #이렇게 써도 됨
with col2:
    st.write('선 그래프')
    st.line_chart(datas)
#col2.line_chart(datas) #이렇게 써도 됨

st.write('2x2 layout')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col1.bar_chart(datas)
col2.line_chart(datas)
col3.area_chart(datas)
col4.table(datas)

