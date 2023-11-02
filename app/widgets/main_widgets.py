from tkinter import PhotoImage, Label, Button
from windows.ingredients_window import ingredients_window

import os

script_directory = os.path.abspath(os.path.dirname(__file__))

def load_and_place_images(self):
    app_folder = os.path.normpath(os.path.join(script_directory, '..', 'assets'))

    self.logo_img = PhotoImage(file=os.path.join(app_folder, 'logo.png'))
    self.l_logo = Label(image=self.logo_img, borderwidth=0, bg="#ED82AE")
    self.l_logo.place(relx=0.33, rely=-0.1)

    self.recipes_img = PhotoImage(file=os.path.join(app_folder, 'recipes.png'))
    self.l_recipes = Label(image=self.recipes_img, borderwidth=0, bg="#ED82AE")
    self.l_recipes.place(relx=0.35, rely=0.35)

    self.ingredients_img = PhotoImage(file=os.path.join(app_folder, 'ingredients.png'))
    self.l_ingredients = Label(image=self.ingredients_img, borderwidth=0, bg="#ED82AE")
    self.l_ingredients.place(relx=0.35, rely=0.50)

    self.packages_img = PhotoImage(file=os.path.join(app_folder, 'packages.png'))
    self.l_packages = Label(image=self.packages_img, borderwidth=0, bg="#ED82AE")
    self.l_packages.place(relx=0.35, rely=0.65)

def button_create(self):
    self.bt_recipes = Button(text='Receitas')
    self.bt_recipes.place(relx=0.45, rely=0.40, width=140,)
    self.bt_recipes.configure(highlightthickness=0, font=('Helvetica', 12))

    self.bt_ingredients = Button(text='Ingredientes', command=ingredients_window)
    self.bt_ingredients.place(relx=0.45, rely=0.55, width=140)
    self.bt_ingredients.configure(highlightthickness=0, font=('Helvetica', 12))

    self.bt_packages = Button(text='Embalagens')
    self.bt_packages.place(relx=0.45, rely=0.70, width=140)
    self.bt_packages.configure(highlightthickness=0, font=('Helvetica', 12))


