Conditionals
============

Conditional statements in Python and C++ are very similar. In Python we
have three patterns:

Simple if
------------------
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
are required because ``if`` is technically a function that evaluates to ``true``
or ``false``.

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

.. activecode :: pyelif
    :language: python

    grade = int(input('enter a grade'))

    if grade < 60:  /* if, elif, and else statement allows for
                     multiple options according to the value of grade */
        print('F')
    elif grade < 70:
        print('D')
    elif grade < 80:
        print('C')
    elif grade < 90:
        print('B')
    else:
        print('A')

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

                  return 0;
              }
          }
      }
    }

We can get even closer to the elif statement by taking advantage of the
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

switch
------------------


C++ also supports a ``switch`` statement that acts something like the
elif statement of Python under certain conditions because the statement takes cases and checks the validity of the case against the code. To write the grade
program using a switch statement we would use the following:

.. activecode:: cppswitch
   :language: cpp
   :sourcefile: switchup.cpp

    #include <iostream>
    using namespace std;

    int main() {

      int grade = 80;

      int tempgrade = grade / 10;
      switch(tempgrade) {  /*switch cases allow for different options based on
                           the value of temp grade similar to if statements*/
      case 1:
          cout<<"The tempgrade is 1" <<endl;
          break;
      case 3:
          cout<<"The tempgrade is 3"<<endl;
          break;
      case 5:
          cout<<"The tempgrade is 5"<<endl;
          break;
      case 8:
          cout<<"The tempgrade is 8"<<endl;
          break;
      default:
          cout<<"Tempgrade for this case is not available"<<endl;
      }

      return 0;
    }

Frankly, the ``switch`` statement is not used very often.
It is not as powerful as the ``else if`` model
because the switch variable can only be compared for equality with an
integer or something called an enumerated constant.
Second it is very easy to forget to put
in the ``break`` statement.
If the break statement is left out then then
the next alternative will be automatically executed.
For example if the
grade was 95 and the ``break`` was omitted from the ``case 9:``
alternative then the program would print out both (A and B.)
So, you might want to just avoid it and use if...
