import mp3play
import time

def play(path):
    clip = mp3play.load(path)
    clip.play()
    time.sleep(2)
    clip.stop()
    