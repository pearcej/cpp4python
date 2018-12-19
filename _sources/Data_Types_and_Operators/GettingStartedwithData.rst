..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Getting Started with Data
~~~~~~~~~~~~~~~~~~~~~~~~~

We stated above that C++ supports the object-oriented programming
paradigm. This means that C++ considers data to be the focal point of
the problem-solving process. In C++, as well as in any other
object-oriented programming language, we define a **class** to be a
description of what the data look like (the state) and what the data can
do (the behavior). Classes are analogous to abstract data types because
a user of a class only sees the state and behavior of a data item. Data
items are called **objects** in the object-oriented paradigm. An object
is an instance of a class.

Built-in Atomic Data Types
^^^^^^^^^^^^^^^^^^^^^^^^^^

We will begin our review by considering the atomic data types. C++
has four main built-in numeric classes that implement the integer and
floating point data types. These C++ classes are called ``int``, ``float``, ``double``,
and ``long``. The standard arithmetic operations, +, -, \*, and /
(exponentiation can be done using ``pow()`` from the ``cmath`` library) can be used with parentheses forcing the order of
operations away from normal operator precedence. Other very useful
operations are the remainder (modulo) operator, %. Note that when two integers are divided, the integer portion of the
quotient is returned and the fractional portion is removed. To get the whole quotient, you must declare one of the numbers as a float.

.. tabbed:: intro

  .. tab:: C++

    .. activecode:: intro_1cpp
        :caption: Basic Arithmetic Operators C++
        :language: cpp

        #include <iostream>
        #include <cmath>
        using namespace std;

        int main(){

            cout << (2+3*4) << endl;
            cout << (2+3)*4 << endl;
            cout << pow(2, 10) << endl;
            cout << float(6)/3 << endl;
            cout << float(7)/3 << endl;
            cout << 7/3 << endl;
            cout << 7%3 << endl;
            cout << float(3)/6 << endl;
            cout << 3/6 << endl;
            cout << 3%6 << endl;
            cout << pow(2, 100) << endl;

            return 0;
        }

  .. tab:: Python

    .. activecode:: intro_1py
        :caption: Basic Arithmetic Operators Python

        def main():

            print(2+3*4)
            print((2+3)*4)
            print(2**10)
            print(6/3)
            print(7/3)
            print(7//3)
            print(7%3)
            print(3/6)
            print(3//6)
            print(3%6)
            print(2**100)

        main()


The boolean data type, implemented as the C++ ``bool`` class, will be
quite useful for representing truth values. The possible state values
for a boolean object are ``true`` and ``false`` with the standard
boolean operators, ``&&`` (and), ``||`` (or), and ``!`` (not). Note that
output values for ``true`` and ``false`` are ``1`` and ``0`` respectively.

::

    >>> true
    1
    >>> false
    0
    >>> false or true
    1
    >>> !(false || true)
    0
    >>> true and true
    1

Boolean data objects are also used as results for comparison operators
such as equality (==) and greater than (:math:`>`). In addition,
relational operators and logical operators can be combined together to
form complex logical questions. :ref:`Table 1 <tab_relational>` shows the relational
and logical operators with examples shown in the session that follows.

.. _tab_relational:

.. table:: **Table 1: Relational and Logical Operators**

    =========================== ============== =================================================================
             **Operation Name**   **Operator**                                                   **Explanation**
    =========================== ============== =================================================================
                      less than      :math:`<`                                                Less than operator
                   greater than      :math:`>`                                             Greater than operator
             less than or equal     :math:`<=`                                    Less than or equal to operator
          greater than or equal     :math:`>=`                                 Greater than or equal to operator
                          equal     :math:`==`                                                 Equality operator
                      not equal     :math:`!=`                                                Not equal operator
                    logical and     :math:`&&`                          Both operands True for result to be True
                     logical or     :math:`||`        One or the other operand is True for the result to be True
                    logical not      :math:`!`   Negates the truth value, False becomes True, True becomes False
    =========================== ============== =================================================================


.. tabbed:: change_this

  .. tab:: C++

    .. activecode:: intro_2cpp
        :caption: Basic Relational and Logical Operators C++
        :language: cpp

        #include <iostream>
        #include <cmath>
        using namespace std;

        int main(){

            cout << (5==10) << endl;
            cout << (10 > 5) << endl;
            cout << (5 >= 1 && 5 <= 10) << endl;

            return 0;
        }

  .. tab:: Python

    .. activecode:: intro_2py
        :caption: Basic Relational and Logical Operators Python

        def main():

            print(5==10)
            print(10 > 5)
            print((5 >= 1) and (5 <= 10))

        main()

A C++ variable is created when a name is used for the first time after declaring a type on
the left-hand side of an assignment statement. Assignment statements
provide a way to associate a name with a value. The variable will hold a
piece of data. Consider the
following session:

.. activecode:: introcpp
    :language: cpp

    #include <iostream>
    using namespace std;

    int main(){

        int theSum = 0;
        cout << theSum << endl;

        theSum = theSum + 1;
        cout << theSum << endl;

        bool theBool = true;
        cout << theBool << endl;

        return 0;
    }

The assignment statement ``int theSum = 0;`` creates a variable called
``theSum`` and lets it hold the data object ``0`` (see
:ref:`Figure 3 <fig_assignment1>`). In general, the right-hand side of the assignment
statement is evaluated and the resulting data object is
“assigned” to the name on the left-hand side. At this point in our
example, the type of the variable is integer as that is the type of the
data currently being referred to by ``theSum``. If the type of the data
changes, as shown above with the boolean
value ``True``, so does the type of the variable (``theSum`` is now of
the type boolean). The assignment statement changes value being
held by the variable. This is a static characteristic of C++. A
variable can hold only one type of data.

.. _fig_assignment1:

.. figure:: Figures/assignment1.png
   :align: center

   Figure 3: Variables Hold Data Objects

Introduction to Pointers
^^^^^^^^^^^^^^^^^^^^^^^^

The kind of variables we have already used are really identifiers that refer to where in memory we store information. We can store things as basic as integers and double precision floating point numbers, or things more complicated as structure and classes. Whenever we want the information, we can simply use the identifier to access it.

Let's look at a simple example of storing an integer. The following code declares a variable called *varName* that has in it a value of 100.

::

    // variable declaration for a single integer value
    int varName = 100;

The results of this code may look like the diagram below:

.. _fig_point1:

.. figure:: Figures/point1.gif
   :align: center
   :alt: image

   Figure 4: FIXME

When we want to output the value to the console, we use the variable name to do so:

::

    // print out the value we stored to the console, assuming that we
    // included the correct headers that define what cout does
    cout << varName << endl;

An important question is: Is this method of declaring variables sophisticated enough to handle all the problems we want to solve using programs?

The answer to that question is due to the way that arrays are stored in memory. Although the full details are complicated, the simple answer is that each program is given a specific amount of memory space to run. All statically allocated and locally declared variables are stored in this region, as well as all occurrences of the functions as the program is running. There is enough storage room available for simple variables, but arrays can be of arbitrary size, so there is a limit to how large they can be...otherwise they could crowd out the other variables and executable code in the program.

So where do large arrays get stored? In a region of memory called the heap, where space can be allocated when needed and then freed when you are done.

Once we reserve space to hold data, we store the location of this data in a special variable called a pointer.

We will talk about how to declare a variable to be a pointer first and then show pictorially what is happening.

Pointer Syntax
--------------

When declaring a pointer that will "point" to the memory address of some data type, you use the same rules of declaring variables and data types. The key difference is that there is an asterisk (*) between the data type and the identifier.

::

    variableType *identifier; // syntax to declare a pointer
    int *ptrx; // example of a pointer to an integer

White space in C++ generally does not matter, so the following pointer declarations are identical:

::

    SOMETYPE *variablename;
    SOMETYPE * variablename;
    SOMETYPE* variablename;

However, the first declaration is preferable in each case, as it is clear to the programmer that the variable is in fact a pointer because the asterisk is closer to the variable name.

The Address Operator: One simple way to get the pointer information into a pointer
----------------------------------------------------------------------------------

Ok, now that we know how to declare pointers, how do we give them the address of where the value is going to be stored? One way to do this is to have a pointer refer to another variable by using the address operator, which is denoted by the ampersand symbol, &. The address operator does exactly what it indicates, namely it returns the address of either (1) a variable, (2) a symbolic constant or (3) a element in an array.

The syntax is shown below, where varName stores the value, and varPntr stores the address of where varName is located:

::

    variableType value;  // a variable to hold the value
    variableType *pointer = &value;  // a variable to hold the address for varName

Keep in mind that when declaring a pointer, the pointer needs to be of the same type as the variable or constant to which it points.

Expanding on the example above where varName has the value of 100.

::

    //variable declaration for a single integer value
    int varName = 100;
    int* varPntr;
    varPntr = &varName;

The results of this code may look like the diagram below.

.. _fig_point2:

.. figure:: Figures/point2.gif
   :align: center
   :alt: image

   Figure 5: FIXME2

Accessing Values from SIMPLE Pointers
-------------------------------------

So, once you have a pointer, how do you access the values associated with that location? You use the asterisk before the pointer variable, which dereferences the pointer, meaning that it will find the location of the value stored where the pointer was referencing.

In other words, varName and \*varPntr (note the asterisk in front!) is the __same thing__ in the code above.

Let's extend the example above to output the value of a variable and its address in memory:

.. _lst_cppcode1:

    .. activecode:: examplecpp
        :language: cpp

        #include <iostream>
        using namespace std;

        int main( ) {
            int varName = 100;
            int *varPntr = &varName;

            cout << "the variable varName has the value: " << varName << endl;
            cout << "varPntr says varName is located at: " << varPntr << endl;
            cout << "the thing that varPntr is pointing to (varName) has the value: " << *varPntr << "\n\n";

            varName = 50;

            cout << "After changing varName, its value is now: " << varName << endl;
            cout << "varPntr is now pointing to a variable that has the value: " << *varPntr << "\n\n";

            *varPntr = 2000;
            cout << "After changing *varPntr, varName now has: " << varName << endl;
            cout << "varPntr is now pointing to a variable that has the value: " << *varPntr << endl;

            return 0;
        }

Compiling and running the above code will have the program output the value in varName, what is in varPntr (the memory address of varName), and what value is located at that memory location.

The second output sentence is the address of varName, which would most likely be different if you run the program on your machine.

WARNING: What happens if you forget the asterisk when assigning a value to a pointer and had the following instructions instead?

::

    varPntr = 2000; // Notice that I forgot the asterisk, so varPntr is now referring

    // to position 2000 in memory, whatever happens to be there
    cout << "After changing \*varPntr, varName now has: " << varName << endl; cout << "varPntr is now pointing to a variable that has the value: " << \*varPntr << endl;

**This is BAD BAD!**

.. _fig_point3:

.. figure:: Figures/point3.gif
   :align: center
   :alt: image

   Figure 6: FIXME3

If your compiler does not catch that error (the one for this class may), the first ``cout`` instruction outputs

::

    After changing *varPntr, varName now has: 50

which is expected because you changed where varPntr pointing to and NOT the contents of where it is pointing.

The second cout instruction is a disaster because (1) You don't know what is stored in location 2000 in memory, and (2) that location is outside of your segment (area in memory reserved for your program), so the operating system will jump in with a message about a "segmentation fault". Although such an error message looks bad, a "seg fault" is in fact a helpful error because unlike the elusive logical errors, the reason is fairly localized.

The Null pointer; another simple way to get the pointer information into a pointer
----------------------------------------------------------------------------------

The null pointer points to nothing and is often denoted by 0 or the keyword null. The null pointer is often used in conditions and/or in logical operations.

The following example demonstrates how the null pointer works. The variable ptrx initially has the address of x when it is declared. On the first iteration of the loop, it is assigned the value of zero (i.e. null) thereby ending the loop:

.. _lst_cppcode2:

    .. activecode:: examplecpp2
        :language: cpp

        #include <iostream>
        using namespace std;

        int main( ) {
            int x = 12345;
            int *ptrx = &x;

            while( ptrx ) {
            cout << "Pointer ptrx points to something\n";
            ptrx = 0;
            }

            cout << "Pointer ptrx points to nothing!\n";
        }

Helpful Tip: The null pointer becomes very useful when you must test the state of a pointer, such as whether the assignment to an address was valid or not.

Collection Data Types
^^^^^^^^^^^^^^^^^^^^^

In addition to the numeric and boolean classes, C++ has a number of
very powerful built-in collection classes. Arrays, strings, and tuples
are ordered collections that are very similar in general structure but
have specific differences that must be understood for them to be used
properly. Sets and hash tables are unordered collections.

An **array** is an ordered collection of zero or more C++ data objects of similar type.
Arrays are written as comma-delimited values enclosed in
curly brackets. Arrays are homogeneous, meaning that the data objects all need to be from the
same class and the collection can be assigned to a variable as below.
The following fragment shows a variety of C++ data objects in an array.

::

    >>> int arr[] = {1, 2, 3, 4};
    >>> char arr2[] = {'a', 'b', 'c'};
    >>> string arr3[] = {"this", "is", "an", "array"};

In order to remember the array for later processing, its
reference needs to be assigned to a variable.

Note that the indices for arrays (sequences) start counting with 0.
Sometimes, you will want to initialize an array. For example,

::

    >>> int myList[6] = { };
    >>> myList
    [0, 0, 0, 0, 0, 0]

**Strings** are sequential collections of zero or more letters, numbers
and other symbols. We can get strings from the Standard template library with ``#include <string>`` We call these letters, numbers and other symbols
*characters*. Literal string values are differentiated from identifiers
by using double quotation marks.

::

    >>> string myName = "David";
    >>> myName[3];
    'i'
    >>> myName.length()
    5

Since strings are sequences, all of the sequence operations described
above work as you would expect. In addition, strings have a number of
methods, some of which are shown in :ref:`Table 4<tab_stringmethods>`.

.. _tab_stringmethods:

.. table:: **Table 4: Methods Provided by Strings in Python**

    ======================== ================================ =============================================================
             **Method Name**                   **Use**                                               **Explanation**
    ======================== ================================ =============================================================
                  ``append``       ``astring.append(string)``                        Append to string the end of the string
               ``push_back``      ``astring.push_back(char)``                  Appends a character to the end of the string
                ``pop_back``           ``astring.pop_back()``         Deletes the last character from the end of the string
                  ``insert``    ``astring.insert(i, string)``                          Inserts a string at a specific index
                   ``erase``          ``astring.erase(i, i)``                   Erases an element from one index to another
                    ``find``           ``astring.find(item)``         Returns the index of the first occurrence of ``item``
    ======================== ================================ =============================================================


A major difference between arrays and strings is that arrays can be
modified while strings cannot. This is referred to as **mutability**.
arrays are mutable; strings are immutable. For example, you can change an
item in a list by using indexing and assignment. With a string that
change is not allowed.

**Tuples** are very similar to arrays in that they are sequential containers.
We can get a tuple from the Standard template library with
``#include <tuple>`` The difference is that a tuple is immutable, like a
string. A tuple cannot be changed. Tuples are written as comma-delimited
values enclosed in parentheses. For example,

::

    >>> myTuple = (2, 3, 4.96)
    >>> myTuple
    (2, True, 4.96)
    >>> get<0>(myTuple);
    2

A **set** is an unordered collection of zero or more immutable C++ data
objects. We can get a set from the Standard template library with ``#include <set>``. Sets do not allow duplicates and are written as comma-delimited
values enclosed in curly braces. The collection can be assigned to
a variable as shown below.

::

    >>> set<int> mySet = {3, 6, 4, 78, 10}
    {3, 6, 4, 78, 10}

Sets support a number of methods that should be familiar to those who
have worked with them in a mathematics setting. :ref:`Table 6 <tab_setmethods>`
provides a summary. Examples of their use follow.

.. _tab_setmethods:

.. table:: **Table 6: Methods Provided by Sets in C++**

    ======================== ================================= ================================================================
             **Method Name**                           **Use**                                                  **Explanation**
    ======================== ================================= ================================================================
                   ``union``                   ``set_union()``               Returns a new set with all elements from both sets
            ``intersection``            ``set_intersection()``   Returns a new set with only those elements common to both sets
              ``difference``              ``set_difference()``    Returns a new set with all items from first set not in second
                     ``add``             ``aset.insert(item)``                                             Adds item to the set
                  ``remove``              ``aset.erase(item)``                                        Removes item from the set
                   ``clear``                  ``aset.clear()``                                Removes all elements from the set
    ======================== ================================= ================================================================

Our final C++ collection is an unordered structure called a
**Hash Table**. Hash Tables are collections of associated pairs of
items where each pair consists of a key and a value. This key-value pair
is typically written as key=value. For example,

::

    >>> unordered_map<string, string> capitals;
    >>> capitals["Iowa"] = "DesMoines";
    >>> capitals["Wisconsin"] = "Madison";


We can manipulate a dictionary by accessing a value via its key or by
adding another key-value pair. The syntax for access looks much like a
sequence access except that instead of using the index of the item we
use the key value. To add a new value is similar.

.. tabbed:: edit

    .. tab:: C++

        .. activecode:: intro_7cpp
            :caption: Using a Hash Table C++
            :language: cpp

            #include <iostream>
            #include <map>
            #include <string>
            using namespace std;

            int main() {
                map<string, string> capitals;

                capitals["Iowa"] = "Desmoines";
                capitals["Wisconsin"] = "Madison";
                cout << capitals["Iowa"] << endl;
                capitals["Utah"] = "SaltLakeCity";

                capitals["California"] = "Sacramento";
                cout << capitals.size() << endl;

                for (map<string, string>::iterator it=capitals.begin(); it!=capitals.end(); ++it){
                    cout << it->second << " is the capital of " << it->first << '\n';
                }
            }

    .. tab:: Python

        .. activecode:: intro_7py
            :caption: Using a Dictionary

            capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
            print(capitals['Iowa'])
            capitals['Utah']='SaltLakeCity'
            capitals['California']='Sacramento'
            print(len(capitals))
            for k in capitals:
                print(capitals[k]," is the capital of ", k)

It is important to note that the hash table is maintained in no
particular order with respect to the keys. The first pair added
(``'Utah':`` ``'SaltLakeCity'``) was placed first in the dictionary and
the second pair added (``'California':`` ``'Sacramento'``) was placed
last. The placement of a key is dependent on the idea of “hashing,”
which will be explained in more detail in Chapter 4. We also show the
size function performing the same role as with previous collections.

Hash Tables have both methods and operators. :ref:`Table 7 <tab_dictopers>` describes them, and the session shows them in action. The
``keys``, ``values``, and ``items`` methods all return objects that
contain the values of interest. You will also see that there are two variations
on the ``get`` method. If the key is not present in the dictionary,
``get`` will return ``None``. However, a second, optional parameter can
specify a return value instead.

.. _tab_dictopers:

.. table:: **Table 7: Operators Provided by Hash Tables in C++**

    ===================== ========================= =====================================================================
             **Operator**            **Use**                                                       **Explanation**
    ===================== ========================= =====================================================================
                   ``[]``             ``myDict[k]``      Returns the value associated with ``k``, otherwise it's an error
                ``count``     ``myDict.count(key)``   Returns ``True`` if key is in the   dictionary, ``False`` otherwise
                ``erase``     ``myDict.erase(key)``                                Removes the entry from the  dictionary
    ===================== ========================= =====================================================================
