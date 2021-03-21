import os
from time import sleep


 
VIDEO_FILE = "./tests/target.mp4"

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

os.system("ffplay -autoexit " + VIDEO_FILE)
print('debug')