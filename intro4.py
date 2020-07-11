# Glossary

# Dictionaries https://www.learnpython.org/en/Dictionaries
    # Iterating over dictionaries
    # Removing a value
# Modules and Packages https://www.learnpython.org/en/Modules_and_Packages


# Dictionaries
    # A dictionary is a data type similar to arrays, but works 
    # with keys and values instead of indexes. 
    # Each value stored in a dictionary can be accessed using a key, 
    # which is any type of object (a string, a number, a list, etc.) 
    # instead of using its index to address it.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

    # Alternatively, a dictionary can be initialized with the same values 
    # in the following notation:
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# Iterating over dictionaries
    # Dictionaries can be iterated over, just like a list. 
    # However, a dictionary, unlike a list, does not keep 
    # the order of the values stored in it. To iterate over 
    # key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value
    # To remove a specified index, use either one of the 
    # following notations:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

    # or

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

# Modules and Packages
    # In programming, a module is a piece of software that has 
    # a specific functionality. For example, when building a 
    # ping pong game, one module would be responsible for the 
    # game logic, and another module would be responsible for 
    # drawing the game on the screen. Each module is a 
    # different file, which can be edited separately.

# Writing modules
    # Modules in Python are simply Python files with a .py extension. 
    # The name of the module will be the name of the file. 
    # A Python module can have a set of functions, 
    # classes or variables defined and implemented. 
    # In the example above, we will have two files, we will have:
mygame/
mygame/game.py
mygame/draw.py

    # The Python script game.py will implement the game. It will use 
    # the function draw_game from the file draw.py, or in other words, 
    # the draw module, that implements the logic for drawing the game 
    # on the screen.

    # Modules are imported from other modules using the import command. 
    # In this example, the game.py script may look something like this:

    # game.py
    # import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

    # this means that if this script is executed, then 
    # main() will be executed
if __name__ == '__main__':
    main()

    # The draw module may look something like this:
    # draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...