import pwmio, board, touchio
from adafruit_motor import servo
import time

pwm = pwmio.PWMOut(board.D12, duty_cycle=2**15, frequency=50) # The servo is set up with pwm
servo0 = servo.Servo(pwm)
servoAngle = 90

buttonLeft = touchio.TouchIn(board.A0) # sets up capacative touch with the wires
buttonRight = touchio.TouchIn(board.A1)

while True:
    servo0.angle = servoAngle

    if buttonLeft.value:
        if servoAngle != 0: # angle vals error if less than 0
            servoAngle -= 1
            time.sleep(0.01)
            print(servoAngle)

    if buttonRight.value:
        if servoAngle != 180: # angle vals error if greater than 180
            servoAngle += 1
            time.sleep(0.01)
            print(servoAngle)