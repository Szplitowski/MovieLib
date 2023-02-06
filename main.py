from random import randint
from datetime import datetime

today = datetime.now().strftime("%d/%m/%Y")


class Title:
    def __init__(self, title, release_year, genre, views):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views

    def play(self):
        self.views += 1

    def __repr__(self):
        return f"{self.title} ({self.release_year}, {self.views})"


class Movie(Title):
    def __init__(self, title, release_year, genre, views):
        super().__init__(title, release_year, genre, views)

    def play(self):
        self.views += 1

    def __repr__(self):
        return f"{self.title} ({self.release_year}, {self.views})"


class Series(Title):
    def __init__(self, title, release_year, genre, views, season, episode):
        super().__init__(title, release_year, genre, views)
        self.season = season
        self.episode = episode

    def play(self):
        self.views += 1

    def __repr__(self):
        return f"{self.title} S0{self.season}E0{self.episode}"


library = [
    Movie("Shrek 1", 2020, "gatunek 1", 100),
    Movie("Shrek 2", 2019, "gatunek 2", 200),
    Series("Serial 1", 2021, "gatunek 3", 300, 1, 1),
    Series("Serial 2", 2018, "gatunek 4", 400, 2, 1),
    Movie("Shrek 3", 2022, "gatunek 1", 150),
    Series("Serial 3", 2021, "gatunek 5", 350, 3, 1),
]


def get_movies():
    return sorted(
        [title for title in library if isinstance(title, Movie)], key=lambda x: x.title
    )


def get_series():
    return sorted(
        [title for title in library if isinstance(title, Series)], key=lambda x: x.title
    )


def search(title):
    for item in library:
        if item.title == title:
            return item
    return None


def generate_views():
    title = library[randint(0, len(library) - 1)]
    title.views += randint(1, 100)


def generate_10():
    for i in range(10):
        generate_views()


def top_titles(n):
    sorted_library = sorted(library, key=lambda x: x.views, reverse=True)
    return [title.title for title in sorted_library[:n]]


print("Biblioteka filmów i seriali")
generate_10()
print(f"Najpopularniejsze filmy i seriale dnia {today}:")
for title in top_titles(5):
    print(title)


"""
# sprawdzenie funkcji play():

print(library[0])
pozycja = library[0]
pozycja.play()
print(library[0])


# sprawdzenie get films i movies:

filmy = get_movies(library)
seriale = get_series(library)
print(filmy)
print(seriale)


# search

wynik = search("Shrek 1")
if wynik:
    print(wynik.title, wynik.release_year, wynik.genre)
else:
    print("Nie znaleziono filmu lub serialu o podanym tytule")

"""
