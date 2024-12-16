import sqlite3

conn = sqlite3.connect("marketplus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id)
)
""")
print("Tables created!")

cursor.executemany("""
INSERT OR IGNORE INTO categories (name) VALUES (?)
""", [
    ("Побутова техніка",),
    ("Новорічні товари",),
    ("Дім та декор",)
])

cursor.executemany("""
INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)
""", [
    ("Пральна машинка", "Пральна машинка LG з сушкою.", 15000, 1),
    ("Холодильник", "Холодильник Samsung з сухою заморозкою", 30000, 1),
    ("Ялинкові кулі", "Ялинкові кулі червоні, набір з 20шт", 450, 2),
    ("Плед", "Плед вовняний в червону клітинку", 750, 3)
])
print("Data added!")

cursor.execute("""
SELECT 
    products.name AS product_name,
    products.description,
    products.price,
    categories.name AS category_name
FROM 
    products
JOIN 
    categories
ON 
    products.category_id = categories.id
""")
results = cursor.fetchall()

print("Products with categories:")
for row in results:
    print(f"Product: {row[0]}, Description: {row[1]}, Price: {row[2]} uah, Category: {row[3]}")

conn.commit()
conn.close()
