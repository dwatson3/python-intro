# Glossary

# Indentation
# Variables and Types
    # Numbers
    # Strings
    # Lists
# Basic Operators
    # Arithmetic Operators
    # Using Operators with Strings
    # Using Operators with Lists
    


# Notes from https://www.learnpython.org

# Python is a very simple language, and has a very straightforward syntax. 
# It encourages programmers to program without boilerplate (prepared) code. 
# The simplest directive in Python is the "print" directive - it simply 
# prints out a line (and also includes a newline, unlike in C).

# Printing a String 
print("Hello World!")

# Indentations 
    # Python uses indentation for blocks, instead of curly braces. 
    # Both tabs and spaces are supported, but the standard indentation 
    # requires standard Python code to use four spaces.

x = 10
if x == 10:
    #indented four spaces
    print("x is 10")

# Variables and Types
    # Python is completely object oriented, and not "statically typed". 
    # You do not need to declare variables before using them, 
    # or declare their type. Every variable in Python is an object.

# Numbers
    # Python supports two types of numbers - integers and floating point numbers. 
    # (It also supports complex numbers, which will not be explained in this 
    # tutorial).

# Integers
myint = 7
print(myint)

# Floating Point Numbers
myfloat = 20.0
print(myfloat)

myfloat = float(20)
print(myfloat)

# Strings
    # Strings are defined either with a single quote or a double quotes.
mystring = 'ciao'
print(mystring)

mystring2 = "hola"
print(mystring2)

    # The difference between the two is that using double quotes makes it easy to 
    # include apostrophes (whereas these would terminate the string if using 
    # single quotes)
mystring = "Don't you worry about apostrophes"
print(mystring)

    # There are additional variations on defining strings that make it easier to 
    # include things such as carriage returns, backslashes and Unicode characters. 
    # These are beyond the scope of this tutorial, but are covered in the
    # Python documentation: https://docs.python.org/3/tutorial/introduction.html#strings
two = 2
three = 3
five = two + three
print(five)

hola = "hola"
mundo = "mundo"
holamundo = hola + " " + mundo
print(holamundo)

    # Assignments can be done on more than one variable "simultaneously" on the same line 
    # like this

a, b = 10, 20
print (a, b)

# Lists
    # Lists are very similar to arrays. They can contain any type of variable, and they can contain 
    # as many variables as you wish. Lists can also be iterated over in a very simple manner. 
    # Here is an example of how to build a list.

mylist = []
mylist.append(10)
mylist.append(20)
mylist.append(30)
print(mylist[0]) # prints 10
print(mylist[1]) # prints 20
print(mylist[2]) # prints 30

# prints out 10,20,30
for x in mylist:
    print(x)

    # Accessing an index which does not exist generates an exception (an error).
mylist = [1,2,3]
print(mylist[10])

# Arithmetic Operators 
    # Just as any other programming languages, the addition, subtraction, multiplication, 
    # and division operators can be used with numbers.

    # Try to predict what the answer will be. Does python follow order of operations?
    # Another operator available is the modulo (%) operator, which returns the integer 
    # remainder of the division. dividend % divisor = remainder.
remainder = 11 % 3
print(remainder)

    # Using two multiplication symbols makes a power relationship.
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Using operators with strings
    # Python supports concatenating strings using the addition operator:
ciaomondo = "ciao" + " " + "mondo"
print(ciaomondo)

    # Python also supports multiplying strings to form a string with a 
    # repeating sequence:
lotsofciaos = "ciao" * 4
print(lotsofciaos)

# Using Operators as Lists
    # Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

    # Just as in strings, Python supports forming new lists 
    # with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)