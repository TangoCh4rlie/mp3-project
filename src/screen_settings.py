import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

class Screen_Settings:
    def __init__(self):
        self._LCD_COLUMNS = 16
        self._LCD_ROWS = 2
        self._LCD_RS = digitalio.DigitalInOut(board.D25)
        self._LCD_EN = digitalio.DigitalInOut(board.D24)
        self._LCD_D7 = digitalio.DigitalInOut(board.D22)
        self._LCD_D6 = digitalio.DigitalInOut(board.D18)
        self._LCD_D5 = digitalio.DigitalInOut(board.D17)
        self._LCD_D4 = digitalio.DigitalInOut(board.D23)

    def get_screen(self) -> character_lcd.Character_LCD:
        return character_lcd.Character_LCD(
            self._LCD_RS,
            self._LCD_EN,
            self._LCD_D4,
            self._LCD_D5,
            self._LCD_D6,
            self._LCD_D7,
            self._LCD_COLUMNS,
            self._LCD_ROWS
        )