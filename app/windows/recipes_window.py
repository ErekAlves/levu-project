from tkinter import Toplevel
from widgets.recipes_widgets import recipes_frame
from database.models.recipes_db_logic import connect_db, disconnect_db, create_recipes_table

def recipes_window(root_main = None):
       root_main= Toplevel(root_main)
       root_main.title('Receitas - Levu Confeitaria')
       root_main.configure(bg="#ED82AE")
       root_main.geometry("1200x720+180+10")
       root_main.resizable(True, True)
       root_main.maxsize(width=1200, height=720)
       root_main.minsize(width=720, height=480)
       root_main.resizable(False, False)
       root_main.transient()
       root_main.focus_force()
       root_main.grab_set()

       recipes_frame(root_main)
  
conn, cursor = connect_db()
create_recipes_table(conn, cursor)
disconnect_db(conn)

