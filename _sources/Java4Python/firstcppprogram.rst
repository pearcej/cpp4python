Lets look at a C++ program
---------------------------

A time honored tradition in Computer Science is to write a program
called “hello world.” The “hello world” program is simple and easy.
There are no logic errors to make, so getting it to run relies only on
understanding the syntax. To be clear lets look at a “complicated”
version of hello world for Python:

::

    def main():
        print("Hello World!")

Remember that we can define this program right at the Python command
line and then run it:

::

    >>> main()
    "Hello World!"
    >>>

Now lets look at the same program written in C++:

::

    #include <iostream>
    using namespace std;

    int main() {
      cout << "Hello World!\n";
      return 0;
    }

What we see is that at the core there are a few similarities, such as a
main and the string “Hello World” However there is a lot more stuff
around the edges that make it harder to see the core of the program. Do
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
world program into a file and save that file using the name
``Hello.cpp`` The file name must be the same as the public class you
define in the file. Once we have saved the file we **compile** it from
the command line as follows:

[//]: # (TODO: Rework section on compiling C++ from the command line)

::

    $ javac Hello.java
    $ ls -l Hello.*
    -rw-r--r--   1 bmiller  bmiller  391 Jul 19 17:47 Hello.class
    -rw-r--r--   1 bmiller  bmiller  117 Jul 19 17:46 Hello.java

The command ``javac`` compiles our java source code into compiled byte
code and saves it in a file called ``Hello.class``. ``Hello.class`` is a
binary file so you won’t learn much if you try to examine the class file
with an editor. Hopefully you didn’t make any mistakes, but if you did
you may want to consult the [sec:common\_mistakes] {Common Mistakes}
section for helpful hints on compiler errors.

Now that we have compiled our java source code we can run the compiled
code using the ``java`` command.

::

    $ java Hello
    Hello World!
    $

[//]: # (TODO: Rework section on compiling C++ from the command line)

Now you may be wondering what good is that extra step? What does
compiling do for us? There are a couple of important benefits we get
from compiling:

-  Early detection of errors

-  Faster Program Execution

The job of the compiler is to turn your C++ code into language that your
machine can understand. We call the code that the computer
understands **machine code**. The computer interprets the machine code
much like the Python interpreter interprets your Python.
However since machine code is much closer to the native language of the
computer it can run faster.

When the compiler does the translation it can find many different kinds
of errors. For example if you make a typo the compiler will find the
typo and point it out to you before you ever run the program. We will
look at some examples of compiler errors shortly. Chances are you will
create some on your own very soon too.

Now that we have run our hello world program, lets go back and look at
it carefully to see what we can learn about the C++ language. This
simple example illustrates a few very important rules:

1. Everything in C++ must have a type

2. Every C++ program must have a function called ``int main()`` that returns 0 when completed

[//]: # (TODO: Rework following section using C++ specifics)
