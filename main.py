import os
import time

from screen_display import Screen_Display

screen_display = Screen_Display()

mp3list: list[str] = os.listdir("./audio")

screen_display.set_row_1(mp3list[0])
screen_display.set_row_2(mp3list[1])

screen_display.display()

time.sleep(2)

screen_display.scroll_down(mp3list[2])






