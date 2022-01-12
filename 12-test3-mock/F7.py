import json


class C:

    def __init__(self):
        with open("mockdata.json") as fp:
            self.data = json.load(fp)

    def m(self, n1, n2):
        counter = 0

        for datum in self.data:
            if datum["wife"]["age"] < n1:
                continue

            if len(datum["children"]) < n2:
                continue

            counter += 1

        return counter

    def m2(self, n1):
        filtered_data = []

        for datum in self.data:
            if len(datum["children"]) < n1:
                continue

            filtered_data.append(datum)

        with open("mockdata1.json", "w") as fp:
            json.dump(filtered_data, fp)
