#test square function 

# from calculator import square

# def main():
#     test_square()


# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# if __name__ =="__main__":
#     main()


"""
    ! rather than writing multiple lines to test a function. you can use assert:
    
    # -> assert : is a keyword that allow me to do that , as in English,
        to assert that something is true. and if it is, nothing's going to happen.
        and no errors going to appear on screen.
        But if you assert something in python and it is not true (it return false) , you actually going to see
        some kind of error on the screen (AssertionError)
"""

# from calculator import square

# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
        


# if __name__ =="__main__":
#     main()

#this will cause AssertionError , we can handle it by try-except

# from calculator import square

# def main():
#     test_square()


# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")
        


# if __name__ =="__main__":
#     main()


"""
    ! - what if we actually want to add additional test cases here as well??
        it seems like we might end up writing way more code than would be ideal. 

    - Why we dont create tools that make it a little easierto do code test.??
    
    ->we can do it by using (pytest tool) 
        #pythest is a third party program that you can dowenload it and install 
        that will automate the testing of my code as long as I write the tests.

    -> Unit Test: Testing individual units (functions) of your program
"""

# use pytest to handle the try-except and printing. pip install pytest 
# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
    #now: pytest will handle the try-except and printing. 

"""
    -> rather than writing all tests in one function,
        lets break down our tests into different categories like test 
        positive numbers separately and negative numbers separately and tests zero separately
"""

from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0

"""
    #assert that passing a string will cause an error, rather assert, we need pytest library itself
        -> raises function allows me to express that i expect an exception to be raised.
"""

def test_str():
    with pytest.raises(TypeError):
        square("cat")   #I expect error of tyoe TypreError when i call square and passing 'cat' value



#test code expect strings input -> go to hello.py