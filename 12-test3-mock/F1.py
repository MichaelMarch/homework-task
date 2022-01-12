class C:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name[:1]}{self.surname[:1]}".upper()
