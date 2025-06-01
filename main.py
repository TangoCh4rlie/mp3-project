from button_manager import Button_Manager
from screen_display import Screen_Display
from track_manager import Track_Manager, File_System_Item
from track_player import VLC
import time

ROOT = "audio"

PLAYER_MODE = False

track_manager = Track_Manager(ROOT)
screen_display = Screen_Display(track_manager)
track_player = VLC()

button_pins = [5, 6, 11, 20, 21]
button_listener = Button_Manager(button_pins, screen_display, track_player)

init_content: list[File_System_Item] = track_manager.get_init()
screen_display.set_row_1(track_manager.get_init()[0].name)
screen_display.set_row_2(track_manager.get_init()[1].name)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    button_listener.cleanup()


# track_manager.get_sound_dir()

# track_player.addPlaylist()
# track_player.play()
# time.sleep(5)
# track_player.next()
# time.sleep(5)

# track_manager._vlc.addPlaylist(track_manager.get_sound_dir())
# track_manager._vlc.play()
# time.sleep(20)

# screen_display.scroll_down()
# screen_display.select()

# screen_display.scroll_down()
# screen_display.scroll_down()
# screen_display.scroll_down()
# screen_display.select()
# time.sleep(1)
# screen_display.go_back()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_down()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# time.sleep(0.5)
# screen_display.scroll_up()
# screen_display.go_back()

