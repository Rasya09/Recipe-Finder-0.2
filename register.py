import mysql.connector
import bcrypt

# Fungsi untuk memeriksa validitas email
def valid_email(email):
    return email.endswith('@gmail.com')

# Fungsi untuk mendaftarkan user
def register_user():
    # Koneksi ke MySQL dengan database yang sudah dibuat
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Username default XAMPP
        password="",  # Kosongkan jika tidak ada password
        database="rf"
    )
    cursor = conn.cursor()

    # Input username
    username = input("Masukkan username: ")

    # Validasi password dan minta input ulang jika tidak valid
    while True:
        password = input("Masukkan password (min 8 karakter): ")

        if len(password) < 8:
            print("Password harus minimal 8 karakter!")
        else:
            break

    # Hash password menggunakan bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Validasi email dan minta input ulang jika tidak valid
    while True:
        email = input("Masukkan email: ")

        if not valid_email(email):
            print("Email harus berformat @gmail.com!")
        else:
            # Cek apakah email sudah terdaftar
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                print("Email sudah terdaftar!")
            else:
                break

    # Input no_hp dan alamat opsional
    no_hp = input("Masukkan nomor HP (opsional): ")
    alamat = input("Masukkan alamat (opsional): ")

    # Menyimpan data ke database
    cursor.execute('''
    INSERT INTO users (username, password, email, no_hp, alamat)
    VALUES (%s, %s, %s, %s, %s)
    ''', (username, hashed_password, email, no_hp, alamat))

    conn.commit()
    print("Pendaftaran berhasil! User baru telah ditambahkan.")

