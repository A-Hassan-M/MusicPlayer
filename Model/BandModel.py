from Model.SqlConnection import connection as conn
from Model.SongModel import song_model

class BandModel:

    def get_songs(self, band_name):
        result = conn.execute("SELECT song_name FROM song_band " +
                              "WHERE band_name = '" + band_name + "'")

        songs = []
        for row in result:
            songs.append(song_model.get_song(row[0]))

        return songs;

