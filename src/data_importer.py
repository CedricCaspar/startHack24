import pandas as pd
import numpy as np
import openpyxl

from src.data import Result, Student, Objective, Exam
import streamlit as st

data = pd.read_excel("src/students/student_data copy.xlsx")

def getIdStudent(name):
    df = data.loc[data['name'] == name]
    val = df['studentId'].unique().item()

    return val
def getIdObjective(name):
    df = data.loc[data['objective'] == name]
    val = df['oId'].unique().item()

    return val
def getIdExam(id):
    df = data.loc[data['exam'] == id+1]
    #print(df.columns)
    date = df['date'].unique()
    sub = df['subject'].unique()
    #print(date, sub)

    tasks = df[['oId', 'task', 'weight']].to_numpy()
    tasks = np.unique(tasks, axis=0)
    #print(tasks.transpose()[2], tasks.transpose()[0], [str(n) for n in tasks.transpose()[1]])
    return Exam(id, date[0], sub[0], [str(n) for n in tasks.transpose()[1]], tasks.transpose()[0], tasks.transpose()[2])


def get_student_names():
    names_column = 'name'

    # Ensure the column exists to avoid KeyError
    if names_column in data.columns:
        unique_names = data[names_column].unique()
        students = [Student(getIdStudent(name), name) for i, name in enumerate(unique_names)]
        print(students)
        return students
    else:
        print(f"Column '{names_column}' not found in the Excel data.")
        return []


def get_objectives():
    objective_column = ['subject', 'uid', 'competency', 'objective', 'oId']
    objs = data[objective_column]
    objs = [Objective(getIdObjective(row[3]), row[3], row[0], row[2], row[1]) for i, row in objs.iterrows()]

    unique = []
    for obj in objs:
        if obj not in unique:
            unique.append(obj)

    return unique

def get_results():
    objective_column = ['studentId', 'oId', 'exam', 'evaluation']
    objs = data[objective_column]

    objs = [Result(row[0], row[2], row[1], row[3]) for i, row in objs.iterrows()]

    return objs


def get_exams():
    objective_column = ['subject', 'exam', 'task', 'objective', 'weight', 'date', 'oId']
    exam_data = data[objective_column]
    max_exams = 10
    exams = []
    for i in range(max_exams):
        exam = getIdExam(i)
        exams.append(exam)
    return exams


students = get_student_names()
objectives = get_objectives()
exams = get_exams()
results = get_results()

data_dict = {
    "objectives": objectives,
    "exams": exams,
    "classes": [students],
    "results": results
}
st.session_state.data = data_dict
