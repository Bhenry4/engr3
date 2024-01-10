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
colorList = {"go": (0,255,0), "caution": (255,255,0), "stop": (255,0,0)}
lastIndex = 0
currentIndex = 0

while True:
    if not button.value and not buttonPressed:
        print("Button Pressed")
        buttonPressed = True
        led[0] = colorList[menuItems[currentIndex%3]]
    if button.value and buttonPressed:
        print("Button Released")
        buttonPressed = False

    currentIndex = encoder.position
    if not lastIndex == currentIndex:
        lcd.clear()
        lcd.print(menuItems[currentIndex%3])
        lastIndex = currentIndex