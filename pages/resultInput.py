import streamlit as st

from data import Result
from src.sg_files.globalData import data

objectives = data["objectives"]

if 'data' not in st.session_state:
    st.session_state["data"] = data
if 'examId' not in st.session_state:
    st.session_state['examId'] = 0
if 'studentId' not in st.session_state:
    st.session_state['studentId'] = 0
if 'classId' not in st.session_state:
    st.session_state['classId'] = 0
formats = {1: "Not reached", 1.5: "", 2: "reached", 2.5: "", 3: "well reached", 3.5: "", 4: "very well reached"}
selectedResults = []


@st.cache_resource
def getResult(eId, sId, oId):
    for i in range(len(st.session_state.data["results"])):
        if st.session_state.data["results"][i].examId == eId and st.session_state.data["results"][i].studentId == sId and st.session_state.data["results"][
            i].objectiveId == oId:
            return st.session_state.data["results"][i]
    st.session_state.data["results"].append(Result(sId, eId, oId, 1))
    return st.session_state.data["results"][-1]


def setResult(eId, sId, oId, value):
    for i in range(len(st.session_state.data["results"])):
        if st.session_state.data["results"][i].examId == eId and st.session_state.data["results"][i].studentId == sId and st.session_state.data["results"][
            i].objectiveId == oId:
            st.session_state.data["results"][i].value = value
            return st.session_state.data["results"][i]


def format_labels(l):
    return formats[l]


def nextStudent():
    for i, question in enumerate(st.session_state.data["exams"][st.session_state.examId].objectives):
        setResult(st.session_state.examId, st.session_state.studentId,
                  question.objectiveId, selectedResults[i])
    st.session_state.studentId += 1
    print("Saved: ", st.session_state.data["results"])


def prevStudent():
    for i, question in enumerate(st.session_state.data["exams"][st.session_state.examId].objectives):
        setResult(st.session_state.examId, st.session_state.studentId,
                  question.objectiveId, selectedResults[i])
    st.session_state.studentId -= 1
    print("Saved: ", st.session_state.data["results"])


st.set_page_config(layout='wide')

st.title("" + st.session_state.data["exams"][st.session_state.examId].subject + ", " + st.session_state.data["exams"][
    st.session_state.examId].creation)
st.divider()

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        }
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: end;
        } 
    </style>
    """, unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

with col1:
    st.button("Previous", disabled=(st.session_state.studentId == 0), on_click=prevStudent)

with col2:
    st.markdown("### " + st.session_state.data["classes"][st.session_state.classId][st.session_state.studentId].objective)
with col3:
    st.button("Next", disabled=(
            st.session_state.studentId == len(st.session_state.data["classes"][st.session_state.classId]) - 1),
              on_click=nextStudent)
st.text("")
col4, col5 = st.columns([8, 4])
with col4:
    st.markdown("## Lernziele")
with col5:
    st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(1)
            {
            } 

            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: left;
            }
            div[data-testid="column"]:nth-of-type(3)
            {
                text_align: left
            }
            div[data-testid="column"]:nth-of-type(4)
            {
                text-align: end;
            } 
        </style>
        """, unsafe_allow_html=True
    )
    col6, col7, col8, col9 = st.columns(4)
    with col6:
        """Not Reached"""
    with col7:
        """Reached"""
    with col8:
        """Well Reached"""
    with col9:
        """Excellent"""
for question in st.session_state.data["exams"][st.session_state.examId].objectives:
    with st.container():
        col4, col5 = st.columns([8, 4])
        with col4:
            st.markdown(f"#### {objectives[question.objectiveId].objective}")
            st.markdown(f"{objectives[question.objectiveId].competency}")
        with col5:
            v = getResult(st.session_state.examId,
                          st.session_state.studentId, question.objectiveId).value
            selected = st.select_slider("label",
                                        [1, 1.5, 2, 2.5, 3, 3.5, 4],
                                        key=question.number,
                                        label_visibility="hidden",
                                        value=v,
                                        # format_func=format_labels,
                                        )
            print("Retrieved: ", v)
            selectedResults.append(selected)
