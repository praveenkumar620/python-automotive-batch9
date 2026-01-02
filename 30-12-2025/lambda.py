# Raw data using collections
managers = ["Manager1", "Manager2", "Manager3"]

employees = [
    "Emp1", "Emp2", "Emp3", "Emp4",
    "Emp5", "Emp6", "Emp7", "Emp8",
    "Emp9", "Emp10", "Emp11", "Emp12",
    "Emp1"   # duplicate employee
]

# Remove duplicate employees using set and map
unique_employees = list(set(map(lambda x: x, employees)))

# Filter only valid employees (just for example)
filtered_employees = list(filter(lambda x: x.startswith("Emp"), unique_employees))

# Assign employees to managers (no duplicate mapping)
manager_employee_map = {}

for index, emp in enumerate(filtered_employees):
    manager = managers[index % len(managers)]
    manager_employee_map.setdefault(manager, []).append(emp)

# Output
print("Employee Reporting Structure:\n")

for manager, emp_list in manager_employee_map.items():
    print(manager, "manages", emp_list)