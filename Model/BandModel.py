from Model.SqlConnection import connection as conn
from Model.SongModel import song_model

class BandModel:

    def get_songs(self, band_name):
        result = conn.execute("SELECT song_name FROM song_band " +
                              "WHERE band_name = '" + band_name + "'")

        songs = []
        for row in result:
            songs.append(song_model.get_song(row[0]))

        return songs
    def add_band(self,band_name):
        conn.execute("INSERT INTO playlist_song VALUES('" + band_name + "')")
        conn.commit()

    def add_song_band(self,song):
        for band_name in song.bands:
            conn.execute("INSERT INTO song_band VALUES'" + song.name +"','"
                                                         + band_name +"',"
                                                         + False +")")
        for band_name in song.featured_bands:
            conn.execute("INSERT INTO song_band VALUES'" + song.name + "','"
                                                         + band_name + "',"
                                                         + True + ")")

        conn.commit()
band_model = BandModel()

