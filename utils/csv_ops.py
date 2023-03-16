import csv

from datetime import datetime


def get_employees_details(file_path):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)

    return reader


def get_emp(reader):
    qualified_employees = []

    for x in reader:
        if 30 < int(x["DEPARTMENT_ID"]) < 110 and int(x["SALARY"]) > 4200:
            hire_date_str = x["HIRE_DATE"][
                :9
            ]  # Extract the date part from the HIRE_DATE field
            hire_date = datetime.strptime(hire_date_str, "%d-%b-%y")
            full_name = x["FIRST_NAME"] + " " + x["LAST_NAME"]

            qualified_employees.append({"hire_date": hire_date, "full_name": full_name})

    return qualified_employees


def group_employees_by_hire_date(qualified_employees):
    employees_by_hire_date = {}

    for employee in qualified_employees:
        hire_date = employee["hire_date"]
        full_name = employee["full_name"]

        if hire_date in employees_by_hire_date:
            employees_by_hire_date[hire_date].append(full_name)
        else:
            employees_by_hire_date[hire_date] = [full_name]

    output_dict = {}
    for hire_date, full_names in employees_by_hire_date.items():
        hire_date_str = datetime.strftime(hire_date, "%Y-%m-%d")
        output_dict[hire_date_str] = full_names

    return output_dict


# "/home/shadow/Downloads/employeescsv/employees.csv"
file_path = "/home/shadow/Downloads/employeescsv/employees.csv"

qualified_employees = get_employees_details(file_path)
output_dict = group_employees_by_hire_date(qualified_employees)
print(output_dict)
