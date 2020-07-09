# Glossary

# Basic String Operations https://www.learnpython.org/en/Basic_String_Operations
 # String Formatting
# Conditions https://www.learnpython.org/en/Conditions
    # Boolean Operators
    # The "In" Operator

# Basic String Operations https://www.learnpython.org/en/Basic_Operators
    # Strings are bits of text. They can be defined as 
    # anything between quotes:
astring = "Ciao mondo!"
astring2 = 'Ciao mondo!'

# String Formatting
    # Python uses C-style string formatting to create new, formatted strings. 
    # The "%" operator is used to format a set of variables enclosed in a "tuple" 
    # (a fixed size list), together with a format string, which contains normal text 
    # together with "argument specifiers", special symbols like "%s" and "%d".

    # Let's say you have a variable called "name" with your user name in it, 
    # and you would then like to print(out a greeting to that user.)

    # This prints out "Hello, John!"
name = "Daphne"
print("Hello, %s!" % name)

    # To use two or more argument specifiers, 
    # use a tuple (parentheses):
name = "Daphne"
age = 32
print("%s is %d years old." % (name, age))

    # Any object which is not a string can be formatted using the %s operator as well. 
    # The string which returns from the "repr" method of that object is formatted 
    # as the string. For example:

    # This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# Here are some basic argument specifiers you should know:
    # %s - String (or any object with a string representation, like numbers)
    # %d - Integers
    # %f - Floating point numbers
    # %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    # %x/%X - Integers in hex representation (lowercase/uppercase)

# Conditions
    # Python uses boolean variables to evaluate conditions. 
    # The boolean values True and False are returned when an 
    # expression is compared or evaluated. For example:
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

    # Notice that variable assignment is done using a single equals operator "=", 
    # whereas comparison between two variables is done using the 
    # double equals operator "==". The "not equals" operator is marked as "!=".

# Boolean Operators
    # The "and" and "or" boolean operators allow building complex 
    # boolean expressions, for example:
name = "Daphne"
age = 32
if name == "Daphne" and age == 32:
    print("Your name is Daphne, and you are also 32 years old.")

if name == "Daphne" or name == "Anders":
    print("Your name is either Daphne or Anders.")

# The "In" Operator
    # The "in" operator could be used to check if a specified object 
    # exists within an iterable object container, such as a list:
name = "Daphne"
if name in ["Daphne", "Anders"]:
    print("Your name is either Daphne or Anders.")

# Python uses indentation to define code blocks, instead of brackets. 
# The standard Python indentation is 4 spaces, although tabs and any 
# other space size will work, as long as it is consistent. Notice that 
# code blocks do not need any termination.

# Here is an example for using Python's "if" statement using code blocks:
