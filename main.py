import time
from screen_display import Screen_Display
from track_manager import Track_Manager, FileSystemItem

ROOT = "./audio"

track_manager = Track_Manager(ROOT)
screen_display = Screen_Display(track_manager)

init_content: list[FileSystemItem] = track_manager.get_init()
screen_display.set_row_1(">" + init_content[len(track_manager._dir_content) - 2].name)
screen_display.set_row_2(init_content[len(track_manager._dir_content) - 1].name)
# print("track", track_manager.get_current_item().name)
# screen_display.scroll_down()
# print("track", track_manager.get_current_item().name)





