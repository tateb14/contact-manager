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
    street_address = contact_file.readline()
    phone_number = contact_file.readline()
    email_address = contact_file.readline()
    
    # counter
    count = 1
    
    
    while name != '' and street_address !='' and phone_number != '' and email_address != '':
        #count
        print(f"Contact Information {count}: ")
        
        
        #strip the line
        name = name.strip('\n')
        street_address = street_address.strip('\n')
        phone_number = phone_number.strip('\n')
        email_address = email_address.strip('\n')
        
        
        #read line
        name = contact_file.readline()
        street_address = contact_file.readline()
        phone_number = contact_file.readline()
        email_address = contact_file.readline()
        
        
        # output the contact
        print("Name: ", name)
        print("Address: ", street_address)
        print("Phone: ", phone_number)
        print("Email: ", email_address)
        print()  # blank line for readability
        
        #increase the counter
        count += 1
        
        
    contact_file.close() #close the file
    print("\n" + str(count), "contacts retrieved.")

def main():
    pass
