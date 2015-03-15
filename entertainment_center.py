__author__ = 'Mikhail'
""" The Movie Trailer Website project


It consists of server-side code
to store a list  of movies titles, along with its respective
box art imagery and movie trailer website.
The data should be served as a web page allowing visitors to
review the movies and watch the trailers
Page allows users to click on a movie image to watch its trailer
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and "
                        "jealous when a new spaceman figure supplants "
                        "him as top toy in a boy's room.",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                        "http://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter",
                        "8.3/10",
                        "22 November 1995 (USA)")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A Paraplegic Marine dispatched to the moon Pandora "
                        "on a unique mission becomes torn between following"
                        " his orders and protecting the world he feels is his home.",
                        "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "http://www.youtube.com/watch?v=cRdxXPV9GNQ",
                        "James Cameron",
                        "7.9/10",
                        "18 December 2009 (USA)")
#print(avatar.storyline)
#toy_story.show_tralier()

matrix = media.Movie("Matrix",
                        "A computer hacker learns from mysterious rebels "
                        "about the true nature of his reality and his role"
                        " in the war against its controllers.",
                        "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                        "http://www.youtube.com/watch?v=m8e-FF8MsqU",
                        "The Wachowski Brothers",
                        "8.7/10",
                        "31 March 1999 (USA)")

transformers = media.Movie("Transformers",
                        "Autobots must escape sight from a bounty hunter who"
                        " takes control of the human serendipity: Unexpectedly,"
                        " Optimus Prime and his remaining gang turn to "
                        "a mechanic and his daughter for help.",
                        "http://ia.media-imdb.com/images/M/MV5BMjEwNTg1MTA5Nl5BMl5BanBnXkFtZTgwOTg2OTM4MTE@._V1_SX214_AL_.jpg",
                        "http://www.youtube.com/watch?v=dYDGqmxMZFI",
                        "Michael Bay",
                        "7.2/10",
                        "3 July 2007 (USA)")


star_wars_7 = media.Movie("Star Wars Episode VII: The Force Awakens",
                        "A continuation of the saga created by George Lucas"
                        " set thirty years after Star Wars: Episode VI - "
                        "Return of the Jedi (1983).",
                        "http://ia.media-imdb.com/images/M/MV5BMjM4MjI2MDMwM15BMl5BanBnXkFtZTgwODI2MDgzMzE@._V1_SX214_AL_.jpg",
                        "http://www.youtube.com/watch?v=TAudKqTZKZk",
                        "J.J. Abrams",
                        "7.9/10",
                        "18 December 2015 (USA)")


terminator_genisys = media.Movie("Terminator Genisys",
                        "After finding himself in a new time-line, Kyle Reese"
                        " teams up with John Connor's mother Sarah and an aging"
                        " terminator to try and stop the one thing that "
                        "the future fears.",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ3OTY2ODY4NV5BMl5BanBnXkFtZTgwNjA1ODQyNDE@._V1_SX214_AL_.jpg",
                        "http://www.youtube.com/watch?v=62E4FJTwSuc",
                        "Alan Taylor",
                        "7.9/10",
                        "1 July 2015 (USA)")

movies = [toy_story, avatar, matrix, transformers, star_wars_7, terminator_genisys]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(toy_story.show_info())