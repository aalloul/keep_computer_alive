from pynput.keyboard import Controller, Key
from time import sleep, time

keyboard = Controller()
duration = 3*3600
start_date = time()

while start_date + duration > time():
    keyboard.press(Key.f15)
    keyboard.release(Key.f15)
    sleep(20)
