class C:
    def __init__(self, t):
        self.t = t

    def m1(self):
        return self.m2("")

    def m2(self, c1):
        occurrences = {}

        for char in self.t:
            if char not in c1 and c1:
                continue
            if char in occurrences:
                occurrences[char] += 1
                continue

            occurrences[char] = 1

        return occurrences
