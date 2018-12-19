..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Defining Functions
------------------

In general, we can hide the details of any computation by defining
a function. A function definition requires a name, a group of
parameters, a return type, and a body. It may either return a variable, value, or nothing (specified by the keyword void). For
example, the simple function defined below returns the double of the
value you pass into it.

::

    int timesTwo(int num) {
        return num*2;
    }

The syntax for this function definition includes the name, ``timesTwo``,
and a parenthesized list of formal parameters and their types. For this function an ``int`` named ``num``
is the only formal parameter, which suggests that ``timesTwo`` needs only
one piece of data to do its work. The details, hidden “inside the box,”
simply compute the result of ``num*2`` and return it. We can invoke or
call the ``timesTwo`` function by asking the C++ to
evaluate it, passing an actual parameter value, in this case, ``3``.
Note that the call to ``timesTwo`` returns an integer that can in turn be
passed to another invocation.


.. _lst_timesTwo:

  .. activecode:: timesTwo
    :language: cpp
    :caption: Implementation of the timesTwo function

    #include <iostream>
    using namespace std;

    int timesTwo(int num) {
        return num*2;
    }

    int main() {
        cout<<timesTwo(5)<<endl;

        return 0;
    }

We could go a step further and implement our own square root function by using a well-known
technique called “Newton’s Method.” Newton’s Method for approximating
square roots performs an iterative computation that converges on the
correct value. The equation
:math:`newguess = \frac {1}{2} * (oldguess + \frac {n}{oldguess})`
takes a value :math:`n` and repeatedly guesses the square root by
making each :math:`newguess` the :math:`oldguess` in the subsequent
iteration. The initial guess used here is :math:`\frac {n}{2}`.
:ref:`Listing 1 <lst_root>` shows a function definition that accepts a value
:math:`n` and returns the square root of :math:`n` after making 20
guesses. Again, the details of Newton’s Method are hidden inside the
function definition and the user does not have to know anything about
the implementation to use the function for its intended purpose.
:ref:`Listing 1 <lst_root>` also shows the use of the // characters as a comment
marker. Any characters that follow the // on a line are ignored.




.. _lst_root:

**Listing 1**

.. activecode:: newtonsmethod
  :language: cpp
  :caption: Newton's Method for finding Square Root

  #include <iostream>
  using namespace std;

  double squareroot(double n) {
  	double root = n / 2;

  	for (int i = 0; i < 20; i++) {
  		root = (.5) * (root + (n / root));
  	}

  	return root;
  }

  int main() {
  	cout << squareroot(9) << endl;
  	cout << squareroot(4563) << endl;

  	return 0;
  }

Functions that Pass by Value versus Pass By Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In all of the functions we have written thus far, we have used a function calling mechanism called **pass by value**. The memory location that stores the values of the arguments when a function is called is different from the location referenced by the function parameters. Calling a function by value involves copying the contents of the arguments into the memory locations of the corresponding formal parameters. If the function changes the values in the parameters, the contents in memory referenced by the arguments of the calling function do not change.

Consider the following two function definitions:

::

    void functionExample( int inputVar ) {
        int nextVar = inputVar * 2;
        inputVar = 4;

        cout << "nextVar = " << nextVar << " inputVar = " << inputVar;
    }

    void callingFunction() {
        int myVar = 10;

        functionExample( myVar );
        cout << "myVar = " << myVar;
    }

When the function ``callingFunction()`` executes, it calls ``functionExample(...)`` with the variable *myVar* having the value 10. Within ``functionExample(...)``, the value of 10 is copied from *myVar* to the formal parameter *inputVar*, so the value of *nextVar* is 10x2, or 20. The next statement changes the contents of *inputVar* to 4, so the ``cout`` statement within this function produces the output:

::

    nextVar = 20 inputVar = 4

Notice what happens when ``functionExample(...)`` ends and execution returns to ``callingFunction()``. The contents of *myVar* is **still the same**, as the location for *myVar* differs from where *inputVar* is stored. Thus, *myVar* still has the value 10, and the ``cout`` statement after the function call will produce the output:

::

    myVar = 10

In other words, any changes to the variables are local to the function, which is exactly what we want.

--------------

However, there is a problem.

We have seen examples of C++ functions that return no value or a single value. How about when we want the function to return **more** than one value? We need another function calling mechanism called **pass by reference**. When using this mechanism, the actual location in memory referenced by the arguments are sent rather than the values in that location. To let the compiler know that you intend to use pass by reference, you attach an "&" to the end of the type name in the formal parameter list in the function declaration and header. When you do this, any changes to the values of the parameters will change the value of the arguments as well.

An example of a function where this is useful is a function that takes two values as input and swaps their order. Consider the following program fragment of a function called ``swap_values(...)`` that swaps its two inputs and the ``main()`` function that calls ``swap_values(...)``.

.. _lst_swap_inputs:

    .. activecode:: activepassrefcpp
        :caption: Pass by Reference
        :language: cpp

        #include <iostream>
        using namespace std;

        // swap_values() function definition
        // Interchanges the values located by variable1 and variable2.

        void swap_values(int &variable1, int &variable2);

        // Notice that this function does not return anything!
        void swap_values(int &variable1, int &variable2) {
            int temp; 		// temporary storage for swap

            temp = variable1;
            variable1 = variable2;
            variable2 = temp;
        }

        int main( ) {
            int first_num, second_num;
            first_num = 7;
            second_num = 8;

            cout << "Two numbers before swap function: 1) " << first_num << " 2) " << second_num << endl;
            swap_values(first_num, second_num);
            cout << "The numbers after swap function: 1) " << first_num << " 2) " << second_num;

            return 0;
        }


For this program :ref:`Swap Inputs <lst_swap_inputs>` to reverse the order of the integers the users types in, the function ``swap_values(...)`` must be able to change the values of the arguments. Try removing one or both of the "&" 's in this code to see what happens.

-----------------------------------------------------------------

Arrays as Parameters in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions can be used with **array parameters** to maintain a structured design. However, a formal parameter for an array is neither a call-by-value nor a call-by-reference, but a new type of parameter pass called an array parameter. In a function definition, an array parameter looks like a pass-by-value parameter because there is no ampersand symbol (&), but the variable name is instead followed by a set of square brackets ([ and ]).

The following example function returns the average hours worked over the array of integers (note that we need to also pass in the number of elements in that array because the array parameter *list[]* does not include that information):

::

    double average( int list[], int length ) {	// It is correct     syntax to omit the array length on the array itself.
        double total = 0;
        int count;
        for( count = 0; count < length; count++ )
            total += double(list[count]);
        return (total / length);
    }

Array parameters look like pass by value, but they are effectively like call by reference parameters. When they execute, the functions with these parameters do not make private copies of the arrays they are passed because doing so this could potentially be very expensive in terms of memory. Arrays can therefore always be permanently changed when passed as arguments to functions.

After a call to the following function, each element in the third array argument is equal to the sum of the corresponding two elements in the first and second arguments:

::

    void add_lists( int first[], int second[], int total[], int length ) {
        int count;
        for( count = 0; count < length; count++ )
            total[count] = first[count] + second[count];
    }

Upon further examination, we can see that the first two arrays do not change values. To prevent ourselves from accidentally modifying any of these arrays, we can add the modifier ``const`` in the function head:

::

    void add_lists( const int first[], const int second[], int total[], int length ) {
        int count;
        for( count = 0; count < length; count++ )
            total[count] = first[count] + second[count];
    }

These changes would ensure that the compiler will then not accept any statements within the function's definition that potentially modify the elements of the arrays *first* or *second*.

Operator Overloading
^^^^^^^^^^^^^^^^^^^^

Defining a new meaning for an already existing operator (such as the arithmetic operators plus "+" or times "*") is called overloading the operator. Such overloading is easy to do in C++ with the correctly structured declaration, using the following prototype:
type operator symbol(s)( parameters );

Operators such as (+, -, \*, /, %, ==, <, >, <=, >=, etc.) are really just C++ functions that use a special syntax for listing the function arguments.

Let's consider an example of  a class called Money which will allow input and output in the form:  $123.45

Note that the input includes both the dollar sign and the decimal point.  Wouldn't it be nice to be able to have a main program which works with Money just as it it were a more simple data type?  Maybe with something as follows:


.. raw :: html

    <div>
    <iframe height="700px" width="100%" src="https://repl.it/@Dostonbek1/StainedOffensiveTechnology?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    </div>

Let's look at the overloaded operator we use in this example.  The most complicated of the bunch is the overloaded instream operator, which is a friend of the class:

::

    istream& operator >>(istream& ins, Money& amount)
    {
        char one_char, decimal_point,
            digit1, digit2; //digits for the amount of cents
        long dollars;
        int cents;

        ins >> one_char; //if input is legal, then one_char == '$' and we do not store it
        ins >> dollars >> decimal_point >> digit1 >> digit2;

        if ( one_char != '$' || decimal_point != '.' || !isdigit(digit1) || !isdigit(digit2) )
        {
            cout << "Error illegal form for money input.\n";
            exit(1);
        }

        cents = digit_to_int(digit1)*10 + digit_to_int(digit2);//Here we convert the cents
        amount.all_cents = dollars*100 + cents;  //Here we convert the money to all cents and store in the private member variable
                                                 //We need this operator to be a friend so it can access this member variable.
        return ins;
      }

Overloaded stream operators always have the stream both as a call-by-reference input as well as send-by-reference output.  This may seem weird, but the issue is that reading or writing a stream changes it.  The structure used the above example  will work BOTH for reading from the keyboard as well as from a file!

The overloaded outstream operator is also a friend, but is a bit simpler.  It can also be used as is to write to the screen or to a file!

::

    ostream& operator <<(ostream& outs, const Money& amount)
    {
        long positive_cents, dollars, cents;
        positive_cents = amount.all_cents;
        dollars = positive_cents/100;
        cents = positive_cents%100;

        outs << "$" << dollars << '.';

        if (cents < 10)
            outs << '0';
        outs << cents;

        return outs;
    }

Once the Money is stored in the private member variable as all_cents, the boolean comparison, which is also a friend, is very simple:

::

    bool operator ==(const Money& amount1, const Money& amount2)
    {
        return (amount1.all_cents == amount2.all_cents);
    }


**General Rules**

1. Only existing operator symbols may be overloaded. New symbols that are not builtin, such as \*\*, cannot be used.
2. The operators ::, #, ., and ? are reserved and cannot be overloaded.
3. Some operators such as =, [], () and -> can only be overloaded as member functions of a class and not as global functions.
4. At least one operand for any overload must be a class or enumeration type. In other words, it is not possible to overload operators involving only built-in data types. For example, trying to overload the addition operator for the int data type would result in a compiler error:

    `int operator +( int i, int j );  // This is not allowed`

5. The number of operands for an operator may not be changed.
6. Operator precedence cannot be changed by overloading.


It is a good idea to match the overloaded operator implementation with the original meaning, even though mismatching is possible. In other words, it would be confusing if the `+` operator is overloaded to subtract values or if the ``<<`` operator gets input from the stream.

In addition to being defined in within the class scope, overloaded operators may be defined in global or namespace scope or as friends of the class. Global scope means that the operator is defined outside of any function (including the main) or class. Namespace scope means that the operator is defined outside of any class but within a namespace, possibly within the main program.

One reason for declaring overloaded operators as friends of a class is that sometimes the operator is intimately related to a class but cannot be declared as a member of that class.

.. admonition:: Self Check

   Here's a self check that really covers everything so far.  You may have
   heard of the infinite monkey theorem?  The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare.  Well, suppose we replace a monkey with a C++ function.  How long do you think it would take for a C++ function to generate just one sentence of Shakespeare?  The sentence we'll shoot for is:  "methinks it is like a weasel"

   You're not going to want to run this one in the browser, so fire up your favorite C++ IDE.  The way we'll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space.  We'll write another function that will score each generated string by comparing the randomly generated string to the goal.

   A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.  If the letters are not correct then we will generate a whole new string. To make it easier to follow your program's progress this third function should print out the best string generated so far and its score every 1000 tries.


.. admonition:: Self Check Challenge

    See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far.  This is a type of algorithm in the class of 'hill climbing' algorithms, that is we only keep the result if it is better than the previous one.
