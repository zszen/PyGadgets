import time
from io import BytesIO

import pygame


class AudioObj(object):
    def __init__(self):
        """播放音频"""
        self.pygame_mixer = pygame.mixer
        self.pygame_mixer.init()
        self.audio_bytes = None

    def play(self, audio_bytes=None):
        """
        传入音频文件字节码，播放音频
        :param audio_bytes:
        :return:
        """
        audio_bytes = self.audio_bytes or audio_bytes
        if audio_bytes is None:
            return
        byte_obj = BytesIO()
        byte_obj.write(audio_bytes)
        byte_obj.seek(0, 0)
        self.pygame_mixer.music.load(byte_obj)
        self.pygame_mixer.music.play()
        while self.pygame_mixer.music.get_busy() == 1:
            time.sleep(0.1)
        self.pygame_mixer.music.stop()



if __name__ == '__main__':
    def read_bytes(fn):
        with open(fn, 'rb') as fp:
            data = fp.read()
        return data
    audio_bytes = read_bytes(r"hello.mp3")
    AudioObj().play()

