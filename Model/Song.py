class Song:
    name = ''
    bands = []
    album = None
    release_date = ''
    lyrics = ''
    genres = []
    length = 0

    def __init__(self, name, artists, bands, album, release_date, lyrics, genres, length):
        self.name = name
        self.bands = bands
        self.album = album
        self.release_date = release_date
        self.lyrics = lyrics
        self.genres = genres
        self.length = length
