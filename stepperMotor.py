import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9),
    digitalio.DigitalInOut(board.D10),
    digitalio.DigitalInOut(board.D11),
    digitalio.DigitalInOut(board.D12),
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
motor = stepper.StepperMotor(*coils, microsteps=None)

while True:
    for i in range(STEPS):
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)
    for i in range(STEPS):
        motor.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
        time.sleep(DELAY)