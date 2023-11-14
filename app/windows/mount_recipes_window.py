from tkinter import Toplevel, messagebox
from widgets.mount_recipes_widgets import recipes_frame
from database.models.recipes_db_logic import connect_db, disconnect_db

def mount_recipes_window(parent_frame=None, lb_code=None, lb_recipes_name=None, lb_category=None, lb_subcategory=None):

    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM Recipes WHERE id = ? AND recipes = ?", (lb_code.get(), lb_recipes_name.get()))
    existing_recipe = cursor.fetchone()
    disconnect_db(conn)

    if not existing_recipe:
        messagebox.showinfo("Receita não cadastrada", "Essa receita ainda não foi cadastrada!", parent=parent_frame)
        return

    root_main = Toplevel(parent_frame)
    root_main.title('Criar Receita - Levu Confeitaria')
    root_main.configure(bg="#ED82AE")
    root_main.geometry("1200x720+180+10")
    root_main.resizable(True, True)
    root_main.maxsize(width=1200, height=720)
    root_main.minsize(width=720, height=480)
    root_main.resizable(False, False)
    root_main.transient()
    root_main.focus_force()
    root_main.grab_set()

    recipes_frame(root_main, lb_code.get(), lb_recipes_name.get(), lb_category.get(), lb_subcategory.get())

conn, cursor = connect_db()
disconnect_db(conn)
