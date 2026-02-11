import pandas as pd
grades = pd.Series([85, None, 92, 45, None,78, 55])
missing_values = grades.isnull()
filled_grades = grades.fillna(0)
passed_students = filled_grades[filled_grades > 60]
print("Original Grades Series:\n",grades)
print("\nMissing values:\n",missing_values)
print("\nGrades after filling missing values with 0:\n",filled_grades)
print("\nScores greater than 60:\n",passed_students)