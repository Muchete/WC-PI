import os
import random
import time
import pygame
import RPi.GPIO as GPIO
SENSOR_PIN = 7
musicPath = "playlist"


def init():
    pygame.mixer.init()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)


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
    print("Checking Input")
    if GPIO.input(SENSOR_PIN):
        print("Motion Detected!")
        playSong()
    time.sleep(1)
