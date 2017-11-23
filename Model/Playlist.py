class Playlist:
    name = ''
    description = ''
    songs = []

    def __init__(self, name, description, songs):
        self.name = name
        self.description = description
        self.songs = songs
