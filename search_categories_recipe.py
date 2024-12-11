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
    while True:
        print("\nSilahkan pilih kategori dibawah ini:")
        print("1. Makanan Berat")
        print("2. Makanan Pembuka")
        print("3. Makanan Penutup")
        print("4. Makanan Ringan")
        print("5. Minuman")
        pilih_kategori= input("Pilih opsi (1/2/3/4/5): ").strip()

        cursor.execute("SELECT id, title, cook_time FROM recipes")
        recipe_categories = cursor.fetchall()

        if recipe_categories:
            print("\n--- Daftar Resep ---")
            for recipe in recipe_categories:
                print(f"ID: {recipe[0]}, Judul: {recipe[1]}, Waktu Masak: {recipe[2]} menit")
        else:
            print("\nBelum ada resep yang tersedia.")

        cursor.close()
        conn.close()

