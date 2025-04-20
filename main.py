import time
from screen_display import Screen_Display
from track_manager import Track_Manager

ROOT = "./audio"

screen_display = Screen_Display()
track_manager = Track_Manager(ROOT)

print(track_manager.get_selected_item().name)
screen_display.set_row_1(track_manager.get_selected_item().name)

screen_display.display()

# screen_display.set_row_1(mp3list[0])
# screen_display.set_row_2(mp3list[1])

# screen_display.display()

# time.sleep(2)

# screen_display.scroll_down(mp3list[2])






