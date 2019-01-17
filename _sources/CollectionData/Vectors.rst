..  Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Vectors
-------

Vectors are similar to arrays in a way that they use contiguous storage locations,
which means that their elements can be accessed and traversed with the help of iterators, and they
can also be accessed randomly using indexes.

However, vectors have a dynamic size meaning that whenever a new element is inserted or deleted,
their size changes automatically. A new element can be inserted into or deleted from any part of a vector,
and automatic reallocation for other existing items in the vector is applied. Nevertheless, computing time for
insertion and deletion might differ depending on the location of the item, and how many items need to be
reallocated. For example, the last item in a vector is removed at a constant time, because no resizing of
the vector is needed for this operation, while an item is removed or inserted into the beginning or the
middle of a vector at a linear time.

Two common operations are indexing and assigning to an index position.
Both of these operations take the same amount of time no matter how
large the vector becomes. When an operation like this is independent of
the size of the vector they are :math:`O(1)`.

Another very common programming task is to grow a vector. There is one
way to create a longer  vector.  You can use the ``push_back()`` method. The ``push_back()`` method is :math:`O(1)`.

Let's look at two different ways we might generate an vector of ``n``
numbers starting with 0.

First we’ll try to the use ``push_back()`` method.  :ref:`Listing 3 <lst_mklistcpp>` shows the code for
making our vector.

.. _lst_mklistcpp:

**Listing 3**

::

    #include <iostream>
    #include <vector>
    using namespace std;

    void test1(){
        vector <int> vect;
        for (int i = 0; i < 1000; i++){
            vect.push_back(i);
        }
    }

    int main() {
        test1();
    }

To capture the time it takes for each of our functions to execute we
will use C++'s ``ctime`` module. The ``ctime`` module is designed
to allow C++ developers to make cross-platform timing measurements by
running functions in a consistent environment and using timing
mechanisms that are as similar as possible across operating systems.

To use ``ctime`` you create two ``clock`` objects. The first clock object marks the current time(start time); the second clock object marks the current time after the function runs a set number of times(end time). To get the total runtime, you subtract the start time from the end time to get the elapsed time. The following session shows how long it takes to run each
of our test functions 1000 times within a ``for`` loop.

.. activecode:: vectcpp2
    :language: cpp

    #include <iostream>
    #include <vector>
    using namespace std;

    void test1(){
        vector<int> vect;
        for (int i = 0; i < 1000; i++){
            vect.push_back(i);
        }
    }

    int main(){
        clock_t begin_t1 = clock();
        for (int i = 0; i < 1000; i++){
            test1();
        }
        clock_t end = clock();
        double elapsed_secs = double(end - begin_t1) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "push back " << elapsed_secs << " milliseconds" << endl;

        return 0;
    }

In the experiment above the statement that we are timing is the function
call to ``test1()``. From the experiment we see that the push_back operation at 0.018
milliseconds.

Now that we have seen how performance can be measured concretely you can
look at :ref:`Table 2 <tbl_listbigocpp>` to see the Big-O efficiency of all the
basic vector operations. When ``pop_back()`` is called, the element at the end of the vector is removed and it takes
:math:`O(1)` but when ``erase()`` is called on the first element in the vector
or anywhere in the middle it is :math:`O(n)`. The reason for this lies
in how C++ chooses to implement vectors. When an item is taken from the
front of the vector, in C++ implementation, all the other elements in
the vector are shifted one position closer to the beginning. This may seem
silly to you now, but if you look at :ref:`Table 2 <tbl_listbigocpp>` you will see
that this implementation also allows the index operation to be
:math:`O(1)`. This is a tradeoff that the C++ implementers thought
was a good one.


.. _tbl_listbigocpp:

.. table:: **Table 2: Big-O Efficiency of C++ Vector Operators**

    ================== ==================
             Operation   Big-O Efficiency
    ================== ==================
              index []               O(1)
      index assignment               O(1)
             push_back               O(1)
            pop_back()               O(1)
              erase(i)               O(n)
        insert(i,item)               O(n)
    ================== ==================

As a way of demonstrating this difference in performance let’s do
another experiment using the ``ctime`` module. Our goal is to be able
to verify the performance of the ``pop_back()`` operation on a vector of a known
size when the program pops from the end of the vector using ``pop_back()``, and again when the
program pops from the beginning of the vector using ``erase()``. We will also want to
measure this time for vectors of different sizes. What we would expect to
see is that the time required to pop from the end of the vector will stay
constant even as the vector grows in size, while the time to pop from the
beginning of the vector will continue to increase as the vector grows.

:ref:`Listing 4 <lst_popmeascpp>` shows one attempt to measure the difference
between the ``pop_back()`` and ``erase()``. As you can see from this first example,
popping from the end takes 0.000023 milliseconds, whereas popping from the
beginning takes 0.473672 milliseconds.

There are a couple of things to notice about :ref:`Listing 4 <lst_popmeascpp>`. This approach allows us to time just the single ``pop_back()`` statement
and get the most accurate measure of the time for that single operation.
Because the timer repeats 1000 times it is also important to point out
that the vector is decreasing in size by 1 each time through the loop. But
since the initial vector is two million elements in size we only reduce
the overall size by :math:`0.05\%`

.. _lst_popmeascpp:

**Listing 4**

.. activecode:: popbackvserase
    :language: cpp

    #include <iostream>
    #include <vector>
    using namespace std;

    int main(){
        vector<int> vect;
        vector<int> vect2;

        for (int i = 0; i < 1000; i++){
            vect.push_back(i);
        }

        for (int i = 0; i < 1000; i++){
            vect2.push_back(i);
        }

        clock_t begin = clock();
        for (int i = 0; i < 1000; i++){
            vect.erase(vect.begin()+0);
        }
        clock_t end = clock();
        double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "popzero = " << elapsed_secs << endl;

        clock_t begin2 = clock();
        for (int i = 0; i < 1000; i++){
            vect2.pop_back();
        }
        clock_t end2 = clock();
        double elapsed_secs2 = double(end2 - begin2) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "popend = " << elapsed_secs2 << endl;

        return 0;
    }
