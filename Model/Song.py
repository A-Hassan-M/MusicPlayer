class Song:
    name = ''
    bands = []
    featured_bands = []
    album = None
    release_date = ''
    lyrics = ''
    genres = []
    length = 0
    path = ''

    def __init__(self, name, bands, featured_bands, album, release_date, lyrics, genres, length):
        self.name = name
        self.bands = bands
        self.featuredBands = featured_bands
        self.album = album
        self.release_date = release_date
        self.lyrics = lyrics
        self.genres = genres
        self.length = length
