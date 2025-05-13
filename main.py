from functions.salary_functions import total_salary
from functions.cat_functions import get_cats_info
from pathlib import Path

# path to the file
salary_path = Path('sources/salary.txt')

cat_path = Path('sources/cats.txt')

if __name__ == '__main__':

    try:
        # calling the function
        average, total = total_salary(salary_path)

        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

        print(get_cats_info(cat_path))

    # handling a missing file
    except FileNotFoundError:
        print('file was not found')
    # handling wrong data
    except TypeError:
        print('incorrect file data')