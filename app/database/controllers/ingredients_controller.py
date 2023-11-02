import tkinter as tk
from tkinter import END
from database.models.ingredients_db_logic import connect_db, disconnect_db, ID_COLUMN, INGREDIENT_COLUMN, PRICE_COLUMN, QUANTITY_COLUMN, UNIT_COLUMN
from widgets.ingredients_widgets import clean_fields

ID_COLUMN = 'id'
INGREDIENT_COLUMN = 'ingredient'
PRICE_COLUMN = 'price'
QUANTITY_COLUMN = 'quantity'
UNIT_COLUMN = 'unit'

conn, cursor = connect_db()

def add_ingredients(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):
    code = lb_code.get()
    ingredient = lb_product.get()
    price = lb_price.get()
    quantity = lb_quantity.get()
    unit = Tipvar.get()
    
    cursor.execute(f"""
        INSERT INTO Ingredients ({INGREDIENT_COLUMN}, {PRICE_COLUMN}, {QUANTITY_COLUMN}, {UNIT_COLUMN}) 
        VALUES (?, ?, ?, ?)
    """, (ingredient, price, quantity, unit))
    conn.commit()

    select_ingredients(ingredients_list)
    clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)

def select_ingredients(ingredients_list):
    ingredients_list.delete(*ingredients_list.get_children())

    cursor.execute(f"""
        SELECT {ID_COLUMN}, {INGREDIENT_COLUMN}, {PRICE_COLUMN}, {QUANTITY_COLUMN}, {UNIT_COLUMN} from Ingredients
        ORDER BY {ID_COLUMN} ASC;
    """)

    for row in cursor:
        ingredients_list.insert("", END, values=row)

def delete_ingredients(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):
    code = lb_code.get()
    ingredient = lb_product.get()
    price = lb_price.get()
    quantity = lb_quantity.get()
    unit = Tipvar.get()

    connect_db()

    cursor.execute(f"""
        DELETE FROM Ingredients WHERE {ID_COLUMN} = ? """, (code,))
    
    conn.commit()
    clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)
    select_ingredients(ingredients_list)
