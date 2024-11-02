from contacts import Contacts

def main():
    contact_list = Contacts()
    
    while True:
        print("\n*** TUFFY TITAN CONTACT MAIN MENU")
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list")
        print("5. Set contact filename")
        print("6. Exit the program")
        
        choice = input("Enter menu choice: ")
        
        if choice == "1":
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contact_list.add_contact(id=id, first_name=first_name, last_name=last_name)
            if result == "error":
                print("Phone number already exists.")
            else:
                print(f"Added: {first_name} {last_name}.")
        
        elif choice == "2":
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contact_list.modify_contact(id=id, first_name=first_name, last_name=last_name)
            if result == "error":
                print("Invalid phone number.")
            else:
                print(f"Modified: {first_name} {last_name}.")
        
        elif choice == "3":
            id = input("Enter phone number: ")
            result = contact_list.delete_contact(id=id)
            if result == "error":
                print("Invalid phone number.")
            else:
                print(f"Deleted: {result[id][0]} {result[id][1]}.")
        
        elif choice == "4":
            print("\n==================== CONTACT LIST ====================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for id, name in sorted(contact_list.data.items(), key=lambda x: (x[1][1], x[1][0])):
                print(f"{name[1]:<20} {name[0]:<20} {id}")
        
        elif choice == "5":
            filename = input("Enter new filename: ")
            contact_list = Contacts(filename=filename)
            print(f"Contact filename set to: {filename}")
        
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
