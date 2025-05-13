def total_salary(salary_path):

    salary = list()

    try:
        # safely opening the file in the right format
        with open(salary_path, 'r', encoding = 'utf-8') as file:

            # splitting numbers from names
            for line in file:
                salary.append(line.split(',')[1].strip())
                
            # turning them into integers
            int_salary = [int(el) for el in salary]

            # calculating the sum and average number
            return {sum(int_salary), sum(int_salary) // len(int_salary)}

        # handling incorrect file data
    except (UnicodeDecodeError, IndexError, ValueError) as e:
        print(f'failed to read file: {e}')