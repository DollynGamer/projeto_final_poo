from model.pedido import Pedido
from model.dao.base_dao import Base_DAO

class Pedido_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, pedido:Pedido):
        sql = """insert into pedido (valor, status_pedido) values (%s, %s)"""

        values = (pedido._valor, pedido._status_pedido)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        pedido._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return pedido
    
    def get_all(self):
        sql = "select id, valor, status_pedido, data from pedido order by status_pedido, data asc"

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        pedido = []
        
        for (id, valor, status_pedido, data) in cursor:
            pedido.append(Pedido(id, valor, status_pedido, data))
        
        cursor.close()
        conn.close()
        return pedido
    
    def get_by_id(self, id):
        sql = """select id, valor, status_pedido, data from pedido where id = %s"""

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        pedido = None

        if row:
            id, valor, status_pedido, data = row
            pedido = Pedido(id, valor, status_pedido, data)

        cursor.close()
        conn.close()
        return pedido
    
    def delete(self, id):
        sql = """delete from pedido where id = %s"""
        
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, pedido_atualizado:Pedido):
        sql = """update pedido set valor = %s, status_pedido = %s where id = %s"""

        values = (pedido_atualizado._valor, pedido_atualizado._status_pedido, pedido_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0