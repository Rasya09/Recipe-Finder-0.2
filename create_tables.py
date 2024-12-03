import mysql.connector

# Koneksi ke MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rf"
)

cursor = conn.cursor()

# Array SQL Query
queries = [
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        no_hp VARCHAR(15),
        alamat TEXT,
        role ENUM('admin', 'chef', 'user') NOT NULL
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL,
        cook_time INT NOT NULL,
        created_by INT,
        FOREIGN KEY (created_by) REFERENCES users(id)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS reviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        recipe_id INT NOT NULL,
        rating INT CHECK (rating BETWEEN 1 AND 5),
        comment TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (recipe_id) REFERENCES recipes(id)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS favorites (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        recipe_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
        UNIQUE (user_id, recipe_id)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS recipe_categories (
        recipe_id INT NOT NULL,
        category_id INT NOT NULL,
        PRIMARY KEY (recipe_id, category_id),
        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS notifications (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        message TEXT NOT NULL,
        is_read BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS recipe_updates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        recipe_id INT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        update_details TEXT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id)
    )
    ''',
    '''
    CREATE TABLE saved_recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    recipe_id INT NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
    )
''',

]

# Eksekusi semua query
for query in queries:
    cursor.execute(query)

conn.commit()
cursor.close()
conn.close()

print("Semua tabel berhasil dibuat!")