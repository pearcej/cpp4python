Conditionals
============

Conditional statements in Python and C++ are very similar. In Python we
have three patterns:

Simple if
---------

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
are required because if is technically a function that evaluates to True
or False.

if else
-------

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
----

C++ does not have an elif pattern like Python. In C++ you can get the
functionality of an elif statement by nesting if and else. Here is a
simple example in both Python and C++.

.. activecode :: pyelif
    :language: python

    grade = int(input('enter a grade'))
    if grade < 60:
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

.. activecode:: C++elif
   :language: C++
   :sourcefile: ElseIf.cpp

    #include <iostream>
    using namespace std;

    int main() {
      int grade = 85;

      if (grade < 60) {
          cout<<'F'<< endl;
      } else {
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

.. activecode:: C++elif2
   :language: C++
   :sourcefile: ElseIf.cpp

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
------

C++ also supports a ``switch`` statement that acts something like the
elif statement of Python under certain conditions because the statement takes cases and checks the validity of the case against the code. To write the grade
program using a switch statement we would use the following:

.. activecode:: C++switch
   :language: C++
   :sourcefile: SwitchUp.cpp

    #include <iostream>
    using namespace std;

    int main() {

      int grade = 85;

      int tempgrade = grade / 10;
      switch(tempgrade) {
      case 10:
      case 9:
          cout<<'A'<<endl;
          break;
      case 8:
          cout<<'B'<<endl;
          break;
      case 7:
          cout<<'C'<<endl;
          break;
      case 6:
          cout<<'A'<<endl;
          break;
      default:
          cout<<'F'<<endl;
      }

      return 0;
    }

The ``switch`` statement is not used very often, and I recommend you do
not use it! First, it is not as powerful as the ``else if`` model
because the switch variable can only be compared for equality with an
integer or enumerated constant. Second it is very easy to forget to put
in the ``break`` statement. If the break statement is left out then then
the next alternative will be automatically executed. For example if the
grade was 95 and the ``break`` was omitted from the ``case 9:``
alternative then the program would print out both (A and B.)

Boolean Operators
-----------------

{sub:boolean\_operators}

The conditionals used in the if statement can be boolean variables,
simple comparisons, and compound boolean expressions.

C++ also supports the boolean expression.
``condition ? trueValue : falseValue`` This expression can be used to
test a condition as part of an assignment statement. For example
``a = a % 2 == 0 ? a*a : 3*x -1`` In the previous assignment statement
the expression ``a%2 ==0`` is first checked. If it is true then a is
assigned the value ``a * a`` if it is false then a is assigned the value
of ``3*x-1``. Of course all of this could have been accomplished using a
regular if else statement, but sometimes the convenience of a single
statement is too much to resist.
