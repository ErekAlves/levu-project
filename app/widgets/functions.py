from tkinter import END

def ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar):
    lb_code.delete(0, END)
    lb_product.delete(0, END)
    lb_price.delete(0, END)
    lb_quantity.delete(0, END)
    Tipvar.set(" ")

def ingredients_on_double_click(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):

    ingredients_clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)

    selected_ingredient = ingredients_list.selection()
    if selected_ingredient:
        col1, col2, col3, col4, col5, col6= ingredients_list.item(selected_ingredient[0], 'values')

        lb_code.insert(END, col1)
        lb_product.insert(END, col2)
        lb_price.insert(END, col3)
        lb_quantity.insert(END, col4)
        Tipvar.set(col5)
        

def recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2):
    lb_code.delete(0, END)
    lb_recipe_name.delete(0, END)
    Tipvar1.set(" ")
    Tipvar2.set(" ")

def recipes_on_double_click(lb_code, lb_recipe_name, Tipvar1, Tipvar2, recipes_list):

    recipes_clean_fields(lb_code, lb_recipe_name, Tipvar1, Tipvar2)

    selected_item = recipes_list.selection()
    if selected_item:
        col1, col2, col3, col4= recipes_list.item(selected_item[0], 'values')

        lb_code.insert(END, col1)
        lb_recipe_name.insert(END, col2)
        Tipvar1.set(col3)
        Tipvar2.set(col4)



    