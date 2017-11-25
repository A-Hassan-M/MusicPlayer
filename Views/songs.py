from Model.Song import Song

class Song_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = SongOptions_listener()
    def showSongDetails(self, song):
        print('/////////////////////////////\n')

        print("Song:",song.name)
        print("Band/Artist:",song.bands)
        print("Featured band/artist:",song.bands)
        print("Album:",song.album)
        print("Release date:",song.release_date)
        print("Genres:",song.genres)

        choice = input("Enter p to play the song or 0 to go back: ")

        print('/////////////////////////////')
        self.choice_listener.onSongOptionsInput(choice)

class AddSongView():
    choice_listener = None
    def __init__(self):
        self.choice_listener = SongOptions_listener()
    def showSongForm(self):
        song = Song()
        song.name = input("Enter song name: ")
        song.genres = input("Enter song genre: ").split(',')
        song.release_date = input("Enter song release date: ")
        song.length = input("Enter song duration: ")
        song.album = input("Enter song album: ")
        song.bands = input("Enter song band/artist: ").split(',')
        song.featured_bands = input("Enter song featured band/artist: ").split(',')
        song.path = input("Enter song's full path: ")
        self.choice_listener.onSongCreated(song)


class SongOptions_listener():
    def onSongOptionsInput(self,choice):
        pass
    def onSongCreated(self,song):
        pass