# Glossary

# Functions https://www.learnpython.org/en/Functions
# Classes and Objects https://www.learnpython.org/en/Classes_and_Objects
    # Accessing Object Variables
    # Accessing Object Functions

    # What are Functions? 
        # Functions are a convenient way to divide your code 
        # into useful blocks, allowing us to order our code, 
        # make it more readable, reuse it and save some time. 
        # Also functions are a key way to define interfaces so 
        # programmers can share their code.

    # How do you write functions in Python?
        # As we have seen on previous tutorials, Python makes use of blocks.
        # A block is a area of code of written in the format of:

block_head:
    1st block line
    2nd block line
    ...

    # Where a block line is more Python code (even another block), 
    # and the block head is of the following format: 
    # block_keyword block_name(argument1,argument2, ...) 
    # Block keywords you already know are "if", "for", and "while".

    # Functions in python are defined using the block keyword "def", 
    # followed with the function's name as the block's name. 
    # For example:
def my_function():
    print("Hello From My Function!")

    # Functions may also receive arguments (variables passed from the caller 
    # to the function). 
    # For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
my_function_with_args("Daphne", "well")

    # Functions may return a value to the caller, using the keyword- 'return' . 
    # For example:
def sum_two_numbers(a, b):
    return a + b
sum_two_numbers(5, 6)

# How do you call functions in Python? 
    # Simply write the function's name followed by (), 
    # placing any required arguments within the brackets. 
    # For example, lets call the functions written above 
    # (in the previous example):

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

    # print(a simple greeting)
my_function()

    #prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

    # after this line x will hold the value 3!
x = sum_two_numbers(1,2)

# Classes and Objects
    # Objects are an encapsulation of variables and functions into 
    # a single entity. Objects get their variables and functions 
    # from classes. Classes are essentially a template to create 
    # your objects.

    # A very basic class would look something like this:
    class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

    # We'll explain why you have to include that "self" as a parameter 
    # a little bit later. First, to assign the above class(template) 
    # to an object you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

    # Now the variable "myobjectx" holds an object of the class "MyClass" 
    # that contains the variable and the function defined within the class
    #  called "MyClass".

# Accessing Object Variables
    # To access the variable inside of the newly created object "myobjectx" 
    # you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable

    # So for instance the below would output the string "blah":
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)

    # You can create multiple different objects that are of the same class
    # (have the same variables and functions defined). 
    # However, each object contains independent copies of the variables 
    # defined in the class. For instance, if we were to define another 
    # object with the "MyClass" class and then change the string in 
    # the variable above:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable) # blah
print(myobjecty.variable) # yackity

# Accessing Object Functions
    # To access a function inside of an object you use notation 
    # similar to accessing a variable:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()

    # The above would print out the message, 
    # "This is a message inside the class."







