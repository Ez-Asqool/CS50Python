#multiplication table game:

def main():
    number = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(number)

def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

main()