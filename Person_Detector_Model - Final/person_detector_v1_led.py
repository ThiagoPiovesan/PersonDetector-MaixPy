#tested with frimware 5-0.22
import sensor,image,lcd
import KPU as kpu

import time

from fpioa_manager import fm
from Maix import GPIO

led = 14
#--------------------------------------------------------------------------------------------------#
lcd.init(freq=15000000)
#--------------------------------------------------------------------------------------------------#
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
sensor.run(1)

fm.register(led, fm.fpioa.GPIO0)
led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(0)
#--------------------------------------------------------------------------------------------------#
classes = ["person"]

task = kpu.load(0x600000) #change to "/sd/name_of_the_model_file.kmodel" if loading from SD card
a = kpu.set_outputs(task, 0, 7,7,30) #the actual shape needs to match the last layer shape of your model(before Reshape)

anchor = (0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828)
a = kpu.init_yolo2(task, 0.3, 0.3, 5, anchor) #tweak the second parameter if you're getting too many false positives

tic = time.time()
#--------------------------------------------------------------------------------------------------#
while(True):


    img = sensor.snapshot().rotation_corr(z_rotation=180.0)
    a = img.pix_to_ai()
    code = kpu.run_yolo2(task, img)
#--------------------------------------------------------------------------------------------------#

    if code:
#--------------------------------------------------------------------------------------------------#
    # Ativa LED
        #c_timer = datetime.datetime.now().second            # Time controler
        toc = time.time()

        if (toc - tic > 1):
            led_r.value(1)

#--------------------------------------------------------------------------------------------------#
        for i in code:
            a = img.draw_rectangle(i.rect(),color = (0, 255, 0))
            a = img.draw_string(i.x(),i.y(), classes[i.classid()], color=(255,0,0), scale=3)

        a = lcd.display(img)

    else:
    # Desativa LED
        led_r.value(0)
        tic = time.time()

        a = lcd.display(img)
#--------------------------------------------------------------------------------------------------#

a = kpu.deinit(task)
