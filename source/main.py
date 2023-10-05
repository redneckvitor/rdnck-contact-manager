import csv
from tkinter import *
import customtkinter

class ContactManager:
    def __init__(self, master):
        self.master = master  # É usado para modificar o root da janela
        self.master.geometry('1280x720')
        self.configure_gui()
        self.master.title("Agenda de Contatos")
        self.set_window_icon()
        self.initialize_csv()

    def configure_gui(self):
        pass

    def set_window_icon(self):
        try:
            self.master.iconbitmap('assets/window_icon.ico')
        except:
            pass

    def initialize_csv(self):
        filepath = 'contacts.csv'
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as file:
                pass
        except FileNotFoundError:
            with open(filepath, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(['Nome', 'Telefone'])

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ContactManager(root)
    root.mainloop()
