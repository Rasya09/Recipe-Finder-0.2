import mysql.connector
import bcrypt

# Fungsi untuk login dengan email
def login_user():
    # Koneksi ke MySQL dengan database yang sudah dibuat
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Username default XAMPP
        password="",  # Kosongkan jika tidak ada password
        database="rf"
    )
    cursor = conn.cursor()

    # Input email
    email = input("Masukkan email: ")

    # Input password
    password = input("Masukkan password: ")

    # Cek apakah email ada di database
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        # Cek apakah password sesuai dengan yang ada di database
        stored_password = user[2]  # Password yang ada di database (indeks ke-2)
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login berhasil!")
        else:
            print("Password salah!")
    else:
        print("Email tidak ditemukan!")

