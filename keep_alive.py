# from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController
from time import sleep, time
from plyer import notification

# keyboard = Controller()
mouse = MouseController()
duration = 8.5*3600
start_date = time()

while start_date + duration > time():
    mouse.move(1, 0)
    # keyboard.press(Key.f15)
    # keyboard.release(Key.f15)
    sleep(20)

notification.notify(
    title='Time',
    message='Keep alive process finished',
    app_icon=None,
    timeout=10,
)
