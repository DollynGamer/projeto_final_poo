import tkinter as tk
import random

class Main_view:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Sistema de Pizzas")
        self.root.geometry("1280x720")
        self.root.state('zoomed')
        
        self._setup_menu()

    def _setup_menu(self):
        # Frame superior com título e descrição
        topo_frame = tk.Frame(self.root)
        topo_frame.pack(pady=50)

        tk.Label(topo_frame, text="Bem-vindo ao Pizzas do SENAC", font=("Comic Sans MS", 24, "bold")).pack(pady=10)
        tk.Label(topo_frame, text="Aqui é SABOR SENAC", font=("Comic Sans MS", 16)).pack()

        # Frame central com os botões de acesso aos módulos
        centro_frame = tk.Frame(self.root)
        centro_frame.pack(expand=True)

        self.btn_sabor = tk.Button(self.root, text="", command=self.mostrar_imagem, bg="#ffffff", width=1, height=1)
        self.btn_sabor.place(relx=0.99, rely=0.99, anchor="sw")  # sw = south-west (inferior esquerdo)

        # Lista de botões: (texto, função)
        botoes = [
            ("Alunos", self._abrir_aluno),
            ("Pedidos", self._abrir_pedido),
            ("Contribuição", self._abrir_contribuicao),
            ("Sabores", self._abrir_sabor),
            ("Sugestões", self._abrir_sugestao),
        ]

        for texto, func in botoes:
            tk.Button(centro_frame, text=texto, font=("Arial", 14, "bold"), 
                      width=20, height=2, command=func).pack(pady=10)

        """
        menu antigo:

        barra_menu = tk.Menu(self.root)

        menu_cadastros = tk.Menu(barra_menu, tearoff=0)
        menu_cadastros.add_command(label="Alunos", command=self._abrir_aluno)
        menu_cadastros.add_command(label="Pedidos", command=self._abrir_pedido)
        menu_cadastros.add_command(label="Contribuição", command=self._abrir_contribuicao)
        menu_cadastros.add_command(label="Sabores", command=self._abrir_sabor)
        menu_cadastros.add_command(label="Sugestões", command=self._abrir_sugestao)
        menu_cadastros.add_separator()
        menu_cadastros.add_command(label="Sair", command=self.root.quit)
        
        
        barra_menu.add_cascade(label="Módulos", menu=menu_cadastros)
        self.root.config(menu=barra_menu)
        """

    def _abrir_aluno(self):
        if self.controller:
            self.controller.exibir_aluno()

    def _abrir_pedido(self):
        if self.controller:
            self.controller.exibir_pedido()

    def _abrir_contribuicao(self):
        if self.controller:
            self.controller.exibir_contribuicao()

    def _abrir_sabor(self):
        if self.controller:
            self.controller.exibir_sabor()

    def _abrir_sugestao(self):
        if self.controller:
            self.controller.exibir_sugestao()

    def run(self):
        self.root.mainloop()

    def mostrar_imagem(self):
        # chance de 50% de mostrar a imagem
        if random.random() < 1:  # 0.5 = 50% (100% agora)
            imagens = ["imagens/idolo.png", 
                       "imagens/zoio.png", 
                       "imagens/cavalos.png", 
                       "imagens/goiabalt.png", 
                       "imagens/dedo.png", 
                       "imagens/Sem_titulo.png",
                       "imagens/32hut4.png"
            ]  # suas imagens
            img_path = random.choice(imagens)  # escolhe uma aleatoriamente

            global img  # mantém referência para não sumir
            img = tk.PhotoImage(file=img_path)

            if not hasattr(self, 'label_imagem'):
                self.label_imagem = tk.Label(self.root)
                self.label_imagem.pack(pady=20)

            self.label_imagem.config(image=img)
        else:
            if hasattr(self, 'label_imagem'):
                self.label_imagem.config(image="")  # limpa a imagem