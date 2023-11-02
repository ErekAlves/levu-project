from tkinter import END

def clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar):
    lb_code.delete(0, END)
    lb_product.delete(0, END)
    lb_price.delete(0, END)
    lb_quantity.delete(0, END)
    Tipvar.set(" ")

def on_double_click(lb_code, lb_product, lb_price, lb_quantity, Tipvar, ingredients_list):

    clean_fields(lb_code, lb_product, lb_price, lb_quantity, Tipvar)

    selected_item = ingredients_list.selection()
    if selected_item:
        col1, col2, col3, col4, col5= ingredients_list.item(selected_item[0], 'values')

        lb_code.insert(END, col1)
        lb_product.insert(END, col2)
        lb_price.insert(END, col3)
        lb_quantity.insert(END, col4)
        Tipvar.set(col5)