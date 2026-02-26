from model.aluno import Aluno
from model.dao.aluno_dao import Aluno_DAO

class Aluno_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def add_aluno(self):
        try:
            dados_aluno = self.view.get_dados_aluno()
            aluno_novo = Aluno(
                id = None,
                nome = dados_aluno['nome'],
                turma = dados_aluno['turma']
            )
            aluno_salvo = self.dao.save(aluno_novo)
            self.view.show_message(f"Aluno adicionado com ID: {aluno_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar aluno: {str(e)}")

    def update_aluno(self):
        try:
            id_aluno = self.view.get_id()
            aluno_existente = self.dao.get_by_id(id_aluno)
            if not aluno_existente:
                self.view.show_error("Aluno não encontrado.")
                return
            dados_aluno = self.view.get_dados_aluno(aluno_existente)
            aluno_atualizado = Aluno(
                id = id_aluno,
                nome = dados_aluno['nome'],
                turma = dados_aluno['turma']
            )
            if self.dao.update(aluno_atualizado):
                self.view.show_message("Aluno atualizado.")
            else:
                self.view.show_error("Erro ao atualizar aluno.")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar aluno: {str(e)}")

    def delete_aluno(self):
        try:
            id_aluno = self.view.get_id()
            if self.dao.delete(id_aluno):
                self.view.show_message("Aluno deletado.")
            else:
                self.view.show_error("Aluno não encontrado.")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar aluno: {str(e)}")

    def list_aluno(self):
        try:
            aluno = self.dao.get_all()
            self.view.show_aluno(aluno)
        except Exception as e:
            self.view.show_error(f"Erro ao listar alunos: {str(e)}")

    def list_aluno_by_id(self):
        try:
            id_aluno = self.view.get_id()
            aluno = self.dao.get_by_id(id_aluno)
            if not aluno:
                self.view.show_error("Aluno não encontrado.")
                return
            self.view.show_aluno_details(aluno)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar aluno: {str(e)}")