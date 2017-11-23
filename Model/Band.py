class Band:
    name =''
    artists = []
    songs = []

    def __init__(self, name, artists, songs):
        self.name = name
        self.artists = artists
        self.songs = songs

    def addSong(self, song):
        self.songs.append(song)