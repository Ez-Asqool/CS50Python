# Simple Quiz (5 questions) Game

def main():
    print("Welcome to the Python 5-questions Quiz. Let's begin.")
    quiz()

def quiz():
    questions = [
        {"body": "Python is a compiled programming language.(t/f)?", "answer": 'f'},
        {"body": "The input() function in Python returns a string.(t/f)?", "answer": 't'},
        {"body": "In Python, == is used for assignment.(t/f)?", "answer": 'f'},
        {"body": "A for loop is used for iteration in Python.(t/f)?", "answer": 't'},
        {"body": "Indentation in Python is optional.(t/f)?", "answer": 'f'}
    ]

    mark = 0

    for question in questions:
        answer = input(f"{question['body']} \n")
        if answer == question["answer"]:
            mark += 1

    print(f"You've got {mark}/{len(questions)}")


main()
