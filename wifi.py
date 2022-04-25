import os
import subprocess

cmd = "echo $(sudo iwlist wlan0 scanning | egrep 'Signal level|ESSID:\"..*\"')"
returned_value=subprocess.check_output(cmd, shell=True)
converted=str(returned_value)
#print(type(converted))
liste=converted.split("ESSID:")
for i in range(len(liste)):
    print(liste[i])