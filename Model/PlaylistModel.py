from Model.Playlist import Playlist
from Model.SongModel import song_model
from Model.SqlConnection import connection as conn

class PlaylistModel:

     def get_playlists(self):
        result = conn.execute("SELECT * FROM playlist")
        playlists = []
        for row in result:
            playlist = Playlist()
            playlist.name = row[0]
            playlist.description = row[1]
            playlists.append(playlist)

        for playlist in playlists:
            result = conn.execute("SELECT song_name " +
                                  "FROM playlist_song " +
                                  "WHERE playlist_name = '" + playlist.name + "'")
            for row in result:
                playlist.songs.append(row[0])

        return playlists


     def get_playlist(self, name):
        playlist = Playlist()
        result = conn.execute("SELECT * FROM playlist " +
                              "WHERE name = '" + name + "'");
        for row in result:
            playlist.name = row[0]
            playlist.description = row[1]

        result = conn.execute("SELECT song_name "
                              "FROM playlist_song " +
                              "WHERE playlist_name = '" + playlist.name + "'")
        for row in result:
            playlist.songs.append(song_model.get_song(row[0]))

        return playlist;


     def add_playlist(self, name, description):
         conn.execute("INSERT INTO playlist VALUES('" + name + "','" + description + "')")
         conn.commit()


     def remove_playlist(self, name):
         conn.execute("DELETE FROM playlist_song " +
                     "WHERE playlist_name = '" + name + "'")

         conn.execute("DELETE FROM playlist " +
                      "WHERE name = '" + name + "'")
         conn.commit()

     def remove_playlist_song(self, playlist_name, song_name):
         conn.execute("DELETE FROM playlist_song " +
                      "WHERE playlist_name = '" + playlist_name + "' " +
                      "AND song_name = '" + song_name + "'")
         conn.commit()

pm = PlaylistModel()