username = None

def ask_username():
    """
    Asks the user for their name and stores it in a global variable.
    """
    global username
    username = input("Please enter your name: ")

def greet_user():
    """
    Uses the stored username to greet the user.
    """
    global username
    if username:
        print(f"Hello, {username}! Welcome back!")
    else:
        print("No username found. Please set it using ask_username().")

