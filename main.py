import os

def menu():
    pass

def add_contact():
    pass

def search_contact():
    pass

def edit_contact():
    # edit_contacts accepts no args
    # finds a contact and edits all data
    # outputs a success msg upon completion.
    
    # boolean flag
    found = False
    
    search = input("Enter the name of the contact you wish to edit: ")
    option_select = int(input("Select which option you wish to edit.\n\n1) Street Address\n2) Phone Number\n3)Email Address\n4) Cancel\n>: "))
    
    while option_select > 4 or option_select < 1:
        print("Please input only numbers within the range")
        option_select = int(input(">: "))
    
    try:
        contacts_file = open("contacts.txt", "r")
        temp_file = open("temp_contacts.txt", "w")
        # define new value
        new = ""
        
        # prompt for certain information
        if option_select == 1:
            new = input("Enter the new street address: ")
        elif option_select == 2:
            new = input("Enter the new phone number: ")
        elif option_select == 3:
            new = input("Enter the new email address: ")
        
        # find name
        name = contacts_file.readline()
        
        # find record
        while name != "":
            # get the other info
            street_address = contacts_file.readline()
            phone_number = contacts_file.readline()
            email_address = contacts_file.readline()
            # strip newlines
            name = name.rstrip("\n")
            street_address = street_address.rstrip("\n")
            phone_number = phone_number.rstrip("\n")
            email_address = email_address.rstrip("\n")

            # check if the search and name are equal
            if search.lower() == name.lower():
                temp_file.write(name + "\n")
                
                # change new value
                if option_select == 1:
                    temp_file.write(new + "\n")
                    temp_file.write(phone_number + "\n")
                    temp_file.write(email_address + "\n")
                elif option_select == 2:
                    temp_file.write(street_address + "\n")
                    temp_file.write(new + "\n")
                    temp_file.write(email_address + "\n")
                elif option_select == 3:
                    temp_file.write(street_address + "\n")
                    temp_file.write(phone_number + "\n")
                    temp_file.write(new + "\n")
                
                # redeine boolean
                found = True
            else:
                temp_file.write(name + "\n")
                temp_file.write(street_address + "\n")
                temp_file.write(phone_number + "\n")
                temp_file.write(email_address + "\n")
                
            name = contacts_file.readline()
            
            # close files
            temp_file.close()
            contacts_file.close()
            
            # remove og & rename temp
            os.remove("contacts.txt")
            os.rename("temp_contacts.txt", "contacts.txt")
            
            # temp print statement
            print("Success.")
            
    except Exception as err:
        print(err)
            

    

def delete_contact():
    pass

def display_contacts():
    pass

def main():
    pass
