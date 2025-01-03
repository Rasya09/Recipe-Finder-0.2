import mysql.connector

# Fungsi untuk mengedit resep
def edit_recipe(recipe_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rf"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
    recipe = cursor.fetchone()

    if recipe:
        print(f"Resep yang akan diedit: Judul: {recipe[1]}, Bahan: {recipe[2]}, Instruksi: {recipe[3]}")
        new_title = input("Masukkan judul baru (kosongkan untuk tidak mengubah): ")
        new_ingredients = input("Masukkan bahan baru (kosongkan untuk tidak mengubah): ")
        new_instructions = input("Masukkan instruksi baru (kosongkan untuk tidak mengubah): ")
        new_cook_time = input("Masukkan waktu masak baru (kosongkan untuk tidak mengubah): ")

        # Update resep jika ada perubahan
        if new_title:
            cursor.execute("UPDATE recipes SET title = %s WHERE id = %s", (new_title, recipe_id))
        if new_ingredients:
            cursor.execute("UPDATE recipes SET ingredients = %s WHERE id = %s", (new_ingredients, recipe_id))
        if new_instructions:
            cursor.execute("UPDATE recipes SET instructions = %s WHERE id = %s", (new_instructions, recipe_id))
        if new_cook_time:
            cursor.execute("UPDATE recipes SET cook_time = %s WHERE id = %s", (new_cook_time, recipe_id))

        conn.commit()
        print("Resep berhasil diupdate!")
    else:
        print("Resep tidak ditemukan.")

    cursor.close()
    conn.close()
