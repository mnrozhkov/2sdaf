__author__ = 'Mikhail'
__author__ = 'Mikhail'
import webbrowser

class Video():
    """Defines a parent class for any video content

    Attributes:
        title: A title of video
    """

    def __init__(self, title):
        """Inits Video class instance with name of title """

        self.title = title
        #self.duration = duration

    def show_info(self):
        """Prints class instance title """

        print("Video Name -" + self.title)


class Movie(Video):
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,poster_image,tralier_youtube, director_name, rating, release_date):
        """Inits Movie class instance

        Attributes:
            movie_title: A movie title
            movie_storyline: A short movie storyline
            poster_image: URL to movie poster image
            tralier_youtube: URL to movie trailer on YouTube
            director_name: Director of the movie
            rating: Rating based on rating from http://www.imdb.com/
            release_date: Release date of the movie
        """

        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = tralier_youtube
        self.director = director_name
        self.rating = rating
        self.release_date = release_date

    def show_tralier(self):
        """Launches movie trailer in web browser"""

        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        """Shows movie title and storyline"""

        print("Movie Name: " + self.title)
        print("Movie Storyline: " + self.storyline)
        print("Director: " + self.director)
        print("Rating: " + self.rating)
        print("Release Date: " + self.release_date)

