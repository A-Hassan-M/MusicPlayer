import sqlite3

connection = sqlite3.connect("/home/ahmed/PycharmProjects/Musicly/Model/musicly.db")

connection.execute("CREATE TABLE IF NOT EXISTS album (" +
                   "name TEXT PRIMARY KEY);")

connection.execute("CREATE TABLE IF NOT EXISTS artist (" +
                   "name TEXT, " +
                   "date_of_birth DATE)")

connection.execute("CREATE TABLE IF NOT EXISTS band (" +
                   "name TEXT PRIMARY KEY);")

connection.execute("CREATE TABLE IF NOT EXISTS playlist ("
                   "name TEXT PRIMARY KEY, " +
                   "description TEXT);")

connection.execute("CREATE TABLE IF NOT EXISTS playlist_song (" +
                   "playlist_name TEXT REFERENCES playlist (name), " +
                   "song_name TEXT REFERENCES song (name));")

connection.execute("CREATE TABLE IF NOT EXISTS song (" +
                   "name TEXT PRIMARY KEY, " +
                   "release_date DATE, " +
                   "lyrics TEXT, " +
                   "length TEXT, " +
                   "path TEXT, " +
                   "album_name TEXT DEFAULT None);")

connection.execute("CREATE TABLE IF NOT EXISTS song_band (" +
                   "song_name TEXT REFERENCES song (name), " +
                   "band_name TEXT REFERENCES band (name), " +
                   "featured BOOLEAN);")


connection.commit()
