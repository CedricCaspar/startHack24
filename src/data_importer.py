import pandas as pd
import openpyxl


def open_excel():
    data = pd.read_excel("src/students/student_data.xlsx")
    return data


def get_student_names():
    data = open_excel()

    names_column = 'name'

    # Ensure the column exists to avoid KeyError
    if names_column in data.columns:
        unique_names = data[names_column].unique()
        return unique_names
    else:
        print(f"Column '{names_column}' not found in the Excel data.")
        return []



print(get_student_names())