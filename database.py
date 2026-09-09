import json
import os
import shutil
from datetime import datetime

DB = "data/accounts.json"


def init_db():
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/backup", exist_ok=True)

    if not os.path.exists(DB):
        with open(DB, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_accounts():
    with open(DB, "r", encoding="utf-8") as f:
        return json.load(f)


def save_accounts(accounts):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=4)


def add_account(name, phone, note):
    accounts = load_accounts()

    account = {
        "id": len(accounts) + 1,
        "name": name,
        "phone": phone,
        "note": note
    }

    accounts.append(account)

    save_accounts(accounts)

    print("\n✅ Saved.")


def show_accounts():
    accounts = load_accounts()

    if not accounts:
        print("\nNo Account Found.")
        return

    print("\n====== Accounts ======")

    for acc in accounts:
        print(f"""
ID    : {acc['id']}
Name  : {acc['name']}
Phone : {acc['phone']}
Note  : {acc['note']}
----------------------------
""")


def delete_account(account_id):
    accounts = load_accounts()

    new_accounts = []

    for acc in accounts:
        if acc["id"] != account_id:
            new_accounts.append(acc)

    for i, acc in enumerate(new_accounts, start=1):
        acc["id"] = i

    save_accounts(new_accounts)

    print("\n✅ Deleted.")


def edit_account(account_id, name, phone, note):
    accounts = load_accounts()

    for acc in accounts:
        if acc["id"] == account_id:
            acc["name"] = name
            acc["phone"] = phone
            acc["note"] = note
            break

    save_accounts(accounts)

    print("\n✅ Updated.")


def search_account(keyword):
    accounts = load_accounts()

    keyword = keyword.lower()

    found = False

    for acc in accounts:
        if (
            keyword in acc["name"].lower()
            or keyword in acc["phone"]
            or keyword in acc["note"].lower()
        ):
            found = True

            print(f"""
ID    : {acc['id']}
Name  : {acc['name']}
Phone : {acc['phone']}
Note  : {acc['note']}
----------------------------
""")

    if not found:
        print("\nNo Account Found.")


def backup_database():
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")

    shutil.copy(
        DB,
        f"data/backup/{filename}"
    )

    print("\n✅ Backup Created.")


def list_backups():
    files = os.listdir("data/backup")

    if not files:
        print("\nNo Backup.")
        return

    print("\n====== Backups ======")

    for file in files:
        print(file)


def restore_database(filename):
    source = f"data/backup/{filename}"

    if not os.path.exists(source):
        print("\nBackup Not Found.")
        return

    shutil.copy(source, DB)

    print("\n✅ Database Restored.")
