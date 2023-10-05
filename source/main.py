from tkinter import *
import customtkinter

class AgendaApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1280x720')
        self.configure_gui()

    def configure_gui(self):
        # Aqui você pode adicionar os widgets e configurações adicionais da GUI
        pass


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = AgendaApp(root)
    root.mainloop()
