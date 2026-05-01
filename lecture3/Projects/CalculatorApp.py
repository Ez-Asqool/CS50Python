# Calculator App (+, - , *, /)

def main():
    print("Welcome to Calculator App")
    while True:
        firstNumber = get_first_number() 
        operation = get_operation()
        secondNumber = get_second_number()
        calculator(firstNumber, operation, secondNumber)
        if not want_to_continue():
            break
    

def calculator(firstNumber, operation, secondNumber):
    match operation:
        case '*':
            print(f"Result = {firstNumber * secondNumber}")
        case '+':
            print(f"Result = {firstNumber + secondNumber}")
        case '/':
            if secondNumber == 0:
                print("Invalid operation. Can't divide by zero!")
            else:
                print(f"Result = {firstNumber / secondNumber}")
        case '-':
            print(f"Result = {firstNumber - secondNumber}")



def get_first_number():
    while True:
        try:
            return float(input("Enter first number: "))
        except ValueError:
            print("Only numbers (integers or decimals) are allowed!")

def get_second_number():
    while True:
        try:
            return float(input("Enter second number: "))
        except ValueError:
            print("Only numbers (integers or decimals) are allowed!")


def get_operation():
    while True:
        operation = input("Choose operation (+, -, *, /): ")
        match operation:
            case '+' | '-' | '*' | '/' :
                return operation    
            case _:
                print(f"({operation}) is not valid.!!")


def want_to_continue():
    while True:
        answer = input("Do you want to continue? (y/n): ")
        match answer:
            case 'y' | 'Y' :
                return True
            case 'n' | 'N' :
                return False
            case _:
                print("Please, answer with (y) for Yes or (n) for No.") 



main()

