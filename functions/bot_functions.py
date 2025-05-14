# input processing
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add contact cmd
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# change contact cmd
def change_contact(args, contacts):
    name, new_phone = args

    if name in contacts:
        contacts[name] = new_phone
        return 'Contact updated.'
    
    else: 
        return 'Contact not found.'     

# show phone cmd
def show_phone(args, contacts):
    name = args[0]

    # checking for contact
    if name in contacts and len(args) == 1:
        return contacts[name]
    
    else:
        return 'Contact not found.'

# show all cmd
def show_all(contacts):
    return contacts