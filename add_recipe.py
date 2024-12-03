import mysql.connector

# Fungsi untuk menambahkan resep
def add_recipe(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    # Mendapatkan user ID berdasarkan username
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()
    if not user_id:
        print("User tidak ditemukan.")
        return

    print("\n--- Tambah Resep ---")
    title = input("Masukkan judul resep: ")
    ingredients = input("Masukkan daftar bahan (pisahkan dengan koma): ")
    instructions = input("Masukkan instruksi masak: ")
    cook_time = input("Masukkan waktu masak (dalam menit): ")

    try:
        cursor.execute(
            "INSERT INTO recipes (title, ingredients, instructions, cook_time, created_by) VALUES (%s, %s, %s, %s, %s)",
            (title, ingredients, instructions, cook_time, user_id[0])
        )
        conn.commit()
        print("Resep berhasil ditambahkan!")
    except Exception as e:
        print("Gagal menambahkan resep:", e)
    finally:
        cursor.close()
        conn.close()
