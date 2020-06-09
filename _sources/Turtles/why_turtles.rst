Introduction to Turtles in C++
=======================================

Python is particularly well-suited for educational purposes due to its
wide array of built in tools and good documentation. These things are particularly
lacking in regards to C++, as many of the built-in tools require complicated syntax
and deep understanding of the language itself. One of these tools is Turtles,
which is very well suited for educational purposes because it offers live, interactive,
and visual representations of your code as you write it.

Visual representations afford students an opportunity to observe a facet of computer science
from a point of view that makes sense: rather than waiting anxiously for the print statement
to come around after your program churns, you get a visual representation of the concept itself.
This is particularly useful for abstract concepts such as recursion and iteration.

For C++, a library titled C-Turtle is used to provide an equivalent of Python's Turtles.
It acts as a close replacement to provide easy to use graphics to C++, while maintaining
the objects and commands you might be used to in Python. It was developed by Jesse Walker
at Berea College during the summer of 2019.

Below is a side-by-side comparison of the two versions, which do the same thing.

.. tabbed:: cturtle_compare_1

    .. tab:: C++

        .. activecode:: cturtle_1
            :language: cpp

            #include <CTurtle.hpp>
            namespace ct = cturtle;

            int main(int argc, char** argv) {
                ct::TurtleScreen scr;
                ct::Turtle turtle(scr);
                turtle.speed(ct::TS_SLOWEST);
                turtle.fillcolor({"purple"});
                turtle.begin_fill();
                for (int i = 0; i < 4; i++) {
                    turtle.forward(50);
                    turtle.right(90);
                }
                turtle.end_fill();
                scr.bye();
                return 0;
            }

    .. tab:: Python

        .. activecode:: cturtle_python_1
            :language: python

            import turtle

            turt = turtle.Turtle()
            turt.fillcolor("purple")
            turt.speed("slowest")

            turt.begin_fill()
            for i in range(4):
                turt.forward(50)
                turt.right(90)
            turt.end_fill()
            turt.bye()

.. mchoice:: cturtle_question_1
    :answer_a: Students receive instant feedback and gratification for their work.
    :answer_b: Students will pay less attention to how their code works, and more attention to its end result.
    :answer_c: Students get more acquainted with RGB values common in web development.
    :answer_d: Students will be more comfortable working with concepts they are used to, such as Turtles.
    :correct: a, d
    :feedback_a: Correct!
    :feedback_b: Incorrect, because equal thought must be put into the usage of Turtles as well as the outcome.
    :feedback_c: Incorrect, because RGB values are not the focus or reason behind using Turtles.
    :feedback_d: Correct!

    How might students benefit from having a visual representation such as C-Turtle? Check all that apply.