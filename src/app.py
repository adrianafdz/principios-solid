# Adriana Fernández López A01197148
# Actividad: Principios Solid

from util.web_parser import MovieWebParser
from util.file_writer import FileWriter

from models.movie import Movie

def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    movie_file_reader = MovieWebParser(url, 'lxml')
    movie_file_reader.download_file()

    movies, links, crew, ratings, votes = movie_file_reader.get_movie_details()

    # create a empty list for storing movie information
    list = []

    # Iterating over movies to extract each movie's details
    for index in range(0, len(movies)):
        # Separating movie into: 'place', 'title', 'year'
        movie_string = movies[index].get_text()
        movie_title, year, place = movie_file_reader.process_movie_string(movie_string, index)

        data = Movie(
            movie_title,
            year,
            place,
            crew[index],
            ratings[index],
            votes[index],
            links[index],
            index % 4 + 1
        )
        
        list.append(data)

    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    
    fileWriter = FileWriter()
    fileWriter.create_csv("movie_results.csv", fields, list)

if __name__ == '__main__':
    main()
