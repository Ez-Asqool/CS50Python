# ask user's name, age, university. Then prints a formatted sammary 
def main():
    hello()
    name = input("What's your name? ").strip().title()
    first, last = name.split(" ")
    hello(first)
    age = int(input("What's your age? "))
    university = input("What's your university name? ").strip().title()
    studentInfoSammary(name, age, university)


def hello(to = "student"):
    print("Hello", to)


def studentInfoSammary(name, age, university):
    print(f"Your student card information is \n- name: {name} \n- age: {age} \n- university: {university}")


main()