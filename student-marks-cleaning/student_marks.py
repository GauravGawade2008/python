import pandas as pd 

# reading csv file 
df = pd.read_csv("student_marks.csv")

# understanding the data statistics.
print("Information: ")
df.info()
print(df.describe())
print(f"\nTotal no. of null values: \n{df.isnull().sum()}")

# removes duplicate column 
df = df.drop_duplicates()

# name column is cleaned with title case and proper spacing.
df["name"] = df["name"].str.strip().str.title()

# filling missing values 
numeric_cols = ["attendance_%","math","science","english"]
df[numeric_cols] = df[numeric_cols].fillna(value = df[numeric_cols].mean(numeric_only = True).round(2))

df["age"] = df["age"].fillna(value = df["age"].median())

#finding out the  students with attendance below 60% and filter them out 
print("\nStudents with attendance below 60% :")
print(df[df["attendance_%"] < 60 ].filter(items= ["name", "attendance_%"]))

# finding out the average marks and adding the column
df["average_marks"] = (( df["math"] + df["science"] + df["english"]) / 3).round(2)

# displaying the top 5 rankers and class average
print(f"Top 5 of the class: \n{df.nlargest(5,'average_marks')[['name','average_marks']]}")
print(f"Class average: {df['average_marks'].mean().round(2)}")
# cleaned data
print(f"Final cleaned data: \n{df}")

# saving the cleaned csv into new csv file
df.to_csv("cleaned_student_marks.csv", index= False)
