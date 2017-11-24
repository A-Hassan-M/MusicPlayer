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
        self.choice_listener.on_input(album_name)


class AlbumMenu_listener():
    def on_input(self, choice):
        pass