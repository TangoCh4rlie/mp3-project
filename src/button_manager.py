import RPi.GPIO as GPIO
import threading

from src.screen_display import Screen_Display
from src.track_info_observer import Track_Info_Observer
from src.track_player import VLC

class Button_Manager:
    def __init__(self, screen_display: Screen_Display, track_info_observer: Track_Info_Observer):
        self.button_pins = [5, 6, 11, 20, 21]
        self.screen_display = screen_display
        self.vlc = VLC()
        self.track_info_observer = track_info_observer
        GPIO.setmode(GPIO.BCM)

        for pin in self.button_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for pin in self.button_pins:
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.button_pressed, bouncetime=300)

        self.button_press_times = {}
        self.button_press_threads = {}

    def button_pressed(self, channel):
        print(f"Bouton pressé sur la broche GPIO {channel}")

        # Démarrer un thread pour surveiller la durée de la pression du bouton
        if channel not in self.button_press_threads or not self.button_press_threads[channel].is_alive():
            self.button_press_times[channel] = threading.Timer(1.0, self.long_press_action, args=[channel])
            self.button_press_times[channel].start()

            # Démarrer un thread pour détecter la relâche du bouton
            self.button_press_threads[channel] = threading.Thread(target=self.wait_for_button_release, args=[channel])
            self.button_press_threads[channel].start()

    def wait_for_button_release(self, channel):
        while GPIO.input(channel) == GPIO.LOW:
            pass
        if channel in self.button_press_times and self.button_press_times[channel].is_alive():
            self.button_press_times[channel].cancel()
            self.short_press_action(channel)

    def long_press_action(self, channel):
            if channel == self.button_pins[0]:
                if self.vlc._is_player_active == True:
                    self.vlc.stop()
                    self.vlc._is_player_active = False

                    self.screen_display.set_row_1(self.screen_display._row_1_tmp)
                    self.screen_display.set_row_2(self.screen_display._row_2_tmp)
                    self.screen_display.display()
                    print("musique arreté")

    def short_press_action(self, channel):
        if channel == self.button_pins[0]:
            self.select_action()
        elif channel == self.button_pins[1]:
            self.up_action()
        elif channel == self.button_pins[2]:
            self.down_action()
        elif channel == self.button_pins[3]:
            self.left_action()
        elif channel == self.button_pins[4]:
            self.right_action()

    def select_action(self):
        if self.vlc._is_player_active == True:
            if self.vlc._is_play == True:
                self.vlc.pause()
                print("pause")
            else:
                self.vlc.play()
                print("play")

    def up_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.increase_volume()
        else:
            self.screen_display.scroll_up()
            print("up")

    def down_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.decrease_volume()
        else:
            self.screen_display.scroll_down()
            print("down")

    def left_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.previous()
            print("musique précédente")
        else:
            self.screen_display.go_back()
            print("retour")

    def right_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.next()
            print("musique suivante")
        else:
            if self.screen_display.select() == True:
                print("joue musique")
                self.vlc.addPlaylist(self.screen_display._track_manager.get_sound_dir())
                self.vlc.play()
                self.start_track_info_updates()

    def start_track_info_updates(self):
        self.update_thread = threading.Thread(target=self.update_track_info)
        self.update_thread.daemon = True
        self.update_thread.start()
    
    def update_track_info(self):
        while self.vlc._is_player_active:
            self.track_info_observer.set_track_info(self.vlc.get_track_info())
            threading.Event().wait(1.0)

    def cleanup(self):
        GPIO.cleanup()
