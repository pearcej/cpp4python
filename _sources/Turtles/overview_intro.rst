Overview of Turtles
=======================================

Turtles are based on the following premise: "There is a turtle on a canvas with a paint brush
attached to their tail." This turtle will follow any command you give it, which consists 
of telling it to go certain directions, what color to put on its brush, and when
to raise or lower its brush. Below is an outline of commonly used methods when working with turtles.

=================  ==========================================================================
    Method Name                                  Description
=================  ==========================================================================
turtle.left        turns the turtle a certain number of units to the left.
turtle.right       turns the turtle a certain number of units to the right.
turtle.penup       raises the paint brush on the end of the turtle's tail.
turtle.pendown     lowers the paint brush on the end of the turtle's tail.
turtle.fillcolor   tells the turtle what color the inside of the shape will be. 
turtle.beginfill   tells the turtle to begin filling a shape as it moves.
turtle.endfill     tells the turtle to finish filling the shape it has created as it moved.
turtle.pencolor    tells the turtle what color it will draw with. 
turtle.width       tells the turtle how large of a paint brush to use.
turtle.speed       tells the turtle how fast it should go, faster or slower than the hare.
turtle.back        moves the turtle back a number of units.
turtle.forward     moves the turtle forward a number of units.
turtle.goto        tells the turtle to move to a specific coordinate.
turtle.write       tells the turtle to write some kind of text. 
=================  ==========================================================================

Many of these methods are used alongside one-another to create different images.
Consider the following annotated example.

.. activecode:: cturtle_4
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        //Create a turtle screen, and add our turtle to it.
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);
        
        //Set the turtle speed to the slowest available option.
        turtle.speed(ct::TS_SLOWEST);
        
        //Sets the turtle's fill color to purple.
        turtle.fillcolor({"purple"});
        
        //Tells the turtle to begin filling a shape as it moves.
        turtle.begin_fill();
        
        //Tells the turtle to iterate trhough the loop 4 times.
        //Once for every corner of a square.
        for (int i = 0; i < 4; i++) {
        
            //Tells the turtle to move forward 50 units.
            turtle.forward(50);
            
            //Tells the turtle to turn 90 degrees to the right.
            turtle.right(90);
        }
        
        //Tells the turtle to finish filling the shape it has outlined.
        turtle.end_fill();
        
        //Closes the turtle screen.
        scr.bye();
        return 0;
    }

The expected output would be a purple square in the center of the turtle's canvas.
Try playing around with the actions of the turtle, you may surprise yourself with what you create!
Some good examples to attempt include a triangle, a star, a rectangle, or a spiral.

The order of operations given to a turtle is important, as some actions must be completed
one after another. A good example of this is the :code:`begin_fill` and :code:`end_fill`
pattern, which must be called in that specified order to actually fill a shape.

.. parsonsprob:: cturtle_question_3

    Construct a program that fills a green triangle using begin_fill and end_fill.
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
        return 0;
    }

.. dragndrop:: cturtle_dnd_1
   :match_1: turn to the left.|||turtle.left
   :match_2: turn to the left.|||turtle.right
   :match_3: pick tail up.|||turtle.penup
   :match_4: put tail down.|||turtle.pendown
   :match_5: what color to fill drawing with.|||turtle.fillcolor
   :match_6: start filling the shape.|||turtle.beginfill
   :match_7: stops filling the shape.|||turtle.endfill
   :match_8: change the paintbrush color.|||turtle.pencolor
   :match_9: change the paintbrush size.|||turtle.width
   :match_10: change the speed|||turtle.speed
   :match_11: move backward.|||turtle.back
   :match_12: move forward.|||turtle.forward
   :match_13: move to a specific coordinate.|||turtle.goto
   :match_14: write some text to the canvas.|||turtle.write

   Match the turtle method descriptions to the methods they belong to.

Differences between Python and C++ Turtles
==========================================

CTurtle varies from Python turtles primarily in syntax. Most of the methods are exactly the same between implementations,
however there are a few notable differences between the two. Colors, for example, must be surrounded by curly brackets (e.g,
'{' and '}') when referring to them by a name such as "red", "green", or "blue".

.. code-block:: cpp

    ct::Color red   = {"red"};
    ct::Color green = {"green"};
    ct::Color blue  = {"blue"};

    //This works...
    turtle.pencolor(red);

    //And so does this.
    turtle.pencolor({"green"});

Unlike in Python, the :code:`write` function does not allow you to specify a font nor size. This is due to the complex handling
and nature of Fonts by the operating system. Furthermore, there is no "world" screen mode like there is in Python. Normally,
this would allow you to specify the "bounds" of your world (e.g, specify minimum and maximum coordinates for your canvas).

Default shapes are also different and somewhat limited in comparison. Python offers six shapes by default, being "arrow", "circle",
"turtle", "square", "triangle", and "classic". CTurtle, on the other hand, offers four shapes by default: "arrow", "triangle",
"indented triangle", and "square".

There are a few utility methods available in CTurtle that are not available in Python, such as :code:`shift` and :code:`middle`.
The former of the two, :code:`shift`, simply adds to the X and Y coordinate position of the turtle. If your turtle is at coordinate
600x, 400y and :code:`shift` is called with coordinate 50x and -50y, the turtle's final position would be 650x, 350y. The latter
of the two, :code:`middle`, returns the point exactly between two other points. Consider the example below.

.. code-block:: cpp

    ct::Point a = {400, 300};
    ct::Point b = {450, 300};

    //Should equal the point 425x, 300y.
    ct::Point middle = ct::middle(a, b);
