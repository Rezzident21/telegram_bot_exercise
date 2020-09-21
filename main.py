#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import time
import datetime
from config import bot
from config import id_channel
import exersise_choises
import os
from os.path import isfile
from os.path import join as joinpath

############Arguments#####################
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--eyes')
parser.add_argument('-b', '--back')
parser.add_argument('-exercise', '--exercise')

args = vars(parser.parse_args())
back_p = args['back']
eyes_p = args['eyes']
exercise_p = args['exercise']

now_hour = datetime.datetime.now().hour
if now_hour >= 23 or now_hour <= 8:
    exit()


class Exercise:  # Клас Exercise
    def __init__(self, time_sleep_min, time_sleep_max, choice, id_channel=id_channel, bot=bot):
        self.id_channel = id_channel  # ID channel
        self.bot = bot
        self.choise = choice
        self.time_sleep_min = time_sleep_min
        self.time_sleep_max = time_sleep_max

    def send_message(self):  # Send message in the channel
        time.sleep(random.uniform(self.time_sleep_min, self.time_sleep_max))
        self.bot.send_message(self.id_channel, random.choice(self.choise))

    def send_photo_in_channel(self): # Send photo
        mypath = "images"
        files = os.listdir(mypath)
        photo = open('images/' + random.choice(files), 'rb')
        self.bot.send_photo(self.id_channel, photo,'Test')



if __name__ == '__main__':

    if back_p:
        exercise_back = Exercise(300, 600, exersise_choises.back_choise)
        exercise_back.send_message()
    elif eyes_p:
        exercise_eyes = Exercise(0, 300, exersise_choises.eyes_choise)
        #exercise_eyes.send_photo_in_channel()
        exercise_eyes.send_message()
    elif exercise_p:
        exercise = Exercise(400, 700, exersise_choises.exercise_choise)
        exercise.send_message()
