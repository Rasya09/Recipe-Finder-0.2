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

    try:
        # Mendapatkan user ID berdasarkan username
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        user_id = cursor.fetchone()
        if not user_id:
            print("User tidak ditemukan.")
            return

        print("\n--- Tambah Resep ---")
        title = input("Masukkan judul resep: ")
        
        # Menampilkan daftar kategori makanan
        categories_map = {
            '1': "Makanan Berat",
            '2': "Makanan Pembuka",
            '3': "Makanan Penutup",
            '4': "Makanan Ringan",
            '5': "Minuman"
        }

        categories = None
        while not categories:  # Loop sampai input valid
            print("\nPilih kategori makanan:")
            for key, value in categories_map.items():
                print(f"{key}. {value}")
            categories_choice = input("Masukkan pilihan (1/2/3/4/5): ")

            categories = categories_map.get(categories_choice)
            if not categories:
                print("Pilihan kategori tidak valid. Silakan coba lagi.")

        ingredients = input("Masukkan daftar bahan (pisahkan dengan koma): ")
        instructions = input("Masukkan instruksi masak: ")
        cook_time = input("Masukkan waktu masak (dalam menit): ")

        # Memasukkan data ke tabel recipes
        cursor.execute(
            "INSERT INTO recipes (title, categories, ingredients, instructions, cook_time, created_by) VALUES (%s, %s, %s, %s, %s, %s)",
            (title, categories, ingredients, instructions, cook_time, user_id[0])
        )
        conn.commit()
        print("Resep berhasil ditambahkan!")

    except Exception as e:
        print("Gagal menambahkan resep:", e)

    finally:
        cursor.close()
        conn.close()