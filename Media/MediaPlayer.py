import threading
import time
import pygame

class MediaPlayer():
    m_pygame = pygame
    songs = []
    def play_song(self,song):
        self.m_pygame.init()
        self.m_pygame.mixer.music.load(song)
        self.m_pygame.mixer.music.play()
    def play_songs(self,songs):
        self.songs = songs
        for song in songs:
            self.play_song(song)
            showOption()
            time.sleep(2)
    def stop(self):
        self.m_pygame.mixer.music.stop()

media_player = MediaPlayer()
thread = threading.Thread(target=media_player.play_songs,args=(["Imagine Dragons - Warriors (Lyrics).mp3","Imagine Dragons - Warriors (Lyrics).mp3"],))

thread.start()

def showOption():
    choice = input("Enter stop to stop")
    print(choice)
    if(choice == 'stop'):
        media_player.stop()


