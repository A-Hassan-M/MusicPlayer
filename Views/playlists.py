
class Playlists_menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()

    def show(self,playlists):
        i = 0
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("PlayLists\n")
        for playlist in playlists:
            print('* '+playlist.name,'\t tracks:',len(playlist.songs))

        playlist_name = input("Choose a playlist or enter 0 for main menu: ")

        print('/////////////////////////////')
        self.choice_listener.on_input(playlist_name)

class PlaylistDetails_View():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlaylistMenu_listener()
    def showPlaylistDetails(self,playlist):
        print('/////////////////////////////\n')
        print("Playlist name: "+playlist.title+'\n')

        for song in playlist.songs:
            print('*',song.name+'\tDuration',song.length)

        song_name = input("Choose a song or enter 0 for main menu: ")

        print('/////////////////////////////')
        self.choice_listener.onSongSelected(song_name)

class PlaylistMenu_listener():
    def on_input(self,playlist_name):
        pass
    def onSongSelected(self,song_name):
        pass