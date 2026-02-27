from model.dao.aluno_dao import Aluno_DAO
from model.dao.pedido_dao import Pedido_DAO
from model.dao.contribuicao_dao import Contribuicao_DAO
from model.dao.sabor_dao import Sabor_DAO
from model.dao.sugestao_sabor_dao import Sugestao_Sabor_DAO
from control.aluno_controller import Aluno_Controller
from control.pedido_controller import Pedido_Controller
from control.contribuicao_controller import Contribuicao_Controller
from control.sabor_controller import Sabor_Controller
from control.sugestao_sabor_controller import Sugestao_Sabor_Controller
from view.aluno_view import Aluno_View
from view.pedido_view import Pedido_View
from view.contribuicao_view import Contribuicao_View
from view.sabor_view import Sabor_View
from view.sugestao_sabor_view import Sugestao_Sabor_View

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

    def exibir_contribuicao(self):
        con_dao = Contribuicao_DAO(self.db_config)
        aluno_dao = Aluno_DAO(self.db_config)
        pedido_dao = Pedido_DAO(self.db_config)
        view = Contribuicao_View()
        control = Contribuicao_Controller(con_dao, aluno_dao, pedido_dao, view)
        control.list_related_aluno()
        control.list_related_pedido()
        view.run()
    
    def exibir_sabor(self):
        dao = Sabor_DAO(self.db_config)
        view = Sabor_View()
        control = Sabor_Controller(dao, view)
        view.run()

    def exibir_sugestao(self):
        su_sa_dao = Sugestao_Sabor_DAO(self.db_config)
        aluno_dao = Aluno_DAO(self.db_config)
        sabor_dao = Sabor_DAO(self.db_config)
        view = Sugestao_Sabor_View()
        control = Sugestao_Sabor_Controller(su_sa_dao, aluno_dao, sabor_dao, view)
        control.list_related_aluno()
        control.list_related_sabor()
        view.run()