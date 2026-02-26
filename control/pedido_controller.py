from model.pedido import Pedido
from model.dao.pedido_dao import Pedido_DAO

class Pedido_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.view.controller = self

    def add_pedido(self):
        try:
            dados_pedido = self.view.get_dados_pedido()
            pedido_novo = Pedido(
                id = None,
                valor = dados_pedido['valor'],
                status_pedido = dados_pedido['status_pedido'],
                data = dados_pedido['data']
            )
            pedido_salvo = self.dao.save(pedido_novo)
            self.view.show_message(f"Pedido adicionado com ID: {pedido_salvo._id}")
        except Exception as e:
            self.view.show_error(f"Erro ao adicionar pedido: {str(e)}")

    def update_pedido(self):
        try:
            id_pedido = self.view.get_id()
            pedido_existente = self.dao.get_by_id(id_pedido)
            if not pedido_existente:
                self.view.show_error("Pedido não encontrado.")
                return
            dados_pedido = self.view.get_dados_pedido(pedido_existente)
            pedido_atualizado = Pedido(
                id = id_pedido,
                valor = dados_pedido['valor'],
                status_pedido = dados_pedido['status_pedido'],
                data = dados_pedido['data']
            )
            if self.dao.update(pedido_atualizado):
                self.view.show_message("Pedido atualizado.")
            else:
                self.view.show_error("Erro ao atualizar pedido.")
        except Exception as e:
            self.view.show_error(f"Erro ao atualizar pedido: {str(e)}")

    def delete_pedido(self):
        try:
            id_pedido = self.view.get_id()
            if self.dao.delete(id_pedido):
                self.view.show_message("Pedido deletado.")
            else:
                self.view.show_error("Pedido não encontrado.")
        except Exception as e:
            self.view.show_error(f"Erro ao deletar pedido: {str(e)}")

    def list_pedido(self):
        try:
            pedido = self.dao.get_all()
            self.view.show_pedido(pedido)
        except Exception as e:
            self.view.show_error(f"Erro ao listar pedido: {str(e)}")

    def list_pedido_by_id(self):
        try:
            id_pedido = self.view.get_id()
            pedido = self.dao.get_by_id(id_pedido)
            if not pedido:
                self.view.show_error("Pedido não encontrado.")
                return
            self.view.show_pedido_details(pedido)
        except Exception as e:
            self.view.show_error(f"Erro ao buscar pedido: {str(e)}")