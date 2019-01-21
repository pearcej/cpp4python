..  Copyright (C)  Jan Pearce and Brad Miller
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Operator Overloading
--------------------

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
