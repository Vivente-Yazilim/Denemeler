import os
import sys
import time
ssid=sys.argv[1]
password=sys.argv[2]
os.system("wifi off")
time.sleep(1)
config_lines= [
    'network={',
    '\tssid="{}"'.format(ssid),
    '\tpsk="{}"'.format(password),
    '\tkey_mgmt=WPA-PSK',
    '}'
    ]
config='\n'.join(config_lines)
with open("/etc/wpa_supplicant/wpa_supplicant.conf", "+a") as wifi:
    wifi.write(config)
time.sleep(1)
os.system("wifi on")
print(config)