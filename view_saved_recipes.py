import mysql.connector

# Fungsi untuk melihat daftar resep yang disimpan
def view_saved_recipes(username):
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

        # Ambil daftar resep yang disimpan oleh user
        cursor.execute("""
            SELECT r.id, r.title, r.cook_time
            FROM saved_recipes sr
            JOIN recipes r ON sr.recipe_id = r.id
            WHERE sr.user_id = %s
        """, (user_id,))
        saved_recipes = cursor.fetchall()

        if saved_recipes:
            print("\n--- Daftar Resep Favorit Anda ---")
            for recipe in saved_recipes:
                print(f"ID: {recipe[0]}, Judul: {recipe[1]}, Waktu Masak: {recipe[2]} menit")
        else:
            print("\nAnda belum menyimpan resep apapun.")

    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
