class Sabor():
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome

    def to_string(self):
        return f"ID: {self._id} | Nome: {self._nome}"