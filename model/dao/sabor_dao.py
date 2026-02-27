from model.sabor import Sabor
from model.dao.base_dao import Base_DAO

class Sabor_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)    

    def save(self, sabor:Sabor):
        sql = """insert into sabor (nome) values (%s)"""

        values = (sabor._nome,)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        sabor._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return sabor
    
    def get_all(self):
        sql = "select id, nome from sabor"

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        sabor = []
        
        for (id, nome) in cursor:
            sabor.append(Sabor(id, nome))
        
        cursor.close()
        conn.close()
        return sabor
    
    def get_by_id(self, id):
        sql = """select id, nome from sabor where id = %s"""

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        sabor = None

        if row:
            id, nome = row
            sabor = Sabor(id, nome)

        cursor.close()
        conn.close()
        return sabor
    
    def delete(self, id):
        sql = """delete from sabor where id = %s"""
        
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, sabor_atualizado:Sabor):
        sql = """update sabor set nome = %s where id = %s"""

        values = (sabor_atualizado._nome, sabor_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0