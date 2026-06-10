import streamlit as st

st.set_page_config(
    page_title="Streamlit 실행 테스트",
    layout="wide"
)

st.title("Streamlit 실행 테스트")
st.success("앱 실행 성공")
st.write("Streamlit Cloud가 정상 작동 중입니다.")
st.info("이 화면이 보이면 Streamlit Cloud 자체 문제나 계정 차단 문제가 아니라, 기존 app.py 코드 또는 파일 경로 문제일 가능성이 큽니다.")
