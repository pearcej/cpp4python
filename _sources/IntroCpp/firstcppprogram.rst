Let's look at a C++ program
===========================

A time honored tradition in computer science is to write a program
called “hello world.” The “hello world” program is simple and easy.
No logic errors are possible to make, so getting it to run relies only on
understanding the syntax. Let's look at an easy version of "hello world"
in Python:

.. activecode:: hellopysimp
  :language: python

  print("Hello World!")

Now, lets look at a more “complicated” version of the "hello world" program with a
``main`` function in Python:

.. activecode:: hellopymain
  :language: python

  def main():
      print("Hello World!")
  main()

Next, lets look at the same program written in C++:

.. activecode:: hellocppstd
    :language: cpp

    #include <iostream>

    int main(){

        std::cout << "Hello World!\n";
        return 0;
    }

The above program can alternatively be written as follows to allow
better facilitate standard input and output:

.. activecode:: hellocppnamespace
    :language: cpp

    #include <iostream>
    using namespace std;

    int main(){
        cout << "Hello World!\n";
        return 0;
    }

What we see is that at the core there are a few similarities with the
complicated Python version, such as the ``main`` function and the
string “Hello world”. However, in C++ there is a lot more
stuff around the edges that make it harder to see the core of the program.
Do not worry! An important skill for a computer scientist is to learn what
to ignore and what to look at carefully. You will soon find that there
are some elements of C++ that will fade into the background as you
become used to seeing them. One thing that will help you is to learn a
little bit more about C++.

Compilation
-----------

A question you may have about this little program is “How would I run it on 
my own machine?” Running a C++ program is not as simple as running a
Python program. The first big difference between C++ and Python is that
Python is an *interpreted language* while C++ is a *compliled language*. 
We could run our Python programs in
the Python **interpreter**, and we were often quite happy to do that.
In C++, running programs is a two step process. 

First, we must type the hello world program into a file and save that file
using a name like ``hello.cpp`` Once we have saved the file we **compile**
it either from the command line or from an integrated development environment (IDE).
Only after the program is compiled, can we run it.

Now you may be wondering what good is this extra step? What does
compiling do for us? There are a couple of important benefits we get
from compiling:

-  Early detection of errors

-  Faster program execution

The job of the compiler is to turn your C++ code into language that your
machine can understand. We call the code that the computer
understands **machine code**. The computer interprets the machine code
much like the Python interpreter interprets your Python.
However, since machine code is much closer to the native language of the
computer, it can run faster.

When the compiler does the translation it can find many different kinds
of errors. For example if you make a typo or forget to declare a variable
the compiler will find these and point them out to you before you ever
run the program. We will look at some examples of  errors that the compiler
catches shortly. Chances are you may create some on your own very soon too,
but first let's talk about each of the statements in a C++ program.


Using headers and libraries
---------------------------

Preprocessor directives in C++ appear as statements preceded by the hash sign ``#``.
These tell the preprocessor which file, header or library to make available to
the compiler. For example, ``#include <iostream>`` will make sure that
the ``iostream`` library is available at compile time.
Here, the term *header* is used for a type of C++ file that contains definitions
of functions and variables, but not the function implementations.

You can think of the ``#include ...`` statement in C++ as working a bit like
the ``import ...`` statement in Python.
Python's ``import`` statement directly accesses the code written in another file
while the ``#include`` statement in C++ copies classes and functions from
another file.

In Python, an import statement looks like:

::

  import classname

There are two ways to use ``#include`` in C++:

::

  #include <libraryname>
  #include "filename"

Here the angle-brackets ``<>`` are used to include libraries or headers provided by
the implementation, such as the
headers in the standard library (``iostream``, ``string``, etc.). The double
quotes ``"`` are used for headers and files not provided by the implementation.

The main function
-----------------

Unlike Python, every C++ program **must** have a ``main`` function which begins
with ``int main()``. This ``main`` function is called implicitly instead of
explicitly like we must do in Python when we have a main function. This is
why you do not see an explicit function call invoking main.

The ``int``  in ``int main()`` indicates that the *return type* of the ``main`` function will be
an integer. The final line of the ``main`` C++ function is typically ``return 0``,
so you can see that the program does actually return the integer 0.
Here zero is returned to indicate successful completion of the ``main``
function. In case you are wondering why an integer is returned, if you do error
handling in C++, instead of 0, you can alternatively return an integer error code representing
a specific error when and where it occurs.

C++ functions and other C++ code blocks are grouped together using the curly ``{}``
brackets. These curly brackets are used much like tabbing is used in Python.
Many people also use tabbing in C++ to indicate blocks, but tabs and other
whitespace (mostly) have no inherent meaning in C++.
Instead, the semi-colon (``;``) must be used to conclude most statements in C++.

In fact, the following program will run perfectly
even though the lack of meaningful spacing is more difficult for humans to read.


.. activecode:: hellocppugly
    :language: cpp

    #include <iostream>
    using namespace std; int main(){cout << "Hello World!\n"; return 0;}


As you program in C++, we strongly recommend you continue to use
the kind of human-readable formatting you have become used to in Python.
You will likely learn to appreciate this when you are debugging.

.. parsonsprob:: questionintrocpp_order

   Construct a block of code that correctly implements hello world
   ---
   #include <iostream>
   ---
   using namespace std;
   ---
   int main()
   ---
   ``{``
   ---
   cout << "Hello World!\n";
   ---
   return 0;
   ---
   \}


Comments in C++
---------------

Python supports three different types of comments, while C++ supports only two types of comments.

Python's single line comment begins with a hash (``#``).
In C++, the equivalent is two forward slashes (``//``)
In each case the rest of the line is treated as a comment and ignored by the
interpreter or compiler.

Python has two types of multiline comments. Like Python, C++ also supports multi-line comments
beginning with
``\*``
and ending with
``*/``.

There is no equivalent in the C++ standard to the triple-quoted docstring in C++.
However, the symbol groups
``\**``
and
``*/``
are often used to indicate documentation blocks
at the beginning of a class, program, or function,
which is legal because the second asterisk ``*``  is simply treated as part of the
multi-line comment.
Certain libraries will also automatically process the text between these symbol groups,
as a docstring for the documentation.

::

  // The remainder of this line is a C++ comment which is ignored by the compiler

  /* This is a multi-line C++ comment that can
  span many lines, beginning and ending with the given symbols */


Standard Input and Output
-------------------------

We often have a need to interact with users,either to get data or to provide some sort of result. 
The C++ ``<iostream>`` library provides us with the functionality to get information 
as console input and to output information to the console. This input and output is handled in what is known as a ``stream``.

A ``stream`` is essentially a channel in which data flows from the source to a destination.
Output streams send data out, and the standard output stream ``cout`` sends data to the screen, also called the console.
So, ``cout`` stands for "console output".
Much like the Python ``print`` statement, ``cout`` is used to
print to the standard output device, which is typically your screen.
When ``cout`` is used, you will also see ``<<`` used.
When this odd set of symbols are used together, they are called the "output operator".
The output operator is used to direct output to the designated output device or file.
The output operator can also be used to concatenate output, much like the "+"
can be used to concatenate in Python.

The command ``cin`` is somewhat similar to ``cout`` except, of course, it is used for input.
Input streams direct data from a source, such as the keyboard or a file. 
As you might have guessed, ``cin`` stands for "console input" and it makes getting input from the standard input device (usually the keyboard) relatively easy.
The input operator in C++ is ``>>``.

Here is an example that uses ``cin``:

.. raw :: html

    <div>
    <iframe height="600px" width="100%" src="https://repl.it/@pearcej/cin-example?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    </div>


Type Declarations
-----------------

In this example, you may note the line ``float num`` which declares a new variable called ``num`` of type ``float``.
Just like functions, all variables in C++ need to be declared before use.
The line ``float num`` essentially tells the compiler to set aside sufficient space for a floating point number, 
and to name this memory location ``num.``
Then whatever the user types in will be stored in the ``num`` variable. 
Using the ``cout`` function, we can write instructions that will prompt the user to enter data and then
incorporate that data into further processing. 
For example, in the code above, the integer input is doubled and then displayed!

We will talk more about type declarations in the section on data types, and 
we will go into more depth on input and output later when we discuss
C++ streams and file handling.


Summary
=======

Now that we have run our "hello world" program, lets go back and look at
it carefully to see what we can learn about the C++ language.

.. activecode:: hellocommented
    :language: cpp

    /* This hello world program demonstrates the C++ concepts
        of commenting, using libraries, and using output.
    */

    #include <iostream>
    using namespace std;

    int main(){         // main() must exist & return an int
        cout << "Hello World!\n";
        return 0;       // 0 indicates program ended correctly.
    }

This simple example illustrates a few very important rules:


1. Everything in C++ must be declared as a specific type of object or variable, including declaring the return type for each function.

2. Every C++ program must have a function which begins as ``int main()``, and ends with the statement ``return 0;`` when successfully
   completed.

3. C++ statements are ended by a semi-colon.

4. White space is mostly meaningless in C++, but all C++ code blocks must be surrounded by curly brackets {}, rather than using
   indentation to delineate blocks as is done in Python.
