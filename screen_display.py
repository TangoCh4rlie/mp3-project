from screen_settings import Screen_Settings
from track_manager import Track_Manager, File_System_Item
from pathlib import Path
import adafruit_character_lcd.character_lcd as character_lcd

ROOT = "audio"

class Screen_Display:
    
    def __init__(self) -> None:
        _screen_settings = Screen_Settings()
        self._track_manager = Track_Manager(ROOT)
        self._lcd: character_lcd.Character_LCD = _screen_settings.get_screen()

        self._row_1: str = ""
        self._row_2: str = ""

        self._row_1_tmp: str = ""
        self._row_2_tmp: str = ""

        self.set_row_1(self._track_manager.get_init()[0].name)
        self.set_row_2(self._track_manager.get_init()[1].name)

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

    def scroll_up(self) -> None:
        item: File_System_Item = self._track_manager.get_previous_item()

        if item:
            self._row_2 = self._row_1
            self._row_1 = item.name

        self.display()
    
    def scroll_down(self) -> None:
        item: File_System_Item = self._track_manager.get_next_item()

        if self._track_manager.get_current_item().name == self._row_2:
            if item:
                self._row_1 = self._row_2
                self._row_2 = item.name
            elif item == None and len(self._row_2) > 0:
                self._row_1 = self._row_2
                self._row_2 = ""

        self.display()
    
    def select(self) -> bool:
        selected_item: File_System_Item = self._track_manager.get_current_item()
        if selected_item.isDirectory:
            self._track_manager.select_dir(selected_item.path)
            self.set_row_1(self._track_manager.get_init()[0].name)
            self.set_row_2(self._track_manager.get_init()[1].name)
            return False
        else:
            self.player_display()
            return True
    
    def go_back(self):
        if str(self._track_manager._path) != self._track_manager._root:
            path = Path(self._track_manager._path)
            self._track_manager.select_dir(path.parent)
            self.set_row_1(self._track_manager.get_init()[0].name)
            self.set_row_2(self._track_manager.get_init()[1].name)

    def player_display(self):
        self._row_1_tmp = self._row_1
        self._row_2_tmp = self._row_2
        self.set_row_1(self._track_manager.get_current_item().name)
        # TODO : implémenter une barre de temps 
        self._lcd.message = self._row_1