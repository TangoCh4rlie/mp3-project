from screen_settings import Screen_Settings
from track_manager import Track_Manager, FileSystemItem
import os
from pathlib import Path
import adafruit_character_lcd.character_lcd as character_lcd

class Screen_Display:
    
    def __init__(self, track_manager: Track_Manager) -> None:
        _screen_settings = Screen_Settings()
        self._track_manager = track_manager
        self._lcd: character_lcd.Character_LCD = _screen_settings.get_screen()

        self._row_1: str = ""
        self._row_2: str = ""

    def set_row_1(self, message: str) -> None:
        self._row_1 = message
        self.display()
    
    def set_row_2(self, message: str) -> None:
        self._row_2 = message
        self.display()

    def display(self) -> None:
        self._lcd.clear()
        self._lcd.message = ">" + self._row_1
        self._lcd.cursor_position(0,1)
        self._lcd.message = self._row_2

        # print("-------------")
        # print(self._row_1)
        # print(self._row_2)
        # print("-------------")

    def scroll_up(self) -> None:
        item: FileSystemItem = self._track_manager.get_previous_item()

        if item:
            self._row_2 = self._row_1
            self._row_1 = item.name

        self.display()
    
    def scroll_down(self) -> None:
        item: FileSystemItem = self._track_manager.get_next_item()

        if self._track_manager.get_current_item().name == self._row_2:
            if item:
                self._row_1 = self._row_2
                self._row_2 = item.name
            elif item == None and len(self._row_2) > 0:
                self._row_1 = self._row_2
                self._row_2 = ""

        self.display()
    
    def select(self):
        selected_item: FileSystemItem = self._track_manager.get_current_item()
        if selected_item.isDirectory():
            self._track_manager.select_dir(selected_item.path)
            self.set_row_1(self._track_manager.get_init()[0].name)
            self.set_row_2(self._track_manager.get_init()[1].name)
        else:
            print("Implémenter pour lire la musique")
    
    def go_back(self):
        if self._track_manager._root != "./audio":
            path = Path(self._track_manager._root)
            self._track_manager.select_dir(path.parent)
            self.set_row_1(self._track_manager.get_init()[0].name)
            self.set_row_2(self._track_manager.get_init()[1].name)