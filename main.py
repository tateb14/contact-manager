import os

def menu():
    pass

def add_contact():#add_contact accepts no arguements
    #add contact adds a contact to the file
    
    #make file contacts.txt
    infile = open("contacts.txt", 'a')
    
    
    try: #validate input for num_contacts
        num_contacts = int(input("How many contacts would you like to add? "))
        
    except ValueError: 
        print("ERROR: Non-numeric date found, calculations haulted")
    except Exception:
        print("An unknown error has occured")
        
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
    pass
