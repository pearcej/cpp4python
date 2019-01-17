..  Copyright (C)  Jan Pearce and Brad Miller
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Collection Data Types
~~~~~~~~~~~~~~~~~~~~~

In addition to the numeric, Boolean, and character types,
C++ has collection classes.
Arrays are a standard part of the C++ language.
Multiple types of strings are available.
Many ordered and unordered collection types are offered
via a library called the Standard Template Library (STL).
Vectors, sets, and sets and hash tables are among these useful
STL collection types.

Arrays
^^^^^^

**What is an Array?**

A statically allocated C++ **array** is an ordered collection
of zero or more C++ data values of identical data type
that is stored in contiguous memory and cannot change size.
As a Python programmer, you might see it as the ancestor
of the Python list, and it is similar except that each element
is of identical type and the number of elements cannot change.
Like in Python lists, the indices for arrays
start counting with 0.

The use of arrays permits us to utilize an ordered set
of memory locations that we can then manipulate as a single
entity, and that at the same time gives us direct access to each
individual component.

**Why use an Array?**

The fact that array elements are stored in memory in contiguous
memory locations making look-up via index very, very fast.

C++ is a language often used for real-time or low-level processing
where speed is essential and/or there is only a fixed amount of space
available.


The following fragment shows a variety of C++ data values
initialized into arrays at compile time.

::

    >>> int arr[] = {1, 2, 3, 4};
    >>> char arr2[] = {'a', 'b', 'c'};
    >>> string arr3[] = {"this", "is", "an", "array"};


Sometimes, you may want to initialize an array
at runtime.

::

    >>> int myarray[6] = { };
    >>> myarray
    [0, 0, 0, 0, 0, 0]


**Taking Care with Arrays**

The speed and low-level control arrays offer us
as programmers is powerful... and dangerous.
As a Python programmer, using a C++ array will
help you better understand the trade-offs of the
protections Python offers.

Here are examples of iteration.

.. tabbed:: list-array

  .. tab:: C++

    .. activecode:: listarray_cpp
        :caption: Iterating an array in C++
        :language: cpp

        #include <iostream>
        using namespace std;

        int main(){
            int myarray[] = {2,4,6,8};
            for (int i=0; i<4; i++){
                cout << myarray[i] << endl;
            }
            return 0;
        }

  .. tab:: Python

    .. activecode:: listarray_py
        :caption: Iterating a list in Python

        def main():
            mylist = [2,4,6,8]
            for i in range(8):
                print(mylist[i])

        main()

Protection takes time, and C++ is designed for speed.
Python would never let you iterate beyond the end of
a list. C++ will not only let you iterate beyond either
end of an array, but it will let you change the values
beyond either end of the array with sometimes catastrophic
results.

The phrase, "be careful what you wish for" is a great one
to remember when programming in C++. Because C++ will
generally try to do everything you ask for.

.. tabbed:: array_error

  .. tab:: C++

    .. activecode:: array_error_cpp
        :caption: Iterating an array in C++
        :language: cpp

        #include <iostream>
        using namespace std;

        int main(){
            int myarray[] = {2,4,6,8};
            for (int i=0; i<=8; i++){
                cout << myarray[i] << endl;
                cout << "id: " << &myarray[i] << endl;
            }
            return 0;
        }

  .. tab:: Python

    .. activecode:: array_error_py
        :caption: Iterating a list in Python

        def main():
            mylist = [2,4,6,8]
            print(mylist)
            for i in range(5):
                print(mylist[i])
                print("id: "+str(id(mylist[i])))

        main()

The speed of C++ comes at the cost of minimal to no error checking.
Sometimes this can have perplexing results such as in the next example.

.. tabbed:: array_werror

  .. tab:: C++

    .. activecode:: array_werror_cpp
        :caption: Array write error in C++
        :language: cpp

        #include <iostream>
        using namespace std;

        int main(){
            int myarray[] = {2, 4};
            int otherdata[]={777, 777};
            for (int i=0; i<4; i++){
                myarray[i]=0;
                cout <<"myarray["<< i << "]=";
                cout << myarray[i]<< endl;
                cout << "add:" << &myarray[i] << endl;
            }

            for (int i=0; i<2; i++){
                cout <<"otherdata["<< i << "]=";
                cout << otherdata[i]<< endl;
                cout << "add:" << &otherdata[i] << endl;
            }

            return 0;
        }

  .. tab:: Python

    .. activecode:: array_werror_py
        :caption: Write error in Python

        def main():
            mylist = [2, 4]
            otherdata = [777, 777]
            for i in range(4):
                print(mylist[i])
                print("id: "+str(id(mylist[i])))

            for j in range(2):
                  print(otherdata[i])
                  print("id: "+str(id(otherdata[i])))

        main()


.. mchoice:: mc_werror
   :answer_a: Nothing. Everything is fine.
   :answer_b: All data was automatically reinitialized.
   :answer_c: I have no idea. Please give me a hint.
   :answer_d: The first loop went out of bounds and wrote over the values in otherdata.
   :answer_e: none of the above
   :correct: d
   :feedback_a: Actually, there is a problem. Look carefully.
   :feedback_b: No. C++ just does what you tell it to do.
   :feedback_c: Try again. One of these is indeed correct. Look at the memory addresses.
   :feedback_d: Right!
   :feedback_e: One of the above is indeed correct.

  In the above example, what happened to otherdata[] in C++?

You should use arrays when you have a need for speed
or you need to work with hardware constraints.
Otherwise, you may want to consider another data type,
the vector.
