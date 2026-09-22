import pandas as pd

data = {
    "Employee": ["Aman", "Neha", "Rahul", "Priya"],
    "Department": ["Sales", "HR", "Sales", "IT"],
    "Salary": [35000, 40000, 50000, 45000],
    "Experience": [1, 2, 3, 2]
}
df = pd.DataFrame(data)
# df.to_excel("employee_data.xlsx", index=False)  # Save the DataFrame to an Excel file without the index 
print("DataFrame saved to employee_data.xlsx")

# for data reading from excel file
excel_data = pd.read_excel("employee_data.xlsx")  # Read the Excel file into a DataFrame

print("\nexcel data:")
print(excel_data)  # Display the DataFrame read from the Excel file 

#filtering data based on a condition

high_salary = excel_data[excel_data["Salary"] >= 40000]  # Filter employees with salary greater than 40000
# high_salary.to_excel("high_salary_employees.xlsx", index=False)  # Save the filtered DataFrame to a new Excel file
print("\nFiltered DataFrame saved to high_salary_employees.xlsx")   
