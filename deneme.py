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
#Gerekli Kutuphaneler import edildi ve LED Driver Nesnesi icerisinde kullanilacak Kart Girilerek olusturuldu.

#Bu Blok Kamera ile alakali
MMAL_PARAMETER_ANALOG_GAIN=mmal.MMAL_PARAMETER_GROUP_CAMERA+0X59
MMAL_PARAMETER_DIGITAL_GAIN=mmal.MMAL_PARAMETER_GROUP_CAMERA+0X5A

#White LED parlaklik ayari yapiliyor.
kart.set_white_brightness(100)
#IR LED parlaklik ayari yapiliyor.
kart.set_ir_brightness(30)
#Gorus icin IR LED aktif hale getiriliyor.
kart.turn_on_ir()

#Kamera kullanimi icin sinif nesne olusturuluyor.
camera=picamera.PiCamera()
image_sayac=0#Cekilen fotolarin isimlendirilmesinde kullanilmak uzere tanimlanan bir sayac

#???????????
set_gain(camera, MMAL_PARAMETER_DIGITAL_GAIN, 2.000)
set_gain(camera, MMAL_PARAMETER_ANALOG_GAIN, 2.000)

#Kamera onizlemesi aktif hale getiriliyor.
camera.start_preview(fullscreen=False, window=(80,0,640,480),alpha=255,layer=0)

#Sonsuz dongu icerisine giriliyor.
while True:
#Eger '1' tusuna basilirsa fotograf yakalanacak, 's' tusuna basilirsa uygulamadan cikilacak
    if keyboard.is_pressed('1'):
        camera.stop_preview()#Kamera onizlemesini durdur ve 0.5s bekle
        time.sleep(0.5)
        image_sayac=image_sayac+1#isimlendirme de ayni isim olmamasi icin bir arttiriliyor.
        image_name="deneme{0:2d}.jpg".format(image_sayac)#image adi olusturuluyor.
        camera.capture('/home/pi/Desktop/camera/images/'+image_name)#kameradan alinan goruntu belirlenen dosya yoluna kaydediliyor.
        time.sleep(0.2)
        #Kamera onizlemesini tekrar aktiflstir.
        camera.start_preview(fullscreen=False, window=(80,0,640,480),alpha=255,layer=0)
            
    if keyboard.is_pressed('s'):
        time.sleep(0.5)
        camera.stop_preview()
        break

