"""
boolean expressions like (x < y) : is an expression with yes or no answer(tichnically true or false answer).
"""

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equla to y")
    
"""
    ##we want the code to be well designed . 
    .assume x is less than y. so what is the feasibility of checking if x is grater than y
    or if x is equal to y. so the code is not well designed eaven if it is coorect. 
    
    So ->>> we want to better our design to get a well designed code
    By redesign if statement to be: if one boolean expression's result is true
    then you does not want to check another boolean expressions. 

    we wellimproving this using elif (else if) keyword:
"""


# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")


"""
    now: if the x is not less than y and not grater than y. then we well go down 
    to the result of third question : x is equal   to y.
    So --> when the first question and the second question is false 
    (if logically true) the answer well be the third question answer 
    and we dont need to ask the third question.


    #To design this program to be even better we will use (else) keyword 
"""

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


"""
    or keyword: if we want to ask a question or another question
"""

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# -> Better Design:
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# !Note: python enforces indentation requirement 


"""
    and keyword: to congunction one or two or more questions

    ------->>> Go to grade.py
"""


