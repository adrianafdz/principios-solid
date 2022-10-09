# En este módulo se aplica el principio de Open Closed.
# Al crear un modelo para los objetos utilizados, fácilmente
# se pueden añadir más funcionalidades sin afectar las demás partes
# del código que instancían esta clase,

class Movie:
    def __init__(self, movie_title, year, place, star_cast, rating, vote, link, preference_key):
        self.movie_title = movie_title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.preference_key = preference_key

    def to_dict(self):
        return {
            'movie_title': self.movie_title,
            'year': self.year,
            'place': self.place,
            'star_cast': self.star_cast,
            'rating': self.rating,
            'vote': self.vote,
            'link': self.link,
            'preference_key': self.preference_key,
        }