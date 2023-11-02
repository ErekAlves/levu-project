from tkinter import Tk
from widgets.main_widgets import load_and_place_images, button_create

root_main = Tk()

class Main:
    def __init__(self):
        self.root_main = root_main
        self.Window()
        self.root_main.mainloop()

    def Window(self):
        self.root_main.title('Levu Confeitaria')
        self.root_main.configure(background='#ED82AE')
        self.root_main.geometry("720x480+400+100")
        self.root_main.resizable(True, True)
        self.root_main.maxsize(width=720, height=480)
        self.root_main.minsize(width=720, height=480)
        self.root_main.resizable(False, False)
        load_and_place_images(self)
        button_create(self)
