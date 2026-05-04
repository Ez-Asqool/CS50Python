"""
    Module
    # Module is a library that has typically one or more functions or other features built in to it.
    -> The purpose of it : To encourage reusability of code.

    .Like random module/library in python and that is one of many modules/libraries with python.
    
    * python provide us with functions like input() and print() that we can access it by default. 
        but sometimes, functions are tucked away in modules , so you have to be more deliberate 
        about loading them into the computers memory.

    ex: random.py : module has one or more functions that I can use it to do things randomly

    # to lead a module into my program we need to use (import) keyword, that allows me
        to import the contents of the functions from some module in python.

    - to use random.choice(seq) you should import random module. (seq: sequence of items "array")    
"""
#flip a coin randomly using random module(library) by importing it:

# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

"""
    from keyword: to import a spesific function from a module, not the hole module.
"""

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)


"""
    random. randint(a, b) , return random int between a and b inclusive
"""
# import random

# number = random.randint(1, 10)
# print(number)


"""
    random.shuffle(x) : take a list of values and shuffles them up 
    (it shuffles the items it self in the lis)
"""
# import random
# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)



#################################################################################

"""
    # statistics module/library , has statustical functions to calculate
        mean or medians or mods or other aspects of a data set.
    
    -> average : function that allows us to calculate average of some numbers.that you've passed in.

    Go to average.py

"""