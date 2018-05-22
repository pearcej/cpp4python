C++ Compound Data Types
===============

Strings
------

Strings are not supported directly in C++. You have to use the standard string
header library, accessed by using:

 `#include <string>`

However, with this library, strings in C++ and Python have many similarities.
In Python, strings can be enclosed by either double or single quotes.
In C++, double quotes must be used for strings, while single quotes are reserved for chars.
Like Python, C++ strings
are immutable. Manipulating strings in C++ is not quite as
obvious since strings do not support indexing or slicing operators.
That is not to say that you can’t index into a C++ string, you can. You
can also pull out a substring just as you can with slicing. The
difference is that C++ uses method calls where Python uses operators.

THe following, table maps common Python string operations to their C++ counterparts. For the
examples shown in the table we use a string variables called “str1” and “str2”.

========================== ======================== =============================================================
                    Python                     C++                                                   Description
========================== ======================== =============================================================
              ``str1[3]``               ``str1[3]``                             Return character in 3rd  position
            ``len(str1)``         ``str1.length()``                               Return the length of the string
       ``str1.find('x')``        ``str1.find('x')``                                Find the first occurrence of x
          ``str1 + str2``           ``str1 + str2``                              Concatenate two strings together
========================== ======================== =============================================================

Python Lists and C++ Arrays
----

The primary compound structure for storing a mutable sequence of values in
Python is the Python list. A Python list has flexibly size, so can be expanded
and/or contracted as needed. C++ offers a similarly flexible data structure in the
Standard Template Library called the vector. However, both the Python list and the
C++ vector are implemented via underlying arrays.

An array is a contiguous set of memory locations used to store a sequence of homogeneous data.
i.e. the data in an array must all of the same data type.
And, unless you choose to make your array dynamically allocated (more on that later),
the size of the C++ array must be fixed when the array is declared. Arrays are important because they are designed to be fast.

C++ arrays use indexing similar to in Python. Indices begin at 0 and use square [] brackets.

[//]: # (TODO: Rework following section using C++ specifics and no files)

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

Let's review what is happening in this little program. In the first line
we create an array and initialize the first 10 positions in the array to be 0.
Next we open the data file called ‘test.dat’.
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

Without the `int` part of the declaration, C++ gives the following
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

As we said at the outset of this Section, C++
``vectors`` more closely match the
way that Python lists behave. However, if you look at C++ code on the
internet or even in your C++ books you are going to see examples
of something called arrays. In fact you have already seen one example of
an array declared in the ‘Hello World’ program. Lets rewrite this
program to use primitive arrays.

.. activecode:: primarrays
    :language: cpp
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
that we declare count to be an array of integers. We also can initialize
short arrays directly using the syntax shown on line 8. Then notice that
on line 24 we can use the square bracket notation to index into an
array.

Pointers
--------
In Python, all variables are stored as references to locations in memory, and
the specific address that we are accessing in memory is unknown to us. These
references can be accessed using the id() function.

    int_a = 3
    int_b = 5
    ref_a=id(int_a)
    ref_b=id(int_b)

    print(int_a, "is stored at", id(ref_a))
    print(int_b, "is stored at", id(ref_b))

The C++ language allows two different ways to store and access variables.
The first is storing into a variable which is a named memory location
(Such as the variables int_a and int_b shown below.)
In the second, you use something called a pointer which stores the memory
address of the actual place in memory where the variable's value is stored
(Such as the variables ptr_a and ptr_b shown below.)
Either technique gives you access the value of the variable.

    #include <iostream>
    using namespace std;

    int main() {
    	int int_a, int_b, *ptr_a, *ptr_b; //Create two ints, and two pointers
      //declares a pointer, the use of "ptr_" in naming is purely for convenience.

    	int_a = 3;
    	int_b = 5;

    	//Using & to access the memory address of a variable
    	ptr_a = &int_a; //Gets the address of the int x and stores it to the pointer a
    	ptr_b = &int_b; //Gets the address of the int y and stores it to the pointer b

    	cout << int_a << " is stored at " << ptr_a << endl;
    	cout << int_b << " is stored at " << ptr_b << endl << endl;

    	int_a = 10;
    	*ptr_b = 15; //Dereferencing a pointer using *, accessing the int by it's address

    	cout << int_a << " is stored at " << ptr_a << endl;
    	cout << int_b << " is stored at " << ptr_b << endl << endl;
    }

More information about Pointers in C++ and their functionality can be found in the
section on Pointers.
