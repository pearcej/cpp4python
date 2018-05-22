C++ Basic Data Types
===============

One of the great things about Python is that all of the basic data types
are objects. Integers are objects, floating point numbers are objects,
lists are objects,.. everything is an object. In C++ that is not the case. In C++
some of the most basic data types like integers and floating point
numbers are not objects. The benefit of having these primitive data
types be non-objects is that operations on the primitives are fast.

Let's go back in time and look at another of our very early Python
programs. Here is a simple Python function to convert a Fahrenheit
temperature to Celsius.

.. activecode:: tcpython
    :language: python

    def TempConv():
        fahr = int(input("Enter the temperature in F: "))
        cel = (fahr - 32.0) * 5.0/9.0
        print("the temperature in C is: ", cel)

    TempConv()

Next, lets look at the C++ Equivalent.

.. activecode:: convert1
    :language: cpp
    :sourcefile: tempConv.cpp
    :stdin: 212

    #include <iostream>
    using namespace std;

    void TempConv() {
      double fahr;
      double cel;

      cout<<"Enter the temperature in F: ";
      cin>>fahr;

      cel = (fahr - 32.0) * 5.0/9.0;
      cout<<"The temperature in C is: "<<cel<<endl;
    }

    int main() {
      TempConv();

      return 0;
    }

There are several new concepts introduced in this example. We will look
at them in the following order:

-  #include

-  Variable declaration

-  Input/Output
