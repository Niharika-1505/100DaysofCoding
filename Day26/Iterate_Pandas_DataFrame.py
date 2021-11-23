import pandas

student_dict = {
    "student": ["Angela", "Barry", "Clinton", "Dahlia"],
    "scores": [65, 72, 68, 83]
}
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

# Looping throw each row in Data Frame using pandas
for (index, row) in student_dataframe.iterrows():
    if row.student == "Barry":
        print(f"{index} {row.student}: {row.scores}")
