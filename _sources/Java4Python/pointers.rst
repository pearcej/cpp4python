Introduction to Pointers
========================

The kind of variables we have already used are really identifiers that refer to where in memory we store information. We can store things as basic as integers and double precision floating point numbers, or things more complicated as structure and classes. Whenever we want the information, we can simply use the identifier to access it.

Let's look at a simple example of storing an integer. The following code declares a variable called varName that has in it a value of 100.

::

    // variable declaration for a single integer value
    int varName = 100;


The results of this code may look like the diagram to the below:

|assign|

When we want to output the value to the console, we use the variable name to do so:

::

    // print out the value we stored to the console, assuming that we
    // included the correct headers that define what cout does
    cout << varName << endl;




An important question is: Is this method of declaring variables sophisticated enough to handle all the problems we want to solve using programs?

The answer to that question is due to the way that arrays are stored in memory. Although the full details are complicated; the simple answer is that each program is given a specific amount of memory space to run. All statically allocated and locally declared variables are stored in this region, as well as all occurrences of the functions as the program is running. There is enough storage room available for simple variables, but arrays can be of arbitrary size, so there is a limit to how large they can be...otherwise they could crowd out the other variables and executable code in the program.

So where do large arrays get stored? In a region of memory called the heap, where space can be allocated when needed and then freed when you are done.

Once we reserve space to hold data, we store the location of this data in a special variable called a pointer.

We will talk about how to declare a variable to be a pointer first and then show pictorially what is happening.

Pointer Syntax
--------------
When declaring a pointer that will "point" to an the memory address of some data type, you use the same rules of declaring variables and data types. The key difference is that there is an asterisk () between the data type and the identifier.

::

    variableType identifier; // syntax to declare a pointer
    int ptrx; // example of a pointer to an integer




White space in C++ generally does not matter, so the following pointer declarations are identical:

::

    SOMETYPE variablename;
    SOMETYPE  variablename;
    SOMETYPE variablename;




However, the first declaration is preferable in each case, as it is clear to the programmer that the variable is in fact a pointer because the asterisk is closer to the variable name.



The Address Operator: One simple way to get the pointer information into a pointer
----------------------------------------------------------------------------------

Ok, now that we know how to declare pointers, how do we give them the address of where the value is going to be stored? One way to do this is to have a pointer refer to another variable by using the address operator, which is denoted by the ampersand symbol, &. The address operator does exactly what it indicates, namely it returns the address of either (1) a variable, (2) a symbolic constant or (3) a element in an array.

The syntax is shown below, where varName stores the value, and varPntr stores the address of where varName is located: >

::

    variableType value;// a variable to hold the value
    variableType pointer = &value; // a variable to hold the address for varName



Keep in mind that when declaring a pointer, the pointer needs to be of the same type as the variable or constant to which it points.

::

 **variable declaration for a single integer value**

    int varName = 100;
    int* varPntr;
    varPntr = &varName;



The results of this code may look like the diagram below.

|pointer|

*

Accessing Values from SIMPLE Pointers
-------------------------------------

So, once you have a pointer, how do you access the values associated with that location? You use the asterix before the pointer variable, which dereferences the pointer, meaning that it will find the location of the value stored where the pointer was referencing.

In other words, varName and varPntr (note the asterix in front!) is the same thing in the code above.

Let's extend the example above to output the value of a variable and its address in memory:

::

    #include <iostream>
    using namespace std;

    int main( ) {
     int varName = 100;
     int varPntr = &varName;

     cout << "the variable varName has the value: " << varName << endl;
     cout << "varPntr says varName is located at: " << varPntr << endl;
     cout << "the thing that varPntr is pointing to (varName) has the value: " << varPntr << "\n\n";

     varName = 50;

     cout << "After changing varName, its value is now: " << varName << endl;
     cout << "varPntr is now pointing to a variable that has the value: " << varPntr << "\n\n";

     varPntr = 2000;
     cout << "After changing varPntr, varName now has: " << varName << endl;
     cout << "varPntr is now pointing to a variable that has the value: " << varPntr << endl;

    }



Compiling and running the above code will have the program output the value in varName, what is in varPntr (the memory address of varName), and what value is located at that memory location. Thus the output is:

::

     the variable varName has the value: 100
     varPntr says varName is located at: 0x22ff7c
     the thing that varPntr is pointing to (varName) has the value: 100

     After changing varName, its value is now: 50
     varPntr is now pointing to a variable that has the value: 50

     After changing varPntr, varName now has: 2000
     varPntr is now pointing to a variable that has the value: 2000



The second output sentence is the address of varName, which would most likely be different if you run the program on your machine.

**WARNING** What happens if you forget the asterisk when assigning a value to a pointer and had the following instructions instead?

::

    varPntr = 2000;
    // Notice that I forgot the asterix, so varPntr is now referring
    // to position 2000 in memory, whatever happens to be there
    cout << "After changing varPntr, varName now has: " << varName << endl;
    cout << "varPntr is now pointing to a variable that has the value: " << varPntr << endl;



This is BAD BAD!
----------------

|badpointer|

::

    After changing varPntr, varName now has: 50



which is expected because you changed where varPntr pointing to and NOT the contents of where it is pointing.

The second cout instruction is a disaster because (1) You don't know what is stored in location 2000 in memory, and (2) that location is outside of your segment (area in memory reserved for your program), so the operating system will jump in with a message about a "segmentation fault". Although such an error message looks bad, a "seg fault" is in fact a helpful error because unlike the elusive logical errors, the reason is fairly localized.



The Null pointer; another simple way to get the pointer information into a pointer
----------------------------------------------------------------------------------

The null pointer points to nothing and is often denoted by 0 or the keyword null. The null pointer is often used in conditions and/or in logical operations.

The following example demonstrates how the null pointer works. The variable ptrx initially has the address of x when it is declared. On the first iteration of the loop, it is assigned the value of zero (i.e. null) thereby ending the loop:

::

    #include <iostream>
    using namespace std;

    int main( ) {
     int x = 12345;
     int ptrx = &x;

     while( ptrx ) {
     cout << "Pointer ptrx points to something\n";
     ptrx = 0;
     }

     cout << "Pointer ptrx points to nothing!\n";
    }




Helpful Tip: The null pointer becomes very useful when you must test the state of a pointer, such as whether the assignment to an address was valid or not.



Dynamically Allocated 1D Arrays
-------------------------------

In other assignments, you have worked with statically allocated arrays. This technique has the advantage that it is easier to implement, but it suffers from the fact that (1) you need to know the size when the program was compiled, which is sometimes a very bad guess, and (2) the size of the array cannot change, which is VERY limiting.

   If your program does not use all the space you saved for an array, it is wasting space.
   If the array needs to be larger, you are out of luck.

Dynamic memory allocation for arrays enables the program to allocate exactly the amount of space needed when it is needed.

The new Operator
----------------

The key here is that the address operator (the ampersand detailed above) is NOT the only operator that you can use to assign an address to a pointer. In C++, there is the new operator that allocates a block of space in memory for a data type (built-in or user defined) and returns a pointer to that block of data.

If the new operator is for a pointer to an array, the returned address is to the first element. The rest of the array can be accessed using indexing as in the case with statically allocated arrays.

Suppose you want to create an integer array of a size that is input from the user. A sample sequence of instructions could be as follows:

1.  Declare the array as a pointer with no initial address (also the variable to hold the number of elements). Note that the value in array is garbage and invalid:

::

    int array;
    int size;



2.  Get input from the user on the number of elements:

::

    cout << "Size? ";
    cin >> size;




3.  Use the new operator to create the array with size elements:

::

    array = new int[size];



If the new operator is successful, the value of array is not null. If, on the other hand, something went wrong, then array would have the value null.

A common way to check program execution is to include statements that see if allocation succeeds and warns the user or aborts the program when it fails:

::

    void worked() {
     int array = new int[size];
     if( array == NULL ) {
     cout << "new operator for array failed!\n";
     exit(1);
     }
    }




WARNING:

1.  The new operator finds an essentially arbitrary area in memory to hold the allocated array, so you cannot assume to know what the address is, even between two consecutive runs of the program!
2.  If you invoke the new operator twice on the same pointer variable without storing the value of the address on the first call, the block of data you allocated will be lost:

::

    array = new int[size]; // array now holds (0xADDRESS), the address of an array
    array = new int[size]; // array now holds (0xHEXNUM), a different address for the array



Pictorally, it looks like this:

First call to new

|oops1|

Second call to new

|oops2|

Once this happens, the block of memory starting at 0xADDRESS is "lost" because the reference to that address is gone. By the way, repeated errors like this (such as in a loop) will result in more and more of memory reserved and not used... too much can crash your machine!

Delete Operator
---------------

The natural counterpart to this allocation is "deallocation", where memory that was reserved for the variable is freed and allowed to be used by other programs if necessary. The delete operator is used in front of a pointer to free up the address in memory to which the pointer is pointing:

::

    delete array;



Why is the delete operator needed? Any allocation of memory needs to be properly deallocated or a phenomena called a **memory leak** may occur. When your program ends without deleting dynamically allocated variables, the computer still will think that the memory taken up by these variables is still used. Because your program is no longer running, however, this occupied space is used by no one, so it "leaked" and it lost. When you run your program again and it attempts to allocate space for variables, it will take space from the memory that is left.

If either the variable takes a lot of space or you run your program many times, it is possible run out of free space, again, crashing your computer.

Therefore, it is a good practice that every time you use the new operator in your program to allocated space for a variable, use the delete operator to free that memory before the program ends. POINTERS:

1.  The delete operator can be used to both "delete" a pointer to an address returned by a call to the new operator and to "delete" a null pointer. Depending on how the compiler was designed, trying to delete the pointer to the same address location more than once can result in a runtime error. This implementation protects the programmer from making a common mistake of telling the computer to "delete" something that does not exist.
2.  The new and delete operators do not have to be used in conjunction with each other within the same function or block of code. A good practice to start now is to define separate member functions of a class using dynamically allocated variables to perform these operations. The destructor of the class is a typical place to put the delete statements.



Dynamically Allocated 2D (or more dimension) Arrays
---------------------------------------------------

One way to dynamically allocate a two-dimensional array (often called a matrix) involves declaring a dynamically allocated array like above, but rather than having the array store integers, it stores pointers to other arrays.

Yeah, a mind-bender, is it not?

::

    int  variableName;
    // Declare a pointer that references an array of pointers.



To allocate space for this kind of structure, the first step is to declare and allocate the array that will eventually contain the pointers:

::

    int size = 100;

    int twoDArray = new int [size];



This code says "create an array of 100 spots to hold pointers to integers", and is pictorially shown below.

|double1|

 The next stage is to allocate space for each row, which requires a loop of some kind to iterate through the rows and allocate as necessary. Suppose you want each row to have 30 elements. The code can look like:

::

    for (int i=0; i<size; i++ ) {
     twoDArray[i] = new int[30];
    }



This code will create 100 individually allocated rows capable of storing 30 items and is pictorally shown below.

|double2|

Note that each row is allocated in a potentially great distance from the ones before or after it, which is a difficult concept to come to terms with initially.

### Deleting 2D Arrays

Deallocating matrices involves freeing up all the rows individually, followed by freeing up the array that holds the rows in the first place.

The code to delete the array allocated above is in a sense the opposite operation, in which each row array is deleted before the main one is:

::

    for (int i=0; i<size; i++ ) {
     delete twoDArray[i];
    }
    delete twoDArray[]; // now, delete the array of pointers



Accessing Array Elements
------------------------

Suppose that you wanted to output the contents of a dynamically allocated array. The syntax is identical to performing the same task on a static array. In the case of a 1D array, the code to output the contents may look like the following:

::

    // assuming that the array myArray has been allocated with size
    // elements and populated with values.
    for( int i=0; i<size; i++ );
     cout << myArray[i] << endl;
    }



Accessing the data in the matrix is exactly the same as with a statically allocated array. The code

::

    twoDArray[40][25] = 50;



essentially states to go to the 40th element in the first reference, which is a pointer, and then travel down the second pointer to the array itself in memory to find the 25th item in that array.

.. |assign| IMAGE:: images\Assign.gif
.. |badpointer| IMAGE:: images\BadPointer.gif
.. |double1| IMAGE:: images\doubleAllocStage1.gif
.. |double2| IMAGE:: images\doubleAllocStage2.gif
.. |oops1| IMAGE:: images\oops_Allocation1.gif
.. |oops2| IMAGE:: images\oops_Allocation2.gif
.. |pointer| IMAGE:: images\Pointer.gif
