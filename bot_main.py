# imorting moduls and other libraries
from functions import bot_functions

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

if __name__ == '__main__':

    # calling bot function
    main()