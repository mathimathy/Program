from pynput import keyboard
class Keyboard:
    def __init__(self):
        self.pressedKey=None
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release, suppress=True)
        listener.start()
    def on_press(self,key):
        self.pressedKey=key

    def on_release(self,key):
        if key==self.pressedKey:
            self.pressedKey=None