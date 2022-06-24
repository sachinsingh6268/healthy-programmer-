from pygame import mixer
from datetime import datetime
import time

def music_player(file): # while using loop a second parameter stopper will be given
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    # while True:
    #     a = input("Enter stop to pause the music\n")
    #     if stopper == a:
    #         mixer.music.stop()
    #         break

    # OR CAN BE DONE THE FOLLOWING WAY TOO AS GIVEN BELOW WITHOUT USING LOOP AS IT WILL WAIT TILL THE INPUT IS NOT GIVEN
    input("Enter any key to pause the music\n")
    mixer.music.stop()


def eye_record(msg):
    with open('eyes.txt',"a") as f:
        f.write(f"{msg} {datetime.now()}\n")

def water_record(msg):
    with open('water.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")

def exercise_record(msg):
    with open('physical_exercise.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    eye_time = time.time()
    water_time = time.time()
    exer_time = time.time()
    while True:
        if time.time()-eye_time > 1800:
            music_player('eyes.mp3')
            eye_record('did eye exercise at')
            eye_time = time.time()
        if time.time()-water_time > 2400:
            music_player('water.mp3')
            water_record('drank water at')
            water_time = time.time()
        if time.time()-exer_time > 2700:
            music_player('physical.mp3')
            exercise_record('did the physical exercise at')
            exer_time = time.time()
