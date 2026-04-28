#Ask user for their name
# name = input("What's your name? ")

#Say hello to user
#print("Hello,", name)
#print('hello, ' + name)

"""
Any thing here is a comment
......
... is a comment

from python offecial documentation:
- parameter: what values can function take.
- argument: the actual values that the function taked.
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=false)
*objects : take infinite objects (arguments)
sep=' ' : separator: separate between objects using ' ' .
end='\n': the hole thing will gonna be ended with new line.

- you can either use single quots or double quots.
"""

# override the default value of end='\n' parameter to change the basic behaviour.
# print("Hello, ", end="")
# print(name)

# override the default value of sep=' ' parameter to change the basic behaviour
# print("hello", name, sep=', ')

#escape character by using back-slash \
# print("hello, \"friend\"")

#formate special string.
# print(f"hello, {name}")


################################################### 46 m

"""
str datatype:
str functions.
"""
#Remove whitespace from beggining and the end of str using .strip() method
#name = name.strip()

#Capitalize user's name, !just first str word
#name = name.capitalize()

#capitalie user's name
#name = name.title()



#chain functions together

#Remove whitespace from beggining and the end of str and capitalie user's name
#name = name.strip().title()

#Take user input,  Remove whitespace from beggining and the end of str and capitalie user's name
#name = input("What's your name? ").strip().title()

#split string to a smaller substrings.- split users name into first name and last name. based on ' ' white space character.
# first, last = name.split(" ") 
# print(f"hello, {first}")



"""
int ,integer datatype
"""

############################
"""
    go to calculator.py then come back again.
"""
############################


"""
def keyword: defining your own functions.
"""

#def/define hello function and call it.
"""
def : to define 
Hello : name of function
(): open prantheses to pass arguments in it , but hello doesnt has any parameter.
: -> colon (stay tuned for indentation) every line of code you indent is treated as the meaning/content of the new function hello()
    so, every thing indented will be part of this function
"""

# def hello():
#     print("Hello")

#passing parameter
# def hello(to):
#     print("hello,", to)

# name = input("What's your name? ")
# hello(name)


#give parameter default value
# def hello(to="world"):
#     print("hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)


"""
What about doing this ?? call function and then defining it.

hello()
name = input("What's your name? ")
hello(name)



def hello(to="world"):
    print("hello,", to)


*** the result will be NameError: name 'hello' is not defined. did you mean help?

    -> because the interpreter will interprit line by line and calling function
    before defining/interpret it is not allowed.

    !!!! but we can fix it in the more standured way by doing this:

    #pot the main part of your code at the top of the file by defining function called main():
    and then define hello(): function that used in main

    .. now to execute your main code, you call main() method and that will not make any problems,
    because when we execute, the interpreter will:
    1- define function main.
    2- define hello function.
    3- call main function that uses hello function and that will not cause any problem because 
    hello() is defined/interpreted , then it used in main. 

"""

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()



#############################################33

"""
Scope , if we doing this

def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello,", name)

main()


    -> this will cause error, name is not defined.
    because the name variable is in the scope of main function and not in the scope of the hello function.

"""



##############################3

"""
return
    ?-> what if i want from hello function to hand me back a value not just take a side effect persay.
    so we want to make the function returen a value

    #you can use return keyword to return a value exciplicitly.


    ------ go to calculator.py

"""

