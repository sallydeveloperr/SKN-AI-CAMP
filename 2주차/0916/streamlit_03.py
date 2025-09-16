# session의 개념
# web에서는 server니까 각각의 사용자를 구분하기 위한 키가 필요하다
# 그것이 바로 session!
# 세션 상태 관리
import streamlit as st
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('카운트 증가'):
    st.write('버튼 클릭됨')
    st.session_state['count'] += 1
st.write('현재 카운트 :', st.session_state['count'])
st.json(st.session_state)   #세션 상태 확인 