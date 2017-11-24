class Albums_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = AlbumMenu_listener()

    def show(self, albums):
        i = 0
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("Albums\n")
        for album in albums:
            print('* ' + album.title, '\t tracks:', len(album.number_of_songs))

        album_name = input("Choose an album or enter 0 for main menu: ")

        print('/////////////////////////////')
        self.choice_listener.onAlbumMenuInput(album_name)

class AlbumDetails_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = AlbumMenu_listener()
    def showAlbumDetails(self,album):
        print('/////////////////////////////\n')
        print("Album name: "+album.title+'\n')

        for song in album.songs:
            print('*',song.name+'\tDuration',song.length)

        song_name = input("Choose a song or enter 0 for main menu: ")

        print('/////////////////////////////')
        self.choice_listener.onSongSelected(song_name)

class AlbumMenu_listener():
    def onAlbumMenuInput(self, choice):
        pass

    def onSongSelected(self, choice):
        pass