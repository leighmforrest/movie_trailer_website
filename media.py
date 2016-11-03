import webbrowser


class Video():
    """Class that contains basic video information."""

    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline


class Movie(Video):
    """This class provides a way to store movie-related information.
    Inherits from Video."""

    def __init__(self, title, storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
