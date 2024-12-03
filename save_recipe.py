import mysql.connector

# Fungsi untuk menyimpan resep ke daftar favorit user
def save_recipe(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    try:
        # Dapatkan user_id berdasarkan username
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if not user:
            print("User tidak ditemukan.")
            return

        user_id = user[0]

        # Tampilkan daftar resep yang tersedia
        cursor.execute("SELECT id, title FROM recipes")
        recipes = cursor.fetchall()

        if recipes:
            print("\n--- Daftar Resep ---")
            for recipe in recipes:
                print(f"ID: {recipe[0]}, Judul: {recipe[1]}")

            # Memilih resep untuk disimpan
            recipe_id = input("\nMasukkan ID resep yang ingin disimpan: ").strip()
            cursor.execute("SELECT id FROM recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()

            if not recipe:
                print("Resep tidak ditemukan.")
                return

            # Simpan resep ke tabel saved_recipes
            cursor.execute(
                "INSERT INTO saved_recipes (user_id, recipe_id) VALUES (%s, %s)",
                (user_id, recipe_id)
            )
            conn.commit()
            print("Resep berhasil disimpan ke daftar favorit!")
        else:
            print("Belum ada resep yang tersedia.")

    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
