import pandas as pd
df = pd.read_csv('EmployeeSampleData/Employee Sample Data.csv', encoding='ISO-8859-1')
print (df['Annual Salary'].max())
print(df['EEID'][df['Department']=="IT"])
print(df['Age'].mean())