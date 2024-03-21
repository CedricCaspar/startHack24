import pandas as pd
import openpyxl

from src.data import Result, Student, Objective

data = pd.read_excel("students/student_data.xlsx")



def get_student_names():
    names_column = 'name'

    # Ensure the column exists to avoid KeyError
    if names_column in data.columns:
        unique_names = data[names_column].unique()
        students = [Student(i, name) for i, name in enumerate(unique_names)]
        print(students)
        return students
    else:
        print(f"Column '{names_column}' not found in the Excel data.")
        return []

def get_objectives():
    objective_column = ['subject', 'uid', 'competency', 'objective']
    objs = data[objective_column]
    objs = [Objective(i, row[3], row[0], row[2], row[1]) for i, row in objs.iterrows()]

    unique = []
    for obj in objs:
        if obj not in unique:
            unique.append(obj)

    return unique


def get_exams():
    objective_column = ['subject', 'exam', 'task', 'objective', 'weight', 'date']
    exam_data = data[objective_column]
    max_exams = 10
    for i in range(max_exams):
        df = exam_data[exam_data['exam'] == i]
        print(df)
    #objs = [Objective(i, row[3], row[0], row[2], row[1]) for i, row in objs.iterrows()]


print (get_exams())