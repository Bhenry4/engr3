import pwmio, board, digitalio
from adafruit_motor import servo
import time

pwm = pwmio.PWMOut(board.D12, duty_cycle=2**15, frequency=50)
servo0 = servo.Servo(pwm)
servoAngle = 90

buttonLeft = digitalio.DigitalInOut(board.D10)
buttonRight = digitalio.DigitalInOut(board.D9)
buttonLeft.pull = digitalio.Pull.DOWN
buttonRight.pull = digitalio.Pull.DOWN

while True:
    servo0.angle = servoAngle

    if buttonLeft.value:
        if servoAngle != 0:
            servoAngle -= 1
            time.sleep(0.01)
            print(servoAngle)

    if buttonRight.value:
        if servoAngle != 180:
            servoAngle += 1
            time.sleep(0.01)
            print(servoAngle)