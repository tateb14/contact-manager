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

def add_contact():#add_contact accepts no arguements
    #add contact adds a contact to the file
    
    #make file contacts.txt
    infile = open("contacts.txt", 'a')
    
    
    try: #validate input for num_contacts
        num_contacts = int(input("How many contacts would you like to add? "))
        
    except ValueError: 
        print("ERROR: Non-numeric date found, calculations haulted")
    
    #loop for all contacts
    for num in range(1, num_contacts +1):
        
        #get input of name, street adress, phone number, and email adress
        print(f"Information for contact number {num}.")
        name = input("Please input your name: ")
        street_address = input("Please input your street address: ")
        phone_number = input("Please input your phone number: ")
        email_address = input("Please input your email address: ")
        
        #store the file
        
        infile.write(name + '\n')
        infile.write(street_address + '\n')
        infile.write(phone_number + '\n')
        infile.write(email_address + '\n')
        
     #close the file
    infile.close()
    print("All input has been saved in contacts.txt")
        
    
    

def search_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def display_contacts():# display contacts accepts no arguements
    #A display contacts function that displays all contacts
    #and their information in a readable format
    
    #open the file
    contact_file = open('contacts.txt', 'r')
    
    
    
    #set the readline name = contact_file.readline()
    name = contact_file.readline()
    
    
    # counter
    count = 0
    
    
    while name != '':
        
        #read line
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()
        
        #count
        print(f"Contact Information {count}: ")
        
        
        
        #strip the line
        name = name.rstrip('\n')
        street_address = street_address.rstrip('\n')
        phone_number = phone_number.rstrip('\n')
        email_address = email_address.rstrip('\n')
        
        
        
        
        
        
        # output the contact
        print("Name: ", name)
        print("Address: ", street_address)
        print("Phone: ", phone_number)
        print("Email: ", email_address)
        print()  # blank line for readability
        
        #increase the counter
        count += 1
        
        #read line
        name = contact_file.readline()
        
    contact_file.close() #close the file
    print("\n" + str(count), "contacts retrieved.")

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
