import os

class FileSystemItem:
    def __init__(self, name: str, path: str, isDirectory: bool):
        self.name = name
        self.path = path
        self.isDirectory = isDirectory

class Track_Manager:
    def __init__(self, root: str) -> None:
        self._root: str = root
        self._dir_content: list[FileSystemItem] = self._load_dir_content(self._root)
        self._current_item: FileSystemItem = self._dir_content[len(self._dir_content) - 2]
    
    def _load_dir_content(self, path: str) -> list[FileSystemItem]:
        dir_content: list[FileSystemItem] = []

        with os.scandir(path) as itr: 
            for entry in itr : 
                if not entry.name.startswith('.'):
                    dir_content.append(FileSystemItem(entry.name, entry.path, entry.is_dir))

        dir_content.sort(key=lambda x: x.name)
        for i in dir_content:
            print(i.name)
        
        return dir_content
    
    def select_dir(self, path: str) -> None:
        dir_content: list[FileSystemItem] = self._load_dir_content(path)
        self._dir_content = dir_content
        self.set_current_item(self._dir_content[0])
    
    def get_init(self) -> list[FileSystemItem]:
        return [self._dir_content[0], self._dir_content[1]]
    
    def get_current_item(self) -> FileSystemItem:
        return self._current_item
    
    def set_current_item(self, new_item: FileSystemItem) -> None:
        self._current_item = new_item
    

    # TODO: modifier ca
    def get_previous_item(self) -> FileSystemItem | None:
        index = self._dir_content.index(self._current_item)
        if index > 2:
            
            return self._dir_content[index - 2]
        else:
            return None
    
    def get_next_item(self) -> FileSystemItem | None:
        index = self._dir_content.index(self._current_item)

        if index < len(self._dir_content) - 2:
            item: FileSystemItem = self._dir_content[index + 2]
            self.set_current_item(self._dir_content[index + 1])
            return self._dir_content[index + 2]
        if index < len(self._dir_content) - 1:
            item: FileSystemItem = self._dir_content[index + 1]
            self.set_current_item(item)

        return None
    
