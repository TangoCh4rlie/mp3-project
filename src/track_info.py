class Track_Info:
    def __init__(
            self,
            total_time: int = 0,
            current_time: int = 0,
            title: str = "unknown",
            is_playing: bool = False
            ):
        self.total_time: int = total_time
        self.currrent_time: int = current_time
        self.title: str = title
        self.is_playing: bool = is_playing