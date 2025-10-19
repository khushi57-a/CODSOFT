contacts = []

def add_contact():
    print("\n---Add New Contact---")
    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email: ")
    address=input("Enter Address: ")

    contact={"name" :name, "phone" :phone, "email" :email, "address" :address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    print("\n---Contact List---")
    if not contacts:
        print("No Contacts Found.")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(i, "." ,contact["name"],"- ",contact["phone"] )

def search_contact():
    print("\n---Search Contact---")
    keyword= input("Enter name or phone number to search: ")
    found = False

    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found: ")
            print("Name: ", contact["name"], "\nPhone: ", contact["phone"], "\nEmail: ",contact["email"], "\nAddress: ", contact["address"])
            found=True
            break

    if not found:
        print("No Matching contact found.")

def update_contact():
    print("\n---Update Contact---")
    name=input("Enter the name of the conntact to update: ")

    for contact in contacts:
        if contact["name"].lower()==name.lower():
            new_phone= input("new Phone Number: ")
            new_email= input("New Email: ")
            new_address= input("New Address: ")

            if new_phone:
                contact["phone"]= new_phone
            if new_email:
                contact["email"]= new_email
            if new_address:
                contact["address"]= new_address

            print("Contact Updated Successfully!")
            return
        
    print("Contact not found.")

def delete_contact():
    print("\n---Delete Contact---")
    name= input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("contact not found.")

def main():
    while True:
        print("\n-----CONTACT BOOK-----")
        print("1. Add contact")
        print("2. View contact details")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice=="1":
            add_contact()
        elif choice=="2":
            view_contacts()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            print("Exiting... Thanks for using contact management system.")
            break
        else:
            print("Invalid choice!")


main()
