film_titles = ["Interstellar", "Z-Nation", "Resident Evil", "Legion", "The Magicians"]


with open("data/films.txt", 'w') as file:
    file.write('\n'.join(film_titles))