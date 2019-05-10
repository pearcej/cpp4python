..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
    To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Collections
~~~~~~~~~~~

In addition to the numeric, Boolean, and character types,
C++ also offers built-in collection types.
A **collection** data type is a grouping of some number of other data items
(possibly only zero or one) that have some shared significance
or need to be operated upon together.

Arrays, vectors, strings, sets, and hash tables are among these useful
C++ collection types.

Arrays
~~~~~~

**What is an Array?**
An array is a data structure consisting of an ordered collection of data elements,
of identical type in which each element can be identified by an array index.
More technically, an array data structure is an ordered arrangement of values
located at equally spaced addresses in contiguous computer memory.

NOTE: A C++ **array** is always stored in contiguous memory. C++ arrays can be allocated in two different ways:

    1) *statically allocated* in which the array size is fixed at compile-time and cannot change
    2) *dynamically allocated* in which pointers are used in the allocation process so the size can change at run-time

    

In modern C++, the statically allocated array is typically used
in situations when speed is essential or where hardware constraints exist, and a data structure
called a vector is typically used when more flexibility is required.

As a Python programmer, you might see the array as the ancestor
of the Python list, and you might remember that Python lists are actually implemented via
an underlying array consisting of references.

C++ arrays are similar to Python lists except that because C++ stores variables
directly, each element of a C++ array must be of identical data type.
Like Python lists, the indices for arrays start counting with 0.

The use of arrays permits us to utilize an ordered set
of memory locations that we can then manipulate as a single
entity, and that at the same time gives us direct access to each
individual component.

**Why use an Array?**

C++ is a language often used for real-time or low-level processing
where speed is essential and/or there is only a fixed amount of space
available.

The fact that array elements are stored in memory in contiguous
memory locations making look-up via index very, very fast.
In computing, a **word** is the unit of data used by a particular processor design,
such as 32 or 64 bits. For example, an array of 100 integer variables, with indices 0 through 99,
might be stored as 100 words at memory addresses 20000, 20004, 20008, ... 20396.
The element with index i would be located at the address 20000 + 4 × i.

Statically allocated C++ arrays must be declared with both a type and a size at compile-time.

::

    double darray[4];
    int iarray[10];
    char arr2[3000];


It is also possible to initialize statically allocated arrays at compile time,
in which case the number of items determines the array's size.

::

    int arr[] = {1, 2, 3, 4};  // This is size 4.
    char arr2[] = {'a', 'b', 'c'}; // This is size 3.
    string arr3[] = {"this", "is", "an", "array"}; // This is size 4.


Note that an array with a single element is not the same type as the **atomic** type,
so the following are not the same.

::

    double darray[] = {1.2};  // must use index to access value
    double ddouble = 1.2;     // can't use index to access value


**Be Cautious with Arrays**

The speed and low-level control that arrays offer us
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
            mylist = [2, 4, 6, 8]
            for i in range(8):
                print(mylist[i])

        main()


The protections Python offers, however, takes time and C++ is designed for speed.
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

You should use an array when you have a need for speed
or you need to work with hardware constraints.
Otherwise, you may want to consider using another collection data type,
the *vector*.


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

   In the above example, what happened to otherdata[ ] in C++?

.. mchoice:: mc_array
    :answer_a: int myarray(5);
    :answer_b: myarray[5];
    :answer_c: int myarray[5];
    :answer_d: None of the above.
    :correct: c
    :feedback_a: Check the characters at the end of the array! Right now that is a function!
    :feedback_b: You are forgetting something important!
    :feedback_c: Good work!
    :feedback_d: Check the characters at the end of the array!

    What is the correct way to declare an array in C++?
