# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)

def login():
    print("**************************")
    username = input("Please enter your username: ")
    print("**************************")
    if username != "":
            password(username)
    else:
        print(f'{username} is not recognized. Please try again.')
        login()

def password(username):
    print("**************************")
    password = input("Please enter your password: ")
    print("**************************")
    if password != "":
        main(username)
    else:
        (f'{password} is not recognized.')
        password(username)


def main(username):
    print(f"Welcome {username}!")
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")

def menu():
    print("**************************")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("**************************")
        



if __name__ == "__main__":
    login()
