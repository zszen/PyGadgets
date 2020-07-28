import pygame
import time

class audioplay:
    def __init__(self):
        pygame.mixer.init()
    
    def play(self, path):
        track = pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        time.sleep(1)
        pygame.mixer.music.stop()