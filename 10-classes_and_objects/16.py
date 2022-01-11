from ebook import EBook

ebook1 = EBook("The mortal instruments: City of Bones", "Cassandra Clare", 505)
ebook1.open()
print(ebook1)
for i in range(11):
    ebook1.read()
print(ebook1)
ebook1.close()
for i in range(3):
    ebook1.read()