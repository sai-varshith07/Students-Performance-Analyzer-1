import numpy as np
import pandas as pd

#creation of dataframe

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Sai varshith", "Varshitha", "kerrthi", "akshara", "maheen"],
    "Math": [80, 90, np.nan, 60, 95],
    "Science": [60, 95, 60, np.nan, 92],
    "English": [85, 99, 50, 65, np.nan],
    "Attendance": [55, 86, 70, 35, 56]
})

print("\n📌 Original Dataset:\n", students)

# #finding null values values
# print(students.isna())

# #filling null values
null_values=students.fillna(students.mean(numeric_only=True),inplace=True)
print(null_values)


#Calculate total marks
students["Total marks"]=students["Math"]+students["Science"]+students["English"]
print(students)

#Calculate average marks
students["Average marks"]=students["Total marks"]/3
print(students)

# setting grades as per their marks
students["Grades"]=np.where(students["Total marks"]>250,"A+",students["Total marks"])
print(students)

#finding toppers 
students["Topper students"]=np.where(students["Total marks"]>250,students["Name"],"None")
print(students)

#finding weak students
students["Weak students"]=np.where(students["Total marks"]<250,students["Name"],"None")
print(students)

#pass / fail detection
students["Pass"]=np.where((students[["Math","Science","English"]]<50).any(axis=1),"Fail","Pass")
print(students)

#Attendece eligibility
students["Attendence Eligibility"]=np.where(students["Attendance"]<75,"Condonation","Eligible")
print(students)

#Perform subject-wise analysis
print("Highest in each subject:")
print(students[["Math","Science","English"]].max())

print("Lowest in each subject:")
print(students[["Math","Science","English"]].min())

#finding subject wise toppers
Subject_toppers={
    "Math Topper":students.loc[students["Math"].idxmax(),"Name"],
    "English Topper":students.loc[students["English"].idxmax(),"Name"],
    "Science Topper":students.loc[students["Science"].idxmax(),"Name"]
}
print(Subject_toppers)

students["Rank"] = students["Total marks"].rank(ascending=False)
print(students)