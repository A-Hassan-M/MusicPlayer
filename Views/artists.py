
class Artists_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = ArtistMenu_listener()

    def show(self, artists):
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("Artists\n")
        for artist in artists:
            print('* ' + artist.name, '\t Birth_Day:', artist.date_of_birth)

        artist_name = input("Choose an artist to show his/her songs\nor enter 0 for main menu: ")

        print('/////////////////////////////')
        self.choice_listener.onAlbumMenuInput(artist_name)

class ArtistMenu_listener():
    def onArtistMenuInput(self,choice):
        print(choice)
        pass