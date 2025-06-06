from button_manager import Button_Manager
from track_info_observer import Track_Info_Observer
from screen_display import Screen_Display
import time


track_info = Track_Info_Observer()
screen_display = Screen_Display()
track_info.add_observer(screen_display)
button_listener = Button_Manager(screen_display, track_info)

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

