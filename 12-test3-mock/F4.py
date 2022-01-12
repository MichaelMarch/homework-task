class C:
    def __init__(self, number_info):
        self.number_info = number_info

    def m(self):
        total = 0
        base = int(self.number_info["system"])
        length = len(self.number_info["value"])

        for i in range(length - 1, -1, -1):
            digit = int(self.number_info["value"][i])
            if digit >= base:
                return -1
            total += digit * pow(base, i)

        return total
