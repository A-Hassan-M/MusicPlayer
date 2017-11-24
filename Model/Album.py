class Album:
    name = ''
    number_of_songs = 0
    songs = []

    def __init__(self, name, num_of_songs, songs):
        self.name = name
        self.number_of_songs = num_of_songs
        self.songs = songs
