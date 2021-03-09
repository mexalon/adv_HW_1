"""Не совсем понял, что имелось с виду в задании 3 под вызовом функий этого модуля """
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    print(f'Today is {date.today()}')
    get_employees()
    calculate_salary()
