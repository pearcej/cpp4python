C++ Basic Data Types
====================

One of the great things about Python is that all of the basic data types
are objects. Integers are objects, floating point numbers are objects,
lists are objects,... everything is an object. In C++ that is not the case.
In C++ some of the most basic data types like integers and floating point
numbers are not objects. The benefit of having these primitive data
types be non-objects is that operations on C++ primitives are fast.

Let's go back in time and look at another of our very early Python
programs. Here is a simple Python function to convert a Fahrenheit
temperature to Celsius.

.. activecode:: convertpy
    :language: python

    def TempConv():
        fahr = int(input("Enter the temperature in F: "))
        cel = (fahr - 32.0) * 5.0/9.0
        print("the temperature in C is: ", cel)

    def main():
      TempConv()
    main()

Next, lets look at the C++ Equivalent.

.. activecode:: convertcpp
    :language: cpp
    :sourcefile: tempConv.cpp
    :stdin: 212

    #include <iostream>
    using namespace std;

    void TempConv(double fah) {
        double cel;

        cel = (fah - 32.0) * 5.0/9.0;
        cout<<"The temperature in C is: "<<cel<<endl;
    }

    int main() {
        double fahr;
        cout << "Enter the temperature in F: ";
        cin >> fahr;
        TempConv(fahr);
        return 0;
    }



Declaring Variables
-------------------

Here is where we run into one of the most obvious differences between
C++ and Python. Python is a **dynamically typed** language. In a
dynamically typed language, a named variable can refer to any kind of object at
any time. When the name  is used, the interpreter figures out what
kind of object it is. C++ is a **statically typed** language. In a
statically typed language the association between a variable and the
type of object the variable can refer to is determined when the variable
is **declared**. Once the variable declaration is made, it is an error for a
variable to try to use that variable to reference anything of any other type.

In the C++ example above, lines 5 and 6 contain variable declarations.
Specifically we are saying that ``fahr`` and ``cel`` are going to
reference objects that are of type ``double``. This means that if we were to try an
assignment like ``fahr = "xyz"`` the compiler would generate an error
because ``"xyz"`` is a string and ``fahr`` is supposed to be a double.

For Python programmers the following error is likely to be even more
common. Suppose we forgot the declaration for ``cel`` and instead left
line 6 blank. What would happen when we compile our program?
We would get an error such as:

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
