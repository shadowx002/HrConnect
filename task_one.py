from utils.csv_operations import CSVProcessor
import pprint


def task_1():
    file_path = "/home/shadow/Downloads/employeescsv/employees.csv"
    process_ = CSVProcessor(file_path)
    employees_1 = process_.get_employees_c1()

    return employees_1


if __name__ == "__main__":
    task_1()
