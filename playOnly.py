import os
import random
import time
import pygame
musicPath = "playlist"


def init():
    pygame.mixer.init()


def getRandomSong():
    songlist = os.listdir(musicPath)
    random_index = random.randrange(len(songlist))
    return musicPath + "/" + songlist[random_index]


def playSong():
    pygame.mixer.music.load(getRandomSong())
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


init()

while True:
    time.sleep(1)
    print("Checking Input")
    playSong()
