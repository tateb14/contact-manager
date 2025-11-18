import os

def menu():
    pass

def add_contact():
    pass

def search_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def display_contacts():
    pass

def main():
    # main accepts no args
    # takes choice from menu() and finds the proper function to call
    # calls the proper function.
    
    # call menu and get choice
    choice = menu()
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        edit_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        display_contacts()
    else:
        print("Thanks for using the contact manager!")
