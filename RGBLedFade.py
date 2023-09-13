# Write your code here :-)
import pwmio
import board
import time

RED_LED = pwmio.PWMOut(board.D9)
GREEN_LED = pwmio.PWMOut(board.D10)
BLUE_LED = pwmio.PWMOut(board.D11)

numColors = 255

animationDelay = 10

RED_LED.direction(OUTPUT)
GREEN_LED.direction(OUTPUT)
BLUE_LED.direction(OUTPUT)

while True:
    fadeToColor(255, 0, 0)    # red
    print("red")

    fadeToColor(0, 255, 0)     # green
    print("green")

    fadeToColor(0, 0, 255)     # blue
    print("blue")

    fadeToColor(255, 255, 0)   # yellow
    print("yellow")

    fadeToColor(80, 0, 80)     # purple
    print("purple")

    fadeToColor(0, 255, 255)   # aqua
    print("aqua")

def fadeToColor(red, green, blue):
    r, g, b = 0

    while r != red or g != green or b != blue:
        if r < red:
            r += 1
        if r > red:
            r -= 1

        if g < green:
            g += 1
        if g > green:
            g -= 1

        if b < blue:
            b += 1
        if b > blue:
            b -= 1

        RED_LED.duty_cycle = r
        GREEN_LED.duty_cycle = g
        BLUE_LED.duty_cycle = b
        time.sleep(0.10)