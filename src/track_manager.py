import os
from pathlib import PosixPath

class File_System_Item:
    def __init__(self, name: str, path: str, isDirectory: bool):
        self.name = name
        self.path = path
        self.isDirectory = isDirectory

class Track_Manager:
    def __init__(self, root: str) -> None:
        self._root: str = root
        self._path: PosixPath = self._root
        self._dir_content: list[File_System_Item] = self._load_dir_content(self._path)
        self._current_item: File_System_Item = self._dir_content[0]
    
    def _load_dir_content(self, path: str) -> list[File_System_Item]:
        dir_content: list[File_System_Item] = []

        with os.scandir(path) as itr: 
            for entry in itr : 
                if not entry.name.startswith('.'):
                    dir_content.append(File_System_Item(entry.name, entry.path, entry.is_dir()))

        dir_content.sort(key=lambda x: x.name)
        
        return dir_content
    
    def select_dir(self, path: str) -> None:
        dir_content: list[File_System_Item] = self._load_dir_content(path)
        self._path = path
        self._dir_content = dir_content
        self.set_current_item(self._dir_content[0])
    
    def get_sound_dir(self) -> list[str]:
        dir_content: list[File_System_Item] = self._load_dir_content(self._path)
        return_list: list[str] = []

        files = [item for item in dir_content if not item.isDirectory]

        current_item = self.get_current_item()

        current_index = -1
        for index, item in enumerate(files):
            if item.path == current_item.path:
                current_index = index
                break

        if current_index != -1:
            reordered_files = files[current_index:] + files[:current_index]
            return_list = [item.path for item in reordered_files]
        else:
            return_list = [item.path for item in files]

        return return_list

    
    def get_init(self) -> list[File_System_Item]:
        return [self._dir_content[0], self._dir_content[1]]
    
    def get_current_item(self) -> File_System_Item:
        return self._current_item
    
    def set_current_item(self, new_item: File_System_Item) -> None:
        self._current_item = new_item
    
    def get_previous_item(self) -> File_System_Item | None:
        index = self._dir_content.index(self._current_item)
        print(index)

        if index >= 1:
            self.set_current_item(self._dir_content[index - 1])
            return self._dir_content[index - 1]
    
    def get_next_item(self) -> File_System_Item | None:
        index = self._dir_content.index(self._current_item)

        if index < len(self._dir_content) - 2:
            self.set_current_item(self._dir_content[index + 1])
            return self._dir_content[index + 2]
        if index < len(self._dir_content) - 1:
            self.set_current_item(self._dir_content[index + 1])
