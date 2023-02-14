#!/usr/bin/python3
#https://learn.adafruit.com/monochrome-oled-breakouts/python-wiring
import board
import busio
import time
import os

loop=True
def handler(signum, frame):
    global loop
    print("Ctrl-c was pressed. Exiting")
    loop=False
    time.sleep(1.5)
    oled.fill(0)
    oled.show()
    exit(0)

import signal
signal.signal(signal.SIGINT, handler)

import subprocess
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

#oled = Adafruit_SSD1306.SSD1306Base(128, 32, i2c,i2c=i2c, i2c_bus=5, i2c_address=0x3C)
import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)


oled.fill(0)
oled.show()

#font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

info=[
#  {text="Uptime XXX", cmd="echo 1"}
  {"text": """CPU XXX%""", "cmd": """cat /proc/loadavg | awk '{printf("%.0f\\n", $1 * 100.0 / 8);}'"""},
  {"text": """CPU XXX°C""", "cmd": """cat /sys/class/thermal/thermal_zone0/temp | awk '{printf("%.0f\\n", $1 / 1000);}'"""},
  {"text": """MEM XXX%""", "cmd": """free | grep Mem | awk '{printf("%.0f\\n", 100 - $7/$2 * 100.0);}'"""},
  {"text": """RAID XXX""", "cmd": """cat /proc/mdstat | grep super | awk '{print $6}'"""},
  {"text": """DKR XXX""", "cmd": """echo \"$(docker ps -q | wc -l)/$(docker ps -a -q | wc -l)\""""},
  {"text": """XXX""", "cmd": """uptime -p | sed 's/ day, /d,/g' | sed 's/ hours, /h,/g' | sed 's/ minutes/m/g'"""}
]

while loop:
  for i in info:
    val = subprocess.check_output(i['cmd'], shell = True )
    text = i['text'].replace("XXX", str(val,'utf-8').replace("\n",""))
    image = Image.new('1', (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((-1, -4), text, font=font, fill=255)
    
    image=image.rotate(180, Image.NEAREST, expand = 1)
    oled.image(image)
    oled.show()
    time.sleep(2)
    if not loop:
      break


