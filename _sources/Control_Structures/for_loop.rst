For Loops
=========

Even though the ``while`` type of construct is very useful in a wide variety of
situations, another iterative structure, the ``for`` statement, can be
used to iterate across a range of values easily.
A ``for`` statement allows us to write a loop that is executed a specific number of times.

.. activecode:: ForLoopIterations
   :language: cpp
   :sourcefile: ForLoopIterations.cpp

   #include <iostream>
   using namespace std;

   int main() {
      for (int i = 0; i < 10; i++){
            cout << i << "hello world" << endl;
       }
    }



In the example above, the **hello world** statement is executed 10 times.

A common use of the ``for`` construct is to implement **certain** repetition  
over a range of values.

.. activecode:: rangeForLoop1
   :language: cpp

   #include <iostream>
   using namespace std;

    // squares the numebers in range 5
    // ex. 0*0, 1*1, 2*2 ...
    int main() {
        for (int i=0; i<5; i++) {
            cout << i*i << " ";
        }

        return 0;
    }


The code will use ``cout`` five times.  The value of the variable ``i`` will
start at 0 and go through the full sequence of values 0,1,2,3,4.  This
value is then squared and printed.


Check yourself
==============

::

    #include <iostream>
    using namespace std;

    int main() {

        for (int counter=0; counter<4; counter++) {
            cout << counter * 2 << " ";
        }

        return 0;
    }

.. mchoice:: mc_forloop
  :answer_a: 0 2 4 6
  :answer_b: 0 0 0 0
  :answer_c: Runtime error
  :answer_d: 0 1 2 3
  :answer_e: all of the above
  :correct: a
  :feedback_a: Good Job!
  :feedback_b: Not quite, take another look at the operation happening in the cout line
  :feedback_c: Not quite, take another look at the for loop
  :feedback_d: Not quite, take another look at the operation happening in the cout line

  Using the code above please select the answer that should appear?
