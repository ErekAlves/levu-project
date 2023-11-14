import tkinter as tk
from tkinter import Frame, Label, Entry, Button, StringVar, OptionMenu, ttk
from widgets.functions import ingredients_clean_fields, ingredients_on_double_click
from database.controllers.ingredients_controller import add_ingredients, select_ingredients ,search_ingredients ,update_ingredients , delete_ingredients
lb_code = None
lb_product = None
lb_price = None
lb_quantity = None
Tipvar = None
ingredients_list = None

def model_create_label_entry(parent, text, x, y, width, height, is_bold=False):
    label = Label(parent, text=text, font=('Helvetica', 10, 'bold' if is_bold else ''))
    label.place(relx=x, rely=y)
    entry = Entry(parent, font=('Helvetica', 12))
    entry.place(relx=x, rely=y + 0.15, width=width, height=height)
    return entry
    
def model_create_button(parent, text, x, y, command=None):
    button = Button(parent, text=text, highlightthickness=0, font=('Helvetica', 12), command=command)
    button.place(relx=x, rely=y, width=80, height=30)
    return button

def create_buttons(frame):
    bt_search_ingredients = model_create_button(frame, 'Buscar', 0.72, 0.4,command=lambda: search_ingredients(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list))
    bt_clear_ingredients = model_create_button(frame, 'Limpar', 0.9, 0.2, command=lambda: ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar))
    bt_save_ingredients = model_create_button(frame, 'Adicionar', 0.82, 0.6, command=lambda: add_ingredients(frame, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list))
    bt_edit_ingredients = model_create_button(frame, 'Editar', 0.82, 0.2,command=lambda: update_ingredients(frame, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list))
    bt_delete_ingredients = model_create_button(frame, 'Excluir', 0.9, 0.6,command=lambda: delete_ingredients(frame, lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list))

def create_labels_and_entries(frame):
    global lb_code, lb_product, lb_price, lb_quantity 
    lb_code = model_create_label_entry(frame, 'Código', 0.03, 0.25, 65, 30, is_bold=True)
    lb_product = model_create_label_entry(frame, 'Produto', 0.14, 0.25, 250, 30, is_bold=True)
    lb_price = model_create_label_entry(frame, 'Preço', 0.40, 0.25, 65, 30, is_bold=True)
    lb_quantity = model_create_label_entry(frame, 'Qtd', 0.50, 0.25, 65, 30, is_bold=True)

def create_option_menu(frame):
    global Tipvar
    Tipvar = StringVar(frame)
    TipV = ("kg", "g", "L", "ml", "und" )
    Tipvar.set(" ")
    lb_popupMenu = model_create_label_entry(frame, 'Und', 0.60, 0.25, 65, 30, is_bold=True)
    popupMenu = OptionMenu(frame, Tipvar, *TipV)
    popupMenu.place(relx=0.60, rely=0.4, width=65, height=30)
    popupMenu.configure(highlightthickness=0, font=('Helvetica', 12), borderwidth=1)


def configure_estyle_treeview(treeview):
    style = ttk.Style()
    style.configure("Treeview.Treeview", font=('Helvetica', 12))
    
    treeview.configure(style="Treeview.Treeview")

def format_quantity(value):
    return str(int(value))

def create_ingredients_list(frame):
    global ingredients_list
    ingredients_list = ttk.Treeview(frame, columns=('col0', 'col1', 'col2', 'col3', 'col4', 'col5','col6'))
    ingredients_list.heading('#0')
    ingredients_list.heading('#1', text='Código')
    ingredients_list.heading('#2', text='Ingrediente')
    ingredients_list.heading('#3', text='Preço')
    ingredients_list.heading('#4', text='Quantidade')
    ingredients_list.heading('#5', text='Unidade')
    ingredients_list.heading('#6', text='Vlr. Und')
    ingredients_list.column('#0', width=0)
    ingredients_list.column('#1', width=100, anchor='center')
    ingredients_list.column('#2', width=250)
    ingredients_list.column('#3', width=180, anchor='center')
    ingredients_list.column('#4', width=180, anchor='center')
    ingredients_list.column('#5', width=180, anchor='center')
    ingredients_list.column('#6', width=200, anchor='center')
    ingredients_list.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
    
    scroll_list = ttk.Scrollbar(frame, orient='vertical')
    ingredients_list.configure(yscrollcommand=scroll_list.set)
    scroll_list.config(command=ingredients_list.yview)
    scroll_list.place(relx=0.98, rely=0.1, relheight=0.85, width=20)
    ingredients_list.bind("<Double-1>", lambda event: ingredients_on_double_click(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list))
    select_ingredients(ingredients_list)
    configure_estyle_treeview(ingredients_list)

def ingredients_frame(parent):
    register_frame_ingredients = Frame(parent)
    register_frame_ingredients.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.25)
    list_frame_ingredients = Frame(parent)
    list_frame_ingredients.place(relx=0.01, rely=0.29, relwidth=0.98, relheight=0.69)

    create_buttons(register_frame_ingredients)
    create_labels_and_entries(register_frame_ingredients)
    create_option_menu(register_frame_ingredients)
    create_ingredients_list(list_frame_ingredients)
