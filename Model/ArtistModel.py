from Model.SqlConnection import connection as conn
from Model.Artist import Artist
class ArtistModel:

    def get_artists(self):
        result = conn.execute("SELECT * FROM artist")
        artists = []

        for row in result:
            artist = Artist()
            artist.name = row[0]
            artist.date_of_birth = row[1]
            artist.band = row[2]
            artists.append(artist)
        return artists

    def add_artist(self, artist):
        conn.execute("INSERT INTO artist " +
                     "VALUES('" + artist.name + "', '" +
                     artist.date_of_birth + "', '" +
                     artist.band + "')")

        conn.commit()