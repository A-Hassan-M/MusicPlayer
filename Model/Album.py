import Model.Band as Band

class Album:
    title = ''
    number_of_songs = 0
    songs = []

    def __init__(self, title, num_of_songs, band, songs):
        self.title = title
        self.number_of_songs = num_of_songs
        self.band = band
        self.songs = songs
