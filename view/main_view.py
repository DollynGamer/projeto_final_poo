import tkinter as tk

class Main_view:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Sistema de Pizzas")
        self.root.geometry("1280x720")
        self.root.state('zoomed')
        
        self._setup_menu()

    def _setup_menu(self):
        tk.Label(self.root, text="Bem-vindo ao Pizzas do SENAC", font=("Arial", 19, "bold")).place(relx=0.5, rely=0.45, anchor="center")
        tk.Label(self.root, text="Test de descrição", font=("Arial", 14)).place(relx=0.5, rely=0.52, anchor="center")

        barra_menu = tk.Menu(self.root)
        
        menu_cadastros = tk.Menu(barra_menu, tearoff=0)
        menu_cadastros.add_command(label="Alunos", command=self._abrir_aluno)
        menu_cadastros.add_command(label="Pedidos", command=self._abrir_pedido)
        menu_cadastros.add_command(label="Contribuição", command=self._abrir_contribuicao)
        menu_cadastros.add_separator()
        menu_cadastros.add_command(label="Sair", command=self.root.quit)
        
        barra_menu.add_cascade(label="Módulos", menu=menu_cadastros)
        self.root.config(menu=barra_menu)

    def _abrir_aluno(self):
        if self.controller:
            self.controller.exibir_aluno()

    def _abrir_pedido(self):
        if self.controller:
            self.controller.exibir_pedido()

    def _abrir_contribuicao(self):
        if self.controller:
            self.controller.exibir_contribuicao()

    def run(self):
        self.root.mainloop()