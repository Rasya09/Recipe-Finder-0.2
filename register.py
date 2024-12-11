import mysql.connector
import bcrypt

# Fungsi untuk memeriksa validitas email
def valid_email(email):
    return email.endswith('@gmail.com')

# Fungsi untuk mendaftarkan user
def register_user():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    username = input("Masukkan username: ")
    email = input("Masukkan email (@gmail.com): ")
    while "@gmail.com" not in email or email.count('@') != 1:
        print("Email harus menggunakan format @gmail.com!")
        email = input("Masukkan email (@gmail.com): ")

    password = input("Masukkan password (minimal 8 karakter): ")
    while len(password) < 8:
        print("Password harus minimal 8 karakter!")
        password = input("Masukkan password: ")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Pilih role (user atau chef)
    print("Pilih peran:")
    print("1. User")
    print("2. Chef")
    role_choice = input("Masukkan pilihan (1/2): ")

    role = "user" if role_choice == '1' else "chef"

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
            (username, email, hashed_password,  role)
        )
        conn.commit()
        print("Registrasi berhasil!")
    except mysql.connector.IntegrityError:
        print("Email sudah digunakan!")
    finally:
        cursor.close()
        conn.close()


