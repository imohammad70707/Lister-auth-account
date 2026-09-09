from database import *

init_db()

while True:

    print("""
===== Rubika Manager =====

1. Add Account
2. Show Accounts
3. Delete Account
4. Edit Account
5. Search Account
6. Backup
7. Restore
8. Exit
""")

    choice = input("Select: ")

    if choice == "1":
        name = input("Name : ")
        phone = input("Phone: ")
        note = input("Note : ")

        add_account(name, phone, note)

        print("\n✅ Saved.")

    elif choice == "2":
        show_accounts()

    elif choice == "3":
        account_id = int(input("ID: "))
        delete_account(account_id)

    elif choice == "4":
        account_id = int(input("ID: "))

        name = input("New Name : ")
        phone = input("New Phone: ")
        note = input("New Note : ")

        edit_account(account_id, name, phone, note)

    elif choice == "5":
        keyword = input("Search: ")
        search_account(keyword)

    elif choice == "6":
        backup_database()

    elif choice == "7":
        list_backups()

        filename = input("\nBackup Name: ")
        restore_database(filename)

    elif choice == "8":
        print("\nGood Bye.")
        break

    else:
        print("\nInvalid Option.\n")
