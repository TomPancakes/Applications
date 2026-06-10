#Simple CLI App

#import libraries/files
import database
import os

def clear(): #allows terminal to be cleared for readability
    os.system('cls' if os.name == 'nt' else 'clear')

def create_entry():
    #Job Title
    title = input("Job Title: ")
    app_type = int(input("""
    Job Type: 
        1. full-time
        2. part-time
        3. internship
                         
    Please Enter Number 1-3: """))
    status = int(input("""
                   Status: (applied/interview/rejected): 
                   1. applied
                   2. rejected
                   3. offered
                   4. accepted
    Please Enter Number 1-4: """))
    
    database.add_entry(title, app_type, status)

def display_table():
    table = database.get_all()
    for row in table:
        print(row)

def delete_entry():
    confirm = ""
    while confirm != "y":
        id = input("Which entry number do you wish to delete? (leave blank to exit) ")
        if id == "":
            return
        confirm = input(f"entry to be deleted: {id}, are you sure? (y/n)")
        if confirm == "y":
            break
    database.remove_entry(id)
    


def modify():
    id = input("Which entry do you want to modify? (click enter to exit modifcation menu) ")
    if id == "":
        return 
    title = input("New job Title (leave blank to keep same): ")
    app_type = input("New Type (internship/full-time) (leave blank to keep same): ")
    status = input("New Status (applied/interview/rejected) (leave blank to keep same): ")

    database.modify(id, title, app_type, status)
    


while True: #main application loop
    applications_count = database.getAppCount()
    print("\n") # New line for readability
    print("Welcome To The Application App \n")
    print(f"You currently have {applications_count} applications! \n")

    display_table()
    print("\n") # New line for readability

    print("Select ADD, DELETE, or EDIT. \n")
    print("To exit application, type EXIT \n")
    menu_selection = input() 

    if menu_selection == "ADD" or menu_selection == "add":
        print("ENTERING ADD MENU: \n")
        create_entry()

    elif menu_selection == "DELETE" or menu_selection == "delete":
        print("ENTERING DELETE MENU \n")
        delete_entry()

    elif menu_selection == "EDIT" or menu_selection == "edit":
        print("ENTERING MODIFCATION MENU")
        modify()

    elif menu_selection == "EXIT" or menu_selection == "exit":
        break

    clear()
    