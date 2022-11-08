from datetime import datetime
import webbrowser

ALARM_SOUND_LINK = "https://www.youtube.com/watch?v=5LCvj6Z_LrA"

input_time = input("What time do you want to set the alarm to (24 hour - HH:MM): ")

time = datetime.now().strftime("%H:%M")

while time != input_time:
    time = datetime.now().strftime("%H:%M") 

webbrowser.open(ALARM_SOUND_LINK)
