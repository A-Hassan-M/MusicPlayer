class Song:
    name = ''
    artists = []
    bands = []
    album_title = ''
    release_date = ''
    lyrics = ''
    genres = ''
    length = 0

    def __init__(self, name, artists, bands, album_title, release_date, lyrics, genres, length):
        self.name = name
        self.artists = artists
        self.bands = bands
        self.album_title = album_title
        self.release_date = release_date
        self.lyrics = lyrics
        self.genres = genres
        self.length = length
