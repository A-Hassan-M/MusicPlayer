class Albums_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = AlbumMenuListener()

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
            album_name = input("Enter album name: ")
            self.choice_listener.onAlbumMenuInput(choice, album_name)
        else:
            self.choice_listener.onAlbumMenuInput(choice)
        print('/////////////////////////////')

class AlbumDetails_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = AlbumMenuListener()
    def showAlbumDetails(self,album):
        print('/////////////////////////////\n')
        print("Album name: "+album.name+'\n')

        if (len(album.songs) == 0):
            print("This album is empty!!\nEnter add to add a song to it\nEnter 0 to go back")
        else:
            for song in album.songs:
                print('*', song.name + '\tDuration', song.length)

        print("\nEnter song name to choose a song\nEnter 0 to go back\nEnter add to add a song")
        print("Or p to play playlist songs")

        choice = input("")

        print('/////////////////////////////')
        self.choice_listener.onSongMenuInput(choice)

class AddAlbumView():
    choice_listener = None
    def __init__(self):
        self.choice_listener = AlbumMenuListener()
    def showAlbumForm(self):
        album_name = input("Enter album name: ")
        self.choice_listener.onAlbumDataEntered(album_name)

class AlbumMenuListener():
    def onAlbumMenuInput(self, choice,additonal_attr=''):
        pass
    def onAlbumDataEntered(self, album_data):
        pass
    def onSongMenuInput(self, choice):
        pass