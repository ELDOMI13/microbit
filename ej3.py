# Imports go at the top
from microbit import *
import music
music.play(music.JUMP_UP)
while True:
    if button_a.get_presses():
        display.show(Image.HEART)
        sleep(100)
    if button_b.get_presses():
        display.show(Image.ANGRY)
        sleep (300)
