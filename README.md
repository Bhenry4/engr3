<h1> CircuitPython</h1>
<p>This is my engineering 3 notebook for the 2023-2024 school year! This readme will be the home of my documentation for all of the non-project assignments this year.</p>

<h2> Table of Contents</h2>
<ul>
<li><a href="#TableOfContents"> Table of Contents</a></li>
<li><a href="#CircuitPython_Servo"> CircuitPython Servo</a></li>
</ul><hr>

<h2>CircuitPython Servo</h2>

<h3>Description & Code</h3>
<p>In this assignment, we were supposed to have a servo sweep its full length. Once we finished that, we were supposed to control it with a set of buttons. Finally, we were supposed to replace the buttons with capacative touch, which is what I have documented</p><br>

```python
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
```


<h3>Evidence</h3>

<img src="media/servo.png">



<h3>Wiring</h3>
<img src="media/servoWiring.png">

<h3>Reflection</h3>
<p>This assignment served as a good introduction to using libraries in curcuitpython. It was also cool to see capacative touch working. One issue a ran into was the angle values going out of range, which was fixed by adding checks before incrementing or decrementing it.