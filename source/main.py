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
        self.name_label.pack(anchor="w", pady=0, padx=40)
        # Campo para escrever o nome
        self.name_entry = customtkinter.CTkEntry(self, width=400, height=32)
        self.name_entry.pack(pady=10)

        # Label do número de telefone
        self.phone_label = customtkinter.CTkLabel(self, text="Telefone:", font=("Arial", 24))
        self.phone_label.pack(anchor="w", pady=10, padx=40)
        # Campo para escrever o número de telefone - Apenas números são permitidos
        self.phone_entry = customtkinter.CTkEntry(self, width=400, height=32, validate="key",
                                                  validatecommand=(self.register(self._validate_phone), "%P"))
        self.phone_entry.pack(pady=0)

        # Label para mostrar mensagens de erro
        self.error_message = customtkinter.CTkLabel(self, text="", font=("Arial", 16))
        self.error_message.pack(pady=10)

        # Botão de salvar contato
        # Para se fazer: salvar contatos com a mesma função de quando o botão é clicado
        # usando quando Enter do teclado é pressionado
        self.save_button = customtkinter.CTkButton(self, text="Salvar Contato", command=self.save_contact,
                                                   width=200, height=40, font=("Arial", 20))
        self.save_button.pack(pady=60)

    def _validate_phone(self, value):
        return value.isdigit() or value == ""

    def _phone_exists(self, phone):
        with open('contacts.csv', 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == phone:
                    return True
        return False

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if not name:
            name = "Desconhecido"

        if phone:
            if not self._phone_exists(phone):
                with open('contacts.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow([name, phone])
                self.name_entry.delete(0, END)
                self.phone_entry.delete(0, END)
                self.error_message.configure(text="")
            else:
                # Se o telefone já existir, mostra uma mensagem de erro
                self.error_message.configure(text="Erro: O número de telefone já existe!")
        else:
            self.error_message.configure(text="Erro: O campo de telefone é obrigatório!")


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ContactManager(root)
    root.mainloop()
