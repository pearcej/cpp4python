Input / Output from Files
-----

TODO: Briefly summarize cin/cout and then explain streams and file Handling

In C++ `cin`, which stands for comsole in, makes getting an input from the standard
input device (usually the keyboard) relatively easy. In our case we simply want to ask the
user to type in a number at the command line, so we call the constructor and pass the number to the ``cin``.
The command `cin` is similar to ``cout`` except of course it is used for input.
We will talk about the reasons why this
is so later when we talk in depth about C++ streams.

<!--

We also use the `cin` object to read in numbers. We
see the implications of C++ being a strongly typed language. Take a look at the
code **insert place where?????** Notice
that we must call the method ``nextDouble`` because the variable
``fahr`` was declared as a double. So, we must have a function that is
guaranteed to return each kind of object we might want to read. In this
case we need to read a Double so we call the function nextDouble. The
compiler matches up these assignment statments and if you try to assign
the results of a method call to the wrong kind of variable it will be
flagged as an error.

Table 2 shows you some commonly used methods of the scanner class. There
are many more methods supported by this class and we will talk about how
to find them in the next chapter.

==================== ================ ======================================================
         Return type      Method name                                            Description
==================== ================ ======================================================
             boolean        hasNext()                   returns true if more data is present
             boolean     hasNextInt()   returns true if the next thing to read is an integer
             boolean   hasNextFloat()      returns true if the next thing to read is a float
             boolean  hasNextDouble()     returns true if the next thing to read is a double
             Integer        nextInt()           returns the next thing to read as an integer
               Float      nextFloat()              returns the next thing to read as a float
              Double     nextDouble()             returns the next thing to read as a Double
              String           next()             returns the next thing to read as a String
==================== ================ ======================================================

Of course Java is more well known for producing applications that have
more of a user interface to them than reading and writing from the
command line. Lets look at a version of our temperature control
application that uses dialog boxes for input and output.

.. activecode:: swing
    :language: C++
    :sourcefile: TempConvGUI.java

    import javax.swing.*;

    #include <iostream>
    using namespace std;

    int main() {
        String fahrString;
        Double fahr, cel;

        cout<<"Enter the temperature in F"<<endl;
        cin>>fahrString>>endl;
        fahr = new Double(fahrString);
        cel = (fahr - 32) * 5.0/9.0;

        cout<<(null,"The temperature in C is, " + cel)<<endl;
    }


This example illustrates a couple of interesting points:

First, the function call ``JOptionPane.showInputDialog`` pops up a
dialog box to allow you to enter a temperature. But, since you could
enter anything into the text input box it returns a ``String``. On the
next line the string is converted into a Double by the Double
constructor. This is similar to what happens in Python when you call
``float()`` with either a string or an integer as the argument.

The next dialog box is ``JOptionPane.showMessageDialog``. Notice that
the first parameter is ``null`` In Java ``null`` serves the same purpose
as ``None`` in Python. The first parameter is null because we do not
have a ‘main window’ for this little application. When we look at
creating full blown java programs with user interfaces, we will learn
more about this parameter.

The second parameter is ``"The temperature in C is, " + cel``. Now you
may be thinking to yourself that this must surely be a violation of the
strong typing I have been describing to you. After all you should not be
able to add together a string and a double right? You are correct,
however, all java objects have a method called ``tostring``. The
``tostring`` method acts much like the Python method ``__str__()`` and
is called automatically by the compiler whenever it makes sense to
convert a Java object to a string.

-->
