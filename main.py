# imorting moduls and other libraries
from functions.salary_functions import total_salary
from functions.cat_functions import get_cats_info
from functions import bot_functions
from pathlib import Path

# bot function
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = bot_functions.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(bot_functions.add_contact(args, contacts))

            elif command == "change":
                print(bot_functions.change_contact(args, contacts))

            elif command == "phone":
                print(bot_functions.show_phone(args, contacts))

            elif command == "all":
                print(bot_functions.show_all(contacts))

            else:
                print("Invalid command.")

    # handling an error
    except (ValueError, IndexError, TypeError) as e:
        print(f'error: {e}')

# paths to the files
salary_path = Path('sources/salary.txt')
cat_path = Path('sources/cats.txt')

if __name__ == '__main__':

    main()

    try:
        # calling the first function
        average, total = total_salary(salary_path)

        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

        # calling the second function
        print(get_cats_info(cat_path))

    # handling a missing file
    except FileNotFoundError:
        print('file was not found')
        
    # handling wrong data
    except TypeError:
        print('incorrect file data')