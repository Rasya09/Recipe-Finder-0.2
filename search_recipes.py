import mysql.connector

# Fungsi untuk mencari resep berdasarkan bahan
def search_recipes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    bahan = input("Masukkan bahan yang ingin dicari (contoh: telur): ")
    cursor.execute("SELECT id, title FROM recipes WHERE ingredients LIKE %s", (f"%{bahan}%",))
    recipes = cursor.fetchall()

    if recipes:
        print("\n--- Hasil Pencarian Resep ---")
        for recipe in recipes:
            print(f"ID: {recipe[0]}, Judul: {recipe[1]}")
    else:
        print("\nTidak ada resep yang cocok dengan bahan tersebut.")

    cursor.close()
    conn.close()
