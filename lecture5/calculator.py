#Unit Test: test your code by another code.

def main():
    x = int(input("What's x? "))
    print("z squared is", square(x))


def square(n):
    # return n + n
    return n * n

#let's sure that main is not always called
if __name__ =="__main__":
    main()

#now lets write another program to test this program: Go to -> test_calculator.py




