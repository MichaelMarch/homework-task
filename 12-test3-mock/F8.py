import xml.etree.ElementTree as ET


class C:
    def __init__(self):
        self.tree = ET.parse("mockdata.xml")
        self.root = self.tree.getroot()

    def m(self, n1, n2):
        counter = 0
        for ele in self.root:
            if int(ele[2][1].text) < n1:
                continue
            if len(ele[3].findall("name")) < n2:
                continue

            counter += 1

        return counter
