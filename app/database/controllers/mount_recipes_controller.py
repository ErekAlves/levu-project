import tkinter as tk
from tkinter import END, messagebox
from database.models.recipes_db_logic import connect_db, FIRST_PREPARATION_COLUMN, SECOND_PREPARATION_COLUMN ,INGREDIENTS_RECIPE_COLUMN, QUANTITY_INGREDIENTS_COLUMN

FIRST_PREPARATION_COLUMN = 'first_preparation'
SECOND_PREPARATION_COLUMN = 'second_preparation'
INGREDIENTS_RECIPE_COLUMN = 'ingredients_list'
QUANTITY_INGREDIENTS_COLUMN = 'quantity'

conn, cursor = connect_db()

def set_master_window(master):
    messagebox._master = master

def add_ingredient_quantity(lb_ingredients, lb_first_preparation, lb_add_quantity):
    ingredients = lb_ingredients.get()
    quantity = lb_add_quantity.get()
    first_preparation = lb_first_preparation
    
    print(ingredients)
    print(quantity)
    print(first_preparation)



