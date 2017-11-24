from Model.Playlist import Playlist

class Playlists_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()

    def show(self,playlists):
        i = 0
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("PlayLists\n")
        if(len(playlists) == 0):
            print("No playlists were found!! write add to create a new one")
        else:
            for playlist in playlists:
                print('* '+playlist.name,'\t tracks:',len(playlist.songs))
            print("1- Enter playlist name to choose a playlist")
            print("2- Enter add to create a new playlist")
        choice = input()

        print('/////////////////////////////')
        self.choice_listener.on_playlists_menu_input(choice)

class PlaylistDetails_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()
    def showPlaylistDetails(self,playlist, songs):
        print('/////////////////////////////\n')
        print("Playlist name:",playlist.name+'\n')
        print("Description:", playlist.description+'\n')

        for song in songs:
            print('*',song.name+'\tDuration',song.length)
        print("Enter song name to choose a song\nEnter 0 to go back\nEnter add to add a song")
        choice = input("")

        print('/////////////////////////////')
        self.choice_listener.onSongSelected(choice)

class AddPlayList_View():
    choice_listener = None
    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()
    def showPlaylistForm(self):
        playlist = Playlist()
        playlist.name = input("Enter playlist name")
        playlist.description = input("Enter playlist description")
        self.choice_listener.onPlaylistCreated(playlist)

class PlaylistMenu_listener():
    def on_playlists_menu_input(self,playlist_name):
        pass
    def onSongSelected(self,song_name):
        pass
    def onPlaylistCreated(self,playlist):
        pass