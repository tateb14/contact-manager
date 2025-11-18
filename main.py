import os

def menu():
    # menu accepts no args
    # displays a menu and the user will be prompted to select an option.
    # validate the option is a number and that the number is within range
    # and that it is a number.
    # returns the choice to be returned to the main function.
    
    print("Please select one of the following options:\n")
    print("1) Add Contact")
    print("2) Search Contact")
    print("3) Edit Contact")
    print("4) Delete Contact")
    print("5) Display All Contact")
    print("6) Exit Contact\n")
    
    try:
        # get user input for choice
        choice = int(input(">: "))
        
        # check if input is within the range
        while choice > 6 or choice < 1:
            # if not, prompt for another number
            print("Please use one of the defined numbers.")
            choice = int(input(">: "))
        
        # return the choice
        return choice
    except ValueError:
        # ensure the choice is a value, no strings
        print("Please input only numbers.")
        menu()
    except Exception as error:
        # handle unknown errors
        print("An unknown error has occurred.")
        print(error)
        menu()

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


main()
