class C:
    def __init__(self, text):
        self.text = text

    def m(self):
        chars = {}

        for char in self.text:
            if char in chars:
                return False

            chars[char] = None

        return True
