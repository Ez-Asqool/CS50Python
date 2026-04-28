"""
    arithmatic operators:
    +
    -
    /
    *
    %
"""

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


"""
    bool datatype: boolean values (True / False)

    -> create my own function is_even() 
"""

# def main():
#     x = int(input("what's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# main()


"""
    ! - if we ask a question with one if -  else statement 
    like is_even() function implementation , then we can pythonk this to be elegant line:
"""

# def main():
#     x = int(input("what's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n%2 == 0 else False

# main()


#or

def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n%2 == 0

main()


"""
    There are another syntax you can used to implement the same idea

    --> match (keyword)  like switch in java !

    Go To house.py
"""