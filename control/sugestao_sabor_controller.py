from model.sugestao_sabor import Sugestao_Sabor

class Sugestao_Sabor_Controller:
    def __init__(self, dao_su_sa, dao_aluno, dao_sabor, view):
        self.dao_su_sa = dao_su_sa
        self.dao_aluno = dao_aluno
        self.dao_sabor = dao_sabor
        self.view = view
        self.view.controller = self

    def add_sugestao(self):
        try:
            dados = self.view.get_dados_sugestao()
            su_sa_novo = Sugestao_Sabor(
                id_aluno = dados['id_aluno'],
                id_sabor = dados['id_sabor'],
                nome_aluno = dados['nome_aluno'],
                turma = dados['turma'],
                nome_sabor = dados['nome_sabor']
            )
            self.dao_su_sa.save(su_sa_novo)
            self.view.show_message(f"Sugestão adicionada.")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar sugestão: {str(e)}")

    def update_sugestao(self, id_aluno_antigo, id_sabor_antigo):
        try:
            dados = self.view.get_dados_sugestao()
            su_sa_existente = Sugestao_Sabor(dados['id_aluno'], dados['id_sabor'])
            
            if self.dao_su_sa.update(su_sa_existente, id_aluno_antigo, id_sabor_antigo):
                self.view.show_message("Sugestão atualizada.")
            else:
                self.view.show_error("Erro ao atualizar sugestão.")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar sugestão: {str(e)}")

    def delete_sugestao(self):
        try:
            id_aluno = self.view.get_id_aluno()
            id_sabor = self.view.get_id_sabor()
            if self.dao_su_sa.delete(id_aluno, id_sabor):
                self.view.show_message("Sugestão deletada.")
            else:
                self.view.show_error("Sugestão não encontrada.")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar sugestão: {str(e)}")

    def list_sugestao(self):
        try:
            su_sa = self.dao_su_sa.get_all()
            self.view.show_sugestao(su_sa)
        except Exception as e:
            self.view.show_error(f"Erro ao listar sugestão: {str(e)}")

    def list_related_aluno(self):
        self.view.preencher_combo_aluno(self.dao_aluno.get_all())

    def list_related_sabor(self):
        self.view.preencher_combo_sabor(self.dao_sabor.get_all())