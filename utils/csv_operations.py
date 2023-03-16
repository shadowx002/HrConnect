import csv
from datetime import datetime

from typing import Dict, List


class CSVProcessor:
    """
    This class do some processes to get data and filer data
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_csv_data(self):
        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return data

    def get_employees_c1(self) -> List:
        """
        This method is used for task_01 operation

        Returns:
            Dict : dictionary of eligible employees filtered by task_one
        """
        employees = []
        data = self.get_csv_data()

        for emp in data:
            if int(emp["SALARY"]) > 9000:
                emp_info = {
                    "Name": emp["FIRST_NAME"] + " " + emp["LAST_NAME"],
                    "email": emp["EMAIL"],
                    "phone_number": emp["PHONE_NUMBER"],
                }
                employees.append(emp_info)
        return employees

    def get_employees_c2(self) -> Dict:
        """
        This method is used for task_two operation

        Returns:
            Dict : dictionary of eligible employees filtered by task_two
        """
        employees_c2 = {}
        data = self.get_csv_data()

        for emp2 in data:
            if 30 < int(emp2["DEPARTMENT_ID"]) < 110 and int(emp2["SALARY"]) > 4200:
                hire_date_str = emp2["HIRE_DATE"][:9]
                hire_date = datetime.strptime(hire_date_str, "%d-%b-%y")
                full_name = emp2["FIRST_NAME"] + " " + emp2["LAST_NAME"]

                if hire_date in employees_c2:
                    employees_c2[hire_date].append(full_name)
                else:
                    employees_c2[hire_date] = [full_name]

        output_dict = {}
        for hire_date, full_names in employees_c2.items():
            hire_date_str = datetime.strftime(hire_date, "%Y-%m-%d")
            output_dict[hire_date_str] = full_names

        return output_dict
