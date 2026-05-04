"""
    sys module: (system), contains a hole funcionality that's specific to the system it self
        and the commands that I typing.

    sys.argv: argv variable (argument vector): the list of all of the words that the human typed
        in at their prompt before they hit enter, all of those provided to me via python
        in a variable called sys.argv .
        this avriable is a list.
"""
# import sys

# print("hello, my name is", sys.argv[1]) 
"""
    #execute the progrm and pass value : (python name.py Ez) sys.argv[1] = Ez, prompt splitted by space, sys.argv[0] = name.py == file name

    !-> if i execute the program and dont pass a value for sys.argv[1]
        it will raise an exception named IndexError (list index out of range)

    * you can handle this error using try-except:
"""
# import sys

# try:
#     print("Hello, my name is", sys.argv[1]) 
# except IndexError:
#     print("Too few arguments")


#or
# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1]) 

# if the user want to pass his full name he can use "" like: "Ez Asqool", to pass it as one argument value

#---------------------
"""
    * more refinment: we want to separate check for errors from print name tags . but this
        will cause an error if the user dont enter any name the program will print Too few arguments
        but we will got IndexError.

    # sys.exit : it's going to exit my program on the line I wrote it in.
"""

# import sys

# #check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# #print name tags 
# print("Hello, my name is", sys.argv[1]) 



# ----- dont limit mac now of words

# import sys

# #check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("Hello, my name is", arg)
"""
    #this wil take file name also and print it because it is the first arg in sys.argv

    -> slices:  to take a slice of a lit (take subset of it) 
        you can use [] after list name and specify the start and the end of the list slice
        i want to return [start:end]
        (in sys.argv, i want to start from 1 to the end so you dont specify the end: sys.argv[1:])
"""

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
#     print("Hello, my name is", arg)


#******* we can slice from the end of the argv (if we want to start from 1st arg to 2args before the last one)

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-2]:
    print("Hello, my name is", arg)


"""
    # lets move from those modules/libraries that python comes with to talk 
        about more generally packages that exist (third-party libraries "Packages")
    
    -> Package: a module that's implemented in a folder , not just a file.
        more generally: a package is a third-party library that i can install in my laptop
        or cloud server and gain access to even more functionality that other people have 
        implemented for us.

    * one of the locations that I can get all of these packages is called PyPI

    - PyPI website: the Python Package Index (pypi.org) 

    - cowsay: is a package in python that allows me to have a caw say something on my screen

    * How can i get the package into my system?
        technically I can figure out how to dowenload the file and maybe unzip it 
        and put it to the right location on my laptop, 
        But nowadays python has what's called its own package manager called pip

    - pip: a program that generally comes with python itself, that allows me to install packages
        onto my own laptop or cloud environment by just running a command, and then I have 
        access to whole new library in python   


    ->>>>>> Go To Say.py
"""