Defining Classes in C++
========================

You have already seen how to define classes in C++. In this section we will look at how we
define classes to create our own data types. Let's start by creating a
fraction class to extend the set of numeric data types provided by our
language. The requirements for this new data type are as follows:

-  Given a numerator and a denominator create a new Fraction.

-  When a fraction is printed it should be simplified.

-  Two fractions can be added or subtracted

-  Two fractions can be multiplied or divided

-  Two fractions can be compared

-  A fraction and an integer can be added together.

-  Given a list of Fractions that list should be sortable by the default
   sorting function.

Here is a mostly complete implementation of a Fraction class in Python
that we will refer to throughout this section:

.. literalinclude:: fraction.py
   :language: python
   :linenos:


The instance variables (data members) we will need for our fraction
class are the numerator and denominator. Of course in Python we can add
instance variables to a class at any time by simply assigning a value to
``objectReference.variableName`` In C++ all data members must be
declared up front.

The declarations of instance variables can come at the beginning of the
class definition. I like them at the
very beginning so you see the variables that are declared before you
begin looking at the code that uses them. With that in mind the first
part of the Fraction class definition is as follows:

.. highlight:: C++
   :linenothreshold: 5


::

    public class Fraction {
      private int numerator;
      private int denominator;

    }

Notice that we have declared the numerator and denominator to be
private. This means that the compiler will generate an error if another
method tries to write code like the following:

::

    Fraction f = new Fraction(1,2);
    int y = f.numerator * 10;

Direct access to instance variables is not allowed. Therefore if we
legitimately want to be able to access information such as the numerator
or denominator for a particular fraction we must have getter functions.
It is very common programming practice to provide getter and setter
functions for instance variables in C++.

::

    int getNumerator() {
        return numerator;
    }

    void setNumerator(int numerator) {
        this->numerator = numerator;
    }

    int getDenominator() {
        return denominator;
    }

    void setDenominator(int denominator) {
        this->denominator = denominator;
    }

Writing a constructor
---------------------

***Needs work.. Add `__init__` from python***

Once you have identified the instance variables for your class the next
thing to consider is the constructor. In C++, constructors have the
same name as the class and are declared public. They are declared
without a return type. So any function that is named the same as the
class and has no return type is a constructor. Our constructor will take
two parameters, the numerator and the denominator.

::

    public Fraction(int top, int bottom) {
        num = top;
        den = bottom;
    }

There are a couple of important things to notice here. First, you will
notice that the constructor does not have a self parameter. You will
also notice that we can simply refer to the instance variables by name
without the self prefix, because they have already been declared. This
allows the C++ compiler to do the work of dereferencing the current
C++ object. C++ does provide a special variable called ``this`` that
works like the self variable. In C++, ``this`` is typically only used
when it is needed to differentiate between a parameter or local variable
and an instance variable. For example this alternate definition of the
the Fraction constructor uses ``this`` to differentiate between
parameters and instance variables.

::

    public Fraction(int num, int den) {
        this->num = num;
        this->den = den;
    }

Methods or Member Functions
---------------------------
***Needs Rewrite***

Now we will write member functions to do addition, subtraction, multiplication, and
division. Let's begin with addition.

::

     Fraction add(Fraction, otherFrac) {
        int newNum, newDen, common;

        newNum = otherFrac.getDenominator()*this.numerator +
                                 this.denominator*otherFrac.getNumerator();
        newDen = this.denominator * otherFrac.getDenominator();
        common = gcd(newNum,newDen);
        return new Fraction(newNum/common, newDen/common );
    }

First you will notice that the add member function is declared as
``public Fraction`` The ``public`` part means that any other method may
call the add method. The ``Fraction`` part means that ``add`` will
return a fraction as its result.

Second, you will notice that on line two all of the local variables used
in the function are declared. In this case there are three local
variables: ``newNum``, ``newDen``, and ``common``. It is a good idea for
you to get in the habit of declaring your local variables at the
beginning of your function. This declaration section provides a simple
road map for the function in terms of the data that will be used. The
listing above also makes use of the ``this`` variable, you may find it
useful to use ``this`` until you are comfortable with abandoning your
Pythonic ideas about ``self``.

Declaring your variables at the top is not a requirement, it is just a
recommended practice for you. Java only requires that you declare your
variables before they are used. The following version of Fraction is
also legal Java, but may be somewhat less readable.

::

    public Fraction add(Fraction otherFrac) {
        int newNum = otherFrac.getDenominator()*numerator +
                                 denominator*otherFrac.getNumerator();
        int newDen = denominator * otherFrac.getDenominator();
        int common = gcd(newNum,newDen);
        return new Fraction(newNum/common, newDen/common );
    }

The addition takes place by multiplying each numerator by the opposite
denominator before adding. This procedure ensures that we are adding two
fractions with common denominators. Using this approach the denominator
is computed by multiplying the two denominators. The greatest common
divisor function is used to find a common divisor to simplify the
numerator and denominator in the result.

Finally on line 8 a new fraction is returned as the result of the
computation. The value that is returned by the return statement must
match the value that is specified as part of the declaration. So, in
this case the return value on line 8 must match the declared value on
line 1.

Method Signatures and Overloading
---------------------------------

***Needs Rewrite***

Our specification for this project said that we need to be able to add a
``Fraction`` to an ``Integer``. In Python we can do this by checking the
type of the parameter using the ``isinstance`` function at runtime.
Recall that ``isinstance(1,int)`` returns ``True`` to indicate that 1 is
indeed an instance of the ``int`` class. See lines 22 and 53—68 of the
Python version of the Fraction class to see how our Python
implementation fulfills this requirement.

In C++ we can do runtime type checking, but the compiler will not allow
us to pass an int to the add function since the parameter has been
declared to be a Fraction. The way that we solve this problem is by
writing another ``add`` method with a different set of parameters. In
C++ this practice is legal and common we call this practice
**overloading**.

This idea of overloading raises a very important difference between
Python and C++. In Python a method is known by its name only. In C++ a
method is known by its signature. The signature of a method includes its
name, and the types of all of its parameters. The name and the types of
the parameters are enough information for the C++ compiler to decide
which method to call at runtime.

To solve the problem of adding an ``int`` and a ``Fraction`` in C++
we will overload both the constructor and the add function. We will
overload the constructor so that if it only receives a single
``int`` it will convert the ``int`` into a ``Fraction``. We will
also overload the add method so that if it receives an ``int`` as a
parameter it first construct a ``Fraction`` from that integer and then
add the two ``Fraction``s together. The new methods that accomplish this
task are as follows:

::

    public Fraction(int num) {
        this->numerator = num;
        this->denominator = 1;
    }

    public Fraction add(int other) {
        return add(new Fraction(other));
    }

Notice that the overloading approach can provide us with a certain
elegance to our code. Rather than utilizing if statements to check the
types of parameters we just overload functions ahead of time which
allows us to call the method we want and allow the compiler to make the
decisions for us. This way of thinking about programming takes some
practice.

Our full Fraction class to this point would look like the following. You
may want to try to compile and run the short test program provided just
to see what happens.

.. activecode:: fraction1
    :language: java
    :sourcefile: Fraction.java

    public class Fraction {

        private int numerator;
        private int denominator;

        public Fraction(int num, int den) {
            this->numerator = num;
            this->denominator = den;
        }

        public Fraction(int num) {
            this->numerator = num;
            this->denominator = 1;
        }

        public Fraction add(Fraction other) {
            int newNum, newDen, common;

            newNum = other.getDenominator()*this.numerator + this.denominator*other.getNumerator();
            newDen = this.denominator * other.getDenominator();
            common = gcd(newNum,newDen);
            return new Fraction(newNum/common, newDen/common );
        }

        public Fraction add(Integer other) {
            return add(new Fraction(other));
        }

        private static Integer gcd(Integer m, Integer n) {
            while (m % n != 0) {
                Integer oldm = m;
                Integer oldn = n;
                m = oldn;
                n = oldm%oldn;
            }
            return n;
        }

        public static void main(String[] args) {
            Fraction f1 = new Fraction(1,2);
            Fraction f2 = new Fraction(2,3);

            System.out.println(f1.mul(f2));
            System.out.println(f1.add(1));
        }

    }

Inheritance
-----------

***Needs Rewrite***

If you ran the program above you probably noticed that the output is not
very satisfying. Chances are your output looked something like this:

::

    Fraction@7b11a3ac
    Fraction@6c22c95b

The reason is that we have not yet provided a friendly string
representation for our Fraction objects. The truth is that, just like in
Python, whenever an object is printed by the ``println`` method it must
be converted to string format. In Python you can control how that looks
by writing an ``__str__`` method for your class. If you do not then you
will get the default, which looked something like the above.

<!---

The ``Object`` Class
--------------------

In C++, the equivalent of ``__str__`` is the ``toString`` method. Every
object in Java already has a ``toString`` method defined for it because
every class in Java automatically inherits from the Object class. The
object class provides default implementations for the following
functions.

-  clone

-  equals

-  finalize

-  getClass

-  hashCode

-  notify

-  notifyAll

-  toString

-  wait

We are not interested in most of the functions on that list, and many
Java programmers live happy and productive lives without knowing much
about most of the functions on that list. However, to make our output
nicer we will implement the ``toString`` method for the ``Fraction``
class. A simple version of the method is provided below.

::

    String toString() {
        return numerator.toString() + "/" + denominator.toString();
    }

The other important class for us to implement from the list of methods
inherited from Object is the ``equals`` method. When two objects are
compared in Java using the == operator they are tested to see if they
are exactly the same object, that is do the two objects occupy the same
exact space in the computers memory. This is the default behavior of the
``equals`` method provided by Object. The ``equals`` method allows us to
decide if two objects are equal by looking at their instance variables.
However it is important to remember that since Java does not have
operator overloading if you want to use your equals method you must call
it directly. Therefore once you write your own ``equals`` method:

::

    object1 == object2

is NOT the same as

::

    object1.equals(object2)

Here is an equals method for the Fraction class:

::

    public boolean equals(Fraction other) {
        Integer num1 = this.numerator * other.getDenominator();
        Integer num2 = this.denominator * other.getNumerator();
        if (num1 == num2)
            return true;
        else
            return false;
    }

One important thing to remember about ``equals`` is that it only checks
to see if two objects are equal it does not have any notion of less than
or greater than. We’ll see more about that shortly.

Abstract Classes and Methods
--

If we want to make our Fraction class behave like Integer, Double, and
the other numeric classes in Java We need to make a couple of additional
modifications to the class. The first thing we will do is plug
``Fraction`` into the Java class hierarchy at the same place as Integer
and its siblings. If you look at the documentation for Integer you will
see that Integer’s parent class is ``Number``. Number is an **abstract
class** that specifies several methods that all of its children must
implement. In Java an abstract class is more than just a placeholder for
common functions. In Java an abstract class has the power to specify
certain functions that all of its children **must** implement. You can
trace this power back to the strong typing nature of Java.

The that makes the Fraction class a child of Number is as follows:

::

    public class Fraction extends Number {
        ...
    }

The keyword extends tells the compiler that the class ``Fraction``
extends, or adds new functionality to the ``Number`` class. A child
class always extends its parent.

The methods we must implement if ``Fraction`` is going to be a child of
``Number`` are:

-  longValue

-  intValue

-  floatValue

-  doubleValue

This really isn’t much work for us to implement these functions as all
we have to do is some conversion of our own and some division. The
implementation of these methods is as follows:

::

    public double doubleValue() {
        return numerator.doubleValue() / denominator.doubleValue();
    }


    public float floatValue() {
        return numerator.floatValue() / denominator.floatValue();
    }


    public int intValue() {
        return numerator.intValue() / denominator.intValue();
    }


    public long longValue() {
        return numerator.longValue() / denominator.longValue();
    }

By having the ``Fraction`` class extend the ``Number`` class we can now
pass a ``Fraction`` to any Java function that specifies it can receive a
``Number`` as one of its parameters. For example many Java user
interface methods accept any object that is a subclass of ``Number`` as
a parameter. In Java the class hierarchy and the IS-A relationships are
very important. Whereas in Python you can pass any kind of object as a
parameter to any function the strong typing of Java makes sure that you
only pass an object as a parameter that is of the type specified in the
function call or one of its children. So, in this case when you see a
parameter of type ``Number`` its important to remember that an
``Integer`` *is-a* ``Number`` and a ``Double`` *is-a* ``Number`` and a
``Fraction`` *is-a* ``Number``.

However, and this is a big however, it is also important to remember
that if you specify ``Number`` as the type on a particular parameter
then the Java compiler will only let you use the methods of a
``Number``. In this case longValue, intValue, floatValue, and
doubleValue.

Lets suppose you define a method in some class as follows:

::

    public void test(Number a, Number b) {
        a.add(b);
    }

The Java compiler would give an error because ``add`` is not a defined
method of the ``Number`` class. Even if you called the add method and
passed two ``Fractions`` as parameters.

Interfaces
----------

Lets turn our attention to making a list of fractions sortable by the
standard Java sorting method ``Collections.sort``. In Python all we
would need to do is implement the ``__cmp__`` method. But in Java we
cannot be that informal. In Java Things that are sortable must be
``Comparable``. Your first thought might be that ``Comparable`` is
Superclass of ``Number``. That would be a good thought but it would not
be correct. Java only supports single inheritance, that is, a class can
have only one parent. Although it would be possible to add an additional
Layer to the class hierarchy it would also complicate things
dramatically. Because Not only are Numbers comparable, but Strings are
also Comparable as would many other types. For example we might have a
``Student`` class and we want to be able to sort Students by their gpa.
But ``Student`` already extends the class ``Person`` for which we have
no natural comparison function.

Java’s answer to this problem is the ``Interface`` mechanism. Interfaces
are like a combination of Inheritance and contracts all rolled into one.
An interface is a *specification* that says any object that claims it
implements this interface must provide the following methods. It sounds
a little bit like an abstract class, however it is outside the
inheritance mechanism. You can never create an instance of
``Comparable``. Many objects, however, do implement the ``Comparable``
interface. What does the Comparable interface specify?

The ``Comparable`` interface says that any object that claims to be
``Comparable`` must implement the ``compareTo`` method. The following is
the documentation for the ``compareTo`` method as specified by the
Comparable interface.

::

    int compareTo(T o)

     Compares this object with the specified object for order. Returns a negative integer, zero, or a
    positive integer as this object is less than, equal to, or greater than the specified object. The
    implementor must ensure sgn(x.compareTo(y)) == -sgn(y.compareTo(x)) for all x and y. (This implies
    that x.compareTo(y) must throw an exception iff y.compareTo(x) throws an exception.)

    The implementor must also ensure that the relation is transitive: (x.compareTo(y)>0 &&
    y.compareTo(z)>0) implies x.compareTo(z)>0.

    Finally, the implementor must ensure that x.compareTo(y)==0 implies that sgn(x.compareTo(z)) ==
    sgn(y.compareTo(z)), for all z.

    It is strongly recommended, but not strictly required that (x.compareTo(y)==0) == (x.equals(y)).
    Generally speaking, any class that implements the Comparable interface and violates this condition
    should clearly indicate this fact. The recommended language is "Note: this class has a natural
    ordering that is inconsistent with equals."

    In the foregoing description, the notation sgn(expression) designates the mathematical signum
    function, which is defined to return one of -1, 0, or 1 according to whether the value of
    expression is negative, zero or positive.

To make our ``Fraction`` class ``Comparable`` we must modify the class
declaration line as follows:

::

    public class Fraction extends Number implements Comparable<Fraction> {
        ...
    }

The specification ``Comparable<Fraction>`` makes it clear that Fraction
is only comparable with another Fraction. The ``compareTo`` method could
be implemented as follows:

::

    public int compareTo(Fraction other) {
        Integer num1 = this.numerator * other.getDenominator();
        Integer num2 = this.denominator * other.getNumerator();
        return num1 - num2;
    }

Static member variables
-----------------------

Suppose that you wanted to write a Student class so that the class could
keep track of the number of students it had created. Although you could
do this with a global counter variable that is an ugly solution. The
right way to do it is to use a static variable. In Python we could do
this as follows:

.. activecode:: pystudent
    :language: python

    class Student:
        numStudents = 0

        def __init__(self, id, name):
            self.id = id
            self.name = name

            Student.numStudents = Student.numStudents + 1

    def main():
        for i in range(10):
            s = Student(i,"Student-"+str(i))
        print('The number of students is: ', Student.numStudents)

    main()

In Java we would write this same example using a static declaration.

.. activecode:: studentclass
    :language: java
    :sourcefile: Student.java

    public class Student {
            public static Integer numStudents = 0;

            private int id;
            private String name;

            public Student(Integer id, String name) {
            this.id = id;
            this.name = name;

            numStudents = numStudents + 1;
            }

            public static void main(String[] args) {
            for(Integer i = 0; i < 10; i++) {
                Student s = new Student(i,"Student"+i.toString());
            }
            System.out.println("The number of students: "+Student.numStudents.toString());
            }
        }


In this example notice that we create a static member variable by using
the static modifier on the variable declaration. Once a variable has
been declared static in Java it can be access from inside the class
without prefixing the name of the class as we had to do in Python.

Static Methods
--------------

We have already discussed the most common static method of all,
``main``. However in our Fraction class we also implemented a method to
calculate the greatest common divisor for two fractions (``gdc``). There
is no reason for this method to be a member method since it takes two
``Integer`` values as its parameters. Therefore we declare the method to
be a static method of the class. Furthermore since we are only going to
use this ``gcd`` method for our own purposes we can make it private.

::

    private static Integer gcd(Integer m, Integer n) {
        while (m % n != 0) {
            Integer oldm = m;
            Integer oldn = n;
            m = oldn;
            n = oldm%oldn;
        }
        return n;
    }

Full Implementation of the Fraction Class
-----------------------------------------

A final version of the Fraction class that exercises all of the features
we have discussed is as follows.

.. activecode:: fullfraction
    :language: java
    :sourcefile: Fraction.java

    import java.util.ArrayList;
    import java.util.Collections;

    public class Fraction extends Number implements Comparable<Fraction> {

        private Integer numerator;
        private Integer denominator;

        /** Creates a new instance of Fraction */
        public Fraction(Integer num, Integer den) {
            this.numerator = num;
            this.denominator = den;
        }

        public Fraction(Integer num) {
            this.numerator = num;
            this.denominator = 1;
        }

        public Fraction add(Fraction other) {
            Integer newNum = other.getDenominator()*this.numerator + this.denominator*other.getNumerator();
            Integer newDen = this.denominator * other.getDenominator();
            Integer common = gcd(newNum,newDen);
            return new Fraction(newNum/common, newDen/common );
        }

        public Fraction add(Integer other) {
            return add(new Fraction(other));
        }

        public Integer getNumerator() {
            return numerator;
        }

        public void setNumerator(Integer numerator) {
            this.numerator = numerator;
        }

        public Integer getDenominator() {
            return denominator;
        }

        public void setDenominator(Integer denominator) {
            this.denominator = denominator;
        }

        public String toString() {
            return numerator.toString() + "/" + denominator.toString();
        }

        public boolean equals(Fraction other) {
            Integer num1 = this.numerator * other.getDenominator();
            Integer num2 = this.denominator * other.getNumerator();
            if (num1 == num2)
                return true;
            else
                return false;
        }

        public double doubleValue() {
            return numerator.doubleValue() / denominator.doubleValue();
        }

        public float floatValue() {
            return numerator.floatValue() / denominator.floatValue();
        }

        public int intValue() {
            return numerator.intValue() / denominator.intValue();
        }

        public long longValue() {
            return numerator.longValue() / denominator.longValue();
        }

        public int compareTo(Fraction other) {
            Integer num1 = this.numerator * other.getDenominator();
            Integer num2 = this.denominator * other.getNumerator();
            return num1 - num2;
        }

        private static Integer gcd(Integer m, Integer n) {
            while (m % n != 0) {
                Integer oldm = m;
                Integer oldn = n;
                m = oldn;
                n = oldm%oldn;
            }
            return n;
        }

        public static void main(String[] args) {
            Fraction f1 = new Fraction(1,2);
            Fraction f2 = new Fraction(2,3);
            Fraction f3 = new Fraction(1,4);

            System.out.println(f1.add(1));
            System.out.println(f1.intValue());
            System.out.println(f1.doubleValue());

            ArrayList<Fraction> myFracs = new ArrayList<Fraction>();
            myFracs.add(f1);
            myFracs.add(f2);
            myFracs.add(f3);
            Collections.sort(myFracs);

            for(Fraction f : myFracs) {
                System.out.println(f);
            }
        }

    }

-->
