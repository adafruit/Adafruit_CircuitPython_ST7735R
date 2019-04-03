"""
This example will test out the display on the Mini TFT FeatherWing
"""
import board
import displayio
from adafruit_seesaw.seesaw import Seesaw
from adafruit_st7735r import ST7735R

reset_pin = 8
i2c = board.I2C()
ss = Seesaw(i2c, 0x5E)
ss.pin_mode(reset_pin, ss.OUTPUT)

spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D6

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)

ss.digital_write(reset_pin, True)
display = ST7735R(display_bus, width=160, height=80, colstart=24, rotation=270, bgr=True)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(160, 80, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

try:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   position=(0, 0))
except TypeError:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
splash.append(bg_sprite)

while True:
    pass
