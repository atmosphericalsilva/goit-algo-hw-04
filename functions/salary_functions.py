def total_salary(salary_path):

    salary = list()

    try:
        # safely opening the file in the right format
        with open(salary_path, 'r', encoding = 'utf-8') as file:

            # splitting numbers from names
            for line in file:
                salary.append(line.split(',')[1].strip())
                
            # turning them into integers
            float_salary = [float(el) for el in salary]

            # checking if list is not empty
            if float_salary:
                return [sum(float_salary), sum(float_salary) / len(float_salary)]
            
            else:
                return "no salaries provided"
            
    # handling incorrect file data
    except (UnicodeDecodeError, IndexError, ValueError) as e:
        print(f'failed to read file: {e}')