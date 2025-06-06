from src.track_info import Track_Info
from vlc import Instance

class VLC:
    def __init__(self):
        self.Player = Instance('--loop')
        self._is_play = False
        self._is_player_active = False

    def addPlaylist(self, playlist: list[str]):
        self.mediaList = self.Player.media_list_new()
        for s in playlist:
            self.mediaList.add_media(self.Player.media_new(s))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)

    def play(self):
        self._is_player_active = True
        self._is_play = True
        self.listPlayer.play()     

    def next(self):
        self.listPlayer.next()

    def pause(self):
        self._is_player_active = True
        self._is_play = False
        self.listPlayer.pause()

    def previous(self):
        self.listPlayer.previous()

    def stop(self):
        self._is_play = False
        self.listPlayer.stop()
        self._is_player_active = False

    def increase_volume(self, increment=5):
        player = self.listPlayer.get_media_player()
        current_volume = player.audio_get_volume()
        new_volume = min(100, current_volume + increment)
        player.audio_set_volume(new_volume)
        print(f"Volume augmenté à {new_volume}%")

    def decrease_volume(self, decrement=5):
        player = self.listPlayer.get_media_player()
        current_volume = player.audio_get_volume()
        new_volume = max(0, current_volume - decrement)
        player.audio_set_volume(new_volume)
        print(f"Volume baissé à {new_volume}%")

    def get_track_info(self):
        player = self.listPlayer.get_media_player()
        media = player.get_media()
        title = media.get_meta(0) if media else "Unknown"
        
        return Track_Info(
            total_time = player.get_length() // 1000,
            current_time = player.get_time() // 1000,
            title = title,
            is_playing = player.is_playing()
        )