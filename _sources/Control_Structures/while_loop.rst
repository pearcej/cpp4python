While Loops
============
 As we noted earlier, algorithms require two important control
structures: iteration and selection. Both of these are supported by
Python in various forms. The programmer can choose the statement that is
most useful for the given circumstance.

For iteration, C++ provides a standard ``while`` statement and a very
powerful ``for`` statement. The while statement repeats a body of code
as long as a condition is true. For example,

::

    int counter = 1;
    while (counter <= 5) {          /*Use of an interactive method until the
                                     the loop ends   */
        cout<<"Hello, world"<<endl;
        counter = counter + 1;
    }

    Console output:
    Hello, world
    Hello, world
    Hello, world
    Hello, world
    Hello, world

prints out the phrase “Hello, world” five times. The condition on the
``while`` statement is evaluated at the start of each repetition. If the
condition is ``true``, the body of the statement will execute.

The ``while`` statement is a very general purpose iterative structure
that we will use in a number of different algorithms. In many cases, a
compound condition will control the iteration. A fragment such as

::

    while (counter <= 10 && not done) {
    ...

would cause the body of the statement to be executed only in the case
where both parts of the condition are satisfied due to the and operator (``&&``). The value of the
variable ``counter`` would need to be less than or equal to 10 and the
value of the variable ``done`` would need to be ``false`` (``not false``
is ``true``) so that ``true and true`` results in ``true``.

Here are some of the logical operators that are useful for true-false boolean statements in C++.

::

    and          - &&

    or           - ||

    not equal to - !=

    not          - !

    greater than - >

    less than    - <

    greater than
    or equal to  - >=

    less than
    or equal to  - <=
