from Model.ArtistModel import ArtistModel
from Model.PlaylistModel import pm
from Model.AlbumModel import album_model
from Model.SongModel import song_model
from Model.BandModel import band_model

from Views.albums import Albums_menu, AlbumMenuListener,AlbumDetails_View,AddAlbumView
from Views.artists import Artists_menu, ArtistMenu_listener
from Views.playlists import Playlists_menu,PlaylistMenu_listener,PlaylistDetails_View
from Views.playlists import AddPlayListView
from Views.songs import Song_View,SongOptions_listener,AddSongView
from Views.menu import Menu,MainMenu_listener

from Media.MediaPlayer import media_player

# Global function
def add_song(song, playlist_name):
    try:
        song_model.add_song(song, playlist_name)
        print("Song created")
    except:pass

    try:
        song_model.add_playlist_songs(song.name, playlist_name)
        print("Song created")
    except:print("Song name already exists")

    try:
        for band_name in song.bands:
            band_model.add_band(band_name)
        band_model.add_song_band(song)
    except:pass
    try:
        album_model.add_album(song.album)
    except: pass

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

    # Listeners
    def on_playlists_menu_input(self,choice,playlist_name=''):
        if(choice == '1'):
            self.showPlaylist(playlist_name)
        elif(choice == '2'):
            Main().showMainMenu()
        elif(choice == '3'):
            self.menu = AddPlayListView()
            self.menu.choice_listener = self
            self.menu.showPlaylistForm()
        elif(choice == '4'):
            pm.remove_playlist(playlist_name)

    def onSongMenuInput(self,choice):
        if (choice == '0'):
            self.showAllPlaylists()
        elif(choice == 'add'):
            if(self.songController is None):
                self.songController = PlaylistSongsController()
            self.songController.addSongToPLaylist(self.playlist.name)
        elif (choice == 'p'):
            print(len(self.playlist.songs))
            media_player.play_songs(self.playlist.songs)
            self.showPlaylist(self.playlist.name)
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
        self.song = song_model.get_song(song_name)
        if (self.song is None):
            print("song doesn't exist!!",self.playlist_name)
            PlaylistController().showPlaylist(self.playlist_name)
        else:
            self.menu.showSongDetails(self.song)

    def addSongToPLaylist(self,playlist_name):
        self.playlist_name = playlist_name
        self.menu = AddSongView()
        self.menu.choice_listener = self
        self.menu.showSongForm()

    # Listeners
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
        add_song(song, self.playlist_name)
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
            self.songs = album_model.get_album(album_name)
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

    # Listeners
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
        add_song(song, self.playlist_name)
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

    # Listeners
    def onArtistMenuInput(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        else:
            pass

# Album Controller
class AlbumMenuController(AlbumMenuListener):
    menu = None
    albums = []
    songController = None
    album = None

    def showAllAlbums(self):
        if(len(self.albums) == 0):
            self.albums = album_model.get_albums()
        self.menu = Albums_menu()
        self.menu.choice_listener = self
        self.menu.show(self.albums)

    def showAlbum(self, album_name):
        self.album = album_model.get_album(album_name)
        if (self.album is None):
            print("album doesn't exist!!")
            self.showAllAlbums()
        else:
            self.menu = AlbumDetails_View()
            self.menu.choice_listener = self
            self.menu.showAlbumDetails(self.album)

    def getAlbum(self,album_name):
        if (len(self.albums) == 0):
            self.albums = album_model.get_albums()
        for album in self.albums:
            if (album.name == album_name):
                return album
        return None

    # Listeners
    def onAlbumMenuInput(self, choice,album_name=''):
        print("w ",choice)
        if (choice == '1'):
            self.showAlbum(album_name)
        elif (choice == '2'):
            Main().showMainMenu()
        elif (choice == '3'):
            self.menu = AddAlbumView()
            self.menu.choice_listener = self
            self.menu.showAlbumForm()
        elif (choice == '4'):
            pm.remove_album(album_name)

    def onSongMenuInput(self, choice):
        if (choice == '0'):
            Main().showMainMenu()
        elif (choice == 'p'):
            media_player.play_songs(self.album.songs)
            self.showAlbum(self.album.name)
        else:
            if (self.songController is None):
                self.songController = SongController()
            self.songController.showSongDescription(choice, self.album.name)

    def onAlbumDataEntered(self, album_data):
        try:
            album_model.add_album(album_data)
        except: print("Album with the same name already exists")

# Main Menu Controller
class Main(MainMenu_listener):
    menu = None
    def showMainMenu(self):
        self.menu = Menu()
        self.menu.choice_listener = self
        self.menu.show_options()

    # Listeners
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