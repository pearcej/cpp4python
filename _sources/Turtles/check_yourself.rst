Check Yourself
==============

.. activecode:: turtle_checkyourself_ac_1
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);

        turtle.begin_fill();

        for(int i = 0; i < 4; i++){
            turtle.forward(50);
            turtle.right(90);
        }

        turtle.end_fill();

        scr.bye();
        return 0;
    }

.. mchoice:: turtle_checkyourself_mchoice_1
   :answer_a: 13
   :answer_b: 10
   :answer_c: 8
   :answer_d: 4
   :correct: b
   :feedback_a: No, think about how many times fill is used...
   :feedback_b: Correct!
   :feedback_c: Incorrect! Consider that almost everything a turtle does is an action, even filling.
   :feedback_d: Incorrect! Consider that there are some actions in a for loop.

   How large would the undo queue be for the above code example?

.. code-block:: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);

        for(int i = 0; i < 5; i++){
            turtle.forward(50);
            turtle.right(144);
        }

        scr.bye();
        return 0;
    }

.. mchoice:: turtle_checkyourself_mchoice_2
   :answer_a: Circle
   :answer_b: No shape
   :answer_c: Pentagon
   :answer_d: Star
   :correct: d
   :feedback_a: Incorrect! Consider how many times the for-loop iterates...
   :feedback_b: Incorrect! The turtle's pen is always down.
   :feedback_c: Incorrect! Consider the angle the turtle turns every iteration.
   :feedback_d: Correct!

   What kind of shape does the above activecode create?

.. mchoice:: turtle_checkyourself_mchoice_3
  :answer_a: True
  :answer_b: False
  :correct: a
  :feedback_a: Correct!
  :feedback_b: Incorrect!

  You can have more than one turtle on one screen.
