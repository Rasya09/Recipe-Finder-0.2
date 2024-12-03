from register import register_user
from login import login_user
import sys

# Menu untuk user
def user_menu(username):
    while True:
        print(f"\n--- Selamat datang, {username} (User) ---")
        print("1. Lihat resep")
        print("2. Keluar")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == '1':
            print("Fitur lihat resep belum tersedia.")
        elif pilihan == '2':
            print("Keluar dari akun user.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu untuk chef
def chef_menu(username):
    while True:
        print(f"\n--- Selamat datang, {username} (Chef) ---")
        print("1. Tambah resep")
        print("2. Lihat resep")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            print("Fitur tambah resep belum tersedia.")
        elif pilihan == '2':
            print("Fitur lihat resep belum tersedia.")
        elif pilihan == '3':
            print("Keluar dari akun chef.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu utama untuk login atau register
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
            role, username = login_user()
            if role == 'user':
                user_menu(username)
            elif role == 'chef':
                chef_menu(username)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Recipe Finder!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
