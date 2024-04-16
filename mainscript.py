from classes import Account

def main():
    print("Welcome to the Airline Management System!")

    # Collect user input for username, password, and user role
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_role = input("Enter your user role: ")

    # Create an Account object with the collected input
    account_manager = Account(username, password, user_role)

    # Authenticate the user
    if account_manager.authenticate(username, password):
        print("Authentication successful!")
        print(f"Welcome, {username}!")
    else:
        print("Authentication failed. Please check your credentials.")

if __name__ == "__main__":
    main()