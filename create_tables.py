import mysql.connector

# Koneksi ke MySQL dengan database yang sudah dibuat
conn = mysql.connector.connect(
    host="localhost",
    user="root",   # Username default XAMPP
    password="",   # Kosongkan jika tidak ada password
    database="rf"  # Koneksi ke database yang sudah dibuat
)

cursor = conn.cursor()

# Membuat tabel users jika belum ada, dengan kolom baru
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    no_hp VARCHAR(15) NOT NULL,
    alamat TEXT NOT NULL
)
''')

conn.commit()
print("Tabel 'users' berhasil dibuat atau sudah ada.")
