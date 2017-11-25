class Albums_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = AlbumMenu_listener()

    def show(self, albums):
        i = 0
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        if (len(albums) == 0):
            print("No albums were found!!\n2- Back to home      3- Add album")
        else:
            i = 1
            for album in albums:
                print(i, '- ' + album.name, '\t tracks:', len(album.songs))
                i += 1
            print("\n1- View album     2- Back to home")
            print("3- Add album      4- Delete album")
        choice = input()

        if (choice == '4' or choice == '1'):
            album_name = input("Enter playlist name: ")
            self.choice_listener.onAlbumMenuInput(choice, album_name)
        else:
            print("choice",choice)
            self.choice_listener.onAlbumMenuInput(choice)
        print('/////////////////////////////')

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
    def onAlbumMenuInput(self, choice,additonal_attr=''):
        pass

    def onSongSelected(self, choice):
        pass