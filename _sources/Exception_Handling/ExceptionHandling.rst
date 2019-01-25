..  Copyright (C)  Jan Pearce and Brad Miller
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Exception Handling
~~~~~~~~~~~~~~~~~~

There are two types of errors that typically occur when writing
programs. The first, known as a **syntax error**, simply means that the
programmer has made a mistake in the structure of a statement or
expression. For example, it is incorrect to write a statement in one line and
forget the semicolon.

::

    int main() {
        int i = 10
        return 0;
    }

    >>  exit status 1
        main.cpp: In function 'int main()':
        main.cpp:3:5: error: expected ',' or ';' before 'return'
             return 0;
         ^~~~~~

In this case, the C++ compiler has found that it cannot complete
the processing of this instruction since it does not conform to the
rules of the language. Syntax errors are usually more frequent when you
are first learning a language.

The other type of error, known as a **logic error**, denotes a situation
where the program executes but gives the wrong result. This can be due
to an error in the underlying algorithm or an error in your translation
of that algorithm. In some cases, logic errors lead to very bad
situations such as trying to divide by zero or trying to access an item
in a list where the index of the item is outside the bounds of the list.
In this case, the logic error leads to a **runtime error** that causes the
program to terminate. These types of runtime errors are typically called
**exceptions**.

Most of the time, beginning programmers simply think of exceptions as
fatal runtime errors that cause the end of execution. However, most
programming languages provide a way to deal with these errors that will
allow the programmer to have some type of intervention if they so
choose. In addition, programmers can create their own exceptions if they
detect a situation in the program execution that warrants it.

When an exception occurs, we say that it has been “thrown.” You can
“catch” the exception that has been raised by using a ``try``
statement. For example, consider the following session that asks the
user for an integer and then uses the division operator.
If the user enters a second number that is not 0, then the print will show the result of division.
However, if the user enters 0, then C++ will throw an error and return a value other than 0.

::

    main.cpp: In function 'int main()':
    main.cpp:5:13: warning: division by zero [-Wdiv-by-zero]
       cout << 10/0;
               ~~^~
    exit status -1

We can handle this exception by creating a divide function that can
``throw`` an error. A corresponding ``try`` and ``catch`` block can “catch” the exception
and prints a message back to the user in the event that an exception
occurs. For example, try changing the values assigned to firstNum and secondNum
in the code below:

.. _lst_divisioncode:

  .. activecode:: divisionErr_cpp
    :caption: Error Handling for Division
    :language: cpp

    #include <iostream>
    using namespace std;

    double div(double num1, double num2) {
    	if (num2 == 0) {
    		// If the second number is 0, throw this error
    		throw "Cannot divide by 0!\n";
    	}

    	return num1 / num2;
    }

    int main() {
        // Get input from the user
    	float firstNum=10;
      float secondNum=0;

    	try {
    		// Attempt to divide the two numbers
    		double result = div(firstNum, secondNum);
    		cout << "result of division: " << result << endl;

    	} catch (const char *err) {
    		// If an error is thrown, print it
    		cout << err;
    	}

    	return 0;
    }

This will catch the fact that an exception is raised by ``div`` and will
instead print the error back to the user.
This means that the program will not terminate but instead will continue
on to the next statements.

It is also possible for a programmer to use nested try and except statements,
along with different thrown errors to manage what happens in their code. The program
will continue running after the error is caught, but we can stop this by returning
a value other than 0 in our main function. This is known as an ``error code``.

The code below should be run inside of a folder, and can be used to open files.
Ideally one of the files should be called "file.txt". The program will prompt
the user for a filename and can catch if that file does not exist or the default
"file.txt" does not exist. This is another useful application for Error handling.

::

    #include <fstream>
    #include <iostream>
    using namespace std;

    void printFile(char filename[32]) {
        ifstream in_stream;
        in_stream.open(filename);

        if (!in_stream.good()) {
            // Throws an error
                in_stream.close();

            throw "\nA file by that name does not exist!";
        }

        char ch;

        cout<<endl;
        while (!in_stream.eof()) {
            cout << ch;
            ch = in_stream.get();
        }
        cout << endl;

        in_stream.close();
    }

    int main() {
        char filename[32];
        cout << "Filename: ";
        cin >> filename;

        try {
            // Tries to print the file
            printFile(filename);
        } catch (const char *msg) {
            // Runs if error is thrown
            cerr << msg << endl;

            // Uses default file to print instead
            try {
                char defaultFile[32] = "file.txt";
                printFile(defaultFile);
            } catch (const char *msg) {
                cerr << "Default file not found!" << endl;
            }
        }

        return 0;
    }


There are many kinds of default exceptions that can be used in the C++ standard library.
See the C++ official documentation for a list
of all the available exception types and for how to create your own exception type.

Summary
~~~~~~~~~~~~

1. There are two types of errors that occur while writing programs: syntax errors and logic errors

2. A syntax error is an error that occurs due to typing error or wrong statement that is not allowed in a language. This can be easily caught as the program does not run until this is fixed.

3. Logic errors are errors happen not due to error in how the code is written, but because the code is producing an unintended or unexpected value such as a division by 0 leading to an undefined value.

4. logic errors can be caught by using ``try`` and ``catch`` which can help pinpoint what is causing the error and avoid confusion about the problem.


Check Yourself
~~~~~~~~~~~~~~

.. clickablearea:: syntax_error
    :question: There are two errors in the following code. Click on the syntax error.
    :iscode:
    :feedback: Remember, syntax errors occur more for people learning a new language.

    :click-incorrect:int age;:endclick:
    :click-incorrect:cout << "age:";:endclick:
    :click-incorrect:cin >> age;:endclick:
    :click-incorrect:if (age > 18) {:endclick:
    :click-incorrect:cout << "You can vote in the U.S!";}:endclick:
    :click-incorrect:else {:endclick:
    :click-correct:cout << You cannot vote in the U.S yet.;:endclick:
    }

.. clickablearea:: logic_error
    :question: There are two errors in the following code. Click on the logic error.
    :iscode:
    :feedback: If we want the code to say when we can vote, what cases should it say when can and cannot?

    :click-incorrect:int age;:endclick:
    :click-incorrect:cout << "age:";:endclick:
    :click-incorrect:cin >> age;:endclick:
    :click-correct:if (age > 18) {:endclick:
    :click-incorrect:cout << "You can vote in the U.S!";}:endclick:
    :click-incorrect:else {:endclick:
    :click-incorrect:cout << You cannot vote in the U.S yet.;:endclick:
    }
