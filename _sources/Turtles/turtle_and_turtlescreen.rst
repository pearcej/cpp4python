Turtle & TurtleScreen
=====================

Turtles must exist on a :code:`TurtleScreen` to be used. This is a significant difference from
Python, as you are required to create your own screen *before* creating a :code:`Turtle` object.

.. code-block:: cpp

    ct::TurtleScreen screen;
    ct::Turtle turtle(screen);
    //Notice how the Screen is given to our Turtle when we create it.

Closing a :code:`TurtleScreen` works exactly how it does in Python. For this chapter, only :code:`bye` is used.
Calling it is not completely necessary, as it is also called automatically if it, or an equivalent method, hasn't been called.
When working outside of the textbook, the :code:`exitonclick` method is also available.

.. code-block:: cpp

    screen.bye();

Turtles are based on the following premise: "There is a turtle on a canvas with a colored pen
attached to their tail." In this case, the *canvas* is a :code:`TurtleScreen`. This Turtle will
follow any command you give it, which consist of telling it to go certain directions, what color
of pen to use, when to raise or lower its pen, and others. Below is an outline of commonly used
methods when working with turtles.

=================  ==========================================================================
    Method Name                                  Description
=================  ==========================================================================
turtle.left        turns the turtle a certain number of units to the left.
turtle.right       turns the turtle a certain number of units to the right.
turtle.penup       raises the paint pen on the end of the turtle's tail.
turtle.pendown     lowers the paint pen on the end of the turtle's tail.
turtle.fillcolor   tells the turtle what color the inside of the shape will be. 
turtle.beginfill   tells the turtle to begin filling a shape as it moves.
turtle.endfill     tells the turtle to finish filling the shape it has created as it moved.
turtle.pencolor    tells the turtle what color it will draw with. 
turtle.width       tells the turtle how large of a paint pen to use.
turtle.speed       tells the turtle how fast it should go, faster or slower than the hare.
turtle.back        moves the turtle back a number of units.
turtle.forward     moves the turtle forward a number of units.
turtle.goto        tells the turtle to move to a specific coordinate.
turtle.write       tells the turtle to write some kind of text. 
=================  ==========================================================================

Many of these methods are used alongside one-another to create different images. All of the :code:`speed` settings
you may be familiar with from Python are also available in CTurtle. All speeds are measured on a range of 1 to 10,
the latter being the fastest and the former being the slowest. The exception is the fastest speed, :code:`TS_FASTEST`,
which is set to 0 just as it is for Python's equivalent :code:`"fastest"`. The :code:`TS` prefix represents "Turtle Speed".

===================== ============== ==========
 Python Turtle Name   C-Turtle Name    Speed
===================== ============== ==========
       "fastest"       TS_FASTEST       0
       "fast"          TS_FAST          10
       "normal"        TS_NORMAL        6
       "slow"          TS_SLOW          3
       "slowest"       TS_SLOWEST       1
===================== ============== ==========

Consider the following annotated example.

.. activecode:: cturtle_4
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        //Create a turtle screen, and add our turtle to it.
        ct::TurtleScreen screen;
        ct::Turtle turtle(screen);
        
        //Set the turtle speed to the slowest available option.
        turtle.speed(ct::TS_SLOWEST);
        //Any number from 0 to 10 would work as well.
        //turtle.speed(7);
        
        //Sets the turtle's fill color to purple.
        turtle.fillcolor({"purple"});
        
        //Tells the turtle to begin filling a shape as it moves.
        turtle.begin_fill();
        
        //Tells the turtle to make a square.
        //Iterates once for every corner of the square.
        for (int i = 0; i < 4; i++) {
        
            //Tells the turtle to move forward 50 units.
            turtle.forward(50);
            
            //Tells the turtle to turn 90 degrees to the right.
            turtle.right(90);
        }
        
        //Tells the turtle to finish filling the shape it has outlined.
        turtle.end_fill();
        
        //Closes the turtle screen.
        screen.bye();
        return 0;
    }

The expected output would be a purple square in the center of the turtle's canvas.
If you have experience with Turtles in Python, a lot of what you see in the example should look
familiar. If not, don't worry! It will all be covered in this chapter.

The order of operations given to a turtle is important, as some actions must be completed
one after another. A good example of this is the :code:`begin_fill` and :code:`end_fill`
pattern, which must be called in that specified order to actually fill a shape.

.. parsonsprob:: cturtle_question_3

    Construct a program that fills a green triangle using begin_fill and end_fill
    using the example code above as a guide.
    -----
    #include <CTurtle.hpp>
    namespace ct = cturtle;
    =====
    int main(){
    =====
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);
    =====
        turtle.fillcolor({"green"});
    =====
        turtle.begin_fill();
    =====
        for(int i = 0; i < 3; i++){
            turtle.forward(50);
            turtle.right(60);
        }
    =====
        turtle.end_fill();
    =====
        scr.bye();
    =====
        return 0;
    =====
    }

There are 14 commonly used methods for Turtles. Many of them have names that indicate what they do. 
See if you can match each method description with their names!

.. dragndrop:: cturtle_dnd_1
   :match_1: turn to the left.|||turtle.left
   :match_2: turn to the right.|||turtle.right
   :match_3: pick pen up.|||turtle.penup
   :match_4: put pen down.|||turtle.pendown
   :match_5: what color to fill drawing with.|||turtle.fillcolor
   :match_6: start filling the shape.|||turtle.beginfill
   :match_7: stops filling the shape.|||turtle.endfill
   :match_8: change the pen color.|||turtle.pencolor
   :match_9: change the pen size.|||turtle.width
   :match_10: change the speed|||turtle.speed

   Match the turtle method descriptions to the methods they belong to.
