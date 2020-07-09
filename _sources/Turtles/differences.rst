Python Turtles vs C++ Turtles
==========================================

CTurtle varies from Python turtles primarily in syntax. Most of the methods are exactly the same between implementations,
however there are a few notable differences between the two. Colors, for example, must be surrounded by curly brackets (e.g,
'{' and '}') when referring to them by a name such as "red", "green", or "blue". You can also ask for a random color by
using the string "random".

.. code-block:: cpp

    ct::Color red   = {"red"};
    ct::Color green = {"green"};
    ct::Color blue  = {"blue"};
    ct::Color random = {"random"};

    //This works...
    turtle.pencolor(red);

    //And so do these.
    turtle.pencolor({"green"});
    turtle.pencolor({"random"});

In Python, we can use the :code:`write` method to specify a font or size. This is not possible in C++ due to the complex 
handling of fonts by operating systems. Furthermore, there is no "world" screen mode like there is in Python. Normally, 
this would allow you to specify the "bounds" of your canvas (e.g, specify minimum and maximum coordinates for your canvas).

Default shapes are also different and somewhat limited in comparison. Python offers six shapes by default, being "arrow", "circle",
"turtle", "square", "triangle", and "classic". CTurtle, on the other hand, offers four shapes by default: "arrow", "triangle",
"indented triangle", and "square".

There are a few utility methods available in CTurtle that are not available in Python, such as :code:`shift` and :code:`middle`.
The former of the two, :code:`shift`, simply adds to the X and Y coordinate position of the turtle. If your turtle is at coordinate
600x, 400y and :code:`shift` is called with coordinate 50x and -50y, the turtle's final position would be 650x, 350y. The latter
of the two, :code:`middle`, returns the point exactly between two other points. See the examples below.

.. code-block:: cpp

    turtle.goTo(600, 400);
    turtle.shift(50, -50);
    //Turtle position is now 650x, 350y.

.. code-block:: cpp

    ct::Point a = {400, 300};
    ct::Point b = {450, 300};

    //Should equal the point 425x, 300y.
    ct::Point middle = ct::middle(a, b);

.. admonition:: Self Check

   .. mchoice:: question_cturtle_1
       :correct: c
       :answer_a: turtle.pencolor{(red)};
       :answer_b: turtle.fillcolor({“red”}};
       :answer_c: turtle.pencolor({“red”});
       :answer_d: turtle.fillcolor(“red”);
       :feedback_a: This answer is close, but check your syntax closely.
       :feedback_b: Almost! We need to change our pencolor, not the turtle's color.
       :feedback_c: Correct!
       :feedback_d: Try again!

       Which of the following answers would result in our turtle’s pen changing to the color red?

.. dragndrop:: cturtle_matching
   :match_1: turtle.goto(400, 250) 
             turtle.shift(25, -50)|||(425, 200)
   :match_2: turtle.goto(275, 130) 
             turtle.shift(15, 20)|||(290, 150)
   :match_3: turtle.goto(325, 305) 
             turtle.shift(-100, -75)|||(225, 230)
   :match_4: turtle.goto(130, 280) 
             turtle.shift(-50, -130)|||(80, 150)
   :match_5: turtle.goto(512, 1024) 
             turtle.shift(-12, -24)|||(500, 1000)
   :match_6: turtle.goto(245, 40) 
             turtle.shift(55, -40)|||(300, 0)
   :match_7: turtle.goto(100, 75) 
             turtle.shift(75, -50)|||(175, 25)
   :match_8: turtle.goto(525, 210) 
             turtle.shift(25, -20)|||(550, 190)