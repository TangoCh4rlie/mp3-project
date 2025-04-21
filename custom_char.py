from typing import Sequence
from screen_display import Screen_Display

chevron: Sequence[int] = 0x10,0x8,0x4,0x2,0x4,0x8,0x10

class Custom_Char:
    def __init__(self, screen_display: Screen_Display):
        self._screen_display = screen_display
        self.custom_chevron = self._screen_display._lcd.create_char(0, chevron)