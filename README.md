<h1> CircuitPython</h1>
<p>This is my engineering 3 notebook for the 2023-2024 school year! This readme will be the home of my documentation for all of the non-project assignments this year.</p>

<h2> Table of Contents</h2>
<ul>
<li><a href="#TableOfContents"> Table of Contents</a></li>
<li><a href="#CircuitPythonServo"> CircuitPython Servo</a></li>
<li><a href="#DistanceSensor"> Distance Sensor</a></li>
</ul><hr>


<h2 name="CircuitPythonServo">CircuitPython Servo</h2>

<h3>Description & Code</h3>
<p>In this assignment, we were supposed to have a servo sweep its full length, using the adafruit_motor library. Once we finished that, we were supposed to control it with a set of buttons. Finally, we were supposed to replace the buttons with capacative touch, which is what I have documented</p>
<a href=servo.py>Code</a><br><br>

<h3>Evidence</h3>
<img src="media/servo.png"><br>

<h3>Wiring</h3>
<img src="media/servoWiring.png"><br>

<h3>Reflection</h3>
<p>To start off, I looked at the <a href=https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo>adafruit tutorial</a>, which provided recommended libraries and example code that happened to serve the assignment's purpose. It was a bit long winded, though. Wiring up the buttons was pretty simple, as I had done it last year. One thing that made it easier was the existence of internal pull-down resistors, which I could control with code, using the <code>DigitalIO</code> library. To convert to capacative touch actually simplified the wiring, as it replaced the buttons with wires going nowhere. The code was pretty simple too, with <code>TouchIO</code> being a drop-in replacement for <code>DigitalIO</code>.</p>


<h2 name="DistanceSensor">Distance Sensor</h2>

<h3>Description & Code</h3>
<p>In this assignment, we were supposed to to print the output of a distance sensor to the serial monitor. Then, we were supposed to have the onboard neopixel go through a range from red to green based on the distance.</p>
<a href=distanceSensor.py>Code</a><br><br>

<h3>Evidence</h3>
<img src="media/distanceSensor.jpg"><br>

<h3>Wiring</h3>
<img src="media/distanceSensorWiring.png"><br>

<h3>Reflection</h3>
<p>Wiring up the sensor was pretty simple, as it was the same as the arduino wiring. The code was pretty simple, using the <code>adafruit_hcsr04</code> library. To get the distance is as simple as <code>sensor.distance</code>, with your previously constructed sensor object. The neopixel was where I ran into problems. The array of colors I was constructing was causing a <code>MemoryError</code> on m0s, which was fixed by decreasing the granularity of the array. In addition, the colors were not displaying properly on a m0 neopixel, which turned out to be a problem with the specific m0 I was using.</p>