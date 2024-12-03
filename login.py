import mysql.connector
import bcrypt

# Fungsi untuk login dengan email
def login_user():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    cursor.execute("SELECT username, password, role FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        stored_username, stored_password, role = user
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print(f"Login berhasil! Anda masuk sebagai {role}.")
            cursor.close()
            conn.close()
            return role, stored_username  # Kembalikan role dan username
        else:
            print("Password salah!")
    else:
        print("Email tidak ditemukan!")

    cursor.close()
    conn.close()
    return None, None  # Jika login gagal, kembalikan None

