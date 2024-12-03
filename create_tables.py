import mysql.connector

# Koneksi ke MySQL dengan database yang sudah dibuat
conn = mysql.connector.connect(
    host="localhost",
    user="root",   # Username default XAMPP
    password="",   # Kosongkan jika tidak ada password
    database="rf"  # Koneksi ke database yang sudah dibuat
)

cursor = conn.cursor()

# Membuat tabel users jika belum ada, dengan kolom role menggunakan ENUM
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    no_hp VARCHAR(15),
    alamat TEXT,
    role ENUM('admin', 'chef', 'user') NOT NULL,
    UNIQUE (email)
)
''')

conn.commit()
print("Tabel 'users' berhasil dibuat atau sudah ada.")
cursor.close()
conn.close()
