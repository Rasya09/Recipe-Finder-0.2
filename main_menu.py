from register import register_user
from login import login_user
import sys

def main_menu():
    while True:
        print("\n--- Recipe Finder ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            register_user()
        elif pilihan == '2':
            login_user()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Recipe Finder!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
