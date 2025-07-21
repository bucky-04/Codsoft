contacts = []

def show_menu():
    print("\n📱 Contact Book - Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n➕ Add New Contact")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"✅ Contact for {name} added successfully.")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📇 All Saved Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n🔍 Search Contact")
    keyword = input("Enter name or phone number: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n✅ Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("❌ No matching contact found.")

def update_contact():
    print("\n✏️ Update Contact")
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep existing info.")
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New email [{contact['email']}]: ") or contact['email']
            new_address = input(f"New address [{contact['address']}]: ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("✅ Contact updated successfully.")
            return
    print("❌ Contact not found.")

def delete_contact():
    print("\n🗑️ Delete Contact")
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("✅ Contact deleted successfully.")
            return
    print("❌ Contact not found.")

def main():
    print("📘 Welcome to Your Personal Contact Book")
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n👋 Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
