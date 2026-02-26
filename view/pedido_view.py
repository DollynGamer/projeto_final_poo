import tkinter as tk
from tkinter import messagebox, ttk

class Pedido_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Pedidos")
        self.root.geometry("1280x720")
        self.root.state('zoomed')

        self.var_id = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_status_pedido = tk.StringVar(value="Preparando")
        self.var_data = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE PEDIDOS", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text="Dados do Pedido",padx=10, pady=10)
        frame_form.pack(padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Valor:").grid(row=0, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_valor, width=25).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Status do Pedido:").grid(row=0, column=4, sticky="e")
        ttk.OptionMenu(frame_form, self.var_status_pedido, "Preparando", "Preparando", "Chegando", "Entregado").grid(row=0, column=5, sticky="w", padx=5)


        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._limpar_campos, bg="#bcd0e3", width=15).pack(side=tk.LEFT, padx=5)


        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "valor", "status_pedido", "data")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("valor", text="Valor")
        self.tree.heading("status_pedido", text="Status do Pedido")
        self.tree.heading("data", text="Data/Hora")

        for col in self.colunas: self.tree.column(col, anchor="center")

        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_pedido(self, pedido_existente=None):
        try:
            return{
                "valor": float(self.var_valor.get()),
                "status_pedido": self.var_status_pedido.get(),
                "data": self.var_data.get()
            }
        except ValueError:
            self.show_error("Dados inválidos.")
            return None
        
    def _acao_adicionar(self):
        self.controller.add_pedido()
        self._acao_listar()

    def _acao_listar(self):
        if self.controller: self.controller.list_pedido()

    def show_pedido(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for p in lista:
            self.tree.insert("","end", values=(p._id, f"R$ {p._valor:.2f}", p._status_pedido, p._data.strftime("%d/%m/%Y %H:%M:%S")))

    def _acao_editar(self):
        self.controller.update_pedido()
        self._acao_listar()

    def get_id(self):
        val = self.var_id.get()
        return int(val) if val else None
    
    def _acao_excluir(self):
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_pedido()
            self._acao_listar()
            self._limpar_campos()

    def _limpar_campos(self):
        for var in [self.var_id, self.var_valor, self.var_data]: var.set("")
        self.var_status_pedido.set("Preparando")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel)['values']
            self.var_id.set(v[0])
            self.var_valor.set(str(v[1]).replace("R$ ", ""))
            self.var_status_pedido.set(v[2])
            self.var_data.set(v[3])
    
    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)

    def show_error(self, err): messagebox.showerror("Erro", err)