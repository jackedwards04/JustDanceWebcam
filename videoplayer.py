from threading import Thread
import os
from time import sleep
import videocapture as vc
import score as sc
import math


TARGET_FILE = "./tests/target.mp4"
TARGET_COORDS="./tests/target_reduced_coordinates.csv"
SOURCE_FILE = "./tests/source.mp4"
SOURCE_REDUCED="./tests/source_reduced.mp4"
SOURCE_COORDS="./tests/source_reduced_coordinates.csv"

print("Press enter to start!")
i = input()
print('3...\n')
sleep(1)
print('2...\n')
sleep(1)
print('1...\n')
sleep(1)
print('Go!')
sleep(0.5)

def playvideo():
  os.system("ffplay -fs -autoexit -loglevel quiet " + TARGET_FILE)

Thread(target=playvideo).start()

vc.record_wcam(15,SOURCE_FILE)
os.system("ffmpeg -i "+SOURCE_FILE+" -loglevel quiet -y -filter:v fps=4 "+SOURCE_REDUCED)
sleep(5)

os.system("python3 track.py --visualize --path="+SOURCE_REDUCED+" --store --model=IV")

diffs = sc.scorevid(SOURCE_COORDS,TARGET_COORDS)
print('Raw Score:',diffs)
print('Your Score:'+ str(max(0,round((5/2)*min(40,100-diffs))))+'%')
