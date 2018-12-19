
Even though this type of construct is very useful in a wide variety of
situations, another iterative structure, the ``for`` statement, can be
used to iterate across a range of values easily. However, you must first find
the length of your container. For vectors, you can simply call the ``.length()`` function.
For arrays, the number of elements can be found by getting the size in memory of the array
by using the ``sizeof()`` function, and then dividing it by the size of the first element of
the array using the same ``sizeof()`` function. Because all elements in C++ arrays are
the same type, they take the same amount of space and that can be used to find the number
of elements the Array contains!

.. activecode:: arrayIteration
  :language: cpp
  :caption: Move across an Array of Integers

  #include <iostream>
  using namespace std;

  int main() {
  	int nums[] = {1,3,6,2,5};

      int numsSize = sizeof(nums)/sizeof(nums[0]); // Get size of the nums array

      for (int index=0; index<numsSize; index++) {
          cout<<nums[index]<<endl;
      }

      // Simpler Implementation that may only work in
      // Newer versions of C++

      // for (int item:nums) {
      //     cout<<item<<endl;
      // }

  	return 0;
  }

An optional secondary version of the ``for`` loop has been commented out of the above code.
You can try running this in your version of C++ to see if it works, but in some older versions of C++,
such as C++98, it does not.

The above loop assigns the variable ``index`` to be each successive value from 0 to numsSize.
 Then, the value at that index in the array is printed to the console.

A common use of the ``for`` statement is to implement definite iteration
over a range of values. The statement

.. activecode:: rangeForLoop
  :language: cpp

  #include <iostream>
  using namespace std;

  int main() {
  	for (int i=0; i<5; i++) {
          cout<<i*i<<endl;
      }

  	return 0;
  }

will perform the ``print`` function five times. The ``range`` function
will return a range object representing the sequence 0,1,2,3,4 and each
value will be assigned to the variable ``item``. This value is then
squared and printed.

The other very useful version of this iteration structure is used to
process each character of a string. The following code fragment iterates
over a list of strings and for each string processes each character by
appending it to a list. The result is a list of all the letters in all
of the words.

.. activecode:: intro_8
    :language: cpp
    :caption: Processing Each Character in a List of Strings

    #include <iostream>
    #include <string>
    using namespace std;

    int main() {
    	string wordList[] = {"cat", "dog", "rabbit"};
    	int wordListSize = sizeof(wordList) / sizeof(wordList[0]);

    	char letterlist[wordListSize];
    	int indx = 0;

    	for (int i = 0; i < wordListSize; i++) {
    		for (unsigned int j = 0; j < wordList[i].size(); j++) {
    			letterlist[indx] = wordList[i][j];
    			indx = indx + 1;
    		}
    	}

    	cout << letterlist << endl;
    }


Selection statements allow programmers to ask questions and then, based
on the result, perform different actions. Most programming languages
provide two versions of this useful construct: the ``ifelse`` and the
``if``. A simple example of a binary selection uses the ``if else``
statement.

::

    if (n<0){
        cout<<"Sorry, the value is negative"<<endl;
    } else {
        cout<<sqrt(n)<<endl;
    }

In this example, the object referred to by ``n`` is checked to see if it
is less than zero. If it is, a message is printed stating that it is
negative. If it is not, the statement performs the ``else`` clause and
computes the square root (a function from ``#include <cmath>``).

Selection constructs, as with any control construct, can be nested so
that the result of one question helps decide whether to ask the next.
For example, assume that ``score`` is a variable holding a reference to
a score for a computer science test.

::

    if (score >= 90) {
        cout << "A" << endl;
    } else {
        if (score >= 80) {
            cout << "B" << endl;
        } else {
            if (score >= 70) {
                cout << "C" << endl;
            } else {
                if (score >= 60) {
                    cout << "D" << endl;
                } else {
                    cout << "F" << endl;
                }
            }
        }
    }

This fragment will classify a value called ``score`` by printing the
letter grade earned. If the score is greater than or equal to 90, the
statement will print ``A``. If it is not (``else``), the next question
is asked. If the score is greater than or equal to 80 then it must be
between 80 and 89 since the answer to the first question was false. In
this case print ``B`` is printed. You can see that consistent
indentation helps to make sense of the association between
``if`` and ``else``.

An alternative syntax for this type of nested selection uses the
``else if`` keyword. The ``else`` and the next ``if`` are combined so as to
eliminate the need for additional nesting levels. Note that the final
``else`` is still necessary to provide the default case if all other
conditions fail.

::

    if (score >= 90) {
       cout << "A" <<endl;
    } else if (score >=80) {
       cout << "C" <<endl;
    } else if (score >= 70) {
       cout << "D" <<endl;
    } else if (score >= 60){
       cout << "E" <<endl;
    } else {
       cout << "F" <<endl;
    }

C++ also has a single way selection construct, the ``if`` statement.
With this statement, if the condition is true, an action is performed.
In the case where the condition is false, processing simply continues on
to the next statement after the ``if``. For example, the following
fragment will first check to see if the value of a variable ``n`` is
negative. If it is, then it is modified by the absolute value function.
Regardless, the next action is to compute the square root.

::

    if (n<0) {
       n = abs(n);
    }
    cout << sqrt(n) << endl;


.. admonition:: Self Check

    Test your understanding of what we have covered so far by trying the following
    exercise.  Modify the code from Activecode 3 so that the final list only contains
    a single copy of each letter.

    .. activecode:: self_check_1
      :language: cpp

       // the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
