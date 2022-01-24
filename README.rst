Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-st7735r/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/st7735r/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_ST7735R/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_ST7735R/actions/
    :alt: Build Status

displayio driver for ST7735R TFT-LCD displays.

Hardware
=========

* `1.8" SPI TFT display, 160x128 18-bit color
  <https://www.adafruit.com/product/618>`_
* `Adafruit 0.96" 160x80 Color TFT Display w/ MicroSD Card Breakout
  <https://www.adafruit.com/product/3533>`_
* `1.8" Color TFT LCD display with MicroSD Card Breakout
  <https://www.adafruit.com/product/358>`_
* `Adafruit 1.44" Color TFT LCD Display with MicroSD Card breakout
  <https://www.adafruit.com/product/2088>`_
* `Adafruit Mini Color TFT with Joystick FeatherWing
  <https://www.adafruit.com/product/3321>`_

If you have a board with a ST7735B chip, you may want to try
`the Adafruit ST7735 Driver <https://github.com/adafruit/Adafruit_CircuitPython_ST7735>`_.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython 4.0.0-beta.0+ <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    import board
    import displayio
    from adafruit_st7735r import ST7735R

    spi = board.SPI()
    tft_cs = board.D5
    tft_dc = board.D6

    displayio.release_displays()
    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)

    display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(128, 128, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFF0000

    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
    splash.append(bg_sprite)

    while True:
        pass

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/st7735r/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ST7735R/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
