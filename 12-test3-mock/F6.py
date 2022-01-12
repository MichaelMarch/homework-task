class C:
    def __init__(self, llist):
        self.llist = llist

    def m(self):
        counter = 0

        i = 1
        while i < len(self.llist) - 1:
            if not self.llist[i - 1] == self.llist[i] and not self.llist[i + 1] == self.llist[i]:
                counter += 1
            i += 1
        return counter
