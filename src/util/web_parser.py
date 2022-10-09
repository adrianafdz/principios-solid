import re
import requests
from bs4 import BeautifulSoup

# En este módulo utilizo el principio de Single Responsibility,
# pues creé esta clase para hacerse responsable de una sola cosa,
# que es parsear las páginas web.
class WebParser:
    '''Clase que permite analizar sitios web y seleccionar datos de estas.'''
    def __init__(self, src, parser):
        self.src = src
        self.parser = parser

    def download_file(self):
        response = requests.get(self.src)
        self.soup = BeautifulSoup(response.text, self.parser)

    def select(self, selector):
        return self.soup.select(selector)

    def get_attribute(self, attribute, selector):
        return [a.attrs.get(attribute) for a in self.select(selector)]

# Aquí utilicé el principio de Interface Segregation, pues creé una clase
# que hereda de Web Parser, pero además añade otras funcionalidades que
# específicamente se utilizan para analizar el sitio sobre películas.
class MovieWebParser(WebParser):
    def get_movie_details(self):
        movies = self.select('td.titleColumn')
        links = self.get_attribute('href', 'td.titleColumn a')
        crew = self.get_attribute('title', 'td.titleColumn a')
        ratings = self.get_attribute('data-value', 'td.posterColumn span[name=ir]')
        votes = self.get_attribute('data-value', 'td.ratingColumn strong')

        return movies, links, crew, ratings, votes

    def process_movie_string(self, movie_string, index):
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]

        return movie_title, year, place