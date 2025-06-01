import RPi.GPIO as GPIO
import threading

from screen_display import Screen_Display
from track_player import VLC

class Button_Manager:
    def __init__(self, button_pins: list[int], screen_display: Screen_Display, vlc: VLC):
        self.button_pins = button_pins
        self.screen_display = screen_display
        self.vlc = vlc
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
            self.vlc.stop()
            self.vlc._is_player_active == False
            self.screen_display.display()
            print("Long press detected on select button")

    def short_press_action(self, channel):
        if channel == self.button_pins[0]:
            self.select_action()
            print("select")
        elif channel == self.button_pins[1]:
            self.up_action()
            print("up_action")
        elif channel == self.button_pins[2]:
            self.down_action()
            print("down_action")
        elif channel == self.button_pins[3]:
            self.left_action()
            print("left_action")
        elif channel == self.button_pins[4]:
            self.right_action()
            print("right_action")

    def select_action(self):
        if self.vlc._is_player_active == True:
            if self.vlc._is_play == True:
                self.vlc.pause()
            else:
                self.vlc.play()

    def up_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.increase_volume()
        else:
            self.screen_display.scroll_up()

    def down_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.decrease_volume()
        else:
            self.screen_display.scroll_down()

    def left_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.previous()
        else:
            self.screen_display.go_back()

    def right_action(self):
        if self.vlc._is_player_active == True:
            self.vlc.next()
        else:
            if self.screen_display.select() == True:
                self.vlc.addPlaylist(self.screen_display._track_manager.get_sound_dir())
                self.vlc.play()

    def cleanup(self):
        GPIO.cleanup()
