import pandas as pd


print("PART 1: Pandas Series")
 
marks = [88, 76, 92, 67, 85]
 
student_marks = pd.Series(marks, index=["Soyinka", "Martin", "Nifemi", "Jack", "Michael"])
 
print(student_marks)


print("PART 2: Pandas DataFrame")
 
data = {
    "Student": ["Soyinka", "Martin", "Nifemi", "Jack", "Michael"],
    "Math": [88, 76, 92, 67, 85],
    "Science": [91, 80, 89, 72, 87],
    "English": [84, 78, 95, 70, 82],
    "Attendance": [96, 90, 98, 85, 92]
}
 
df = pd.DataFrame(data)
 
print(df)

 
print("PART 3: Reading Data from a CSV File")
 
df.to_csv("student_marks.csv", index=False)
 
student_data = pd.read_csv("student_marks.csv")
 
print("CSV file read successfully!")
print(student_data)

 
print("PART 4: Viewing Data")
 
print("First 3 rows:")
print(student_data.head(3))
 
print("Last 2 rows:")
print(student_data.tail(2))
 
print("Data Information:")
print(student_data.info())

 
print("PART 5: Cleaning Data")
 
messy_data = {
    "Student": ["Soyinka", "Martin", "Nifemi", "Jack", "Michael"],
    "Math": [88, None, 92, 67, 85],
    "Science": [91, 80, None, 72, 87],
    "English": [84, 78, 95, None, 82]
}
 
messy_df = pd.DataFrame(messy_data)
 
print("Data with Missing Values:")
print(messy_df)
 
cleaned_df = messy_df.fillna(0)
 
print("Cleaned Data:")
print(cleaned_df)