import mysql.connector

# Koneksi ke MySQL tanpa database
conn = mysql.connector.connect(
    host="localhost",
    user="root",   # Username default XAMPP
    password=""    # Kosongkan jika tidak ada password
)

cursor = conn.cursor()

# Mengecek apakah database sudah ada
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

db_exists = False
for db in databases:
    if db[0] == 'rf':
        db_exists = True
        break

if not db_exists:
    # Membuat database jika belum ada
    cursor.execute("CREATE DATABASE rf")
    print("Database 'rf' berhasil dibuat.")
else:
    print("Database 'rf' sudah ada.")
