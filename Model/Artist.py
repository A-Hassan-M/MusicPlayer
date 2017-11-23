class Artist:
    name =''
    date_of_birth = ''
    songs = []

    def __init__(self, name, date_of_birth, songs):
        self.name = name
        self.date_of_birth = date_of_birth
        self.songs = songs

    def addSong(self, song):
        self.songs.append(song)