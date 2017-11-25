import sys

from Model.SqlConnection import connection as conn
from Model.Song import Song

class SongModel:

    def get_song(self, name):

        song = Song()

        result = conn.execute("SELECT * FROM song " +
                              "WHERE name = '" + name + "'")

        for row in result:
            song.name = row[0]
            song.release_date = row[1]
            song.lyrics = row[2]
            song.length = row[3]
            song.path = row[4]
            song.album = row[5]

        result = conn.execute("SELECT band_name "+
                              "FROM song_band "+
                              "WHERE song_name = '" + name + "'" +
                              "AND featured = 'false'")
        for row in result:
            song.bands.append(row[0])

        result = conn.execute("SELECT band_name " +
                              "FROM song_band " +
                              "WHERE song_name = '" + name + "'" +
                              "AND featured = 'true'")
        for row in result:
            song.featured_bands.append(row[0])

        return song

    def add_song(self, song, playlist_name):
        conn.execute("INSERT INTO song VALUES('"+ song.name + "','"
                                                + song.release_date + "','"
                                                + song.lyrics + "','"
                                                + song.length + "','"
                                                + song.path + "','"
                                                + song.album + "')")

        conn.execute("INSERT INTO playlist_song VALUES('"+ playlist_name + "','"
                                                         + song.name + "')")
        conn.commit()

    def getPlaylistSongs(self,playlist_name):
        result = conn.execute("SELECT song_name "
                              "FROM playlist_song " +
                              "WHERE playlist_name = '" + playlist_name + "'")
        songs = []
        for row in result:
            songs.append(song_model.get_song(row[0]))

        return songs

    def remove_song(self, song_name):

        return True


song_model = SongModel()