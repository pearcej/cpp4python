..  Copyright (C)  Jan Pearce and Brad Miller
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Strings
^^^^^^^
**Strings** are sequential collections of zero or more characters such as letters, numbers
and other symbols. There are actually two types of strings in C++ . The *C++ string* or just *string* from the
``<string>`` library is the more modern type, and it is very similar to the Python string class.
The old style *C-string* which is essentially
an array of ``char`` type. The char type itself is actually distinct from both types of strings.

::

    char cppchar = 'a';   // char values use single quotes
    string cppstring = "Hello World!";  // C++ strings use double quotes
    char cstring[] = {"Hello World!"};    // C-string or char array uses double quotes


In older versions of C++, you must use a ``char`` array to work with filenames. In modern
C++ (from C++11 onward), however, you can use a C++ string for everything.
Since C++ strings are so much nicer and similar to Python strings, I would not recommend using C-strings.

.. mchoice:: cstringquestion1_1
    :answer_a: An array of characters that ends with a terminating null character. i.e. \0
    :answer_b: A sequential data structure consisting of zero or more characters
    :answer_c: A data structure consisting of an ordered collection of data elements of identical type in which each element can be identified by an array index.
    :answer_d: sequence container storing data of a single type that is stored in a dynamically allocated array which can change in size.
    :correct: a
    :feedback_a: Correct! a c-string is different from a string
    :feedback_b: Close, but that is the definition of a string, not a c-string
    :feedback_c: Sorry, thats not a string or a c-string
    :feedback_d: No, that's a vector

    What is the correct definition of c-strings?

Because strings are sequences, all of the typical sequence operations work as you would expect.
In addition, the string library offers a huge number of
methods, some of the most useful of which are shown in :ref:`Table 4<tab_stringmethods>`.

.. _tab_stringmethods:

.. table:: **Table 4: String Methods Provided in C++**

    ===================  ==============================  =========================================================
        **Method Name**                         **Use**                                            **Explanation**
    ===================  ==============================  =========================================================
                ``[ ]``                  ``astring[i]``                       access value of character at index i
                  ``=``            ``astring[i]=value``                       change value of character at index i
                  ``+``          ``string1 + astring2``                                        concatenate strings
             ``append``      ``astring.append(string)``                  Appends a string to the end of the string
          ``push_back``     ``astring.push_back(char)``               Appends a character to the end of the string
           ``pop_back``          ``astring.pop_back()``      Deletes the last character from the end of the string
             ``insert``   ``astring.insert(i, string)``                       Inserts a string at a specific index
              ``erase``         ``astring.erase(i, j)``                Erases an element from one index to another
               ``find``          ``astring.find(item)``          Returns the index of the first occurrence of item
               ``size``              ``astring.size()``                             Returns the size of the string
    ===================  ==============================  =========================================================



Matching
========
.. dragndrop:: matching_strings
   :feedback: Feedback shows incorrect matches.
   :match_1: [ ]|||Accesses value of an element. 
   :match_2: =||| Assigns value to an element. 
   :match_3: push_back|||Adjoins a character to the end of the string.
   :match_4: pop_back|||Removes the last character from the end of the string.
   :match_5: insert|||Injects a string at a specific index. 
   :match_6: erase|||Deletes an element from one index to another.
   :match_7: size|||Returns the capacity of the string.
   :match_8: +|||connects strings.
   :match_9: append|||Adjoins a string to the end of the string.
   :match_10: find||| Returns the index of the first occurrence of item.

    Match the String operations with their corresponding explination. 

.. tabbed:: intro_string

  .. tab:: C++

    .. activecode:: introstring_cpp
        :caption: Strings in C++
        :language: cpp

        // This function concatenates the string hello World
        // Then it says where World begins in the concatenated string
        #include <iostream>
        #include <string>
        using namespace std;

        int main(){

            string mystring1 = "Hello";
            string mystring2 = "World!";
            string mystring3;

            mystring3 = mystring1 + " " + mystring2;
            cout << mystring3 << endl;

            cout << mystring2 << " begins at ";
            cout << mystring3.find(mystring2) << endl;

            return 0;
        }

  .. tab:: Python

    .. activecode:: introstring_py
        :caption: Python strings

        """This does the same thing as the C++ function """
        def main():
            mystring1 = "Hello"
            mystring2 = "World!"

            mystring3 = mystring1 + " " + mystring2
            print(mystring3)

            print(mystring2, end=" ")
            print("begins at", end=" ")
            print(str(mystring3.find(mystring2)))

        main()


Check your understanding by completing the following question.


.. dragndrop:: string_types
   :feedback: Feedback shows incorrect matches.
   :match_1: char|||'a'
   :match_2: char array|||{'a'}
   :match_3: string|||"a"


   Drag each data type to its' corresponding C++ initialization syntax.
