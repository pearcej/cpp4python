..  Copyright (C)  Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Hash Tables
^^^^^^^^^^^

If you have used a Python dictionary, then you have used a *hash table*.
A **hash table** is a collection of associated pairs of
items where each pair consists of a *key* and a *value*.
Hash tables are often called the more general term *map*
because the associated hash function "maps" the key to the value.
Nevertheless, it is much better to use the more precise term, *hash table*
because other kinds of maps are sometimes implemented with a different underlying data structure.

Each hash table has a *hash function* which
given the key as input to the hash function
returns the location of the associated value as the output.
This makes look up fast.

In Python, the dictionary data type represents the implementation of the hash table.
In C++, the *unordered_map* implements the hash table, andthe ``<unordered_map>``
library must be included as follows:

::

  #include <unordered_map>

The syntax for hash table access is much like we might expect
except that instead of using the index of the item for look-up, we
use the key. In both Python and C++, hash tables can be initialized with key-value pairs and
key-value pairs can also be added later as we see in the following example.
In C++, the keyword ``first`` is used for the key, and ``second`` is used for the
associated value.

.. tabbed:: hashtable1

    .. tab:: C++

        .. activecode:: hashtable1_cpp
            :caption: Using a Hash Table C++
            :language: cpp

            #include <iostream>
            #include <unordered_map>
            #include <string>
            using namespace std;

            int main() {
                unordered_map<string, string> spnumbers;

                spnumbers = {{"one", "uno"}, {"two", "dos"}};

                spnumbers["three"] = "tres";
                spnumbers["four"] = "cuatro";

                cout << "one is ";
                cout << spnumbers["one"] << endl;

                cout << spnumbers.size() << endl;
            }

    .. tab:: Python

        .. activecode:: hashtable1_py
            :caption: Using a Dictionary

            def main():
                spnumbers = {"one":"uno","two":"dos"}

                spnumbers["four"]="cuatro"
                spnumbers["three"]="tres"

                print("one is", end=" ")
                print(spnumbers["one"])

                print(len(spnumbers))
            main()


It is important to note that hash tables are organized by the location given
by the hash function rather than being in any
particular order with respect to the keys. This makes look-up extremely fast.
Hence, although it is possible to iterate through a hash table in both C++ and Python,
it is an odd thing to do
because the data is not typically stored sequentially.
Iterators of a ``unordered_map`` are
implemented using pointers to point to elements of the value type as we see in
the following example.

.. tabbed:: hashtable2

    .. tab:: C++

        .. activecode:: hashtable2_cpp
            :caption: Iterating a Hash Table C++
            :language: cpp

            #include <iostream>
            #include <unordered_map>
            #include <string>
            using namespace std;

            int main() {
                unordered_map<string, string> spnumbers;

                spnumbers = {{"one","uno"},{"two","dos"},{"three","tres"},{"four","cuatro"},{"five","cinco"}};

                for (auto i=spnumbers.begin(); i!=spnumbers.end(); i++ ){
                    cout << i->first << ":";
                    cout << i->second << endl;
                }
            }

    .. tab:: Python

        .. activecode:: hashtable2_py
            :caption: Iterating a Dictionary

            def main():
                spnumbers = {"one":"uno","two":"dos","three":"tres","four":"cuatro","five":"cinco" }

                for key in spnumbers:
                    print(key, end=":")
                    print(spnumbers[key])

            main()


Hash Tables have both methods and operators. :ref:`Table 7 <tab_hashopers>`
describes them, and the session shows them in action.

.. _tab_hashopers:

.. table:: **Table 7: Important Hash Table Operators Provided in C++**

    ===================== ========================= ================================================================
             **Operator**                   **Use**                                                  **Explanation**
    ===================== ========================= ================================================================
                 ``[ ]``               ``mymap[k]``  Returns the value associated with ``k``, otherwise throws error
                ``count``      ``mymap.count(key)``     Returns ``true`` if key is in ``mymap``, ``false`` otherwise
                ``erase``      ``mymap.erase(key)``                                 Removes the entry from ``mymap``
                ``begin``         ``mymap.begin()``                    An iterator to the first element in ``mymap``
                  ``end``        ``mymap.end(key)``        An iterator pointing to past-the-end element of ``mymap``
    ===================== ========================= ================================================================

Unordered Sets
^^^^^^^^^^^^^^

An **unordered_set** is an unordered collection of zero or more unique C++ data values
of a particular type.
To use unordered_sets, you import ``unordered_set`` from the Standard template library with
``#include <unorderd_set>``.

Unordered_sets allow for fast retrieval of individual elements based on their value.
In an unordered_set, the value of an element is at the same time its key, that identifies it uniquely.
``Keys`` are immutable, therefore, the elements in an ``unordered_set`` cannot be modified once in the container -
However, they can be inserted and removed.


Unordered sets do not allow duplicates and are initialized using comma-delimited
values enclosed in curly braces. The collection can be assigned to
a variable as shown below.


::

    set<int> mySet = {3, 6, 4, 78, 10}


Unordered sets support a number of methods that should be familiar to those who
have worked with sets in a mathematics setting. :ref:`Table 6 <tab_setmethods>`
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



Collection Data Type Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. A statically allocated C++ array is an ordered collection of one or more C++ data values of identical type stored in contiguous memory.

2. A vector is a dynamically allocated array with many useful methods. It is more similar to the Python list than the array.

3. C++ strings are a sequential collection of zero or more characters. They are very similar to Python strings.

4. A hash table is used to store keys-value pairs. It applies a related hash function to the key in order to compute the location of the associated value. Look-up is typically very fast.

5. A set is an unordered collection of unique values.
