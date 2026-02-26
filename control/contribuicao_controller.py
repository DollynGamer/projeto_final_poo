from model.contribuicao import Contribuicao

class Contribuicao_Controller:
    def __init__(self, dao_con, dao_aluno, dao_pedido, view):
        self.dao_con = dao_con
        self.dao_aluno = dao_aluno
        self.dao_pedido = dao_pedido
        self.view = view
        self.view.controller = self

    def add_contribuicao(self):
        try:
            dados = self.view.get_dados_contribuicao()
            con_novo = Contribuicao(
                id = None,
                id_aluno = dados['id_aluno'],
                id_pedido = dados['id_pedido'],
                valor = dados['valor'],
                pago = dados['pago']
            )
            self.dao_con.save(con_novo)
            self.view.show_message(f"Contribuição adicionado com ID: {con_novo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar contribuição: {str(e)}")

    def update_contribuicao(self):
        try:
            id_con = self.view.get_id()
            dados = self.view.get_dados_contribuicao()
            con_existente = Contribuicao(id_con, dados['id_aluno'], dados['id_pedido'], dados['valor'], dados['pago'])
            
            if self.dao_con.update(con_existente):
                self.view.show_message("Contribuição atualizado.")
            else:
                self.view.show_error("Erro ao atualizar contribuição.")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar contribuição: {str(e)}")

    def delete_contribuicao(self):
        try:
            id_con = self.view.get_id()
            if self.dao_con.delete(id_con):
                self.view.show_message("Contribuição deletado.")
            else:
                self.view.show_error("Contribuição não encontrado.")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar contribuição: {str(e)}")

    def list_contribuicao(self):
        try:
            con = self.dao_con.get_all()
            self.view.show_contribuicao(con)
        except Exception as e:
            self.view.show_error(f"Erro ao listar contribuição: {str(e)}")

    def list_related_aluno(self):
        self.view.preencher_combo_aluno(self.dao_aluno.get_all())

    def list_related_pedido(self):
        self.view.preencher_combo_pedido(self.dao_pedido.get_all())