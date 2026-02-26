class Contribuicao():
    def __init__(self, id, id_aluno, id_pedido, valor, pago, nome="", turma=""):
        self._id = id
        self._id_aluno = id_aluno
        self._id_pedido = id_pedido
        self._valor = valor
        self._pago = pago
        self._nome = nome
        self._turma = turma

    def to_string(self):
        return f"ID: {self._id} | ID (Aluno): {self._id_aluno} | ID (Pedido): {self._id_pedido} | Valor: {self._valor} | Pago: {self._pago} | Nome: {self._nome} | Turma: {self._turma}"