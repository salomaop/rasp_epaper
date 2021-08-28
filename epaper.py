import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

import logging
from lib.waveshare_epd import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont

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
        drawblack = ImageDraw.Draw(HBlackimage)
        drawblack.text((10, 0), 'Salomao', font = font20, fill = 0)
        drawblack.line((20, 50, 70, 100), fill = 0)
        drawblack.line((70, 50, 20, 100), fill = 0)
        drawblack.rectangle((20, 50, 70, 100), outline = 0)
        epd.display(epd.getbuffer(HBlackimage))

        logging.info("Goto Sleep...")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13b_V3.epdconfig.module_exit()
        exit()
