C++ Data Types
===============

Numeric
-------

One of the great things about Python is that all of the basic data types
are objects. Integers are objects, floating point numbers are objects,
lists are objects, everything. In C++ that is not the case. In C++
some of the most basic data types like integers and floating point
numbers are not objects. The benefit of having these primitive data
types be non-objects is that operations on the primitives are fast.

Lets go back in time and look at another of our very early Python
programs. Here is a simple Python function to convert a Fahrenheit
temperature to Celsius.

.. activecode:: tcpython
    :language: python

    def main():
        fahr = int(input("Enter the temperature in F: "))
        cel = (fahr - 32) * 5.0/9.0
        print("the temperature in C is: ", cel)

    main()

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

      cel = (fahr - 32) * 5.0/9.0;
      cout<<"The temperature in C is: "<<cel<<endl;
    }

    int main() {
      TempConv();

      return 0;
    }

There are several new concepts introduced in this example. We will look
at them in the following order:

-  Include

-  Variable Declaration

-  Input/Output

**Needs rewrite**

Include
----

In C++ you can use any class that is available without having to import
the class subject to two very important conditions:

1. The g++(C++ compiler) and C++ must know that the class exists.

2. You must use the full name of the class.

You first question might be how do the ``C++`` and ``g++`` commands
know that certain classes exist. The answer is the following:

1. C++ knows about all the classes that are defined in .cpp
files in your current working directory.

2. C++ knows about all the classes that are included in your
   ``CLASSPATH`` environment variable. Your ``CLASSPATH`` environment
   variable can name two kinds of structures.

   1. A jar file that contains C++ classes.

   2. Another unix directory that contains C++ class files.

You can think of the `#include` statement in C++ as working a little bit
like the ``from module import xxx`` statement in Python. However, behind
the scenes the two statements actually do very different things. The
first important difference to understand is that the class naming system
in Java is very hierarchical. The *full* name of the Scanner class is
really ``java.util.Scanner``. You can think of this name as having two
parts: The first part ``java.util`` is called the **package** and the
last part is the class. We’ll talk more about the class naming system a
bit later. The second important difference is that it is the Java class
loader’s responsibility to load classes into memory, not the import
statement’s.

So, what exactly does the import statement do? What it does is tell the
compiler that we are going to use a shortened version of the class’s
name. In this example we are going to use the class
``java.util.Scanner`` but we can refer to it as just ``Scanner``. We
could use the ``java.util.Scanner`` class without any problem and
without any import statement provided that we always referred to it by
its full name. As an Experiment you may want to try this yourself.
Remove the import statement and change the string Scanner to
``java.util.Scanner`` in the rest of the code. The program should still
compile and run.

Declaring Variables
-----

Here is where we run into one of the most important differences between
C++ and Python. Python is a **dynamically typed** language. In a
dynamically typed language a variable can refer to any kind of object at
any time. When the variable is used, the interpreter figures out what
kind of object it is. C++ is a **statically typed** language. In a
statically typed language the association between a variable and the
type of object the variable can refer to is determined when the variable
is **declared**. Once the declaration is made it is an error for a
variable to refer to an object of any other type.

In the example above, lines 5—6 contain variable declarations.
Specifically we are saying that ``fahr`` and ``cel`` are going to
reference objects that are of type ``double``. This means that if we were to try an
assignment like ``fahr = "xyz"`` the compiler would generate an error
because ``"xyz"`` is a string and ``fahr`` is supposed to be a double.

For Python programmers the following error is likely to be even more
common. Suppose we forgot the declaration for ``cel`` and instead left
line 6 blank. What would happen when we type ``gcc tempConv.cpp`` on
the command line?

::

    exit status 1
    main.cpp: In function 'void TempConv()':
    main.cpp:11:3: error: 'cel' was not declared in this scope
    cel = (fahr - 32) * 5.0/9.0;
    ^~~

When you see the first kind of error, where the symbol is on the left
side of the equals sign it usually means that you have not declared the
variable. If you have ever tried to use a Python variable that you have
not initialized the second error message will be familiar to you. The
difference here is that we see the message before we ever try to test
our program. More common error messages are discussed in the section
[sec:common\_mistakes] {Common Mistakes}.

The general rule in C++ is that you must decide what kind of a data type
your variable is going to reference and then you must declare that
variable before you use it. There is much more to say about the static
typing of C++ but for now this is enough.

**Needs Editing**
Input / Output
-----

In C++ `cin` makes getting an input from the user, a file, or even
over the network relatively easy. In our case we simply want to ask the
user to type in a number at the command line, so we call the constructor and pass the number to the ``cin``.
`cin` is similar to ``cout`` except of course it is used for input. We will talk about the reasons why this
is so later when we talk in depth about C++ streams. You will also see
in other examples that we can add inputs by passing the `cin` a
File object. You can think of a input stream `cin` as a kind of “adapter” that
makes low level objects easier to use.

<!---

We also use the `cin` object to read in numbers. We
see the implications of C++ being a strongly typed language. Take a look at the code **insert place where?????** Notice
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

**Needs rewrite???**

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
able to add together a string and a Double right? You are correct,
however, all java objects have a method called ``tostring``. The
``tostring`` method acts much like the Python method ``__str__()`` and
is called automatically by the compiler whenever it makes sense to
convert a Java object to a string.

-->

String
------

Strings in C++ and Python are quite similar. Like Python, C++ strings
are immutable. However, manipulating strings in C++ is not quite as
obvious since Strings do not support an indexing or slicing operator.
That is not to say that you can’t index into a C++ string, you can. You
can also pull out a substring just as you can with slicing. The
difference is that C++ uses method calls where Python uses Operators.

In fact this is the first example of another big difference between C++
and Python. Table 3 maps common Python string operations to their C++ counterparts. For the
examples shown in the table we will use a string variable called “str”

========================== ======================== =============================================================
                    Python                     C++                                                   Description
========================== ======================== =============================================================
                ``str[3]``               ``str[3]``                             Return character in 3rd  position
              ``len(str)``         ``str.length()``                               Return the length of the string
         ``str.find('x')``        ``str.find('x')``                                Find the first occurrence of x
             ``str + str``            ``str + str``                              Concatenate two strings together
========================== ======================== =============================================================

Arrays
----

Lets look at another early Python program. We are going to read numbers
from a file and produce a histogram that shows the frequency of the
various numbers. The data file we will use has one number between 0 and
9 on each line of the file. Here is a simple Python program that creates
and prints a histogram.

.. activecode:: histopy
    :language: python

    def main():
        count = [0]*10
        data = open('test.dat')

        for line in data:
            count[int(line)] = count[int(line)] + 1

        idx = 0
        for num in count:
            print(idx, " occured ", num, " times.")
            idx += 1

Now if we run this program on a data file that looks like this:

    9 8 4 5 3 5 2 1 5

We will get output that looks like this:

::

    0 occurred 0 times
    1 occurred 1 times
    2 occurred 1 times
    3 occurred 1 times
    4 occurred 1 times
    5 occurred 3 times
    6 occurred 0 times
    7 occurred 0 times
    8 occurred 1 times
    9 occurred 1 times

Lets review what is happening in this little program. In the first line
we create an array and initialize the first 10 positions in the array to be 0. Next we open the data file called ‘test.dat’.
Third, we have a loop that reads each line of the file. As we read each line we convert it to
an integer and increment the counter at the position in the array
indicated by the number on the line we just read. Finally we iterate
over each element in the array printing out both the position in the array
and the total value stored in that position.

To write the C++ version of this program we will have to introduce
several new C++ concepts. You will see three different kinds
of loops used in C++. Two of the loops we will use are going to be very
familiar, the third one is different from what you are used to in Python
but is easy when you understand the syntax:

while
    Used with boolean expression for loop exit condition.

for
    Used to iterate over a sequence. This is very similar to
    ``for i in xxx`` where xxx is a list or string or file.

for
    Used to iterate through a sequence of numbers. This is most similar
    to for ``i in range()``, except the syntax is different.

Here is the C++ code needed to write the exact same program:

.. activecode:: histojava
    :language: java
    :sourcefile: Histo.java
    :datafile: test.dat

    using namespace std;
    #include <iostream>
    #include <fstream>
    #include <string>

    int main() {
      string line;
      ifstream myfile("input.txt");
      int idx;

      int count[10];
      for (int i=0;i<10;i++) {
        count[i]=0;
      }

      if (myfile.is_open())
      {
        while(getline(myfile, line)) {
          idx=stoi(line);
          count[idx]++;
        }

        myfile.close();
      } else {
        cout<<"Sorry but I was unable to open your data file"<<endl;
      }

      idx=0;
      for (int i:count) {
        cout<<idx<<" occurred "<<i<<" times."<<endl;
        idx++;
      }


      return 0;
    }


.. datafile:: test.dat

   1 2 3
   4 5
   6
   7
   8 9 1 2 3
   4
   5


Before going any further, I suggest you try to compile the above program
and run it on some test data that you create.

Now, lets look at what is happening in the C++ source. As usual we
declare the variables we are going to use at the beginning of the
method. In this example we are declaring
an integer called idx and an ``array`` called count. However, there
is a new twist to the ``array`` declaration. Unlike Python where
lists can contain just about anything, in C++ we let the compiler know
what kind of objects our array is going to contain. In this case
the ``array`` will contain Integers. The syntax we use to declare
what kind of object the array will contain is the ``<Type>``
syntax.


Without the `<Integer>` part of the declaration, C++ gives the following
error:

    error: ‘variable’ was not declared in this scope

Lines 11—21 are required to open the file. Why so many lines to open a
file in C++? The additional code mainly comes form the fact that you
may want to reckon with the possibility that the file you want to open
is not going to be there. If you attempt to open a file that does not exist
using this method, the second block of code will run, but you will not get
an error.

<!--- Commented out section on Error Handling

try/catch construct allows us to try things that are risky, and
gracefully recover from an error if one occurs. The following example shows the
general structure of a try catch block.

::

    try {
       Put some risky code in here.... like opening a file
    }
    catch (Exception e) {
       If an error happens in the try block an exception is thrown.
       We will catch that exception here!
    }

Notice that in line 16 we are catching an ``IOException``. In fact we
will see later that we can have multiple catch blocks to catch different
types of exceptions. If we want to be lazy and catch any old exception
we can catch an ``Exception`` which is the parent of all exceptions.
--->

On line 11 we create our array and give it an initial size of 10.
On line 12 we start the first of three loops. The for loop on
lines 12-14 serves the same purpose as the Python statement
``count = [0]*10``, that is it initializes the first 10 positions in the
``array`` to hold the value 0.

The syntax of this for loop probably looks very strange to you, but in
fact it is not too different from what happens in Python using range. In
fact ``for(int i = 0; i < 10; i++)`` is exactly equivalent to the
Python ``for i in range(10)`` The first statement inside the parenthesis
declares and initializes a loop variable i. The second statement is a
Boolean expression that is our exit condition. In other words we will
keep looping as long as this expression evaluates to true. The third
clause is used to increment the value of the loop variable at the end of
iteration through the loop. In fact ``i++`` is C++ shorthand for
``i = i + 1`` C++ also supports the shorthand ``i--`` to decrement the
value of i. Like Python you can also write ``i += 2`` as shorthand for
``i = i + 2`` Try to rewrite the following Python for loops as C++ for
loops:

    -  ``for i in range(2,101,2)``

    -  ``for i in range(1,100)``

    -  ``for i in range(100,0,-1)``

    -  ``for x,y in zip(range(10),range(0,20,2))`` [hint, you can
       separate statements in the same clause with a ,]

The next loop (lines 16-25) shows a typical C++ pattern for reading
data from a file. C++ while loops and Python while loops are identical
in their logic. In this case we will continue to process the body of the
loop as long as `getline(myfile, line)` returns true.

The last loop in this example is similar to the Python for loop where
the object of the loop is a Sequence. In C++ we can use this kind of
for loop over all kinds of sequences. The for loop on line 30 ``for(int i : count)`` is
equivalent to the Python loop ``for i in count:`` This loop iterates
over all of the elements in the `array` called count. Each time
through the loop the Integer variable i is bound to the next element of
the ``array``.

<!---
Arrays
------

As I said at the outset of this Section we are going to use C++
``vectors`` because they are easier to use and more closely match the
way that Python lists behave. However, if you look at C++ code on the
internet or even in your C++ books you are going to see examples
of something called arrays. In fact you have already seen one example of
an array declared in the ‘Hello World’ program. Lets rewrite this
program to use primitive arrays.

.. activecode:: primarrays
    :language: java
    :sourcefile: HistoArray.java
    :datafile: test.dat

    using namespace std;
    #include <fstream>
    #include <iostream>
    #include <string>

    int main() {
    	int count[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    	int idx;
    	ifstream data("input.txt");
    	string line;

    	if (data.is_open()) {
    		while (getline(data, line)) {
    			idx = stoi(line);
    			count[idx]++;
    		}
    		data.close();
    	} else {
    		cout << "Sorry but I was unable to open your data file" << endl;
    	}

    	idx = 0;
    	for (int i : count) {
    		cout << idx << " occurred " << i << " times." << endl;
    		idx++;
    	}
    }

The main difference between this example and the previous example is
that we declare count to be an Array of integers. We also can initialize
short arrays directly using the syntax shown on line 8. Then notice that
on line 24 we can use the square bracket notation to index into an
array.

-->

Pointers
--------
In Python, all variables are stored as references to locations in memory, and
the specific address that we are accessing in memory is unknown to us. The
C++ allows you to use pointers to access the specific location of a variable
in memory, and gives you the ability to change what is written there.
