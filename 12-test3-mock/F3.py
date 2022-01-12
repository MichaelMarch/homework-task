class C:
    def __init__(self, names):
        self.names = names

    def m(self):
        for i in range(len(self.names)):
            if self.names[i] in self.names[i + 1:]:
                return True

        return False
