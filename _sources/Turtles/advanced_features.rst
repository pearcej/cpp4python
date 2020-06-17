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

.. code-block:: cpp

    turtle.degrees();
    turtle.right(90);//90-degree turn to the right
    turtle.radians();
    turtle.left(1.5708f);//Equivalent rotation in radians to the left.

The :code:`tracer(N)` method is used to control how many times the Turtle is actually
drawn on the screen. This method belongs to the :code:`TurtleScreen` object, and effects
all turtles that are on the screen. The :code:`N` in the method represents the input,
only allowing the :code:`TurtleScreen` to display one frame out every :code:`N`.

.. core-block:: cpp

    screen.tracer(12);
    //Show one out of every 12 frames of animation.

This can be combined with the :code:`speed` method available to turtles to achieve **very** quickly
drawn images. The maximum speed a Turtle can have, :code:`TS_FASTEST`, completely disables animation
for Turtles between movements and rotations. This allows the :code:`tracer` setting to directly relate
to the total number of actions the turtle makes. The actions the turtle takes happen regardless
of whether or not they are actually shown on the screen.

.. code-block:: cpp

    screen.tracer(3); //Show one out of every 3 frames of animation.
    turtle.speed(ct::TS_FASTEST);  //Disables Turtle animation

    turtle.forward(50);//This is not shown on-screen...
    turtle.right(90);//Neither is this...
    turtle.forward(50);//But this action is, because it is third out of three.

A frame of animation is added for almost every action a turtle takes, regardless of whether or not
the turtle is moving or adding something to the screen. This includes methods like
:code:`begin_fill` and :code:`end_fill`, which don't do anything visually but do
tell the turtle to start or stop tracking its own movements.

Consider the following example and related questions.

.. code-block:: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;
    
    int main(){
        ct::TurtleScreen screen;
        ct::Turtle turtle(screen);

        turtle.speed(ct::TS_FASTEST);
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
of actions it is performing over a period of time. The queue is only allowed to grow to a certain size, starting at 100 actions total.
This is modifiable through the :code:`setundobuffer` method that belongs to turtles. Every action is added, even if
the action doesn't change anything visually. This feature is comparable to the "undo" tool available in most text editors.
Turtles can "undo" their progress with the :code:`undo` method.

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
