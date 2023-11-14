import tkinter as tk
from tkinter import Frame, Label, Entry, Button, StringVar, OptionMenu, ttk
from widgets.functions import recipes_clean_fields, recipes_on_double_click
from database.controllers.recipes_controller import add_recipes, select_recipes ,search_recipes ,update_recipes , delete_recipes
from windows.mount_recipes_window import mount_recipes_window

lb_code = None
lb_recipe_name = None
tipvar1 = None
tipvar2 = None
recipes_list = None

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
    bt_search_recipes = model_create_button(frame, 'Buscar', 0.72, 0.4,command=lambda: search_recipes(lb_code, lb_recipe_name, tipvar1, tipvar2, recipes_list))
    bt_clear_recipes = model_create_button(frame, 'Limpar', 0.9, 0.2, command=lambda: recipes_clean_fields(lb_code, lb_recipe_name, tipvar1, tipvar2))
    bt_add_recipes = model_create_button(frame, 'Adicionar', 0.82, 0.6, command=lambda: add_recipes(frame, lb_code, lb_recipe_name, tipvar1, tipvar2, recipes_list))
    bt_edit_recipes = model_create_button(frame, 'Editar', 0.82, 0.2,command=lambda: update_recipes(frame, lb_code, lb_recipe_name, tipvar1, tipvar2, recipes_list))
    bt_delete_recipes = model_create_button(frame, 'Excluir', 0.9, 0.6,command=lambda: delete_recipes(frame, lb_code, lb_recipe_name, tipvar1, tipvar2, recipes_list))
    bt_open_recipes = model_create_button(frame, 'Abrir', 0.14, 0.6, command=lambda: mount_recipes_window(parent_frame=frame, lb_code=lb_code, lb_recipes_name=lb_recipe_name, lb_category=tipvar1, lb_subcategory=tipvar2))

def create_labels_and_entries(frame):
    global lb_code, lb_recipe_name
    lb_code = model_create_label_entry(frame, 'Código', 0.03, 0.25, 80, 30, is_bold=True)
    lb_recipe_name = model_create_label_entry(frame, 'Nome da Receita', 0.14, 0.25, 250, 30, is_bold=True)
    return lb_code, lb_recipe_name

def create_category_menu(frame):    
    global tipvar1
    tipvar1 = StringVar(frame)
    TipV = ("Doces","Salgadas" )
    tipvar1.set(" ")
    lb_popupMenu = model_create_label_entry(frame, 'Categoria', 0.40, 0.25, 0, 0, is_bold=True)
    popupMenu = OptionMenu(frame, tipvar1, *TipV)
    popupMenu.place(relx=0.40, rely=0.4, width=120, height=30)
    popupMenu.configure(highlightthickness=0, font=('Helvetica', 12), borderwidth=1)
    return tipvar1

def create_subcategory_menu(frame):
    global tipvar2
    tipvar2 = StringVar(frame)
    TipV = ("Pascoa", "Natal", "Anual" )
    tipvar2.set(" ")
    lb_popupMenu = model_create_label_entry(frame, 'Subcategoria', 0.55, 0.25, 0, 0, is_bold=True)
    popupMenu = OptionMenu(frame, tipvar2, *TipV)
    popupMenu.place(relx=0.55, rely=0.4, width=120, height=30)
    popupMenu.configure(highlightthickness=0, font=('Helvetica', 12), borderwidth=1)
    return tipvar2

def configure_estyle_treeview(treeview):
    style = ttk.Style()
    style.configure("Treeview.Treeview", font=('Helvetica', 12))
    
    treeview.configure(style="Treeview.Treeview")

def format_quantity(value):
    return str(int(value))

def create_recipes_list(frame):
    global recipes_list
    recipes_list = ttk.Treeview(frame, columns=('col0', 'col1', 'col2', 'col3', 'col4', 'col5'))
    recipes_list.heading('#0')
    recipes_list.heading('#1', text='Código')
    recipes_list.heading('#2', text='Receita')
    recipes_list.heading('#3', text='Categoria')
    recipes_list.heading('#4', text='Sub Categoria')
    recipes_list.heading('#5', text='Preço de Venda')
    recipes_list.column('#0', width=0)
    recipes_list.column('#1', width=100, anchor='center')
    recipes_list.column('#2', width=250)
    recipes_list.column('#3', width=180, anchor='center')
    recipes_list.column('#4', width=180, anchor='center')
    recipes_list.column('#5', width=180, anchor='center')
    recipes_list.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
    
    scroll_list = ttk.Scrollbar(frame, orient='vertical')
    recipes_list.configure(yscrollcommand=scroll_list.set)
    scroll_list.config(command=recipes_list.yview)
    scroll_list.place(relx=0.98, rely=0.1, relheight=0.85, width=20)
    recipes_list.bind("<Double-1>", lambda event: recipes_on_double_click(lb_code, lb_recipe_name, tipvar1, tipvar2, recipes_list))
    select_recipes(recipes_list)
    configure_estyle_treeview(recipes_list)


def recipes_frame(parent):
    register_frame_recipes = Frame(parent)
    register_frame_recipes.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.25)
    list_frame_recipes = Frame(parent)
    list_frame_recipes.place(relx=0.01, rely=0.29, relwidth=0.98, relheight=0.69)

    create_buttons(register_frame_recipes)
    create_labels_and_entries(register_frame_recipes)
    create_category_menu(register_frame_recipes)
    create_subcategory_menu(register_frame_recipes)
    create_recipes_list(list_frame_recipes)
