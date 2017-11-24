class Song_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = SongOptions_listener()
    def showSongDetails(self, song):
        print('/////////////////////////////\n')

        print("Song:",song.name)
        print("Band/Artist:",song.bands)
        print("Featured artist/band:",song.bands)
        print("Album:",song.album_title)
        print("Release date:",song.release_date)
        print("Genres:",song.genres)

        choice = input("Enter p to play the song or 0 to go back")

        print('/////////////////////////////')
        self.choice_listener.onSongSelected(choice)

class SongOptions_listener():
    def on_input(self,choice):
        pass