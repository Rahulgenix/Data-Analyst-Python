employees = [
    {"name": "Aman", "department": "Sales", "sales": 80000},
    {"name": "Neha", "department": "Marketing", "sales": 45000},
    {"name": "Rahul", "department": "Sales", "sales": 95000},
    {"name": "Priya", "department": "IT", "sales": 30000}
]

for employee in employees:
    print(
        employee["name"],
        employee["department"],
        employee["sales"]
    )

total_sales = 0
highest_sales = 0
top_employee = ""

for employee in employees:
    total_sales = total_sales + employee["sales"]

    if employee["sales"] > highest_sales:
        highest_sales = employee["sales"]
        top_employee = employee["name"]

average_sales = total_sales / len(employees)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Top Employee:", top_employee)