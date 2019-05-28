Conditionals
============

Conditional statements in Python and C++ are very similar.

Simple if
---------
In Python, we write a simple if statement in the following way:

::

    if condition:
        statement1
        statement2
        ...

In C++ this same pattern is simply written as:

::

    if (condition) {
        statement1
        statement2
        ...
    }

Once again you can see that in C++ the curly braces define a block
rather than indentation. In C++ the parenthesis around the condition
are required because ``if`` is technically a function that
evaluates to ``true`` or ``false``.

if else
-------
The if-else statement in Python looks like this:

::

    if condition:
        statement1
        statement2
        ...
    else:
        statement1
        statement2
        ...

In C++ this is written as:

::

    if (condition) {
        statement1
        statement2
        ...
    } else {
        statement1
        statement2
        ...
    }

elif
------------------

C++ does not have an elif pattern like Python. In C++ you can get the
functionality of an elif statement by nesting if and else. Here is a
simple example in both Python and C++.


.. activecode:: pyelif
    :language: python

    def main():
        grade = 85

        if (grade < 60):
            print('F')
        elif (grade < 70):
            print('D')
        elif grade < 80:
            print('C')
        elif grade < 90:
            print('B')
        else:
            print('A')

    main()


In C++ we have a couple of ways to write this

.. activecode:: cppelif
   :language: cpp
   :sourcefile: elseif.cpp

    #include <iostream>
    using namespace std;

    int main() {

      int grade = 85;

      if (grade < 60) {
          cout<<'F'<< endl;
      } else {      /* if, elif, and else statement can be used
                        inside of themselves to allow for sub options */
          if (grade < 70) {
              cout<<'D'<< endl;
          } else {
              if (grade < 80) {
                  cout<<'C'<< endl;
              } else {
                  if (grade < 90) {
                      cout<<'B'<< endl;
                  } else {
                      cout<<'A'<< endl;
                  }
              }
           }
      }
      return 0;
    }


We can get closer to the look of the elif statement in C++ by
taking advantage of the
C++ rule that a single statement does not need to be enclosed in curly
braces. Since the if is the only statement used in each else we can get
away with the following.


.. activecode:: cppelif2
   :language: cpp
   :sourcefile: elseif2.cpp

    #include <iostream>
    using namespace std;

    int main() {

      int grade = 85;

      if (grade < 60) {
          cout<<'F'<<endl;
      } else if (grade < 70) {
          cout<<'D'<<endl;
      } else if (grade < 80) {
          cout<<'C'<<endl;
      } else if (grade < 90) {
          cout<<'B'<<endl;
      } else  cout<<'A'<<endl;

      return 0;
    }

Check Yourself
~~~~~~~~~~~~~~

.. mchoice:: mc_cpp_elsecond
   :answer_a: True
   :answer_b: False 
   :correct: b
   :feedback_a: Not quite, try modifying the code above to test it out.
   :feedback_b: Good job!

   T/F: Is is necessary to have an else statement after an if statement? (Hint: Test it out in the code above)

switch
------


C++ also supports a ``switch`` statement that acts something like the
elif statement of Python under certain conditions because the statement
takes cases and checks the validity of the case against the code.
It uses cases instead of conditions and the case must be based on
integers or a user-defined data type called an enumerated constant.

To write the grade
program using a switch statement we would use the following:

.. activecode:: cppswitch
   :language: cpp
   :sourcefile: switchup.cpp

    #include <iostream>
    using namespace std;

    int main() {

      int grade = 85;

      int tempgrade = grade/10;
      switch(tempgrade) {  /*switch cases allow for different options based on
                           the value of temp grade similar to if statements*/
      case 10:
      case 9:
          cout << "The grade is A" << endl;
          break;
      case 8:
          cout << "The grade is B" << endl;
          break;
      case 7:
          cout << "The grade is C" << endl;
          break;
      case 6:
          cout << "The grade is D" << endl;
          break;
      default:
          cout << "The grade is F" << endl;
      }

      return 0;
    }

Frankly, the ``switch`` statement is not used very often.
It is not as powerful as the ``else if`` model
because the switch variable can only be compared for equality with an
integer or something called an enumerated constant.
Second it is very easy to forget to put
in the ``break`` statement. Note above how cases 10 and 9 are coded together.
If the break statement is left out then then
the next alternative will be automatically executed.
For example if the
grade was 95 and the ``break`` was omitted from the ``case 9:``
alternative then the program would print out both (A and B.)
So, you might want to just avoid it and use if...

Check Yourself
~~~~~~~~~~~~~~

.. mchoice:: mc_cpp_ifcond
   :answer_a: { }
   :answer_b: [ ]
   :answer_c: ( )
   :answer_d: Any set of matching braces may be used.
   :answer_e: none of the above
   :correct: c
   :feedback_a: No. Try again.
   :feedback_b: No. Try again.
   :feedback_c: Right!
   :feedback_d: No. Try again.
   :feedback_e: One of the above is indeed correct.

   When indicating the condition for a C++ if statement, what symbols are used?


.. mchoice:: mc_cpp_switch
  :answer_a: Ending statements with ;
  :answer_b: Using break
  :answer_c: Enclosing each cases with { }
  :answer_d: Setting a default case
  :correct: c
  :feedback_a: No. This is always needed.
  :feedback_b: Good job!
  :feedback_c: No. Try again.
  :feedback_d: No. This is a good idea, but it will not help.

  When using a switch, what prevents all the cases from passing as correct?


.. mchoice:: mc_cpp_and
  :answer_a: ||
  :answer_b: and
  :answer_c: !
  :answer_d: &&
  :correct: d
  :feedback_a: No, this means "or".
  :feedback_b: No, this is Python.
  :feedback_c: No, this means "not"
  :feedback_d: Very good!

  What symbol is used to indicate the “and” in C++ such as in a compound condition?
