..  Copyright (C)  Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Hash Tables
^^^^^^^^^^^

If you have used a Python dictionary, then you have used a *hash table*.
A **hash table** is a collection of associated pairs of
items where each pair consists of a *key* and a *value*.
Hash tables are often called the more general term *map*
because the associated hash function "maps" the key to the value.
Nevertheless, it is better to use the more precise term, *hash table*
because other kinds of maps are sometimes implemented with a different underlying data structure.

Each hash table has a *hash function* which
given the key as input to the hash function
returns the location of the associated value as the output.
This makes look up fast.

In Python, the dictionary data type represents the implementation of the hash table.
In C++, the *unordered_map* implements the hash table, and the ``<unordered_map>``
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
Iterators of an ``unordered_map`` are
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


Matching
========
.. dragndrop:: matching_HT
   :feedback: Feedback shows incorrect matches.
   :match_1: [ ]|||Returns the value associated with the key, otherwise throws error.
   :match_2: erase|||Deletes the entry from the hash table.
   :match_3: count|||Returns true if key is in the hash table, and false otherwise.
   :match_4: begin|||An iterator to the first element in the hash table.
   :match_5: end|||An iterator pointing to past-the-end element of the hash table.
   
    Match the Hash Table operations with their corresponding explination. 
