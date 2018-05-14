Common Mistakes
===============

We will be using the following code for illustration:


::

     #include <iostream>
     using namespace std;

     class calculations {

         public:
           int calculate(int first, int second){
             return (first * second);
             }
      };

     int main() {
       int first;
       int second;
       calculations x;

       cout << "Enter your numbers: " << endl;
       cin >> first >> second;

       cout << "The product is: " << x.calculate(first, second) << endl;
       return 0;
     }




  - **Forgetting to declare your variables.**

      ###### calculate(first, second)

      Error: 'first' has not been declared
        calculate(first, second)
                  ^

      Error: 'second' has not been declared
        calculate(first, second)
                         ^

      Error: calculate has not been declared
        calculate(first, second)
        ^

::

    #include <iostream>
    using namespace std;

     class calculations {
       public:
        calculate(first, second){
         return (first * second);
         }
      };
    int main() {
     int first;
     int second;
     calculations x;

     cout << "Enter your numbers: " << endl;
     cin >> first >> second;

     cout << "The product is: " << x.calculate(first, second) << endl;
     return 0;
    }

  -  **Not importing a class**:

  Here the class has been moved to a different file and forgetting to add the following include statement:

          #include "classfile.cpp"

  will result in the following errors.

        Error: calculations was not declared in this scope
            calculations x;
            ^

        Error: expected ';' before 'x'
          calculations x;
                       ^

        Error: ‘x’ was not declared in this scope
          cout << "The product is: " << x.calculate(first, second) << endl;
                                        ^
::


     #include <iostream>
     using namespace std;

     int main() {
         int first;
         int second;
         calculations x;
         // int calculate();

         cout << "Enter your numbers: " << endl;
         cin >> first >> second;

         cout << "The product is: " << x.calculate(first, second) << endl;
       return 0;
     }

  -  **Forgetting to use the correct arrows for iostream:**

 Here’s
 an example of the error message that occurs when you forget to
 use the appropriate arrows for inputting a value into the istream:

           Error: no match for ‘operator<<’ (operand types are ‘std::istream {aka std::basic_istream<char>}’ and ‘int’)
                 cin << first << second;

     The following code shows the error occurring where the wrong set of arrows used for inputting values into stream.

         #include <iostream>
         using namespace std;

         class calculations {

             public:
               int calculate(int first, int second){
               return (first * second);
               }
           };

         int main() {
         int first;
         int second;
         calculations x;

         cout << "Enter your numbers: " << endl;
         cin << first << second;

         cout << "The product is: " << x.calculate(first, second) << endl;
         return 0;
         }


  -  **Forgetting a Semicolon**:

  This is the type of error you get when you forget to add a semicolon to the
      end of a line.

  Error: expected ‘;’ before ‘cout’
          cout << "The product is: " << x.calculate(first, second) << endl;
          ^


  ::

         #include <iostream>
         using namespace std;

         class calculations {

             public:
               int calculate(int first, int second){
                 return (first * second);
                 }
          };

         int main() {
           int first;
           int second;
           calculations x;

           cout << "Enter your numbers: " << endl;
           cin >> first >> second

           cout << "The product is: " << x.calculate(first, second) << endl;
           return 0;
         }
