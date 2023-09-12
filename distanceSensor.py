import board, neopixel
import adafruit_hcsr04
import time

trig = board.D8
echo = board.D9
#sensor = adafruit_hcsr04.HCSR04(trig, echo)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.01)

while True:
    # try:
    #     print(sensor.distance)
    # except:
    #     print("Timed Out")
    # time.sleep(0.1)
    led[0] = (255,0,255)
    time.sleep(0.1)