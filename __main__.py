from src.button_manager import Button_Manager
from src.track_info_observer import Track_Info_Observer
from src.screen_display import Screen_Display
import time

def main():
    track_info = Track_Info_Observer()
    screen_display = Screen_Display()
    track_info.add_observer(screen_display)
    button_listener = Button_Manager(screen_display, track_info)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        button_listener.cleanup()

if __name__=="__main__":
    main()