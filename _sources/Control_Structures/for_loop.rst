For Loops
=========

Even though the ``while`` type of construct is very useful in a wide variety of
situations, another iterative structure, the ``for`` statement, can be
used to iterate across a range of values easily. However, you must first find
the length of your container. For vectors, you can simply call the ``.length()`` function.
For arrays, the number of elements can be found by getting the size in memory of the array
by using the ``sizeof()`` function, and then dividing it by the size of the first element of
the array using the same ``sizeof()`` function. Because all elements in C++ arrays are
the same type, they take the same amount of space and that can be used to find the number
of elements the Array contains!

.. activecode:: arrayIteration1
   :language: cpp
   :sourcefile: ArrayIteration.cpp

   #include <iostream>
   using namespace std;

   int main() {
       int nums[] = {1,3,6,2,5};
       //Divide the size of the array (in bytes) by the size of a single element (in bytes)
       // to get the total number of elements in the array.
       int numsSize = sizeof(nums)/sizeof(nums[0]); // Get size of the nums array

       for (int index=0; index<numsSize; index++) {
           cout << nums[index] << endl;
       }


      // Simpler Implementation that may only work in
      // Newer versions of C++

      // for (int item:nums) {
      //     cout << item << endl;
      // }

  	return 0;
   }


An optional secondary version of the ``for`` loop has been commented out of the above code.
You can try running this in your version of C++ to see if it works, but in some older versions of C++,
such as C++98, it does not.

The above loop assigns the variable ``index`` to be each successive value from 0 to numsSize.
 Then, the value at that index in the array is printed to the console.

A common use of the ``for`` statement is to implement definite iteration
over a range of values. The code

.. activecode:: rangeForLoop1
   :language: cpp

   #include <iostream>
   using namespace std;
    
    // squares the numebers in range 5
    // ex. 0*0, 1*1, 2*2 ... 
    int main() {
        for (int i=0; i<5; i++) {
            cout<<i*i<<endl;
        }

        return 0;
    }

will use ``cout`` five times.  The value of the variable ``i`` will
start at 0 and go through the full sequence of values 0,1,2,3,4.  This
valu e is then squared and printed.

The other very useful version of this iteration structure is used to
process each character of a string. The following code fragment iterates
over a list of strings and for each string processes each character by
appending it to a list. The result is a list of all the letters in all
of the words.

.. activecode:: intro_81
   :language: cpp

   // Concatenates every character from a vector of strings
   // to another string, then prints it.
   #include <iostream>
   #include <vector>
   #include <string>
   using namespace std;

    int main() {
    	vector<string> wordList = {"cat", "dog", "rabbit"};
    	string letterlist;

    	for (size_t i = 0; i < wordList.size(); i++) {
    		for (size_t j = 0; j < wordList[i].size(); j++) {
                        letterlist.push_back(wordList[i][j]);
    		}
    	}

    	cout << letterlist << endl;
    }

Check yourself
==============

::

    #include <iostream>
    using namespace std;

    int main() {
    
        for (int counter=0; counter<4; counter++) {
            cout << counter * 2 << endl;
        }

        return 0;
    }

.. mchoice:: mc_forloop
  :answer_a: 0, 2, 4, 6
  :answer_b: 0, 0, 0, 0
  :answer_c: Runtime error
  :answer_d: 0, 1, 2, 3
  :correct: a
  :feedback_a: Good Job!
  :feedback_b: Not quite, take another look at the operation happening in the cout line 
  :feedback_c: Not quite, take another look at the for loop
  :feedback_d: Not quite, take another look at the operation happening in the cout line 

  Using the code above please select the answer that should appear?
