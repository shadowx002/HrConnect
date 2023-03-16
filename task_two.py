from utils.csv_operations import CSVProcessor
import pprint


def task_2():
    file_path = "/home/shadow/Downloads/employeescsv/employees.csv"
    process_ = CSVProcessor(file_path)
    employees_2 = process_.get_employees_c2()

    return employees_2


if __name__ == "__main__":
    task_2()
