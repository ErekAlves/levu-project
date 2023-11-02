from tkinter import Toplevel
from widgets.ingredients_widgets import ingredients_frame
from database.models.ingredients_db_logic import connect_db, disconnect_db, create_ingredients_table
from database.controllers.ingredients_controller import select_ingredients

def ingredients_window(root_main = None):
       root_main= Toplevel(root_main)
       root_main.title('Ingredientes - Levu Confeitaria')
       root_main.configure(bg="#ED82AE")
       root_main.geometry("1200x720+180+10")
       root_main.resizable(True, True)
       root_main.maxsize(width=1200, height=720)
       root_main.minsize(width=720, height=480)
       root_main.resizable(False, False)
       root_main.transient()
       root_main.focus_force()
       root_main.grab_set()

       ingredients_frame(root_main)
  
conn, cursor = connect_db()
create_ingredients_table(conn, cursor)
disconnect_db(conn)

