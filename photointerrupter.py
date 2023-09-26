import board, digitalio
import time

photointerrupter = digitalio.DigitalInOut(board.D8)
photointerrupter.pull = digitalio.Pull.UP # Photointerrupter on pin 8 with a pull-up
interrupted = 0
oldTime = time.monotonic() # seconds since program start

while True:
    if photointerrupter.value:
        interrupted += 1
    if time.monotonic() - oldTime > 4: # tests if four seconds have passed since last reset oldTime
            print("Number of interrupts: " + str(interrupted))
            oldTime = time.monotonic() # resets oldTime