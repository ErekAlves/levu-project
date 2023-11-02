import sqlite3

# Constantes para os nomes das colunas
ID_COLUMN = 'id'
INGREDIENT_COLUMN = 'ingredient'
PRICE_COLUMN = 'price'
QUANTITY_COLUMN = 'quantity'
UNIT_COLUMN = 'unit'

def connect_db():
    conn = sqlite3.connect('app/database/Ingredients.db')
    cursor = conn.cursor()
    print('Connecting to database')
    return conn, cursor

def disconnect_db(conn):
    conn.close()  # Corrigido: adicione os parênteses para fechar a conexão
    print('Disconnecting from the database')

def create_ingredients_table(conn, cursor):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS ingredients (
            {ID_COLUMN} INTEGER PRIMARY KEY,
            {INGREDIENT_COLUMN} TEXT NOT NULL,
            {PRICE_COLUMN} REAL NOT NULL,
            {QUANTITY_COLUMN} REAL NOT NULL,
            {UNIT_COLUMN} TEXT NOT NULL
        );
    """)
    conn.commit()
    print('BD successfully created')
    print('Database table "ingredients" successfully created')
