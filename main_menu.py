from register import register_user
from login import login_user
from view_recipes import view_recipes
from add_recipe import add_recipe
from search_recipes import search_recipes
from save_recipe import save_recipe  # Fungsi untuk menyimpan resep
from view_saved_recipes import view_saved_recipes  # Fungsi untuk melihat resep favorit
from edit_recipe import edit_recipe  # Import fungsi edit resep
from delete_recipe import delete_recipe  # Import fungsi delete resep
import sys

# Menu untuk user
def user_menu(username):
    while True:
        print(f"\n--- Selamat datang, {username} (User) ---")
        print("1. Lihat resep")
        print("2. Cari resep berdasarkan bahan")
        print("3. Simpan resep ke daftar favorit")
        print("4. Lihat daftar resep favorit")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ").strip()

        if pilihan == '1':
            view_recipes()  # Fungsi untuk melihat daftar resep
        elif pilihan == '2':
            search_recipes()  # Fungsi untuk mencari resep
        elif pilihan == '3':
            save_recipe(username)  # Fungsi untuk menyimpan resep
        elif pilihan == '4':
            view_saved_recipes(username)  # Fungsi untuk melihat daftar resep favorit
        elif pilihan == '5':
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
        print("3. Edit resep")
        print("4. Hapus resep")
        print("5. Simpan resep ke daftar favorit")
        print("6. Lihat daftar resep favorit")
        print("7. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5/6/7): ").strip()

        if pilihan == '1':
            add_recipe(username)  # Fungsi untuk menambahkan resep
        elif pilihan == '2':
            view_recipes()  # Fungsi untuk melihat daftar resep
        elif pilihan == '3':
            recipe_id = input("Masukkan ID resep yang ingin diedit: ").strip()
            try:
                edit_recipe(int(recipe_id))  # Memanggil fungsi edit resep dengan ID resep
            except ValueError:
                print("ID resep tidak valid, silakan coba lagi.")
        elif pilihan == '4':
            recipe_id = input("Masukkan ID resep yang ingin dihapus: ").strip()
            try:
                delete_recipe(int(recipe_id))  # Memanggil fungsi delete resep dengan ID resep
            except ValueError:
                print("ID resep tidak valid, silakan coba lagi.")
        elif pilihan == '5':
            save_recipe(username)  # Fungsi untuk menyimpan resep
        elif pilihan == '6':
            view_saved_recipes(username)  # Fungsi untuk melihat daftar resep favorit
        elif pilihan == '7':
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
        pilihan = input("Pilih opsi (1/2/3): ").strip()

        if pilihan == '1':
            register_user()  # Fungsi untuk registrasi user baru
        elif pilihan == '2':
            role, username = login_user()  # Login dan mendapatkan role pengguna
            if role == 'user':
                user_menu(username)  # Menu untuk user
            elif role == 'chef':
                chef_menu(username)  # Menu untuk chef
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Recipe Finder!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
