Let's look at a C++ program
==========================

A time honored tradition in Computer Science is to write a program
called “hello world.” The “hello world” program is simple and easy.
There are no logic errors to make, so getting it to run relies only on
understanding the syntax. To be clear lets look at a “complicated”
version of the hello world program in Python:

.. activecode:: hellopy
  :language: python

    def main():
        print("Hello World!")
    main()

Remember that we can define this program right at the Python command
line and then run it:

::

    >>> main()
    "Hello World!"
    >>>

Now lets look at the same program written in C++:

.. activecode:: hellocpp
    :language: cpp

    #include <iostream>

    int main() {
      std::cout << "Hello World!\n";
      return 0;
    }

This can alternatively be written as to allow
better facilitate standard input and output:

.. activecode:: hellocpp
    :language: cpp

    #include <iostream>
    using namespace std;

    int main() {
      cout << "Hello World!\n";
      return 0;
    }

What we see is that at the core there are a few similarities, such as the
main function and the string “Hello World” However there is a lot more
stuff  around the edges that make it harder to see the core of the program. Do
not worry! An important skill for a computer scientist is to learn what
to ignore and what to look at carefully. You will soon find that there
are some elements of Java that will fade into the background as you
become used to seeing them. One thing that will help you is to learn a
little bit about C++.

[//]: # (TODO: Add link to section on Naming Conventions)

The first question you probably have about this little program is “How
do I run it?” Running a C++ program is not as simple as running a
Python program. The first thing you need to do with a C++ program is
compile it. The first big difference between C++ and Python is that
Python is an interpreted language. We could run our Python programs in
the Python **interpreter** and we were quite happy to do that. C++
makes running programs a two step process. First we must type the hello
world program into a file and save that file using a name like
``hello.cpp`` Once we have saved the file we **compile** it either from
the command line or from an IDE.

Now you may be wondering what good is that extra step? What does
compiling do for us? There are a couple of important benefits we get
from compiling:

-  Early detection of errors

-  Faster Program Execution

The job of the compiler is to turn your C++ code into language that your
machine can understand. We call the code that the computer
understands **machine code**. The computer interprets the machine code
much like the Python interpreter interprets your Python.
However, since machine code is much closer to the native language of the
computer, it can run faster.

When the compiler does the translation it can find many different kinds
of errors. For example if you make a typo or forget to declar a variable
 the compiler will find these and point them out to you before you ever
 run the program. We will
look at some examples of compiler errors shortly. Chances are you may
create some on your own very soon too.

Using headers and libraries
----
Preprocessor directives in C++ appear as statements preceded by the hash sign #.
These tell the preprocessor which file, header or library to make available to the compiler.
For example, #include <iostream> will make sure that the iostream library is available at compile time.
Here, the term header is used for a type of C++ file that contains definitions of functions and variables,
but not the function implementations.

You can think of the `#include` statement in C++ as working a little bit like the ``import...``
statement in Python. Python's `import` statement directly accesses the code written in another file
while the `#include` statement in C++ copies the classes and functions from another file.

In Python, an import statement looks like:

    import classname

There are two ways to use #include in C++:

    #include <...>

    #include "..."

Angle-brackets are used to include libraries or headers provided by the implementation, such as the
headers in the standard library (iostream, string, etc.), and quotes are used for headers and files
not provided by the implementation.

Declaring Variables
-----

Here is where we run into one of the most important differences between
C++ and Python. Python is a **dynamically typed** language. In a
dynamically typed language a named variable can refer to any kind of object at
any time. When the name  is used, the interpreter figures out what
kind of object it is. C++ is a **statically typed** language. In a
statically typed language the association between a variable and the
type of object the variable can refer to is determined when the variable
is **declared**. Once the declaration is made it is an error for a
variable to refer to an object of any other type.

In the example above, lines 5 and 6 contain variable declarations.
Specifically we are saying that ``fahr`` and ``cel`` are going to
reference objects that are of type ``double``. This means that if we were to try an
assignment like ``fahr = "xyz"`` the compiler would generate an error
because ``"xyz"`` is a string and ``fahr`` is supposed to be a double.

For Python programmers the following error is likely to be even more
common. Suppose we forgot the declaration for ``cel`` and instead left
line 6 blank. What would happen when we type ``gcc tempConv.cpp`` on
the command line? We would get an error such as:

::

    exit status 1
    main.cpp: In function 'void TempConv()':
    main.cpp:11:3: error: 'cel' was not declared in this scope
    cel = (fahr - 32.0) * 5.0/9.0;
    ^~~

When you see the first kind of error, where the symbol is on the left
side of the equals sign it usually means that you have not declared the
variable. If you have ever tried to use a Python variable that you have
not initialized, the second error message will be familiar to you. The
difference here is that we see the message before we ever try to test
our program. More common error messages are discussed in the section
[sec:common\_mistakes] {Common Mistakes}.

The general rule in C++ is that you must decide what kind of a data type
your variable is going to reference and then you must declare that
variable before you use it. There is much more to say about the static
typing of C++, but for now, this is enough.

Standard Input and Output
-----

In C++ `cin`, which stands for console in, makes getting an input from the standard
input device (usually the keyboard) relatively easy. In our case we simply want to ask the
user to type in a number at the command line, so we call the constructor and pass the number to the ``cin``.
The command `cin` is similar to ``cout`` except of course it is used for input.
We will talk about the reasons why this
is the case later when we talk in more depth about C++ streams and file handling.





Summary
------

Now that we have run our hello world program, lets go back and look at
it carefully to see what we can learn about the C++ language. This
simple example illustrates a few very important rules:

1. Everything in C++ must be declared with a specific type.

2. Every C++ program must have a function which begins as ``int main()``
and returns 0 when sucessfully completed.
