import sqlite3

conn = sqlite3.connect("musicly.db")


conn.execute('''CREATE TABLE IF NOT EXISTS Band
            (
            band_name TEXT NOT NULL PRIMARY KEY
            );''')

conn.execute('''CREATE TABLE IF NOT EXISTS Artist
            (
            ID INT AUTO_INCREMENT PRIMARY KEY, 
            band_name TEXT NOT NULL,
            name VARCHAR(100) NOT NULL,
            date_of_birth date NOT NULL,
            
            FOREIGN KEY (band_name) references Band(band_name)
            );''')

conn.execute('''CREATE TABLE IF NOT EXISTS Playlist
            (
            ID INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(100) NOT NULL,
            describtion TEXT NOT NULL
            );''')

conn.execute('''CREATE TABLE IF NOT EXISTS Album 
            (
            ID INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR(100) NOT NULL,
            num_of_songs INT NOT NULL
            );''')


conn.execute('''CREATE TABLE IF NOT EXISTS Song 
            (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            albumID INT,
            name VARCHAR(100) NOT NULL,
            release_date DATE NOT NULL,
            lyrics TEXT NOT NULL,
            genres VARCHAR(100) NOT NULL,
            length TEXT NOT NULL,
            
            FOREIGN KEY (albumID) references Album(ID)
            );''')

conn.execute('''CREATE TABLE IF NOT EXISTS Playlist_songs 
            (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            songID INT,
            playlistID INT,

            FOREIGN KEY (songID) references Song(ID),
            FOREIGN KEY (playlistID) references Playlist(ID)
            );''')

conn.execute('''CREATE TABLE IF NOT EXISTS Band_songs 
            (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            band_name TEXT,
            songID INT,

            FOREIGN KEY (band_name) references Band(band_name),
            FOREIGN KEY (songID) references Song(ID)

            );''')

conn.commit()


