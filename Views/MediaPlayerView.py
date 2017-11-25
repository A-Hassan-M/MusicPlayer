class MediaPlayerView():
    choice_listener = None

    def __init__(self):
        self.choice_listener = PlayerOptionsListener()

    def show_player(self,song):
        print("Song name:",song)
        print("1- Stop\t2- next")
        choice = input()
        self.choice_listener.on_option_selected(choice)

class PlayerOptionsListener():
    def on_option_selected(self,choice):
        pass