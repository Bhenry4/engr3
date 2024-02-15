import board #imports the board library
import neopixel #imports the neopixel library
import digitalio #imports the digitalio library

IRSensor = digitalio.DigitalInOut(board.D9) #creates an object of class DigitalInOut
IRSensor.direction = digitalio.Direction.INPUT #sets the member direction to Direction.Input
IRSensor.pull = digitalio.Pull.UP #sets the member pull to Pull.UP

led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3) #creates an object of class NeoPixel
colors ={"red": (255, 0, 0), "green": (0, 255, 0)} #creates a dictionary object named colors

while True: #runs until True equals False
    if IRSensor.value: #runs if IRSensor.value equals True
        print("Nothing nearby") #calls function print with value "Nothing nearby"
        led[0] = colors["red"] #sets value at position zero of list led to the value corresponding to the key "red" in the dict colors
    if not IRSensor.value: #runs if IRSensor.value does not equal True
        print("Object detected") #calls function print with value "Object detected"
        led[0] = colors["green"] #sets value at position zero of list led to the value corresponding to the key "green" in the dict colors
        #test