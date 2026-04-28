# from cmd - to create new file, run command: code fileName.py

# *what users enter from keyboard treating as text.
'''
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
'''

# int not is just a datatype, its a function: int() used to get the integer value of variables
# and covert in to the actual number
"""
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
"""

# the returend value of the inner function becoming the input/argument of the outer function. 
"""
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
"""
# 1- Readability. 2- Smplicity. 
#print(int(input("What's x? ")) + int(input("What's y? ")))



####################################################################### 1:15 m
# float
"""
- float datatype

prev:   -str: sequence of characters/text
        -int: integer number

float: floating/decimal point number

"""

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print(x + y)


#####################################################################

#round user float inputs to the nearest integer, using python built in function
"""
-- in python documentation: round(number[, ndigits])
   * round function taks just one round argument called number. period
    [] when you see sequare pracets [] in documentation like this: this means that you about 
    to see something optional
    - in round function the ndigits parameter is optional 
    if you want to round to ndigits after decimal point. 

    * you can use :, for long integers to split each 3 digits of the number with , by using it with format string
"""
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}")

#specify ndigits to round to nearest digitsinteger not to nearest .
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x / y,2)

# print(z)

#specify ndigits to round to nearest integer not to nearest digits using fprmat strings.(:.nf)
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = x/y

# print(f"{z:.2f}")


"""
return to hello.py
"""


# return value
#calculate power using n*n, or n ** 2, or pow(n, 2)
def main():
    x = int(input("What's x? "))
    print("x sequared is", square(x))


def square(n):
    return n ** 2

main()