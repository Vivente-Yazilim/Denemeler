from gpiozero import Button
import time

button= Button(27, pull_up=False)
while True:
    if button.is_active:
        print("HIGH")
        time.sleep(1)