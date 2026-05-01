# x = int(input("What's x? "))

# print(f"x is {x}")

"""
    if the user enters string in x rather than a number wee will get:
        ValueError: invalid literal for int() with base 10: 'sd'

    So, its better to write our code with error handling 
    (to handle errors that might unexpectedly happen)

    --------------------------------------------------------------------------

    To catch errors use (try , except) keyword to try to execute python code and check whether or not
    something exceptional, something erroneous has happened.

    (try , except): can I go and try to do something except if something goes wrong, 
    I can do something else instead.
"""
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

#Best Practice: try to do the one or very few lines of code that can actually raise an exception and fail in someway

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}") #but here, Iam introduced a new kind of error (NameError: name x is not defined)
"""
    NameError: tring to use undefined variable

    -> why x is undefined even i was intending to define it in line 2 ??
    # when the error ValueError happening here (int(input("What's x? "))), 
    its prevent x from defining and getting a value.

    -> How can i solve something like this ?? there is another feature in try-except syntax whish is
    the keyword (else): try to do something except if this goes wrong,but if nothing goes wrong
    else go ahead and do this.  
"""
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

#or logically
# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")        

# print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x =  int(input("What's x? "))
#             #1 return x. or
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x        

# main()


#or 
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")

# main()


"""
    # rather than asking user "What's x? " every time he enter anything not an integer
    , if you wan to just ignore what the users enter not an integer, 
    -> you can use (pass) keyword: catch error and just silently ignore it
"""
def main(): #caller of the get_int() function
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt): # the callee function by main()
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass 

main()



"""
    raise: You can raise exceptions yourself using python's raise keyword.
"""