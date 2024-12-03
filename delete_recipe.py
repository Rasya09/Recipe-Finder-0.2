import mysql.connector

# Fungsi untuk menghapus resep
def delete_recipe():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    recipe_id = input("Masukkan ID resep yang ingin dihapus: ")
    cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
    recipe = cursor.fetchone()

    if recipe:
        confirmation = input(f"Apakah Anda yakin ingin menghapus resep '{recipe[1]}'? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute("DELETE FROM recipes WHERE id = %s", (recipe_id,))
            conn.commit()
            print("Resep berhasil dihapus!")
        else:
            print("Penghapusan resep dibatalkan.")
    else:
        print("Resep tidak ditemukan.")

    cursor.close()
    conn.close()
