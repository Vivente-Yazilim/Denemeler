from driver import LED_Driver
from driver import eski_kart
import time
import keyboard
import picamera
import smbus
import subprocess
from picamera import mmal
from set_gain import set_gain

kart=LED_Driver('AG_PCB_v3')
kart.set_white_brightness(0)
kart.set_ir_brightness(75)
kart.turn_off_ir()