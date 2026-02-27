import tkinter as tk
from tkinter import messagebox, ttk

class Sugestao_Sabor_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Sugestões")
        self.root.geometry("1280x720")
        self.root.state('zoomed')

        self.var_aluno = tk.StringVar()
        self.var_sabor = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE DE SUGESTÕES", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.LabelFrame(self.root, text=" Dados da Sugestão ", padx=10, pady=10)
        frame_form.pack(padx=20, pady=5)

        tk.Label(frame_form, text="Aluno:").grid(row=0, column=0, sticky="w")
        self.combo_aluno = ttk.Combobox(frame_form, textvariable=self.var_aluno, width=50, state="readonly")
        self.combo_aluno.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Sabor:").grid(row=0, column=2, sticky="w")
        self.combo_sabor = ttk.Combobox(frame_form, textvariable=self.var_sabor, width=50, state="readonly")
        self.combo_sabor.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#d4edda", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_editar, bg="#fff3cd", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="EXCLUIR", command=self._acao_excluir, bg="#f8d7da", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._limpar_campos, bg="#bcd0e3", width=15).pack(side=tk.LEFT, padx=5)

        frame_tabela = tk.Frame(self.root, padx=20, pady=10)
        frame_tabela.pack(expand=True, fill="both")

        self.colunas = ("aluno", "sabor")
        self.tree = ttk.Treeview(frame_tabela, columns=self.colunas, show="headings")
        self.tree.heading("aluno", text="Aluno")
        self.tree.heading("sabor", text="Sabor")

        for col in self.colunas: self.tree.column(col, anchor="center")

        self.tree.pack(side="left", expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self._ao_selecionar_tabela)

    def run(self):
        self.root.after(200, self._acao_listar)
        self.root.grab_set()
        self.root.focus_force()

    def get_dados_sugestao(self):
        try:
            aluno_parts = self.var_aluno.get().split(" - ")
            sabor_parts = self.var_sabor.get().split(" - ")
            return {
                "id_aluno": int(aluno_parts[0]),
                "id_sabor": int(sabor_parts[0]),
                "nome_aluno": aluno_parts[1] if len(aluno_parts) > 1 else None,
                "turma": aluno_parts[2] if len(aluno_parts) > 2 else None,
                "nome_sabor": sabor_parts[1] if len(sabor_parts) > 1 else None
            }
        except Exception as e:
            self.show_error(f"Dados inválidos: {str(e)}")
            return None

    def _acao_adicionar(self): 
        self.controller.add_sugestao()
        self._acao_listar()
        self._limpar_campos()

    def _acao_editar(self): 
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel[0])['values']
            id_aluno_antigo = int(v[0].split(" - ")[0])
            id_sabor_antigo = int(v[1].split(" - ")[0])
            self.controller.update_sugestao(id_aluno_antigo, id_sabor_antigo)
            self._acao_listar()

    def _acao_excluir(self):
        if messagebox.askyesno("Confirmação", "Deseja excluir?"):
            self.controller.delete_sugestao()
            self._acao_listar()
            self._limpar_campos()

    def _acao_listar(self):
        if self.controller: self.controller.list_sugestao()

    def show_sugestao(self, lista):
        for i in self.tree.get_children(): self.tree.delete(i)
        for s in lista:
            aluno = f"{s._id_aluno} - {s._nome_aluno} - {s._turma}".strip()
            sabor = f"{s._id_sabor} - {s._nome_sabor}".strip()
            self.tree.insert("", "end", values=(aluno, sabor))


    def preencher_combo_aluno(self, lista):
        self.combo_aluno['values'] = [f"{a._id} - {a._nome} - {a._turma}" for a in lista]

    def preencher_combo_sabor(self, lista):
        self.combo_sabor['values'] = [f"{s._id} - {s._nome}" for s in lista]

    def get_id_aluno(self):
        aluno = self.var_aluno.get()
        if aluno:
            return int(aluno.split(" - ")[0])
        return None
    
    def get_id_sabor(self):
        sabor = self.var_sabor.get()
        if sabor:
            return int(sabor.split(" - ")[0])
        return None

    def _limpar_campos(self):
        for v in [self.var_aluno, self.var_sabor]: v.set("")

    def _ao_selecionar_tabela(self, event):
        item_sel = self.tree.selection()
        if item_sel:
            v = self.tree.item(item_sel[0])['values']
            self.var_aluno.set(str(v[0]))
            self.var_sabor.set(v[1])

    def show_message(self, txt): messagebox.showinfo("Sucesso", txt)
    def show_error(self, err): messagebox.showerror("Erro", err)