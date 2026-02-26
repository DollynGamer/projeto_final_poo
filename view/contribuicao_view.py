import tkinter as tk
from tkinter import messagebox, ttk

class Contribuicao_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Contribuições")
        self.root.geometry("1280x720")
        self.root.state('zoomed')

        self.var_id = tk.StringVar()
        self.var_aluno = tk.StringVar()
        self.var_pedido = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_pago = tk.IntVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE CONTRIBUIÇÃO", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text=" Dados da Contribuição ", padx=10, pady=10)
        frame_form.pack(padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Aluno:").grid(row=0, column=2, sticky="w")
        self.combo_aluno = ttk.Combobox(frame_form, textvariable=self.var_aluno, width=50, state="readonly")
        self.combo_aluno.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Pedido:").grid(row=1, column=0, sticky="w")
        self.combo_pedido = ttk.Combobox(frame_form, textvariable=self.var_pedido, width=10, state="readonly")
        self.combo_pedido.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Valor da Contribuição:").grid(row=1, column=2, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_valor, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Já Pagou?").grid(row=1, column=4, sticky="w")
        tk.Checkbutton(frame_form, variable=self.var_pago).grid(row=1, column=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._limpar_campos, bg="#bcd0e3", width=15).pack(side=tk.LEFT, padx=5)

        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("id", "aluno", "pedido", "valor", "pago")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("aluno", text="Aluno")
        self.tree.heading("pedido", text="Pedido")
        self.tree.heading("valor", text="Valor")
        self.tree.heading("pago", text="Pago?")

        for col in self.colunas: self.tree.column(col, anchor="center")

        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_contribuicao(self):
        try:
            return {
                "id_aluno": int(self.var_aluno.get().split(" - ")[0]),
                "id_pedido": int(self.var_pedido.get()),
                "valor": float(self.var_valor.get()),
                "pago": self.var_pago.get()
            }
        except Exception as e:
            self.show_error(f"Dados inválidos: {str(e)}")
            return None

    def _acao_adicionar(self): 
        self.controller.add_contribuicao()
        self._acao_listar()
        self._limpar_campos()

    def _acao_editar(self): 
        self.controller.update_contribuicao()
        self._acao_listar()

    def _acao_excluir(self): 
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_contribuicao()
            self._acao_listar()
            self._limpar_campos()

    def _acao_listar(self): 
        if self.controller: self.controller.list_contribuicao()

    def show_contribuicao(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for c in lista:
            aluno = f"{c._id_aluno} - {c._nome} - {c._turma}".strip()
            pago_text = "Sim" if c._pago == 1 else "Não"
            self.tree.insert("", "end", values=(c._id, aluno, c._id_pedido, f"R$ {c._valor:.2f}", pago_text))


    def preencher_combo_aluno(self, lista):
        self.combo_aluno['values'] = [f"{a._id} - {a._nome} - {a._turma}" for a in lista]

    def preencher_combo_pedido(self, lista):
        self.combo_pedido['values'] = [(p._id) for p in lista]

    def get_id(self):
        val = self.var_id.get()
        return int(val) if val else None

    def _limpar_campos(self):
        for v in [self.var_id, self.var_aluno, self.var_pedido, self.var_valor]: v.set("")
        self.var_pago.set(0)

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel[0])['values']
            self.var_id.set(v[0])
            self.var_aluno.set(str(v[1]))
            self.var_pedido.set(v[2])
            self.var_valor.set(str(v[3]).replace("R$ ", ""))
            self.var_pago.set(1 if v[4] == "Sim" else 0)

    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)
    def show_error(self, err): messagebox.showerror("Erro", err)