#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.waveshare_epd import epd2in7
from PIL import Image,ImageDraw,ImageFont

# epd means e-paper display
# you have to specify a font yourself, there's no default
# init connects the pin (check this for yourself in the e-Paper repo epd2in7 driver)
epd = epd2in7.EPD()
epd.init()
font18 = ImageFont.truetype('Font.ttc', 18)

# draw image with specific mode, size and color
# black and white image, the complete screen, completely white image
Himage = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(Himage)

# draw text on image specifying coordinates, text, font and text color
# color 0 refers to black (we use a black and white e-display)
draw.text((10, 0), 'hello world', font = font18, fill = 0)

# send the image to the e-paper display
epd.display(epd.getbuffer(Himage))