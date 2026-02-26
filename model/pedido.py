class Pedido():
    def __init__(self, id, valor, status_pedido, data=None):
        self._id = id
        self._valor = valor
        self._status_pedido = status_pedido
        self._data = data

    def to_string(self):
        return (f"ID: {self._id} | Valor: {self._valor} | Status: {self._status_pedido} | Data: {self._data}")