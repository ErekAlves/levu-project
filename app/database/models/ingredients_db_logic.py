import sqlite3

ID_COLUMN = 'id'
INGREDIENT_COLUMN = 'ingredient'
PRICE_COLUMN = 'price'
QUANTITY_COLUMN = 'quantity'
UNIT_COLUMN = 'unit'
UNIT_PRICE_COLUMN = 'unit_price'

def connect_db():
    conn = sqlite3.connect('Ingredients.db')
    cursor = conn.cursor()
    print('Connecting to database')
    return conn, cursor

def disconnect_db(conn):
    conn.close()
    print('Disconnecting from the database')

def create_ingredients_table(conn, cursor):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS ingredients (
            {ID_COLUMN} INTEGER PRIMARY KEY,
            {INGREDIENT_COLUMN} TEXT NOT NULL,
            {PRICE_COLUMN} REAL NOT NULL,
            {QUANTITY_COLUMN} REAL NOT NULL,
            {UNIT_COLUMN} TEXT NOT NULL,
            {UNIT_PRICE_COLUMN} REAL
        );
    """)
    conn.commit()
    print('BD successfully created')
    print('Database table "ingredients" successfully created')
