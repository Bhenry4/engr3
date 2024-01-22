import asyncio
import board
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

limitSwitch = digitalio.DigitalInOut(board.D2)
limitSwitch.pull = digitalio.Pull.UP

async def catchPinTransitions(button):
    buttonPressed = False # for debouncing
    while True:
        if not button.value and not buttonPressed:
            print("Button Pressed")
            buttonPressed = True
            for i in range(STEPS):
                motor.onestep(style=stepper.DOUBLE, direction=stepper.BACKWARD)
                time.sleep(DELAY)
        if button.value and buttonPressed:
            print("Button Released")
            buttonPressed = False
        await asyncio.sleep(0)

async def runMotor(motor):
    while True:
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    interruptTask = asyncio.create_task(catchPinTransitions(limitSwitch))
    motorTask = asyncio.create_task(runMotor(motor))
    await asyncio.gather(interruptTask, motorTask)

asyncio.run(main())