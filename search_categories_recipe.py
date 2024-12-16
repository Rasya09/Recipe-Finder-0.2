import mysql.connector

#fungsi untuk mencari resep berdasarkan kategori

def recipe_categories():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()
 
    print("\nSilahkan pilih kategori dibawah ini:")
    print("1. Makanan Berat")
    print("2. Makanan Pembuka")
    print("3. Makanan Penutup")
    print("4. Makanan Ringan")
    print("5. Minuman")

    kategori = input("Masukkan kategor yang ingin dicari: ")
    cursor.execute("SELECT id, title FROM recipes WHERE ingredients LIKE %s", (f"%{kategori}%",))
    recipes = cursor.fetchall()

    if recipes:
        print("\n--- Hasil Pencarian Resep ---")
        for recipe in recipes:
            print(f"ID: {recipe[0]}, Judul: {recipe[1]}")
    else:
        print("\nBelum ada resep dalam kategori tersebut.")

    cursor.close()
    conn.close()