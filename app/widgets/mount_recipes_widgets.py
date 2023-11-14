import tkinter as tk
from tkinter import Frame, Label, Entry, Button,StringVar, ttk
from database.controllers.ingredients_controller import update_combobox
from database.controllers.mount_recipes_controller import add_ingredient_quantity


available_ingredients = [""]
lb_add_quantity = None
ingredients_of_recipes = None
lb_first_preparation = None

def model_create_label_entry(parent, text, x, y, width, height, is_bold=False, readonly=False, var=None):
    label = Label(parent, text=text, font=('Helvetica', 10, 'bold' if is_bold else ''))
    label.place(relx=x, rely=y)

    entry_state = 'readonly' if readonly else 'normal'
    entry = Entry(parent, font=('Helvetica', 12), state=entry_state, textvariable=var)
    entry.place(relx=x, rely=y + 0.05, width=width, height=height)
    return entry

def model_create_button(parent, text, x, y, command=None):
    button = Button(parent, text=text, highlightthickness=0, font=('Helvetica', 12), command=command)
    button.place(relx=x, rely=y, width=85, height=35)
    return button

def create_ingredient_combobox(parent, x, y):
    ingredientes_var = StringVar()
    ingredientes_var.set(available_ingredients[0]) 
    label_adicionar = Label(parent, text='Adicionar Ingredientes', font=('Helvetica', 10, 'bold'))
    label_adicionar.place(relx=x, rely=y - 0.05)

    combo = ttk.Combobox(parent,textvariable=ingredientes_var, values=available_ingredients)
    combo.place(relx=x, rely=y, width= 270, height= 30)
    return combo

def autocomplete_recipe_infos(frame1, code, recipes_name, category, subcategory):
    var_code = StringVar(value=code)
    var_recipes_name = StringVar(value=recipes_name)
    var_category = StringVar(value=category)
    var_subcategory = StringVar(value=subcategory)

    lb_code = model_create_label_entry(frame1, 'Código', 0.03, 0.06, 65, 30, is_bold=True, readonly=True, var=var_code)
    lb_product = model_create_label_entry(frame1, 'Receita', 0.14, 0.06, 250, 30, is_bold=True, readonly=True, var=var_recipes_name)
    lb_category = model_create_label_entry(frame1, 'Categoria', 0.40, 0.06, 100, 30, is_bold=True, readonly=True, var=var_category)
    lb_subcategory = model_create_label_entry(frame1, 'Subcategoria', 0.54, 0.06, 100, 30, is_bold=True, readonly=True, var=var_subcategory)

def complete_recipes_infos(frame1):
    global lb_first_preparation, lb_add_quantity, ingredients_of_recipes
    lb_first_preparation = model_create_label_entry(frame1, 'Nome do Preparo', 0.03, 0.20, 200, 30, is_bold=True)
    ingredients_of_recipes = create_ingredient_combobox(frame1, 0.25, 0.25)
    update_combobox(ingredients_of_recipes)
    lb_add_quantity = model_create_label_entry(frame1, 'Qtd.Utl', 0.54, 0.20, 100, 30, is_bold=True)

def packages_tabs_labels_and_entries(frame1, code, recipes_name, category, subcategory):
    var_code = StringVar(value=code)
    var_recipes_name = StringVar(value=recipes_name)
    var_category = StringVar(value=category)
    var_subcategory = StringVar(value=subcategory)

    lb_code = model_create_label_entry(frame1, 'Código', 0.03, 0.06, 65, 30, is_bold=True, readonly=True, var=var_code)
    lb_product = model_create_label_entry(frame1, 'Receita', 0.14, 0.06, 250, 30, is_bold=True, readonly=True, var=var_recipes_name)
    lb_category = model_create_label_entry(frame1, 'Categoria', 0.40, 0.06, 100, 30, is_bold=True, readonly=True, var=var_category)
    lb_subcategory = model_create_label_entry(frame1, 'Subcategoria', 0.54, 0.06, 100, 30, is_bold=True, readonly=True, var=var_subcategory)
    lb_add_ingredient = model_create_label_entry(frame1, 'Adicionar Embalagens', 0.03, 0.20, 270, 30, is_bold=True)
    lb_add_quantity = model_create_label_entry(frame1, 'Qtd.Utl', 0.35, 0.20, 100, 30, is_bold=True)

def create_buttons_ingredients_packages(frame1):
    bt_clear_ingredients = model_create_button(frame1, 'Limpar', 0.9, 0.11)
    bt_save_ingredients = model_create_button(frame1, 'Editar', 0.8, 0.11)
    bt_add_ingredients = model_create_button(frame1, 'Adicionar', 0.8, 0.25, command=lambda: add_ingredient_quantity(lb_first_preparation, ingredients_of_recipes, lb_add_quantity ))
    bt_delete_ingredients = model_create_button(frame1, 'Excluir', 0.9, 0.25)
    bt_save_ingredients = model_create_button(frame1, 'Salvar', 0.7, 0.18)

def create_ingredients_frame(parent):
    ingredients_frame = Frame(parent)
    ingredients_frame.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.45)

def create_ingredients_treeview(tab):

    frame2 = Frame(tab) 
    frame2.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.9)
    ingredients_treeview = ttk.Treeview(frame2, columns=('col0', 'col1', 'col2' 'col3', 'col4', 'col5'))

    ingredients_treeview.heading('#1', text='Ingredientes')
    ingredients_treeview.heading('#2', text='Quantidade')
    ingredients_treeview.heading('#3', text='Vlr. Unit')
    ingredients_treeview.heading('#4', text='Custo P/Und')
    ingredients_treeview.heading('#5')
    ingredients_treeview.column('#0', width=0)
    ingredients_treeview.column('#1', width=100)
    ingredients_treeview.column('#2', width=50)
    ingredients_treeview.column('#3', width=50)
    ingredients_treeview.column('#4', width=50)
    ingredients_treeview.column('#5', width=0)
    ingredients_treeview.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.65)

def create_recipes_frame(tab):
    frame1 = Frame(tab)
    frame1.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.45)

    create_ingredients_frame(frame1)

def recipes_tabs(parent, code, recipes_name, category, subcategory):
    notebook = ttk.Notebook(parent, style='Custom.TNotebook')
    notebook.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
    
    s = ttk.Style()
    s.configure('Custom.TNotebook.Tab', font=('Helvetica', 12))
    
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text="Preparo 1")
    create_recipes_frame(tab1)
    create_ingredients_treeview(tab1)
    autocomplete_recipe_infos(tab1, code, recipes_name, category, subcategory)
    complete_recipes_infos(tab1)
    create_buttons_ingredients_packages(tab1)

    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text="Preparo 2")
    create_recipes_frame(tab2)
    create_ingredients_treeview(tab2)
    autocomplete_recipe_infos(tab2, code, recipes_name, category, subcategory)
    create_buttons_ingredients_packages(tab2)

    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text="Embalagens")
    create_recipes_frame(tab3)
    create_ingredients_treeview(tab3)
    packages_tabs_labels_and_entries(tab3, code, recipes_name, category, subcategory)
    create_buttons_ingredients_packages(tab3)
    
    tab4 = tk.Frame(notebook)
    notebook.add(tab4, text="Custos")
    create_recipes_frame(tab4)

def recipes_frame(parent, code, recipes_name, category, subcategory):
    frame_for_notebook = tk.Frame(parent)
    frame_for_notebook.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)
    autocomplete_recipe_infos(frame_for_notebook, code, recipes_name, category, subcategory,)
    packages_tabs_labels_and_entries(frame_for_notebook, code, recipes_name, category, subcategory)
    recipes_tabs(frame_for_notebook, code, recipes_name, category, subcategory)
