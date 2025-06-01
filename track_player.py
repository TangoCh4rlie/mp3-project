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
        """
        Augmente le volume du lecteur VLC.

        :param increment: Incrément de volume (par défaut 10).
        """
        player = self.listPlayer.get_media_player()
        current_volume = player.audio_get_volume()
        new_volume = min(100, current_volume + increment)
        player.audio_set_volume(new_volume)
        print(f"Volume augmenté à {new_volume}%")

    def decrease_volume(self, decrement=5):
        """
        Baisse le volume du lecteur VLC.

        :param decrement: Décrément de volume (par défaut 10).
        """
        player = self.listPlayer.get_media_player()
        current_volume = player.audio_get_volume()
        new_volume = max(0, current_volume - decrement)
        player.audio_set_volume(new_volume)
        print(f"Volume baissé à {new_volume}%")