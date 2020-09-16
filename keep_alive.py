from pynput.keyboard import Controller, Key
from time import sleep

keyboard = Controller()
while True:
    keyboard.press(Key.f15)
    keyboard.release(Key.f15)
    sleep(20)
