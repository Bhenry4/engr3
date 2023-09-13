import board, neopixel
import adafruit_hcsr04
import time

trig = board.D8
echo = board.D9
sensor = adafruit_hcsr04.HCSR04(trig, echo)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

colorList=[]
for b in range(0,256):
    colorList.append((255,0,b))
for r in range(255,-1,-1):
    colorList.append((r,0,255))
    print(len(colorList))
for g in range(0,256):
    colorList.append((0,g,255))
for b in range(255,-1,-1):
    colorList.append((0,255,b))

while True:
    try:
        scaledDistance = (1024/30) * sensor.distance-5
        print(sensor.distance)

        led[0] = colorList[int(scaledDistance)]
        time.sleep(0.1)
    except:
        print("Too high or low")