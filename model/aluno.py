class Aluno():
    def __init__(self, id, nome, turma):
        self._id = id
        self._nome = nome
        self._turma = turma

    def to_string(self):
        return f"ID: {self._id} | Nome: {self._nome} | Turma: {self._turma}"