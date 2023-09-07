import board, neopixel
import adafruit_hcsr04
import time

trig = board.D8
echo = board.D9
sensor = adafruit_hcsr04.HCSR04(trig, echo)
led = neopixel.NeoPixel(board.NEOPIXEL)

while True:
    try:
        print(sensor.distance)
    except:
        print("Timed Out")
    time.sleep(0.1)