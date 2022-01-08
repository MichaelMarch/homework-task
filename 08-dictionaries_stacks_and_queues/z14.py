import json

book = {
    "title": "The Mortal Instruments: City of Bones",
    "author": "Cassandra Clare",
    "genre": "Fantasy adventure",
    "pages": 512,
    "is_cover_hard": False,
}

with open("data/favourite.json", "w") as file:
    json.dump(book, file, indent=4)

