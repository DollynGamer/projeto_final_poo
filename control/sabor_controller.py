from model.sabor import Sabor

class Sabor_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def add_sabor(self):
        try:
            dados_sabor = self.view.get_dados_sabor()
            sabor_novo = Sabor(
                id = None,
                nome = dados_sabor['nome']
            )
            sabor_salvo = self.dao.save(sabor_novo)
            self.view.show_message(f"Sabor adicionado com ID: {sabor_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar sabor: {str(e)}")

    def update_sabor(self):
        try:
            id_sabor = self.view.get_id()
            sabor_existente = self.dao.get_by_id(id_sabor)
            if not sabor_existente:
                self.view.show_error("Sabor não encontrado.")
                return
            dados_sabor = self.view.get_dados_sabor(sabor_existente)
            sabor_atualizado = Sabor(
                id = id_sabor,
                nome = dados_sabor['nome']
            )
            if self.dao.update(sabor_atualizado):
                self.view.show_message("Sabor atualizado.")
            else:
                self.view.show_error("Erro ao atualizar sabor.")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar sabor: {str(e)}")

    def delete_sabor(self):
        try:
            id_sabor = self.view.get_id()
            if self.dao.delete(id_sabor):
                self.view.show_message("Sabor deletado.")
            else:
                self.view.show_error("Sabor não encontrado.")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar sabor: {str(e)}")

    def list_sabor(self):
        try:
            sabor = self.dao.get_all()
            self.view.show_sabor(sabor)
        except Exception as e:
            self.view.show_error(f"Erro ao listar sabor: {str(e)}")

    def list_sabor_by_id(self):
        try:
            id_sabor = self.view.get_id()
            sabor = self.dao.get_by_id(id_sabor)
            if not sabor:
                self.view.show_error("Sabor não encontrado.")
                return
            self.view.show_sabor_details(sabor)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar sabor: {str(e)}")