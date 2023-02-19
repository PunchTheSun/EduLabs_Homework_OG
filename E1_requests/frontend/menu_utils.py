

def get_name() -> str:
    name = input("Please enter your first name: ")
    if ' ' in name:
        raise ValueError
    if not name.isalpha():
        raise NameError
    return name


def ask_continue() -> str:
    choice = input("Would you like to continue? (Y/N): ").lower()
    if choice not in {'y', 'n'}:
        raise ValueError
    return choice

