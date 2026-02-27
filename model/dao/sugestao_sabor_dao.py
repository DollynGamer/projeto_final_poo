from model.sugestao_sabor import Sugestao_Sabor
from model.dao.base_dao import Base_DAO

class Sugestao_Sabor_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)    

    def save(self, su_sa:Sugestao_Sabor):
        sql = """insert into sugestao_sabor (id_aluno, id_sabor) values (%s, %s)"""

        values = (su_sa._id_aluno, su_sa._id_sabor)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return su_sa
    
    def get_all(self):
        sql = """select su.id_aluno, su.id_sabor, a.nome, a.turma, s.nome
                from sugestao_sabor su
                inner join aluno a on su.id_aluno = a.id
                inner join sabor s on su.id_sabor = s.id"""

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        su_sa = []
        
        for (id_aluno, id_sabor, nome_aluno, turma, nome_sabor) in cursor:
            su_sa.append(Sugestao_Sabor(id_aluno, id_sabor, nome_aluno, turma, nome_sabor))
        
        cursor.close()
        conn.close()
        return su_sa
    
    def get_by_id(self, id_aluno, id_sabor):
        sql = """select su.id_aluno, su.id_sabor, a.nome, a.turma, s.nome 
                from sugestao_sabor su
                inner join aluno a on su.id_aluno = a.id
                inner join sabor s on su.id_sabor = s.id
                where id_aluno = %s and id_sabor = %s"""

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_aluno, id_sabor))
        row = cursor.fetchone()
        su_sa = None

        if row:
            id_aluno, id_sabor, nome_aluno, turma, nome_sabor = row
            su_sa = Sugestao_Sabor(id_aluno, id_sabor, nome_aluno, turma, nome_sabor)

        cursor.close()
        conn.close()
        return su_sa
    
    def delete(self, id_aluno, id_sabor):
        sql = """delete from sugestao_sabor where id_aluno = %s and id_sabor = %s"""
        
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id_aluno, id_sabor))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows > 0
    
    def update(self, sugestao_sabor_atualizado: Sugestao_Sabor, id_aluno_antigo, id_sabor_antigo):
        sql = """update sugestao_sabor set id_aluno = %s, id_sabor = %s where id_aluno = %s and id_sabor = %s"""

        values = (sugestao_sabor_atualizado._id_aluno, sugestao_sabor_atualizado._id_sabor, id_aluno_antigo, id_sabor_antigo)

        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        updated_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return updated_rows > 0