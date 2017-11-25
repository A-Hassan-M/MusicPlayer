from Model.SqlConnection import connection as conn
from Model.Album import Album
from Model.SongModel import song_model

class AlbumModel:

    def get_albums(self):
        result = conn.execute("SELECT * FROM album")

        albums = []

        for row in result:
            album = self.get_album(row[0])
            albums.append(album)

        return albums

    def get_album(self, name):
        result = conn.execute("SELECT * FROM album " +
                              "WHERE name = '" + name + "'")
        album = Album()

        for row in result:
            album.name = row[0]

        result = conn.execute("SELECT name FROM song " +
                              "WHERE album_name = '" + album + "'")
        for song_name in result:
            album.songs.append(song_model.get_song(song_name))

        album.number_of_songs = len(album.songs)

        return album

    def add_album(self, name):
        conn.execute("INSERT INTO album VALUES('" + name + "'")
        conn.execute()

    def remove_album(self,title):


        return True

album_model = AlbumModel()