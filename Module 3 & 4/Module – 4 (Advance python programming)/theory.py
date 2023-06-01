"""
1) What is File function in python? What is keywords to create and write
file

        Python file object provides methods and attributes to access and manipulate files. 
        Using file objects, we can read or write any files.
        Whenever we open a file to perform any operations on it, 
        Python returns a file object. 
        To create a file object in Python use the built-in functions, such as open() and os. popen()
    
==>What is keywords to create and write

    Write to an Existing File
    To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

Create a New File:
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

13) Explain Exception handling? What is an Error in Python? 

        Exception :- which disturb the normal flow of program

        to handle a this kind of exception its called exception handling
        
        exception handling is possible try and except block

==> What is an Error in Python?

Exception	     Description
   |                  |
IndexError  	When the wrong index of a list is retrieved.
AssertionError 	It occurs when the assert statement fails
AttributeError	It occurs when an attribute assignment is failed.
ImportError	    It occurs when an imported module is not found.
KeyError	    It occurs when the key of the dictionary is not found.
NameError	    It occurs when the variable is not defined.
MemoryError	    It occurs when a program runs out of memory.
TypeError	    It occurs when a function and operation are applied in an incorrect type.

14) How many except statements can a try-except block have? Name Some
built-in exception classes: 
answer:-
        There has to be at least one except statement
        or --> more than zero

=>Name Some built-in exception classes: 
answer :
        IndexError	Raised when an index of a sequence does not exist
        NameError	Raised when a variable does not exist
        SyntaxError	Raised when a syntax error occurs
        RuntimeError	Raised when an error occurs that do not belong to any specific exceptions
        TypeError	Raised when two different types are combined


15) When will the else part of try-except-else be executed? 
    answer:-
            when no exception occurs
Explanation: The else part is executed when no exception occurs.
        
16)Can one block of except statements handle multiple exception?
    answer:-
            You can also have one except block handle multiple exceptions.

17) When is the finally block executed?
    answer:
            Always
            the finally block is always executed.

18) What happens when „1‟== 1 is executed? 
    answer:-
            It simply evaluates to False and does not raise any exception

19) How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets
    answer:-
            The finally block lets you execute code, regardless of the result of the try- and except blocks.
In Python, the finally block is always executed no matter whether there is an exception or not.
The finally block is optional. And, for each try block, there can be only one finally block.

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")
            
***Output***

Error: Denominator cannot be 0.
This is finally block.

Explanation: 
            In the above example, we are dividing a number by 0 inside the try block. 
            Here, this code generates an exception.
            The exception is caught by the except block. And, then the finally block is executed.

21)What are oops concepts? Is multiple inheritance supported in python
oops : object oriented programming system 
class : class is a collection of data member and member function
        or
        class which is contain data mamber amd member function in single enity
        or
        class is like group which is store different different data member in it
		or
	    class is a user define datatype
             
object : object is in instance of class

        if class is a datatype than object is an instance or variable  of class
        using of object we can aceess all the properties of class 

-->one class can have many objects

==>Is multiple inheritance supported in python
Yes, Python supports multiple inheritance


22)How to Define a Class in Python? What Is Self? Give An Example Of
A Python Class
    answer:
            A class in Python can be defined using the class keyword
            syntax:
                    class <ClassName>:
                        <statement1>
                        <statement2>
                        .
                        .
                        <statementN>
==>What Is Self?
                self is keyword which is represent current class properties
                self keyword is used to represent an instance (object) of the given class
example:
class student:
    def display(self):
    print("This is student class ")
        
obj = student()
obj.display()

25) Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?

inheritance :- inheritance is a powerfull concept in oops

        inheritance which is provide parent and child relationship
        
        one class derived properties of another class its called inheritance 
        using of inheritance we can reduce our code
        
        inhertitance provide reusability and reduce code , so , we can ave our time
        
there  are mainly 5 type of inheritance

        1.single level
        2.multi level
        3.multiple
        4.hierachical
        5.hybrid inharitance
----------------------------------        
 1.single
            a
            |
            v
            b

#sinle level

class A : #parent class
    def displayA(self):
        print("A class here")
        
class B(A) : #child class
    def displayB(self):
        print("B class here")
        
o = B()
o.displayA()
o.displayB()
------------------------
2.multilevel
            a
            |
            v
            b
            |
            v
            c
--------------------------
3.multiple

        a       b
        |       |
        ---------
            |
            v
            c
-----------------------------
4.Hierachical
            a
            |
        ------------
        |          |
        b          c

5.hybrid

26) What is Instantiation in terms of OOP terminology
    answer:-
            Instantiation refers to creating an object/instance for a class.

27) What is used to check whether an object o is an instance of class A?
    answer:
            isinstance() Function

28) What relationship is appropriate for Course and Faculty?
    answer:-
            association

29) What relationship is appropriate for Student and Person?
    answer:-
            inheritance          
"""