
from playsound import playsound
import time
from tkinter import tk

CLEAR ="\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left// 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
        
    playsound("alarm_clock.mp3")

print("Welcome to a simple intepretation of an alarm clock")       
minutes_entered = input("Please enter the number of minutes you want to set: ")
seconds_entered = input("Please enter the number of seconds you want to set: ")

total_seconds = minutes_entered * 60 + seconds_entered

alarm(total_seconds)

##################################################################################
#GUI IMPLEMENTATION:

