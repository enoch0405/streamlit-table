import streamlit as st
# from datetime import datetime as datetime
# import datetime

# 제목
st.title('여러 종류 버튼')

# 일반 버튼
st.subheader('일반 버튼')
button = st.button('버튼을 누르시오', use_container_width=True)
if button:    
    st.write('버튼이 눌렸습니다')
st.divider()

# 체크 버튼
st.subheader('체크 버튼')
check = st.checkbox('동의하십니까')
if check:
    st.write('동의함')
st.divider()

# 콤보 버튼
st.subheader('콤보 버튼')
subject = st.selectbox(
    '당신이 좋아하는 과목이 무엇입니까?',
    ('국어', '영어', '수학'),
    index=2
)
if subject == '국어':
    st.write('국어를 잘하면 책을 잘 읽습니다')
elif subject == '영어':
    st.write('영어를 잘하면 외국여행이 즐겁습니다')
elif subject == '수학':
    st.write('수학을 잘하면 코딩을 잘 합니다')

st.divider()
    
# 라디오 버튼
st.subheader('라디오 버튼')
money = st.radio(
    '원하는 직업이 무엇입니까?',
    ('의사', '개발자', '경찰')
)
if money == '의사':
    st.write('연봉은 3억입니다')
elif money == '개발자':
    st.write('연봉은 1억입니다')
elif money == '경찰':
    st.write('연봉은 10억입니다')

# 다중선택 버튼
st.subheader('다중선택버튼')
options = st.multiselect(
    '어떤 생각을 하고 계십니까?',
    ['공부', '미래', '집값'],
    ['공부', '미래'])

st.write(f'당신의 선택은 좋습니다')
st.divider()

# 슬라이더
st.header('슬라이더')
values = st.slider(
    '범위의 값을 다음으로 입력하시오 : sparkles',
    0, 100, (24, 90)
)
st.write('선택범위:', values)
st.divider()
