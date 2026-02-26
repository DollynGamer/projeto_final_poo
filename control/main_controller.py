from model.dao.aluno_dao import Aluno_DAO
from model.dao.pedido_dao import Pedido_DAO
from control.aluno_controller import Aluno_Controller
from control.pedido_controller import Pedido_Controller
from view.aluno_view import Aluno_View
from view.pedido_view import Pedido_View

class Main_Controller:
    def __init__(self, main_view, db_config):
        self.main_view = main_view
        self.db_config = db_config

    def exibir_aluno(self):
        dao = Aluno_DAO(self.db_config)
        view = Aluno_View()
        control = Aluno_Controller(dao, view)
        view.run()

    def exibir_pedido(self):
        dao = Pedido_DAO(self.db_config)
        view = Pedido_View()
        control = Pedido_Controller(dao, view)
        view.run()