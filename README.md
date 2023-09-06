<h1> CircuitPython</h1>
<p>This is my engineering 3 notebook for the 2023-2024 school year! This readme will be the home of my documentation for all of the non-project assignments this year.</p>

<h2> Table of Contents</h2>
<ul>
<li><a href="#TableOfContents"> Table of Contents</a></li>
<li><a href="#CircuitPython_Servo"> CircuitPython Servo</a></li>
</ul><hr>

<h2>CircuitPython Servo</h2>

<h3>Description & Code</h3>
<p>In this assignment, we were supposed to have a servo sweep its full length, using the adafruit_motor library. Once we finished that, we were supposed to control it with a set of buttons. Finally, we were supposed to replace the buttons with capacative touch, which is what I have documented</p>
<a href=servo.py>Code</a><br><br>

<h3>Evidence</h3>
<img src="media/servo.png"><br>

<h3>Wiring</h3>
<img src="media/servoWiring.png"><br>

<h3>Reflection</h3>
<p>To start off, I looked at the <a href=https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo>adafruit tutorial</a>, which provided recommended libraries and example code that happened to serve the assignment's purpose. It was a bit long winded, though. Wiring up the buttons was pretty simple, as I had done it last year. One thing that made it easier was the existence of internal pull-down resistors, which I could control with code, using the <code>DigitalIO</code> library. To convert to capacative touch actually simplified the wiring, as it replaced the buttons with wires going nowhere. The code was pretty simple too, with <code>TouchIO</code> being a drop-in replacement for <code>DigitalIO</code>.</p>