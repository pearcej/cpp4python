..  Copyright (C)  Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
    4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Vectors
-------

**Vectors** are much more similar to Python lists than arrays are.
Vectors use a dynamically allocated array to store their elements,
so they can change size, and they have other friendly features as well.
Because they use a dynamically allocated array, they use contiguous storage locations
which means that their elements can be accessed and traversed, and they
can also be accessed randomly using indexes.
However, vectors are dynamically sized, so their size can change automatically.
A new element can be inserted into or deleted from any part of a vector,
and automatic reallocation for other existing items in the vector will be applied.
Unlike Python lists, vectors are homogeneous, so every element in the vector must be of the same type.

Vectors are a class that is available through a library called the Standard Template Library (STL), and one uses a ``< >``
notation to indicate the data type of the elements. In order to use vectors, One
needs to include the vector library.

::

    #include <vector>


.. _tbl_vectorbasics:

.. table:: **Common C++ Vector Operators**


    ===================== ============================= ====================================================
     **Vector Operation**                       **Use**                                      **Explanation**
    ===================== ============================= ====================================================
                  ``[ ]``               ``myvector[i]``                   access value of element at index i
                    ``=``         ``myvector[i]=value``                   assign value to element at index i
            ``push_back``    ``myvect.push_back(item)``            Appends item to the far end of the vector
             ``pop_back``         ``myvect.pop_back()``      Deletes last item (from  far end) of the vector
               ``insert``    ``myvect.insert(i, item)``                           Inserts an item at index i
                ``erase``           ``myvect.erase(i)``                       Erases an element from index i
                 ``size``             ``myvect.size()``             Returns the actual size used by elements
             ``capacity``         ``myvect.capacity()``       Returns the size of allocated storage capacity
              ``reserve``    ``myvect.reserve(amount)``               Request a change in capacity to amount
    ===================== ============================= ====================================================


A very common programming task is to grow a vector using the ``push_back()`` method to append to the vector
as we see in the next example.
Because vectors can change size, vectors typically allocate some extra storage to accommodate for possible growth.
Thus the vector typically has an actual *capacity* greater than the storage *size* strictly needed to contain its elements.


Matching
^^^^^^^^
.. dragndrop:: matching_vectors
   :feedback: Feedback shows incorrect matches.
   :match_1: [ ]|||Accesses value of an element. 
   :match_2: =||| Assigns value to an element. 
   :match_3: push_back|||Appends item to the end of the vector.
   :match_4: pop_back||| Deletes last item of the vector.
   :match_5: insert|||Injects an item into the vector. 
   :match_6: erase|||Deletes an element from the choosen index.
   :match_7: size|||Returns the actual capacity used by elements.
   :match_8: capacity|||Returns the ammount of allocated storage space.
   :match_9: reserve||| Request a change in space to amount

    Match the Vector operations with their corresponding explination. 

.. tabbed:: intro_vector

  .. tab:: C++

    .. activecode:: introvector_cpp
        :caption: Using a vector in C++
        :language: cpp

        #include <iostream>
        #include <vector>
        using namespace std;

        int main(){

            vector<int> intvector;
            intvector.reserve(50);

            for (int i=0; i<50; i++){
                intvector.push_back(i*i);
                cout << intvector[i] << endl;
            }
            return 0;
        }

  .. tab:: Python

    .. activecode:: introvector_py
        :caption: Using a Python list

        def main():
            intlist=[]
            for i in range(50):
                intlist.append(i*i)
                print(intlist[i])

        main()


In the above example, the use of ``reserve`` was optional. However, it is a good
idea to use it before growing a vector in this way because it will save time.
Because vectors are stored in underlying arrays which require contiguous memory,
every time the vector's size gets too large for the capacity, the entire vector must
be moved to a larger location in memory, and all that copying takes time.
In a typical implementation, the capacity is doubled each time. as in the
example that follows.


.. activecode:: vector_no_reserve_cpp
    :caption: With use of ``reserve``
    :language: cpp

    #include <iostream>
    #include <vector>
    using namespace std;

    int main(){

        vector<int> intvector;
        // without intvector.reserve(50);

        for (int i=0; i<50; i++){
            intvector.push_back(i*i);
            cout << intvector[i] << endl;
            cout << "capacity: " << intvector.capacity() << endl;
        }
        return 0;
    }


Remembering that C++ is designed for speed, not protection,
we will likely not be surprised by the following:

.. tabbed:: vector_errors

  .. tab:: C++

    .. activecode:: vector_errors_cpp
        :caption: Vectors out of bounds
        :language: cpp

        #include <iostream>
        #include <vector>
        using namespace std;

        int main(){

            vector<int> intvector;
            intvector.reserve(10);

            for (int i=0; i<10; i++){
                intvector.push_back(i);
            }

            for (int i=0; i<=10; i++){
                cout << "intvector[" << i << "]="<<intvector[i] << endl;
            }

            return 0;
        }

  .. tab:: Python

    .. activecode:: vector_errors_py
        :caption: Python list out of bounds

        def main():
            intlist=[]
            for i in range(10):
                intlist.append(i)

            for i in range(11):
                print("intlist[" + str(i) + "]=" + str(intlist[i]))

        main()



.. mchoice:: mc_array_vector
   :answer_a: Vectors can change size.
   :answer_b: Vectors offer all of the features and protections of Python lists
   :answer_c: Vectors don't use contiguous memory, so elements can be inserted.
   :answer_d: more than one of the above
   :answer_e: none of the above
   :correct: b
   :feedback_a: Right! Good job!
   :feedback_b: Not all of the protections of lists are offered by vectors; one can still iterate off of either end.
   :feedback_c: No. Although elements can be inserted in vectors, they do require contiguous memory.
   :feedback_d: No. Only one of the above is correct.
   :feedback_e: One of the above is indeed correct.

   Which of the following is the biggest difference between a C++ array and a C++ vector?


.. mchoice:: mc_vector1
   :answer_a: Nothing. It is completely optional.
   :answer_b: Using it will save time if you know the maximum size needed.
   :answer_c: It is required so memory can be allocated.
   :answer_d: none of the above
   :correct: b
   :feedback_a: It is optional but it does serve a purpose. Try again.
   :feedback_b: Right!
   :feedback_c: It is not required.
   :feedback_d: One of the above is indeed correct.

   What good is the ``reserve`` method in a vector?
