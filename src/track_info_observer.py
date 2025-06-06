from src.screen_display import Screen_Display
from src.track_info import Track_Info

class Track_Info_Observer:
    def __init__(self):
        self._screen_display: Screen_Display = None
        self._track_info: Track_Info = Track_Info()
    
    def add_observer(self, screen_display: Screen_Display):
        self._screen_display = screen_display

    def _notify_observer(self):
        self._screen_display.player_display(self._track_info)

    def set_track_info(self, new_value: Track_Info):
        self._track_info = new_value
        self._notify_observer()