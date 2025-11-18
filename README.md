# Contact Manager with Menu

Programmed by Tate B. & Alex W.

## Description
This project includes an easy to use interface which allows the user to do the following tasks: Add contacts, edit contacts, search contacts, delete contacts, and show all contacts.

Each contact is to display the following information: Name, Address, Phone Number, and Email Address

## Flowchart
```mermaid
graph TD;
  main-->menu;
  main-->add_contact;
  main-->search_contact;
  main-->edit_contact;
  main-->delete_contact;
  main-->display_contacts;
```

## IPO Charts

### Main Tate B.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`   | takes choice from menu() and finds the proper function to call  | `Outputs` the function called from menu option.        |

### Menu Tate B.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | displays a menu and the user will be prompted to select an option.  | `Returns` the choice to be returned to main.        |

### Add_Contact Alex W.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | append the contacts TXT file and add the contact data. It will prompt the user for: Name, Street Address, Phone Number, Email Address  | `Outputs` a success message.        |

### Search_Contact Alex W.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | searches the contact TXT for a contact based on the name, returns the other info.  | `Outputs` the address, email, and phone number.        |

### Display_Contacts Alex W.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | displays all contacts and then seperates each by a new line.  | `Outputs` the entire contact file with readability.        |

### Delete_Contact Alex W.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | fetches the name entered by the user from the Contact TXT file and removes all the information for that user.  | `Outputs` a success message        |

### Edit_Contacts Tate B.
| Arguments | Processing                                                      | Output/Return                                          |
| ------------------ | ------------- | ------------ |
| `none`    | finds a contact and edits the entire contact.  | `Outputs` a success message.        |
