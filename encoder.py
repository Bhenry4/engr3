import rotaryio
import digitalio
import board
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

encoder = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
button = digitalio.DigitalInOut(board.D2)

button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
buttonPressed = False

menuItems = ["go", "caution", "stop"]
lastIndex = 0
currentIndex = 0

while True:
    if not button.value and not buttonPressed:
        lcd.clear()
        lcd.print("Button Pressed")
        buttonPressed = True
    if button.value and buttonPressed:
        lcd.clear()
        lcd.print("Button Released")
        buttonPressed = False

    currentIndex = encoder.position
    if not lastIndex == currentIndex:
        print(currentIndex%3)
        lastIndex = currentIndex