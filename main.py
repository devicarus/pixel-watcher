from time import sleep
import pyscreenshot as ImageGrab
import os
from dotenv import load_dotenv

from lib.audio import WavePlayerLoop

from lib.xdotool import getmouselocation
from lib.grabc import rgb
from lib.utility import inputBool

load_dotenv()
alert = os.getenv("ALERT")

playing = False

nodes = []
add = True
while add:
    print("Select a spot to watch")
    nodes.append({
        "color": rgb(),
        "coordinates": getmouselocation()
    })
    add = inputBool("Add another one?")
    
os.system("clear")

print("Watching")

while True:
    screenshot = ImageGrab.grab()
    
    match = False

    for node in nodes:
        pixel = screenshot.getpixel((node["coordinates"]["x"], node["coordinates"]["y"]))
        if pixel != node["color"]:
            match = True
            
    if match and not playing:
        player = WavePlayerLoop(alert)
        player.play()
        playing = True
        
        sleep(0.1)
        os.system("clear")
        print("Changes detected, alerting")
    elif not match and playing:
        player.stop()
        playing = False
        
        os.system("clear")
        print("Changes reverted, stopping alert")
    
    sleep(2)
