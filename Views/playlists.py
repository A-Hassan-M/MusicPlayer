from Model.Playlist import Playlist

class Playlists_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()

    def show(self,playlists):
        i = 0
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("PlayLists:\n")
        if(len(playlists) == 0):
            print("No playlists were found!!\n2- Back to home      3- Add playlist")
        else:
            i = 1
            for playlist in playlists:
                print(i,'- '+playlist.name,'\t tracks:',len(playlist.songs))
                i +=1
            print("\n1- View pLaylist     2- Back to home")
            print("3- Add playlist      4- Delete Playlist")
        choice = input()

        if(choice == '4' or choice == '1'):
            playlist_name = input("Enter playlist name: ")
            self.choice_listener.on_playlists_menu_input(choice,playlist_name)
        else:
            self.choice_listener.on_playlists_menu_input(choice)
        print('/////////////////////////////')

class PlaylistDetails_View():
    choice_listener = None
    playlist = []
    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()
    def showPlaylistDetails(self,playlist):
        self.playlist = playlist
        print('/////////////////////////////\n')
        print("Playlist name:",playlist.name+'\n')
        print("Description:", playlist.description+'\n')

        if(len(playlist.songs) == 0):
            print("This playlist is empty!!\nEnter add to add a song to it\nEnter 0 to go back")
        else:
            self.show_songs()

            print("\nEnter song name to choose a song\nEnter 0 to go back\nEnter add to add a song")
            print("Or p to play playlist songs")
        choice = input("")

        # if(choice == 'order'):
        #     order_attr = self.get_order_choice()

        print('/////////////////////////////')
        self.choice_listener.onSongMenuInput(choice)

    def show_songs(self):
        songs = self.playlist.songs
        for song in songs:
            print('*', song.name + '\tDuration', song.length)

    def get_order_choice(self):
        print("1- Name\t2- Album\t3- Release date")
        options = {'1':'name','2':'album','3':'release_date'}
        order_choice = options[input()]
        return order_choice


class AddPlayListView():
    choice_listener = None
    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()
    def showPlaylistForm(self):
        playlist = Playlist()
        playlist.name = input("Enter playlist name: ")
        playlist.description = input("Enter playlist description: ")
        self.choice_listener.onPlaylistCreated(playlist)

class PlaylistMenu_listener():
    def on_playlists_menu_input(self,choice,additional_attr=''):
        pass
    def onSongMenuInput(self,song_name):
        pass
    def onPlaylistCreated(self,playlist):
        pass
    def onOrderOptionChosen(self,order_attr):
        pass