import rotaryio
import digitalio
import board
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574INTERFACE

encoder = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574INTERFACE(board.I2C(), 0x27), num_rows=2, num_cols=16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
button = digitalio.DigitalInOut(board.D2)

button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
buttonPressed = False

while True:
    if button.value and not buttonPressed:
        print("Button Pressed")
        buttonPressed = True
    if not button.value and buttonPressed:
        print("Button Released")
        buttonPressed = False