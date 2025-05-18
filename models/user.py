

class User:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"User: {self.name} (ID: {self.id})"
