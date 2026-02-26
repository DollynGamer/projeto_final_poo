from model.aluno import Aluno
from model.dao.base_dao import Base_DAO

class Aluno_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)    

    def save(self, aluno:Aluno):
        sql = """insert into aluno (nome, turma) values (%s, %s)"""

        values = (aluno._nome, aluno._turma)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        aluno._id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return aluno
    
    def get_all(self):
        sql = "select id, nome, turma from aluno"

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        aluno = []
        
        for (id, nome, turma) in cursor:
            aluno.append(Aluno(id, nome, turma))
        
        cursor.close()
        conn.close()
        return aluno
    
    def get_by_id(self, id):
        sql = """select id, nome, turma from aluno where id = %s"""

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        aluno = None

        if row:
            id, nome, turma = row
            aluno = Aluno(id, nome, turma)

        cursor.close()
        conn.close()
        return aluno
    
    def delete(self, id):
        sql = """delete from aluno where id = %s"""
        
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, aluno_atualizado:Aluno):
        sql = """update aluno set nome = %s, turma = %s where id = %s"""

        values = (aluno_atualizado._nome, aluno_atualizado._turma, aluno_atualizado._id)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0