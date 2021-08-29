import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'rasp_epaper/pic')
print(picdir)

import logging
from lib.waveshare_epd import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    try:
        IP = s.getsockname()[0]
    except Exception:
        IP = '0.0.0.0'
    return IP

logging.basicConfig(level=logging.DEBUG)

def run():
    try:
        logging.info("rodando")

        epd = epd2in13b_V3.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        time.sleep(1)
        font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
        font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

        HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
        HRYimage = Image.new('1', (epd.height, epd.width), 255)
        drawblack = ImageDraw.Draw(HBlackimage)
        drawred = ImageDraw.Draw(HRYimage)
        msg = "IP: " + get_ip()
        logging.info(msg)
        drawblack.text((10, 0), msg, font = font20, fill = 0)
        drawred.text((10, 52), msg, font=font20, fill=0)
        epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

        logging.info("Goto Sleep...")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13b_V3.epdconfig.module_exit()
        exit()
