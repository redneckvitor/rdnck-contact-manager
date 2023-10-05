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
        self.add_contact_component = AddContactComponent(self.master)

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


class Component(customtkinter.CTkFrame):
    def __init__(self, parent):
        """ Abaixo estão largura e altura máximas do componente, mas o Tkinter
                renderiza os componentes ocm o tamanho mínimo necessário de acordo com
                os tamanhos fixos dos compoentes, então caso queria mudar o tamanho do componente,
                é necessário mudar os tamanhos fixos de seus componentes internos"""
        super().__init__(parent, width=1280, height=720)

        self.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o componente


class AddContactComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)

        # Título H1 "Adicionar novos contatos"
        self.title_label = customtkinter.CTkLabel(self, text="Adicionar novo contato", font=("Arial", 40))
        self.title_label.pack(pady=40, padx=40)

        # Label do nome
        self.name_label = customtkinter.CTkLabel(self, text="Nome:", font=("Arial", 24))
        self.name_label.pack(anchor="w", pady=(0), padx=(40))
        # Campo para escrever o nome
        self.name_entry = customtkinter.CTkEntry(self, width=400, height=32)
        self.name_entry.pack(pady=10)

        # Label do número de telefone
        self.phone_label = customtkinter.CTkLabel(self, text="Telefone:", font=("Arial", 24))
        self.phone_label.pack(anchor="w", pady=(0), padx=(40))
        # A se fazer: permitir que apenas números sejam escritos e caso a pessoa tente
        # digitar letras ou o contato não salva até que seja resolvido ou as
        # letras não são adicionadas

        # Campo para escrever o número de telefone
        self.phone_entry = customtkinter.CTkEntry(self, width=400, height=32)
        self.phone_entry.pack(pady=10)

        # Botão de salvar contato
        # Para se fazer: salvar contatos com a mesma função de quando o botão é clicado
        # usando quando Enter do teclado é pressionado
        self.save_button = customtkinter.CTkButton(self, text="Salvar Contato", command=self.save_contact,
                                                   width=200, height=40, font=("Arial", 20))
        self.save_button.pack(pady=20)

    def save_contact(self):
        # Aqui você pode adicionar a funcionalidade para salvar o contato
        pass


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ContactManager(root)
    root.mainloop()
