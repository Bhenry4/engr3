import board, analogio
import time

input = analogio.AnalogIn(board.A1)
output = analogio.AnalogOut(board.A0) # A0 has a Digital-to-Analog converter on it

while True:
    print(input.value)
    output.value = input.value # They have the same scales (0-65535)
    time.sleep(1)