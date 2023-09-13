import board, neopixel
import adafruit_hcsr04
import time

trig = board.D8
echo = board.D9
sensor = adafruit_hcsr04.HCSR04(trig, echo)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# Creates a list of the necessary range of colors by looping through the increasing/decreasing variables
colorList=[]
for b in range(0,256): # (255,0,0)-(255,0,255)
    colorList.append((255,0,b))
for r in range(255,-1,-1): # (255,0,255)-(0,0,255)
    colorList.append((r,0,255)) # Crashes here(at element 350) on m0
    print(len(colorList))
for g in range(0,256): # (0,0,255)-(0,255,255)
    colorList.append((0,g,255))
for b in range(255,-1,-1): # (0,255,255)-(0,255,0)
    colorList.append((0,255,b))

while True:
    try:
        scaledDistance = (1024/30) * sensor.distance-5 # converts distance into array index
        print(sensor.distance)

        led[0] = colorList[int(scaledDistance)] # int because division results in a float
        time.sleep(0.1)
    except:
        print("Too high or low") # Errors if sensor times out or index out of bounds
