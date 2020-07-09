# Glossary

# Basic String Operations https://www.learnpython.org/en/Basic_String_Operations
 # String Formatting

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

