..  Copyright (C)  Jan Pearce and Brad Miller
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Strings
^^^^^^^
**Strings** are sequential collections of zero or more letters, numbers
and other symbols. We can get strings from the library with ``#include <string>`` We call these letters, numbers and other symbols
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

C Strings and C++ String Objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Both the C and C++ cstring library functions are available to C++ programs. However, do not overlook the fact that these two function libraries are very different, and the functions of the first library have a different notion of what a string is from the corresponding notion held by the functions of the second library. There are two further complications: first, though a function from one of the libraries may have a counterpart in the other library (i.e., a function in the other library designed to perform the same operation), the functions may not be used in the same way, and may not even have the same name; second, because of backward compatibility many functions from the C++ String library can be expected to work fine and do the expected thing with C strings, but not the other way around.
The last statement above might seem to suggest we should use C++ Strings and forget about C-strings altogether, and it is certainly t rue that there is a wider variety of more intuitive operations available for C++ Strings. However, C-strings are more primitive, you may therefore find them simpler to use (provided you remember a few simple rules, such as the fact that the null character must always terminate such strings), and certainly if you read other, older programs you will see lots of C-strings. You should thus use whichever you find more convenient, but remember that they are very different; if you occasionally need to mix the two for some reason, be extra careful. Finally, there are certain situations in which C-Strings must be used as in the use of filenames as we have seen.


.. _tab_stringmethods2:

.. table:: **Table 5: String Methods in C++**

    ====================================== ================================================= ================================
                            **Categories**                     **C-Strings**                         **C++ Strings**
    ====================================== ================================================= ================================
                             Import Syntax                             ``#include<cstring>``             ``#include<string>``
                            Declare Syntax             ``char str[10];//can store <=9chars`` ``string str;//Unlimitedlength``
                       Initializing Syntax                 ``char str1[11] = "Call home!";``   ``string str1("Call home!");``
                       Initializing Syntax                  ``char str2[] = "Send money!";`` ``string str2 = "Send money!";``
                       Initializing Syntax               ``char str3[] = {'O', 'K', '\0'};``           ``string str3("OK");``
                       Initializing Syntax              ``// which has the same effect as:``        ``string str4(10, 'x');``
                       Initializing Syntax                           ``char str3[] = "OK";``          ``string str3 = "OK";``
            Concatenating/Combining Syntax                           ``strcat(str1, str2);``           ``str = str1 + str2;``
                          Comparing Syntax                   ``if(strcmp(str1, str2) < 0 )``            ``if( str1 < str2):``
                          Comparing Syntax                    ``cout<< "str1 comes first."``  ``cout<< "str1 comes first.";``
                          Comparing Syntax                  ``if(strstrcmp(str1, str2)==0)``            ``if( str1 == str2)``
                          Comparing Syntax                       ``cout<< "Equal Strings."``    ``cout << "Equal strings.";``
                          Comparing Syntax                   ``if(strstrcmp(str1, str2)>0)``           ``if( str1 > str2 ):``
                          Comparing Syntax                    ``cout<< "str2 comes first."``   ``cout<<"str2 comes first.";``
    ====================================== ================================================= ================================


A major difference between arrays and strings is that arrays can be
modified while strings cannot. This is referred to as **mutability**.
arrays are mutable; strings are immutable. For example, you can change an
item in a list by using indexing and assignment. With a string that
change is not allowed.

Tuples
^^^^^^

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

Sets
^^^^

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

Hash Tables
^^^^^^^^^^^
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



Collection Data Type Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. An array is an ordered collection of zero or more C++ data objects of identical type. It is used because it allows for the manipulation of collection of same data objects
and access of individual data objects within this collection.

2.  Strings are a sequential collection of zero or more letters, numbers ,or other symbols. A major difference between a string and array datatype is
that string cannot be manipulated while an array can be manipulated.

3. An alternative to C++ strings library is C-strings. C++ string does the same things as C Strings but the other way is not true.

4. The use of C-string comes when we want to do simpler tasks with strings as C-strings are more primitive in some cases.
