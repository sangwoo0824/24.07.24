import streamlit as st
st.title('나의 첫 번째 웹 서비스')
name = st.text_input('이름을 입력해 주세요 :  ')
menu = st.selectbox('좋아하는 파스타을 선택하세요!', ['까르보나라 파스타', '로제 파스타', '토마토 파스타', '알리오올리오'])
if st.button('인사말 생성'):
  st.write(f'안녕하세요! (naeme)님! 당신이 좋아하는 파스타는 (menu)이군요! 너무 맛있겠어요!')
