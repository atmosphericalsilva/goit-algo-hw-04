from functions.salary_functions import total_salary
from pathlib import Path

# path to the file
salary_path = Path('sources/salary.txt')

if __name__ == '__main__':

    try:
        # calling the function
        average, total = total_salary(salary_path)

        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    # handling an error
    except TypeError:
        pass