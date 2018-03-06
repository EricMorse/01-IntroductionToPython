"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Eric Morse.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)  

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)
red_turtle.speed = 30
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 20
for k in range (10):
    blue_turtle.left(90)
    red_turtle.forward(20*k)
    blue_turtle.forward(20*k)
    red_turtle.left(90)
    red_turtle.pen_up()
    blue_turtle.pen_up()
    blue_turtle.left(90)
    red_turtle.forward(20*k)
    blue_turtle.forward(20*k)
    red_turtle.left(90)
    red_turtle.pen_down()
    blue_turtle.pen_down()

window.close_on_mouse_click()