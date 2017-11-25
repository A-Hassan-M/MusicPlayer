import threading
import time
import pygame
from Views.MediaPlayerView import MediaPlayerView,PlayerOptionsListener

class MediaPlayer(PlayerOptionsListener):
    songs = []
    player_view = None
    stop = False
    def __init__(self):
        self.player_view = MediaPlayerView()
        self.player_view.choice_listener = self

    def play_song(self,song):
        pygame.init()
        pygame.mixer.music.load(song.path)
        pygame.mixer.music.play()
        self.player_view.show_player(song.name)

    def play_songs(self,songs):
        self.songs = songs
        for song in songs:
            if(self.stop):
                break
            self.play_song(song)
            time.sleep(1)
        print("show")

    def on_option_selected(self,choice):
        if(choice == '1'):
            pygame.quit()
            self.stop = True
        elif(choice == '2'):
            pygame.mixer.music.stop()

media_player = MediaPlayer()


