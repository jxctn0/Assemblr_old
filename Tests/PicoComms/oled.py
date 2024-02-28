from machine import Pin, I2C
import ssd1306

class I2C_Display:
    def __init__(self, width=128, height=64, scl_pin=1, sda_pin=0):
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        self.oled = ssd1306.SSD1306_I2C(width, height, self.i2c)
        self.width = width
        self.height = height
        self.line_height = 8  # Assuming 8 pixels per line
        self.lines = height // self.line_height
        self.cursor = [0, 0]  # x, y coordinates of the cursor

    def println(self, text, line=None):
        if line is None:
            line = self.cursor[1]
            self.cursor[1] = (self.cursor[1] + 1) % self.lines  # Move cursor to the next line
        self.clearln(line)
        self.oled.text(text, 0, line * self.line_height)
        self.oled.show()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()
        self.cursor = [0, 0]

    def clearln(self, line):
        self.oled.fill_rect(0, line * self.line_height, self.width, self.line_height, 0)
        self.oled.show()

    def clean(self):
        self.oled.fill(0)
        self.oled.show()
        self.i2c.init(I2C.MASTER, baudrate=400000)  # Re-initialize I2C in master mode

