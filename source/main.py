import csv
from tkinter import *
import customtkinter


class ContactManager:
    """ Classe main do programa, responsável por gerenciar a janela
    e processos"""

    def __init__(self, master):
        self.master = master  # Se refere a janela 'root'
        self.master.geometry('1280x720')
        self.manage_components()
        self.master.title("Agenda de Contatos")
        self.set_window_icon()
        self.initialize_csv()

    def manage_components(self):
        """ Gerencia os componentes da interface e seus estados"""
        self.add_contact_component = AddContactComponent(self.master)

    def set_window_icon(self):
        try:
            self.master.iconbitmap('assets/window_icon.ico')
        except:
            pass

    def initialize_csv(self):
        """ Inicializa a tabela de contatos, verificando se a tabela existe,
        caso não exista, cria uma nova tabela"""
        filepath = 'contacts.csv'
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as file:
                pass
        except FileNotFoundError:
            with open(filepath, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(['Nome', 'Telefone'])


class Component(customtkinter.CTkFrame):
    """ Classe pai dos componentes da interface gráfica"""

    def __init__(self, parent):
        """ O tamanho dos componentes é definido pelo tamanho mínimo
        necessário para renderizar seus elementos que tem tamanhos fixos
        a largura e altura não são definidos diretamente no componente"""
        super().__init__(parent, width=1280, height=720)

        self.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o componente


class AddContactComponent(Component):
    """ Componente de adicionar novos contatos, contém alguns campos e um botão para
    adicionar novos contatos na tabela de contatos"""

    def __init__(self, parent):
        super().__init__(parent)

        # Título "Adicionar novos contatos"
        self.title_label = customtkinter.CTkLabel(self, text="Adicionar novo contato", font=("Arial", 40))
        self.title_label.pack(pady=40, padx=40)

        # Label do nome
        self.name_label = customtkinter.CTkLabel(self, text="Nome:", font=("Arial", 24))
        self.name_label.pack(anchor="w", pady=0, padx=40)
        # Campo para escrever o nome
        self.name_entry = customtkinter.CTkEntry(self, width=400, height=32)
        self.name_entry.pack(pady=10)
        self.name_entry.bind("<Return>", lambda event=None: self.save_contact())

        # Label do número de telefone
        self.phone_label = customtkinter.CTkLabel(self, text="Telefone:", font=("Arial", 24))
        self.phone_label.pack(anchor="w", pady=10, padx=40)
        # Campo para escrever o número de telefone - Apenas números são permitidos
        self.phone_entry = customtkinter.CTkEntry(self, width=400, height=32, validate="key",
                                                  validatecommand=(self.register(self._validate_phone), "%P"))
        self.phone_entry.pack(pady=0)
        self.phone_entry.bind("<Return>", lambda event=None: self.save_contact())

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
        """ Verifica se o número de telefone contém letras"""
        return value.isdigit() or value == ""

    def _phone_exists(self, phone):
        """ Verifica se o número de telefone digitado já existe na tabela"""
        with open('contacts.csv', 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == phone:
                    return True
        return False

    def save_contact(self):
        """ Adiciona um novo contato na tabela de contatos com os
        dados fornecidos pelo usuário, o único campo obrigatório é
        o campo de telefone, caso o usuário não forneça um nome o 
        programa adiciona o número como 'desconhecido' na tabela"""

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
                self.error_message.configure(text="Erro: O número de telefone já existe!")
        else:
            self.error_message.configure(text="Erro: O campo de telefone é obrigatório!")


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ContactManager(root)
    root.mainloop()
