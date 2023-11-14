import sqlite3

ID_COLUMN = 'id'
RECIPES_COLUMN = 'recipes'
CATEGORY_COLUMN = 'category'
SUBCATEGORY_COLUMN = 'subcategory'
INGREDIENTS_RECIPE_COLUMN = 'ingredients_recipe'
QUANTITY_INGREDIENTS_COLUMN = 'quantity_ingredients'
FIRST_PREPARATION_COLUMN = 'first_preparation'
SECOND_PREPARATION_COLUMN = 'second_preparation' 

def connect_db():
    conn = sqlite3.connect('Mount_Recipes.db')
    cursor = conn.cursor()
    print('Connecting to database')
    return conn, cursor

def disconnect_db(conn):
    conn.close() 
    print('Disconnecting from the database')

def create_recipes_table(conn, cursor):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS Recipes (
            {ID_COLUMN} INTEGER PRIMARY KEY,
            {RECIPES_COLUMN} TEXT NOT NULL,
            {CATEGORY_COLUMN} TEXT NOT NULL,
            {SUBCATEGORY_COLUMN} TEXT NOT NULL
        );
    """)
    conn.commit()
    print('Database table "Recipes" successfully created')

def create_mount_recipes_table(conn, cursor):
    create_recipes_table(conn, cursor) 

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS Mount_Recipes (
            {ID_COLUMN} INTEGER PRIMARY KEY,
            {RECIPES_COLUMN} TEXT,
            {CATEGORY_COLUMN} TEXT,
            {SUBCATEGORY_COLUMN} TEXT,
            {INGREDIENTS_RECIPE_COLUMN} TEXT NOT NULL,
            {QUANTITY_INGREDIENTS_COLUMN} INTEGER NOT NULL,
            {FIRST_PREPARATION_COLUMN} TEXT NOT NULL,
            {SECOND_PREPARATION_COLUMN} TEXT NOT NULL,
            FOREIGN KEY ({RECIPES_COLUMN}) REFERENCES Recipes({RECIPES_COLUMN}),
            FOREIGN KEY ({CATEGORY_COLUMN}) REFERENCES Recipes({CATEGORY_COLUMN}),
            FOREIGN KEY ({SUBCATEGORY_COLUMN}) REFERENCES Recipes({SUBCATEGORY_COLUMN})
        );
    """)
    conn.commit()
    print('Database table "Mount_Recipes" successfully created with foreign keys')

conn, cursor = connect_db()

create_mount_recipes_table(conn, cursor)

disconnect_db(conn)

print('BD successfully created')
print('Database tables "Recipes" and "Mount Recipes" successfully created')
