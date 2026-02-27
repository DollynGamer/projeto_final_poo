class Sugestao_Sabor:
    def __init__(self, id_aluno, id_sabor, nome_aluno=None, turma=None, nome_sabor=None):
        self._id_aluno = id_aluno
        self._id_sabor = id_sabor
        self._nome_aluno = nome_aluno
        self._turma = turma
        self._nome_sabor = nome_sabor

    def to_string(self):
        return f"Aluno: {self._id_aluno} - {self._nome_aluno} - {self._turma}| Sabor: {self._id_sabor} - {self._nome_sabor}"