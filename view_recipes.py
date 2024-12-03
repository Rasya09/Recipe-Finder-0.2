import mysql.connector

# Fungsi untuk melihat daftar resep
def view_recipes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, cook_time FROM recipes")
    recipes = cursor.fetchall()

    if recipes:
        print("\n--- Daftar Resep ---")
        for recipe in recipes:
            print(f"ID: {recipe[0]}, Judul: {recipe[1]}, Waktu Masak: {recipe[2]} menit")
    else:
        print("\nBelum ada resep yang tersedia.")

    cursor.close()
    conn.close()
