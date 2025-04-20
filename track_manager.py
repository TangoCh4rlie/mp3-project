import os

class FileSystemItem:
    def __init__(self, name: str, path: str, isDirectory: bool):
        self.name = name
        self.path = path
        self.isDirectory = isDirectory

class Track_Manager:
    def __init__(self, root: str) -> None:
        self._root: str = root
        self._dir_content: list[FileSystemItem] = self.load_dir_content(self._root)
        self._selected_item: FileSystemItem = self._dir_content[0]
    
    def load_dir_content(self, path:str) -> list[FileSystemItem]:
        dir_content: list[FileSystemItem] = []

        with os.scandir(path) as itr: 
            for entry in itr : 
                if not entry.name.startswith('.'):
                    dir_content.append(FileSystemItem(entry.name, entry.path, entry.is_dir))
        
        return dir_content
    
    def get_selected_item(self) -> FileSystemItem:
        return self._selected_item