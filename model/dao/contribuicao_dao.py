from model.dao.base_dao import Base_DAO
from model.contribuicao import Contribuicao

class Contribuicao_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, con:Contribuicao):
        sql = """insert into contribuicao (id_aluno, id_pedido, valor, pago) values (%s, %s, %s, %s)"""

        values = (con._id_aluno,con._id_pedido, con._valor, con._pago)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        con._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return con

    def get_all(self):
        sql = """select c.id, c.id_aluno, c.id_pedido, c.valor, c.pago, a.nome, a.turma
                from contribuicao c
                inner join aluno a on c.id_aluno = a.id
                inner join pedido p on c.id_pedido = p.id
                order by c.pago asc"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        con = []
        for (id, id_aluno, id_pedido, valor, pago, nome, turma) in cursor:
            con.append(Contribuicao(id, id_aluno, id_pedido, valor, pago, nome, turma))
        cursor.close()
        conn.close()
        return con
    
    def get_by_id(self, id):
        sql = """select id, id_aluno, id_pedido, valor, pago from contribuicao where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        con = None
        if row:
            id, id_aluno, id_pedido, valor, pago = row
            con = Contribuicao(id, id_aluno, id_pedido, valor, pago)
        cursor.close()
        conn.close()
        return con
    
    def delete(self, id):
        sql = """delete from contribuicao where id = %s"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, con:Contribuicao):
        sql = """update contribuicao set id_aluno = %s, id_pedido = %s, valor = %s, pago = %s where id = %s"""
        values = (con._id_aluno, con._id_pedido, con._valor, con._pago, con._id)
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0