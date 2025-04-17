from screen_settings import Screen_Settings
import adafruit_character_lcd.character_lcd as character_lcd

class Screen_Display:
    
    def __init__(self):
        _screen_settings = Screen_Settings()
        self._lcd: character_lcd.Character_LCD = _screen_settings.get_screen()

        self._row_1: str = ""
        self._row_2: str = ""

    def set_row_1(self, message: str) -> None:
        self._row_1 = message
    
    def set_row_2(self, message: str) -> None:
        self._row_2 = message

    def display(self) -> None:
        self._lcd.message = self._row_1
        self._lcd.cursor_position(0,1)
        self._lcd.message = self._row_2

    def scroll_up(self, message: str) -> None:
        self._row_2 = self._row_1
        self._row_1 = message
        self.display()
    
    def scroll_down(self, message: str) -> None:
        self._row_1 = self._row_2
        self._row_2 = message
        self.display()