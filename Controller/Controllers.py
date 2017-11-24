from Model.ArtistModel import ArtistModel
from Model.PlaylistModel import PlaylistModel
from Model.AlbumModel import AlbumModel
from Model.SongModel import SongModel

from Views.albums import Albums_menu, AlbumMenu_listener,AlbumDetails_View
from Views.artists import Artists_menu, ArtistMenu_listener
from Views.playlists import Playlists_menu,PlaylistMenu_listener,PlaylistDetails_View
from Views.songs import Song_View,SongOptions_listener
from Views.menu import Menu,MainMenu_listener


class Playlist_Menu_Controller(PlaylistMenu_listener):
    playlistDBModel = None
    playlists = []
    menu = None
    def __init__(self):
        self.playlistDBModel = PlaylistModel()

        self.menu = Playlists_menu()
        self.menu.choice_listener = self

    def showAllPlaylists(self):
        if(len(self.playlists) == 0):
            self.playlists = self.playlistDBModel.get_playlists()
        self.menu.show(self.playlists)

    def on_input(self,playlist_name):
        if(playlist_name == '0'):
            Main().showMainMenu()
        else:
            playlist = None
            for pl in self.playlists():
                if (pl.name == playlist_name):
                    playlist = pl
                    break
            if(playlist is None):
                print("playlist doesn't exist!!")
            else:
                songController = SongController()
                songs = songController.getPlaylistSongs(playlist_name)

                self.menu = PlaylistDetails_View()
                self.menu.choice_listener = self
                self.menu.showPlaylistDetails(playlist, songs)
    def onSongSelected(self,song_name):
        if (song_name == '0'):
            Main().showMainMenu()
        else: print(song_name)


class SongController(SongOptions_listener):
    songDBModel = None
    songs = []
    menu = None

    def __init__(self):
        self.songDBModel = SongModel
        self.menu = Song_View()
        self.menu.choice_listener = self
    def getPlaylistSongs(self,playlist_name):
        if (len(self.songs) == 0):
            self.songs = self.songDBModel.getPlaylistSongs(playlist_name)
        return self.songs
    def showSongDescription(self,song_name):
        song = None
        for sg in self.songs():
            if (sg.name == song_name):
                song = sg
                break
        self.menu.showSongDetails(song)
    def on_input(self,choice):
        if(choice == '0'):
            Playlist_Menu_Controller.showAllPlaylists()
        else:print("play song")


class ArtistMenuController(ArtistMenu_listener):
    artistDBModel = None
    menu = None

    def __init__(self):
        self.artistDBModel = ArtistModel()
        self.menu = Artists_menu()
        self.menu.choice_listener = self

    def showAllArtists(self):
        artists = self.artistDBModel.get_artists()
        self.menu.show(artists)

    def on_input(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            pass

class AlbumMenuController(AlbumMenu_listener):
    albumDBModel = None
    menu = None

    def __init__(self):
        self.albumDBModel = AlbumModel()
        self.menu = Albums_menu()
        self.menu.choice_listener = self

    def showAllAlbums(self):
        albums = self.albumDBModel.get_albums()
        self.menu.show(albums)

    def on_input(self, choice):
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

#Done
class Main(MainMenu_listener):
    menu = None
    def showMainMenu(self):
        self.menu = Menu()
        self.menu.choice_listener = self
        self.menu.show_options()

    def on_input(self, choice):
        if(choice == '1'):
            playlist_controller = Playlist_Menu_Controller()
            playlist_controller.showAllPlaylists()

        elif (choice == '2'):
            artist_controller = ArtistMenuController()
            artist_controller.showAllArtists()

        elif(choice == '3'):
            album_controller = AlbumMenuController()
            album_controller.showAllAlbums()

        else: print("Bye :)")

Main().showMainMenu()