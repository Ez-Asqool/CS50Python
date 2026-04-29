# print("meow")
# print("meow")
# print("meow")

"""
    why this code is poorly designed ??
    -> the code is repeating him self.

    To get a more well designed version of code we will 
    use (while) loop: a block of code that's going to do something again and again and again
    as many times as we want.
"""

# i = 3

# while i != 0:
#     print("meow"); 
#     i = i - 1

#another way

# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1


#start counting from 0

# i = 0
# while i < 3:
#     print("meow")
#     i += 1


"""
    for loop. 
    list datatypes: a list of things (containing multiple values, all in the same place, variable)

    * for loop allows you to iterate over alist of items.
"""

# for i in [0, 1, 2]:
#     print("meow")

# poorly designed ? -> dont manually specify the list of values , use a function.
# range(n) python function returns a range of values 

# for i in range(3):
#     print("meow")

# if you define i just for counting and you dont use it (dont care about its value) replace it with _

# for _ in [0, 1, 2]:
#     print("meow")

# pythonic magic
# print("meow\n" * 3, end="")

# ask user using infinite loop !!! :
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break


# while True:
#     n = int(input("what's n? "))
#     if n > 0:
#         break
    
# for _ in range(n):
#     print("meow")

# better design
def main():
    number = get_number()
    meow(number)

def get_number():
    n = int(input("What's n? "))
    if n > 0:
        #break
        return n
    #return n

def meow(n):
    for _ in range(n):
        print("meow")


main()

"""
    list, go to hogwarts.py
"""