from pynput.keyboard import Controller, Key
from time import sleep, time
from plyer import notification

keyboard = Controller()
duration = 8.5 * 3600
start_date = time()


def notify_user(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=2,
    )


def wait(sd, dur):
    while sd + dur > time():
        keyboard.press(Key.f15)
        keyboard.release(Key.f15)
        sleep(20)


if __name__ == '__main__':
    notify_user("Time", 'Keep alive process started')
    wait(start_date, duration)
    notify_user("Time", 'Keep alive process finished')
