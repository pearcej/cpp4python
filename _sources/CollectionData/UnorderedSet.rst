..  Copyright (C)  Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Unordered Sets
^^^^^^^^^^^^^^

An **unordered_set** is an unordered collection of zero or more unique C++ data values
of a particular type.
To use unordered_sets, you import ``unordered_set`` from the Standard template library with
``#include <unorderd_set>``.

Unordered_sets allow for fast retrieval of individual elements based on their value.
In an unordered_set, the value of an element is at the same time its key, that identifies it uniquely.
``Keys`` are **immutable**, therefore, the elements in an ``unordered_set`` cannot be modified once in the container -
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


Matching
========
.. dragndrop:: matching_us
   :feedback: Feedback shows incorrect matches.
   :match_1: union|||Returns a new set with all elements from both sets.
   :match_2: intersection|||Returns a new set with only those elements common to both sets.
   :match_3: difference||| Returns a new set with all items from first set not in second.
   :match_4: add|||Adds item to the set.
   :match_5: remove|||erases item from the set.
   :match_6: clear|||Removes all elements from the set.
   
    Match the Unordered Sets operations with their corresponding explination. 


Summary
^^^^^^^

1.  A statically allocated C++ array is an ordered collection of one or more C++ data values of identical type stored in contiguous memory.

2.  A vector is a dynamically allocated array with many useful methods. It is more similar to the Python list than the array.

3.  C++ strings are a sequential collection of zero or more characters. They are very similar to Python strings.

4.  A hash table is used to store keys-value pairs. It applies a related hash function to the key in order to compute the location of the associated value. Look-up is typically very fast.

5.  A set is an unordered collection of unique values.


Check Yourself
^^^^^^^^^^^^^^


.. mchoice:: mc_fixed
   :answer_a: array
   :answer_b: hash table
   :answer_c: string
   :answer_d: vector
   :answer_e: more than one of the above
   :correct: a
   :feedback_a: Correct!
   :feedback_b: No. hash tables are not ordered.
   :feedback_c: A string would only work for character data. Try again.
   :feedback_d: There is a better choice given that the group is fixed length
   :feedback_e: Only of the above is best.

   Which C++ structure is the best choice for a group of ordered data of a fixed length?



.. dragndrop:: collect_data_types
   :feedback: Feedback shows incorrect matches.
   :match_1: Array|||{“What”, “am”, “I”, "am"}
   :match_2: Set|||{“What”, “am”, “I”}
   :match_3: String|||“What am I”
   :match_4: Hash Table|||{{“What”, “am I”}}

   Drag each data type to its' corresponding C++ initialization syntax.
