import tkinter as tk
from tkinter import END, messagebox
from database.models.recipes_db_logic import connect_db, ID_COLUMN, RECIPES_COLUMN, CATEGORY_COLUMN, SUBCATEGORY_COLUMN
from widgets.functions import recipes_clean_fields

ID_COLUMN = 'id'
RECIPES_COLUMN = 'recipes'
CATEGORY_COLUMN = 'category'
SUBCATEGORY_COLUMN = 'subcategory'

conn, cursor = connect_db()

def set_master_window(master):
    messagebox._master = master

from tkinter import messagebox

def add_recipes(parent, lb_code, lb_recipe_name, Tipvar1, Tipvar2, recipes_list):
    code = lb_code.get()
    recipe = lb_recipe_name.get().title()
    category = Tipvar1.get()
    subcategory = Tipvar2.get()

    if not recipe or not category or subcategory == " ":
        messagebox.showinfo("Campo vazio", "Preencha todos os campos.", parent=parent)
        return

    cursor.execute(f"""
        SELECT {RECIPES_COLUMN} FROM Recipes WHERE {RECIPES_COLUMN} = ?;
    """, (recipe,))
    
    existing_recipe = cursor.fetchone()

    if existing_recipe:
        confirm = messagebox.askyesno("Duplicar Receita?", "a Receita já está na lista. Deseja duplicá-lo?", parent=parent)

        if not confirm:
            return

    cursor.execute(f"""
        INSERT INTO Recipes ({RECIPES_COLUMN},  {CATEGORY_COLUMN}, {SUBCATEGORY_COLUMN}) 
        VALUES (?, ?, ?);
    """, (recipe, category, subcategory))
    conn.commit()

    select_recipes(recipes_list)
    recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2)


def select_recipes(recipes_list):
    recipes_list.delete(*recipes_list.get_children())

    cursor.execute(f"""
        SELECT {ID_COLUMN}, {RECIPES_COLUMN}, {CATEGORY_COLUMN}, {SUBCATEGORY_COLUMN} from Recipes
        ORDER BY {ID_COLUMN} ASC;
    """)

    for row in cursor:
    
        row = list(row)
        recipes_list.insert("", END, values=row)

def search_recipes(lb_code, lb_recipe_name, Tipvar1, Tipvar2, recipes_list):

    recipes_list.delete(*recipes_list.get_children())
    lb_recipe_name.insert(END, '%')
    recipes = lb_recipe_name.get()
    category = Tipvar1.get()
    subcategory = Tipvar2.get()

    if recipes == '%' and category == ' ' and subcategory == ' ':
        cursor.execute(f"""
            SELECT {ID_COLUMN}, {RECIPES_COLUMN}, ({CATEGORY_COLUMN}), {SUBCATEGORY_COLUMN} from Recipes
            WHERE {RECIPES_COLUMN} LIKE '%s' ORDER BY {ID_COLUMN} """ % recipes)
        
    elif recipes == '%' and category != ' ' and subcategory != ' ':
        cursor.execute(f"""
            SELECT {ID_COLUMN}, {RECIPES_COLUMN}, ({CATEGORY_COLUMN}), {SUBCATEGORY_COLUMN} FROM Recipes
            WHERE {CATEGORY_COLUMN} LIKE ? AND {SUBCATEGORY_COLUMN} LIKE ?
            ORDER BY {CATEGORY_COLUMN}""", ('%' + category + '%', '%' + subcategory + '%'))

    elif recipes == '%' and category == ' ' and subcategory != ' ':
        cursor.execute(f"""
            SELECT {ID_COLUMN}, {RECIPES_COLUMN}, ({CATEGORY_COLUMN}), {SUBCATEGORY_COLUMN} from Recipes
            WHERE {SUBCATEGORY_COLUMN} LIKE '%s' ORDER BY {ID_COLUMN} """ % subcategory)

    elif recipes == '%' and category != ' ':
        cursor.execute(f"""
            SELECT {ID_COLUMN}, {RECIPES_COLUMN}, ({CATEGORY_COLUMN}), {SUBCATEGORY_COLUMN} from Recipes
            WHERE {CATEGORY_COLUMN} LIKE '%s' ORDER BY {ID_COLUMN} """ % category)
    elif recipes != '%':
        print('receita preenchida, categoria vazia, subcategoria preenchida')
        cursor.execute(f"""
            SELECT {ID_COLUMN}, {RECIPES_COLUMN}, ({CATEGORY_COLUMN}), {SUBCATEGORY_COLUMN} from Recipes
            WHERE {RECIPES_COLUMN} LIKE '%s' ORDER BY {ID_COLUMN} """ % recipes)

    search_list_recipe = cursor.fetchall() 
    for i in search_list_recipe:
        recipes_list.insert("", END, values=i)
    
    recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2)

def update_recipes( parent, lb_code, lb_recipe_name, Tipvar1, Tipvar2, recipes_list):
    code = lb_code.get()
    recipe = lb_recipe_name.get()
    category = Tipvar1.get()
    subcategory = Tipvar2.get() if Tipvar2.get() else ""

    if not recipe or not category or not subcategory:
        messagebox.showinfo("Campo vazio", "Preencha todos os campos.",  parent=parent)
        return
    
    cursor.execute(f"""
        UPDATE Recipes SET {RECIPES_COLUMN} = ?, {CATEGORY_COLUMN} = ?, {SUBCATEGORY_COLUMN} = ?
        WHERE {ID_COLUMN} = ? """, (recipe, category, subcategory, code))
    
    conn.commit()

    select_recipes(recipes_list)
    recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2)

def delete_recipes(parent, lb_code, lb_recipe_name, Tipvar1, Tipvar2, recipes_list):
    code = lb_code.get()
    recipe = lb_recipe_name.get()
    category = Tipvar1.get()
    subcategory = Tipvar2.get()

    if not code:
        messagebox.showinfo("Campo vazio", "Selecione uma receita para deletar.", parent=parent)
        return

    messagebox_result = messagebox.askyesno("Deletar Receita", "Tem certeza que deseja deletar a Receita?", parent=parent)

    if messagebox_result:
        cursor.execute(f"""
            DELETE FROM Recipes WHERE {ID_COLUMN} = ? """, (code,))
    
        conn.commit()
        recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2)
        select_recipes(recipes_list)
