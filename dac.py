import smbus
import time
import picamera

camera=picamera.PiCamera()
device_addr=0x61
pot_addr=0x2F

mcp4725=smbus.SMBus(1)
mcp4017=smbus.SMBus(1)
fast_mode: int=0x00 #FAST MODE
fast_mode=fast_mode<<6
 
power_down: int=0x00 #NORMAL MODE
power_down=power_down<<4

digital_data:int=2048 

digital_data_4_bit: int=int(digital_data>>8)
digital_data_8_bit: int=int(digital_data & 0xFF)
#print(fast_mode | power_down |digital_data_4_bit)
first_byte: int=int(fast_mode | power_down |digital_data_4_bit)

mcp4725.write_byte_data(device_addr, first_byte,digital_data_8_bit)

for i in range(20):
    mcp4017.write_byte(pot_addr, int(i))
    camera.capture('/home/pi/Desktop/a/deneme1.jpg')
    time.sleep(0.5)

#camera.start_preview()
#time.sleep(1)
#
#camera.stop_preview()
