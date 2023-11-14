from tkinter import PhotoImage, Label, Button
from windows.ingredients_window import ingredients_window
from windows.recipes_window import recipes_window
from imgs.logo_base64 import logo_img
from imgs.ingredients_base64 import ingredients_img
from imgs.packages_base64 import packages_img
from imgs.recipes_base64 import recipes_img

import base64

def load_and_place_images(self):

    self.logo_img = PhotoImage(data=base64.b64decode(logo_img))
    self.l_logo = Label(image=self.logo_img, borderwidth=0, bg="#ED82AE")
    self.l_logo.place(relx=0.33, rely=-0.1)

    self.recipes_img = PhotoImage(data=base64.b64decode(recipes_img))
    self.l_recipes = Label(image=self.recipes_img, borderwidth=0, bg="#ED82AE")
    self.l_recipes.place(relx=0.35, rely=0.35)

    self.ingredients_img = PhotoImage(data=base64.b64decode(ingredients_img))
    self.l_ingredients = Label(image=self.ingredients_img, borderwidth=0, bg="#ED82AE")
    self.l_ingredients.place(relx=0.35, rely=0.50)

    self.packages_img = PhotoImage(data=base64.b64decode(packages_img))
    self.l_packages = Label(image=self.packages_img, borderwidth=0, bg="#ED82AE")
    self.l_packages.place(relx=0.35, rely=0.65)

def button_create(self):
    self.bt_recipes = Button(text='Receitas', command=recipes_window)
    self.bt_recipes.place(relx=0.45, rely=0.40, width=140,)
    self.bt_recipes.configure(highlightthickness=0, font=('Helvetica', 12))

    self.bt_ingredients = Button(text='Ingredientes', command=ingredients_window)
    self.bt_ingredients.place(relx=0.45, rely=0.55, width=140)
    self.bt_ingredients.configure(highlightthickness=0, font=('Helvetica', 12))

    self.bt_packages = Button(text='Embalagens')
    self.bt_packages.place(relx=0.45, rely=0.70, width=140)
    self.bt_packages.configure(highlightthickness=0, font=('Helvetica', 12))

