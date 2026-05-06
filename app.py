#Simple CLI App

#import libraries/files
import database
import os

def create_entry():
    title = input("Job Title: ")
    app_type = input("Type (internship/full-time): ")
    status = input("Status (applied/interview/rejected):")

    database.add_entry(title, app_type, status)

def display_table():
    table = database.get_all()
    for row in table:
        print(row)


def delete_entry():
    id = input("Which entry number do you wish to delete?")
    database.remove_entry(id)

while True: #main application loop
    applications_count = database.getAppCount()
    print("\n") # New line for readability
    print("Welcome To The Application App \n")
    print(f"You currently have {applications_count} applications! \n")

    display_table()
    print("\n") # New line for readability

    print("To add an entry, type ADD. To delete an entry, type DELETE: \n")
    print("To exit application, type EXIT \n")
    menu_selection = input() 

    if menu_selection == "ADD" or menu_selection == "add":
        print("ENTERING ADD MENU: \n")
        create_entry()

    elif menu_selection == "DELETE" or menu_selection == "delete":
        print("ENTERING DELETE MENU \n")
        delete_entry()

    elif menu_selection == "EXIT" or menu_selection == "exit":
        break
