
class Menu():
    choice_listener = None

    def __init__(self):
        self.choice_listener = MainMenu_listener()

    def show_options(self):
        print('/////////////////////////////')
        print("Welcome To Musicly\n")

        print("1. Playlist\n2. Artists\n3. Albums\n4. Exit")
        choice = input("choose your option: ")

        print('/////////////////////////////')
        self.choice_listener.on_input(choice)

class MainMenu_listener():
    def on_input(self,choice):
        pass