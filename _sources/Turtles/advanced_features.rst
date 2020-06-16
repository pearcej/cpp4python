Advanced Features
=================

Turtles are a large tool, and thus have a lot of options dictating how they function.
Some features and functionality are more complicated than others, relating to the inner workings
of turtles themselves. A few of these include the :code:`tracer` and :code:`undo` methods, and also screen modes.

Screen modes dictate the direction of angle measurements. This means that, depending on which mode a :code:`TurtleScreen`
object is in, positive angles could represent clockwise rotations or counterclockwise rotations. The :code:`mode` method
for :code:`TurtleScreen` allows you to set which mode a screen is in.

=========== ================ ================
    Mode    Default Rotation Positive Angles
=========== ================ ================
SM_STANDARD       East       Counterclockwise
  SM_LOGO         North         Clockwise
=========== ================ ================

Regarding angles, Turtles can use both *degrees* and *radians* for their rotations. You can choose between the two using the
:code:`radians` and :code:`degrees` methods for the Turtle object. By default, all angles are measured in *degrees*. This option
only effects methods regarding rotation, such as :code:`left` and :code:`right`.

The :code:`tracer` method is used to control how fast and how many times the Turtle is actually
drawn on the screen. Using it can significantly speed up the drawing of complicated figures and
images because it dictates however many frames of animation gets put on
the screen. It also lets you specify a delay, in milliseconds, between frames of animation.

A frame of animation is added for almost every action a turtle takes, regardless of whether or not
the turtle is moving or adding something to the screen. This includes methods like
:code:`begin_fill` and :code:`end_fill`, which don't do anything visually but do
tell the turtle to start or stop tracking its own movements.

Consider the following example.

.. activecode:: cturtle_advanced_ac_1
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;
    
    int main(){
        ct::TurtleScreen screen;
        ct::Turtle turtle(screen);

        screen.tracer(6);

        for(int i = 0; i < 3; i++){
            turtle.right(60);
            turtle.forward(50);
        }   

        screen.bye();

        return 0;
    }

.. mchoice:: cturtle_advanced_mchoice_1
   :answer_a: 3
   :answer_b: 6
   :answer_c: 1
   :answer_d: 12
   :correct: c
   :feedback_a: Incorrect! Consider how many actions the turtle takes in the for loop.
   :feedback_b: Incorrect! Consider the tracer setting for the screen.
   :feedback_c: Correct!
   :feedback_d: Incorrect! Consider how many actions the turtle takes in the for loop.

   How many frames of animation does the above code create?

Similarly to tracer settings, every action a turtle takes is also added to the *undo queue*. This allows it to keep track
of actions it is performing over a period of time. The queue is only allowed to grow to a certain size, starting at 100 actions.
This is modifiable through the :code:`setundobuffer` function that belongs to turtles. Every action is added, even if
the action doesn't change anything visuall, much like tracer settings.

.. mchoice:: cturtle_advanced_mchoice_2
    :answer_a: 3
    :answer_b: 6
    :answer_c: 1
    :answer_d: 12
    :correct: b
    :feedback_a: Incorrect! Consider how many actions the turtle takes in the for loop.
    :feedback_b: Correct!
    :feedback_c: Incorrect! Consider how many actions the turtle takes in the for loop.
    :feedback_d: Incorrect! Consider how many actions the turtle takes in the for loop.

    How many actions will be in the turtle's undo queue for the code above?

Polygons, for custom shapes, must have their points defined in counter-clockwise order to appear correctly. This is due to
the mathematics behind filling arbitrary shapes, and is a limitation almost all computer graphics need to abide by. CTurtle
features four default shapes, :code:`triangle`, :code:`indented_triangle`, :code:`square`, and :code:`arrow`. Consider
the construction of their points, and how they could be considered "counter-clockwise". One edge exists between the first
last points for each of these shapes.

======== ===================== ========== ========
Triangle   Indented Triangle     Square    Arrow
======== ===================== ========== ========
(0, 0)          (0, 0)          (-5, -5)   (0, 0)
(-5, 5)        (-5, 10)          (-5, 5)  (-5, 5)      
(5, 5)          (0, 8)           (5, 5)   (-3, 5)
  .             (5, 10)          (5, 10)  (-3, 10)
  .               .                .       (3, 10)
  .               .                .       (3, 5)
  .               .                .       (5, 5)
======== ===================== ========== ========