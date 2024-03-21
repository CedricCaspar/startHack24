import streamlit as st

from src.sg_files.globalData import getExam

exam = getExam(0)


st.title("" + exam.subject + ", " + exam.creation)
st.divider()
st.button("Previous")
