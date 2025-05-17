# imorting moduls and other libraries
from functions.salary_functions import total_salary
from functions.cat_functions import get_cats_info
from pathlib import Path

# paths to the files
salary_path = Path('sources/salary.txt')
cat_path = Path('sources/cats.txt')

try:
    # calling the first function
    total, average = total_salary(salary_path)

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    # calling the second function
    print(get_cats_info(cat_path))

# handling a missing file
except FileNotFoundError:
    print('file was not found')
        
# handling wrong data
except TypeError:
    print('incorrect file data')