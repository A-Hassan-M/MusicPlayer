from Model.ArtistModel import ArtistModel
from Model.PlaylistModel import PlaylistModel
from Model.AlbumModel import AlbumModel
from Model.SongModel import SongModel

from Views.albums import Albums_menu, AlbumMenu_listener,AlbumDetails_View
from Views.artists import Artists_menu, ArtistMenu_listener
from Views.playlists import Playlists_menu,PlaylistMenu_listener,PlaylistDetails_View
from Views.playlists import AddPlayList_View
from Views.songs import Song_View,SongOptions_listener,AddSong_View
from Views.menu import Menu,MainMenu_listener

# Playlist Controller
class PlaylistController(PlaylistMenu_listener):
    playlistDBModel = None
    playlists = []
    playlist = None
    menu = None

    def __init__(self):
        self.playlistDBModel = PlaylistModel()

    def showAllPlaylists(self):
        self.menu = Playlists_menu()
        self.menu.choice_listener = self
        self.playlists = self.playlistDBModel.get_playlists()
        self.menu.show(self.playlists)

    def showPlaylist(self, playlist_name):
        self.playlist = self.getPlaylist(playlist_name)
        if (self.playlist is None):
            print("playlist doesn't exist!!")
        else:
            songController = SongController()
            songs = songController.getPlaylistSongs(playlist_name)
            self.menu = PlaylistDetails_View()
            self.menu.choice_listener = self
            self.menu.showPlaylistDetails(self.playlist, songs)

    def getPlaylist(self,playlist_name):
        if(len(self.playlists)==0):
            self.playlists = self.playlistDBModel.get_playlists()
        for pl in self.playlists:
            if (pl.name == playlist_name):
                return pl
        return None

    def on_playlists_menu_input(self,choice):
        if(choice == '0'):
            Main().showMainMenu()
        elif(choice == 'add'):
            self.menu = AddPlayList_View()
            self.menu.choice_listener = self
            self.menu.showPlaylistForm()
        else:
            self.showPlaylist(choice)

    def onSongSelected(self,choice):
        if (choice == '0'):
            self.showAllPlaylists()
        elif(choice == 'add'):
            songController = SongController()
            songController.addSongToPLaylist(self.playlist.name)
        else: print(choice)

    def onPlaylistCreated(self,playlist):
        self.playlistDBModel.add_playlist(playlist.name,playlist.description)
        print("playlist created")
        self.showAllPlaylists()

# Song Controller
class SongController(SongOptions_listener):
    songDBModel = None
    songs = []
    playlist_name = ''
    menu = None

    def __init__(self):
        self.songDBModel = SongModel
        self.menu = Song_View()
        self.menu.choice_listener = self

    def getPlaylistSongs(self,playlist_name):
        self.playlist_name = playlist_name
        if (len(self.songs) == 0):
            self.songs = self.songDBModel.getPlaylistSongs(playlist_name)
        return self.songs

    def addSongToPLaylist(self,playlist_name):
        self.playlist_name = playlist_name
        self.menu = AddSong_View()
        self.menu.choice_listener = self
        self.menu.showSongForm()

    def showSongDescription(self,song_name):
        song = self.getSong(song_name)
        if (song is None):
            print("song doesn't exist!!")
        else:
            self.menu.showSongDetails(song)

    def getSong(self,song_name):
        if(len(self.songs) == 0):
            self.songs = self.songDBModel.getPlaylistSongs(song_name)
        for song in self.songs():
            if (song.name == song_name):
                return song
        return None

    def onSongOptionsInput(self,choice):
        if(choice == '0'):
            PlaylistController().showPlaylist(self.playlist_name)
        else:print("play song")

    def onSongCreated(self,song):
        #self.songDBModel.add_song(song)
        print("song created")
        PlaylistController().showPlaylist(self.playlist_name)

# Artist Controller
class ArtistMenuController(ArtistMenu_listener):
    artistDBModel = None
    artists = []
    menu = None

    def __init__(self):
        self.artistDBModel = ArtistModel()
        self.menu = Artists_menu()
        self.menu.choice_listener = self

    def showAllArtists(self):
        self.artists = self.artistDBModel.get_artists()
        self.menu.show(self.artists)

    def onAlbumMenuInput(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            pass

# Album Controller
class AlbumMenuController(AlbumMenu_listener):
    albumDBModel = None
    menu = None
    albums = []

    def __init__(self):
        self.albumDBModel = AlbumModel()
        self.menu = Albums_menu()
        self.menu.choice_listener = self

    def showAllAlbums(self):
        self.albums = self.albumDBModel.get_albums()
        self.menu.show(self.albums)

    def onAlbumMenueInput(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            album = self.albumDBModel.get_album(choice)
            self.menu = AlbumDetails_View()
            self.menu.choice_listener = self
            self.menu.showAlbumDetails(album)

    def onSongSelected(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            pass

# Main Menu Controller
class Main(MainMenu_listener):
    menu = None
    def showMainMenu(self):
        self.menu = Menu()
        self.menu.choice_listener = self
        self.menu.show_options()

    def on_input(self, choice):
        if(choice == '1'):
            playlist_controller = PlaylistController()
            playlist_controller.showAllPlaylists()

        elif (choice == '2'):
            artist_controller = ArtistMenuController()
            artist_controller.showAllArtists()

        elif(choice == '3'):
            album_controller = AlbumMenuController()
            album_controller.showAllAlbums()

        else: print("Bye :)")

Main().showMainMenu()