from screen_settings import Screen_Settings
from track_info import Track_Info
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

    def set_row_1(self, message: str, cursor: bool = True) -> None:
        self._row_1 = message
        self.display(cursor)
    
    def set_row_2(self, message: str, cursor: bool = True) -> None:
        self._row_2 = message
        self.display(cursor)

    def display(self, cursor: bool) -> None:
        self._lcd.clear()
        if cursor:
            self._lcd.message = ">" + self._row_1
        else:
            self._lcd.message = self._row_1
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
            self._row_1_tmp = self._row_1
            self._row_2_tmp = self._row_2
            self.player_display(Track_Info())
            return True
    
    def go_back(self):
        if str(self._track_manager._path) != self._track_manager._root:
            path = Path(self._track_manager._path)
            self._track_manager.select_dir(path.parent)
            self.set_row_1(self._track_manager.get_init()[0].name)
            self.set_row_2(self._track_manager.get_init()[1].name)

    def player_display(self, track_info: Track_Info):
        current_minutes = track_info.currrent_time // 60
        current_seconds = track_info.currrent_time % 60
        total_minutes = track_info.total_time // 60
        total_seconds = track_info.total_time % 60

        # PLAY
        custom_char = [8, 12, 14, 15, 15, 14, 12, 8]
        self._lcd.create_char(0, custom_char)

        # PAUSE
        custom_char = [0, 27, 27, 27, 27, 27, 27, 0]
        self._lcd.create_char(1, custom_char)

        status = "\x00" if track_info.is_playing else "\x01"

        if isinstance(track_info.title, str):
            title = track_info.title
            self.set_row_1(f"{status} {title}", False)
        else:
            self.set_row_1(f"{status} unknown", False)

        time_display = f"{current_minutes:02}:{current_seconds:02} / {total_minutes:02}:{total_seconds:02}"
        self.set_row_2(time_display, False)