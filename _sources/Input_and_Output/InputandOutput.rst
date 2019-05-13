..  Copyright (C) Jan Pearce and Brad Miller
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


File Handling
~~~~~~~~~~~~~

File handling in C++ also uses a ``stream`` in a similar way to the cout and cin functions of ``<iostream>``. The library that allows for input and output of files is ``<fstream>``.

You must declare any file streams before you use them to read and write data. For example, the following statements inform the compiler to create a stream called ``in_stream`` that is an input-file-stream object, ``<ifstream>``, and another called ``out_stream`` that is an output-file-stream object, ``<ofstream>``.

::

    ifstream in_stream;
    ofstream out_stream;

Member Functions and Precision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function that is associated with a certain type of object is called a **member function** of that object. You have already used member functions ``setf(...)`` and ``precision(...)`` for formatting our output streams using ``cout``. These functions are included briefly below:

::

    // Use cout's member function "set flags", called setf
    // The argument here means to use a fixed point rather than scientific notation
    cout.setf(ios::fixed);

    // Use cout's setf function again, but this time
    // The argument tells cout to show the decimal point
    cout.setf(ios::showpoint);

    // Use cout's member function, called Precision
    // The argument indicated to display 2 digits of precision
    cout.precision(2);

File Operations
~~~~~~~~~~~~~~~

Having created a stream with the declaration above, we can connect it to a file (i.e. open the file) using the member function ``open(filename)``. For example, the following statement will allow the C++ program to open the file called "myFile.txt", assuming a file named that exists in the current directory, and connect ``in_stream`` to the beginning of the file:

::

    in_stream.open("myFile.txt");

Once connected, the program can read from that file. Pictorially, this is what happens:

.. _fig_read_read:

.. figure:: Figures/Read_Open.jpg
  :align: center
  :alt: image

the ``<ostream>`` class also has an ``open(filename)`` member function, but it is defined differently. Consider the following statement:

::

    out_stream.open("anotherFile.txt");

Pictorally, we get a stream of data flowing out of the program:

.. _fig_read_write:

.. figure:: Figures/Write_Open.jpg
  :align: center
  :alt: image

Because out_stream is an object of type ``<ostream>``, connecting it to the file named "anotherFile.txt" will create that file if it does not exist. If the file "anotherFile.txt" already exists, it will be wiped and replaced with whatever is fed into the output stream.

To disconnect the ``ifstream`` in_stream from whatever file it opened, we use it's ``close()`` member function:

::

    in_stream.close();

To close the file for ``out_stream``, we use its ``close()`` function, which also adds an end-of-file marker to indicate where the end of the file is:

::

    out_stream.close();

Dealing with I/O Failures
~~~~~~~~~~~~~~~~~~~~~~~~~

File operations, such as opening and closing files, are often a source of runtime
errors for various reasons. Well-written programs always should include error checking
and Handling routines for possible problems dealing with files. Error checking
and handling generally involves the programmer inserting statements in functions
that perform I/O to check if any of the operations have failed. In C (the predecessor to C++),
the system call to open a file returns a value after the function is called.
A negative number means the operation failed for some reason, which the program can
check to see if reading from a file is alright. In C++, a simple error checking mechanism
is provided by the member function ``fail()``:

::

    in_stream.fail();

This function returns ``true`` only if the previous stream operation for in_stream
was not successful, such as if we tried to open a non-existent file. If a failure has
occured, in_stream may be in a corrupted state and it is best not to attempt any more
operations with it.

The following example code fragment safely quits the program entirely in case an I/O operation fails:

.. raw :: html

    <div>
        <iframe height="400px" width="100%" src="https://repl.it/@CodyWMitchell/File-Handling-1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    </div>

After opening the "myFile.txt" file, the ``if`` conditional checks to see if there was an error. If so, the program will output the apologetic error message and then exit. The ``exit(1)`` function from the library ``cstdlib`` enables the program to terminate at that point and have it return a "1" versus a "0", indicating an Error has occurred.

For more on Error Handling, see section 1.11.

Reading and Writing with File Streams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As file I/O streams work in a similar way to ``cin`` and ``cout``, the operators ">>" and "<<" perform the same direction of data for files, with the exact same syntax.

For example, execution of the following statement will write the number 25, a space, the number 15, and another space into the out_stream output stream.

::

    out_stream << 25 << endl;
    out_stream << 15 << endl;

The extra space after the value 25 is important because data in a text file is typically seperated by a space, tab, or newline. Without the space, the value 2515 will be placed in the file, and subsequent read operations on that file would consider 2515 as a single value. For example, suppose that after the previous statement, the program opens the same file with the input stream in_stream. The following statement would put the number 25 into the variable ``inputn``.

::

    int inputn;
    in_stream >> inputn;

The End-Of-File (EOF) for Systems that Implement eof()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So far, the assumption was that the programmer knew exactly how much data to read from
an open file. However, it is common for a program to keep reading from a file without
any idea how much data exists. Most versions of C++ incorporate an end-of-file (EOF)
flag at the end of the file to let programs know when to stop.
Otherwise, they could read data from a different file that happened to be
right after it in the hard drive, which can be disastrous.

Many development environments have I/O libraries that define how the member
function eof() works for ifstream variables to test if this flag is set to ``true`` or ``false``. Typically, one would like to know when the EOF has not been reached, so a common way is a negative boolean value. An alternative implementation is to keep reading using the >> operator; if that operation was successful (i.e. there was something in the file that was read), this success is interpreted as a 1 (true).

Incidentally, that is why if you forget the second equals sign in a comparison
between a variable and a value, you are assigning the value to the variable,
which is a successful operation, which means the condition ends up evaluating to ``true``.

The following two code fragments highlight the possibilities:

Using the ``eof()`` member function

::

    while(!in_stream.eof()) {
        // statements to execute
        // while EOF has not been
        // reached
    }

Using the >> operator

::

    while(in_stream>>inputn) {
        // statements to execute
        // while reads are successful
    }

Here is an example of a program that essentially uses the second technique
mentioned above to read all the numbers in a file and output them in a neater format.
The ``while`` loop to scan through a file is located in the ``make_neat(...)`` function.

.. raw :: html

    <div>
        <iframe height="400px" width="100%" src="https://repl.it/@CodyWMitchell/File-Handling-2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    </div>

The input file ``rawdata.txt`` must be in the same directory (folder) as the program in order for it to open successfully. The program will create a file called "neat.dat" to output the results.

.. mchoice:: eofFirst
    :multiple_answers:
    :answer_a: To keep a program from writing into other files.
    :answer_b: To keep a program from stopping.
    :answer_c: To make sure you do not overflow into temporary buffer.
    :answer_d: To stop an input files stream.
    :correct: a,c,d
    :feedback_a: Yes, EOFs are intended to prevent the program from overwriting a file.
    :feedback_b: Not quite, the point of EOFs is to do the opposite.
    :feedback_c: Yes, EOFs prevent overflow into temporary buffer.
    :feedback_d: Yes, EOFs stop input file streams. 

    What are good use cases for EOFs in C++ programming?
    
Passing Streams as Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the above program, you see that the input and output streams are passed to the file
via ``pass by reference``. This fact may at first seem like a surprising choice
until you realize that a stream must be changed in order to read from it or write to it.
In other words, as streams "flow", they are changed.
For this reason, all streams will always be passed by reference.

File Names and C-Strings
~~~~~~~~~~~~~~~~~~~~~~~~

In modern versions of C++, you can use the <string> library for filenames,
but earlier versions of C++ required the use of C-strings.
The program above will try to open the file called "rawdata.txt" and
output its results to a file called "neat.dat" every time it runs,
which is not very flexible. Ideally, the user should be able to enter
filenames that the program will use instead of the same names.
We have previously talked about the ``char`` data type that allows users to store
and manipulate a single character at a time. A sequence of characters such as "myFileName.dat"
can be stored in an array of chars called a ``c-string``, which can be declared as follows:

::

    // Syntax: char C-string_name[LEN];
    // Example:
    char filename[16];

This declaration creates a variable called ``filename`` that can hold a string of
length up to ``16``-1 characters.
The square brackets after the variable name indicate to the compiler the maximum
number of character storage that is needed for the variable.
A ``\0`` or ``NULL`` character terminates the C-string, wo the system know how much of
the array is actually used.


    Warnings:
        1. The number of characters for a c-string must be one greater than the number of actual characters!
        2. Also, LEN must be an integer number or a declared const int, it cannot be a variable.

**C-strings** are an older type of string that was inherited from the C language, and people frequently refer to both types as "strings", which can be confusing.

Typically, `string` from the ``<string>`` library should be used in all other cases when not
working with file names or when a modern version of C+++ can be used.

Putting it all Together
~~~~~~~~~~~~~~~~~~~~~~~

The following program combines all of the elements above and asks the user for the input and output filenames. After testing for open failures, it will read three numbers from the input file and write the sum into the output file.

.. raw :: html

    <div>
        <iframe height="400px" width="100%" src="https://repl.it/@CodyWMitchell/File-Handling-3?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    </div>


Summary
~~~~~~~

1. File handling in C++ uses ``stream`` similar to cout and cin in ``<iosteam>`` library but is ``<fsream>`` for file stream.

2. ``ifstream in_stream`` creates an input stream object, in_stream, that can be used to input text from a file to C++.

3. ``ofstream out_stream`` creates an output stream object,out_steam, that can be used to write text from C++ to a file.

4. End-of-File or ``.eof()`` is a method for the instance variables of fstream, input and output stream objects, and can be used to carry out a task until a file has ended or do some task after a file has ended.


Check Yourself
~~~~~~~~~~~~~~


.. mchoice:: stream_library
   :multiple_answers:
   :answer_a: fstream
   :answer_b: ifstream
   :answer_c: ofstream
   :answer_d: iostream
   :correct: a,d
   :feedback_a: Yes, fstream is library for handling file input and output.
   :feedback_b: No, ifstream is an object type for handling input.
   :feedback_c: No, ofstream is an object type for handling output.
   :feedback_d: Yes, iostream is a library for handling console input and output.

   Which of the following are libraries for C++ input and output? (Choose all that are true.)


.. dragndrop:: dnd_streamuse
   :feedback: Which library is used for which task?
   :match_1: fstream|||I want to write to a file
   :match_2: iostream|||I want to write to the console

   Drag the corresponding library to what you would use it for.



.. fillintheblank:: file_reading

  Fill in the blank with the value of ``inputn`` when the following code runs.
  ::

      ifstream in_stream;
      ofstream out_stream;
      int inputn;

      out_stream.open("anotherFile.txt");
      out_stream << 25;
      out_stream << 15 << endl;
      out_stream << 101 << endl;

      in_stream.open("anotherFile.txt");
      in_stream >> inputn;
      cout << inputn;
      in_stream >> inputn;

  - :101: That is the correct answer! Good job!
    :25: No. Hint: ``inputn`` is changed twice.
    :2515: No. Hint: ``inputn`` is changed twice.
    :15: No. Hint: note that there is no space between the first 25 and 15!
    :.*: No. Hint: Observe what specific numbers are being written to the file!
