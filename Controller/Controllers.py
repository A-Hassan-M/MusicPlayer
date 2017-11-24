from Model.ArtistModel import ArtistModel
from Model.PlaylistModel import PlaylistModel
from Model.AlbumModel import AlbumModel
from Model.SongModel import SongModel

from Views.albums import Albums_menu, AlbumMenu_listener,AlbumDetails_View
from Views.artists import Artists_menu, ArtistMenu_listener
from Views.playlists import Playlists_menu,PlaylistMenu_listener,PlaylistDetails_View
from Views.menu import Menu,MainMenu_listener


class Playlist_Menu_Controller(PlaylistMenu_listener):
    playlistDBModel = None
    menu = None
    def __init__(self):
        self.playlistDBModel = PlaylistModel()
        self.menu = Playlists_menu()
        self.menu.choice_listener = self

    def showAllPlaylists(self):
        playlists = self.playlistDBModel.get_playlists()
        self.menu.show(playlists)

    def on_input(self,choice):
        if(choice == '0'):
            Main().showMainMenu()
        else:
            playlist = self.playlistDBModel.get_playlist(choice)
            self.menu = PlaylistDetails_View()
            self.menu.choice_listener = self
            self.menu.showPlaylistDetails(playlist)
    def onSongSelected(self,song_name):
        if (song_name == '0'):
            Main().showMainMenu()
        else: print(song_name)


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