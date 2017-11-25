from Model.ArtistModel import ArtistModel
from Model.PlaylistModel import pm
from Model.AlbumModel import AlbumModel
from Model.SongModel import song_model

from Views.albums import Albums_menu, AlbumMenu_listener,AlbumDetails_View
from Views.artists import Artists_menu, ArtistMenu_listener
from Views.playlists import Playlists_menu,PlaylistMenu_listener,PlaylistDetails_View
from Views.playlists import AddPlayList_View
from Views.songs import Song_View,SongOptions_listener,AddSong_View
from Views.menu import Menu,MainMenu_listener

from Media.MediaPlayer import media_player

# Playlist Controller
class PlaylistController(PlaylistMenu_listener):
    playlists = []
    playlist = None
    menu = None
    songController = None

    def showAllPlaylists(self):
        if(len(self.playlists) == 0):
            self.playlists = pm.get_playlists()
        self.menu = Playlists_menu()
        self.menu.choice_listener = self
        self.menu.show(self.playlists)

    def showPlaylist(self, playlist_name):
        self.playlist = self.getPlaylist(playlist_name)
        if (self.playlist is None):
            print("playlist doesn't exist!!")
            self.showAllPlaylists()
        else:
            self.playlist = pm.get_playlist(playlist_name)
            self.menu = PlaylistDetails_View()
            self.menu.choice_listener = self
            self.menu.showPlaylistDetails(self.playlist)

    def getPlaylist(self,playlist_name):
        if(len(self.playlists)==0):
            self.playlists = pm.get_playlists()
        for pl in self.playlists:
            if (pl.name == playlist_name):
                return pl
        return None

    def on_playlists_menu_input(self,choice,playlist_name=''):
        if(choice == '1'):
            self.showPlaylist(playlist_name)
        elif(choice == '2'):
            Main().showMainMenu()
        elif(choice == '3'):
            self.menu = AddPlayList_View()
            self.menu.choice_listener = self
            self.menu.showPlaylistForm()
        elif(choice == '4'):
            pm.remove_playlist(playlist_name)

    def onSongSelected(self,choice):
        if (choice == '0'):
            self.showAllPlaylists()
        elif(choice == 'add'):
            if(self.songController is None):
                self.songController = PlaylistSongsController()
            self.songController.addSongToPLaylist(self.playlist.name)
        else:
            if (self.songController is None):
                self.songController = PlaylistSongsController()
            self.songController.showSongDescription(choice,self.playlist.name)

    def onPlaylistCreated(self,playlist):
        try:
            pm.add_playlist(playlist.name,playlist.description)
            self.playlists.append(playlist)
            print("\nPlaylist created")
        except:
            print("/////////////////////////////")
            print("There is a playlist with this name")
        self.showAllPlaylists()

# Association Controller
class PlaylistSongsController(SongOptions_listener):
    songs = []
    playlist_name = ''
    song = None
    def __init__(self):
        self.menu = Song_View()
        self.menu.choice_listener = self

    def getPlaylistSongs(self,playlist_name):
        self.playlist_name = playlist_name
        if (len(self.songs) == 0):
            self.songs = song_model.getPlaylistSongs(playlist_name)
        return self.songs

    def getSong(self, song_name):
        if(len(self.songs) == 0):
            self.songs = song_model.getPlaylistSongs(self.playlist_name)
        for song in self.songs:
            if (song.name == song_name):
                return song
        return None

    def showSongDescription(self, song_name,playlist_name):
        self.playlist_name = playlist_name
        self.song = self.getSong(song_name)
        if (self.song is None):
            print("song doesn't exist!!")
            PlaylistController.showPlaylist(self.playlist_name)
        else:
            self.menu.showSongDetails(self.song)

    def addSongToPLaylist(self,playlist_name):
        self.playlist_name = playlist_name
        self.menu = AddSong_View()
        self.menu.choice_listener = self
        self.menu.showSongForm()

    def onSongOptionsInput(self,choice):
        if(choice == '0'):
            PlaylistController().showPlaylist(self.playlist_name)
        elif (choice == 'p'):
            try:
                media_player.play_song(self.song)
            except:
                print("The associated path is invalid")
            self.showSongDescription(self.song.name,self.playlist_name)


    def onSongCreated(self,song):
        #song_model.add_song(song)
        print("song created")
        PlaylistController().showPlaylist(self.playlist_name)

# Song Controller
class SongController(SongOptions_listener):
    songs = []
    menu = None
    media_player = None
    song = None
    def __init__(self):
        self.menu = Song_View()
        self.menu.choice_listener = self
        self.album_name = ''

    def getAlbumSongs(self,album_name):
        self.album_name = album_name
        if (len(self.songs) == 0):
            self.songs = song_model.getAlbumSongs(album_name)
        return self.songs

    def showSongDescription(self, song_name):
        self.song = self.getSong(song_name)
        if (self.song is None):
            print("song doesn't exist!!")
            AlbumMenuController().showAlbum(self.album_name)
        else:
            self.menu.showSongDetails(self.song)

    def getSong(self, song_name):
        if(len(self.songs) == 0):
            self.songs = song_model.getAlbumSongs(self.album_name)
        for song in self.songs:
            if (song.name == song_name):
                return song
        return None

    def onSongOptionsInput(self,choice):
        if(choice == '0'):
            AlbumMenuController().showAlbum(self.album_name)
        elif(choice == 'p'):
            try:
                media_player.play_song(self.song)
            except:
                print("The associated path is invalid")
            self.showSongDescription(self.song.name, self.playlist_name)

    def onSongCreated(self,song):
        #song_model.add_song(song)
        print("song created")
        AlbumMenuController().showAlbum(self.album_name)

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

    def onArtistMenuInput(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            pass

# Album Controller
class AlbumMenuController(AlbumMenu_listener):
    albumDBModel = None
    menu = None
    albums = []
    songController = None

    def __init__(self):
        self.albumDBModel = AlbumModel()

    def showAllAlbums(self):
        if(len(self.albums) == 0):
            self.albums = self.albumDBModel.get_albums()
        self.menu = Albums_menu()
        self.menu.choice_listener = self
        self.menu.show(self.albums)

    def showAlbum(self, album_name):
        album = self.getAlbum(album_name)
        if (album is None):
            print("album doesn't exist!!")
            self.showAllAlbums()
        else:
            if (self.songController is None):
                self.songController = SongController()
            songs = self.songController.getAlbumSongs(album_name)
            self.menu = AlbumDetails_View()
            self.menu.choice_listener = self
            self.menu.showAlbumDetails(album, songs)

    def getAlbum(self,album_name):
        if (len(self.albums) == 0):
            self.albums = self.albumDBModel.get_albums()
        for album in self.albums:
            if (album.name == album_name):
                return album
        return None

    def onAlbumMenuInput(self, choice,album_name=''):
        print("w ",choice)
        if (choice == '1'):
            self.showAlbum(album_name)
        elif (choice == '2'):
            Main().showMainMenu()
        elif (choice == '3'):
            # self.menu = AddAlbum_View()
            # self.menu.choice_listener = self
            # self.menu.showAlbumForm()
            pass
        elif (choice == '4'):
            pm.remove_album(album_name)

    def onSongSelected(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            if (self.songController is None):
                self.songController = SongController()
            self.songController.showSongDescription(choice)

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