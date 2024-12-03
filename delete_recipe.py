import mysql.connector

def delete_recipe(recipe_id):
    try:
        # Koneksi ke database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=''
        )
        cursor = connection.cursor()

        # Menghapus data di tabel saved_recipes yang terkait dengan resep
        cursor.execute("DELETE FROM saved_recipes WHERE recipe_id = %s", (recipe_id,))
        print(f"Data resep dengan ID {recipe_id} telah dihapus dari daftar favorit.")

        # Menghapus resep dari tabel recipes
        cursor.execute("DELETE FROM recipes WHERE id = %s", (recipe_id,))
        print(f"Resep dengan ID {recipe_id} telah dihapus.")

        # Commit perubahan ke database
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
