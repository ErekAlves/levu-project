import tkinter as tk
from tkinter import END, messagebox
from database.models.ingredients_db_logic import connect_db, ID_COLUMN, INGREDIENT_COLUMN, PRICE_COLUMN, QUANTITY_COLUMN, UNIT_COLUMN
from widgets.functions import ingredients_clean_fields

ID_COLUMN = 'id'
INGREDIENT_COLUMN = 'ingredient'
PRICE_COLUMN = 'price'
QUANTITY_COLUMN = 'quantity'
UNIT_COLUMN = 'unit'
UNIT_PRICE_COLUMN = 'unit_price'

conn, cursor = connect_db()

def set_master_window(master):
    messagebox._master = master

from tkinter import messagebox

def calculate_unit_price(ingredient, price, quantity, unit):
    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        return None

    unit_price = 0

    if unit.lower() == "kg":
        unit_price = price / (quantity * 1000)
    elif unit.lower() == "g":
        unit_price = (price / quantity)
    elif unit.lower() == "l":
        unit_price = price / (quantity * 1000)
    elif unit.lower() == "ml":
        unit_price = (price / quantity)
    elif unit.lower() == "und":
        unit_price = price / quantity

    unit_price = round(unit_price, 4)  

    return unit_price


def add_ingredients(parent, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):
    code = lb_code.get()
    ingredient = lb_product.get().title()
    price = lb_price.get()
    quantity = lb_quantity.get()
    unit = Tipvar.get()


    if not ingredient or not price or not quantity or unit == " ":
        messagebox.showinfo("Campo vazio", "Preencha todos os campos.", parent=parent)
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showinfo("Valor inválido", "O campo Preço deve conter um valor numérico.", parent=parent)
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showinfo("Valor inválido", "O campo Quantidade deve conter apenas números inteiros.", parent=parent)
        return
    
    unit_price = calculate_unit_price(ingredient, price, quantity, unit)
    
    if unit_price is not None:
        cursor.execute(f"""
            UPDATE Ingredients SET {UNIT_PRICE_COLUMN} = COALESCE({UNIT_PRICE_COLUMN}, 0) + ?
            WHERE {ID_COLUMN} = ?;
        """, (unit_price, ingredient))
        conn.commit()

    cursor.execute(f"""
        SELECT {INGREDIENT_COLUMN} FROM Ingredients WHERE {INGREDIENT_COLUMN} = ?;
    """, (ingredient,))
    
    existing_ingredient = cursor.fetchone()

    if existing_ingredient:
        confirm = messagebox.askyesno("Duplicar Ingrediente?", "O ingrediente já está na lista. Deseja duplicá-lo?", parent=parent)

        if not confirm:
            return

    cursor.execute(f"""
        INSERT INTO Ingredients ({INGREDIENT_COLUMN}, {PRICE_COLUMN}, {QUANTITY_COLUMN}, {UNIT_COLUMN}, {UNIT_PRICE_COLUMN}) 
        VALUES (?, ?, ?, ?, ?);
    """, (ingredient, price, quantity, unit, unit_price))
    conn.commit()

    select_ingredients(ingredients_list)
    ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)

def select_ingredients(ingredients_list):
    ingredients_list.delete(*ingredients_list.get_children())

    cursor.execute(f"""
        SELECT {ID_COLUMN}, {INGREDIENT_COLUMN}, {PRICE_COLUMN}, {QUANTITY_COLUMN}, {UNIT_COLUMN}, {UNIT_PRICE_COLUMN} from Ingredients
        ORDER BY {ID_COLUMN} ASC;
    """)

    for row in cursor:
        row = list(row)
        row[3] = int(row[3])
        row[2] = f'{row[2]:.2f}' if row[2] is not None else '' 
        row[5] = f'R$ {row[5]:.4f}' if row[5] is not None else ''
        ingredients_list.insert("", END, values=row)

def search_ingredients(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):

    ingredients_list.delete(*ingredients_list.get_children())
    lb_product.insert(END, '%')
    ingredients = lb_product.get()

    cursor.execute(f"""
        SELECT {ID_COLUMN}, {INGREDIENT_COLUMN}, {PRICE_COLUMN}, CAST({QUANTITY_COLUMN} AS INTEGER), {UNIT_COLUMN}, {UNIT_PRICE_COLUMN}  from Ingredients
        WHERE {INGREDIENT_COLUMN} LIKE '%s' ORDER BY {ID_COLUMN} ASC """ % ingredients)

    search_list_ingredient = cursor.fetchall() 
    for i in search_list_ingredient:
        i = list(i)
        i[2] = f'{i[2]:.2f}' if i[2] is not None else ''
        i[5] = f'R$ {i[5]:.4f}' if i[5] is not None else ''
        ingredients_list.insert("", END, values=i)

    ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)


def update_ingredients(parent, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):
    code = lb_code.get()
    ingredient = lb_product.get()
    price = lb_price.get()
    quantity = lb_quantity.get()
    unit = Tipvar.get() if Tipvar.get() else ""

    if not ingredient or not price or not quantity or not unit:
        messagebox.showinfo("Campo vazio", "Preencha todos os campos.", parent=parent)
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showinfo("Valor inválido", "O campo Price deve conter um número real.", parent=parent)
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showinfo("Valor inválido", "O campo Quantidade deve conter apenas números inteiros.", parent=parent)
        return

    unit_price = calculate_unit_price(ingredient, price, quantity, unit)

    if unit_price is not None:
        cursor.execute(f"""
            UPDATE Ingredients SET {INGREDIENT_COLUMN} = ?, {PRICE_COLUMN} = ?, {QUANTITY_COLUMN} = ?, {UNIT_COLUMN} = ?, {UNIT_PRICE_COLUMN} = ?
            WHERE {ID_COLUMN} = ? """, (ingredient, price, quantity, unit, unit_price, code))
    else:
        cursor.execute(f"""
            UPDATE Ingredients SET {INGREDIENT_COLUMN} = ?, {PRICE_COLUMN} = ?, {QUANTITY_COLUMN} = ?, {UNIT_COLUMN} = ?
            WHERE {ID_COLUMN} = ? """, (ingredient, price, quantity, unit, code))

    conn.commit()

    select_ingredients(ingredients_list)
    ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)

def delete_ingredients(parent, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):
    code = lb_code.get()
    ingredient = lb_product.get()
    price = lb_price.get()
    quantity = lb_quantity.get()
    unit = Tipvar.get()

    if not code:
        messagebox.showinfo("Campo vazio", "Selecione um ingrediente para deletar.", parent=parent)
        return

    messagebox_result = messagebox.askyesno("Deletar ingrediente", "Tem certeza que deseja deletar o ingrediente?", parent=parent)

    if messagebox_result:
        cursor.execute(f"""
            DELETE FROM Ingredients WHERE {ID_COLUMN} = ? """, (code,))

        conn.commit()
        ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)
        select_ingredients(ingredients_list)


def update_combobox(combo_ingredientes):
    cursor.execute(f"""
        SELECT {INGREDIENT_COLUMN} FROM Ingredients ORDER BY {INGREDIENT_COLUMN} ASC;
    """)
    ingredientes_disponiveis = [row[0] for row in cursor.fetchall()]
    combo_ingredientes['values'] = ingredientes_disponiveis


