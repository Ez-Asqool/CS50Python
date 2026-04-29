# number guessing game

def main():
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)
    number_guessing_game()



def number_guessing_game():
    numberOfTrials = 5
    actualNumber = 0
    print(f"Guess a number between 0 and 100. You have just {numberOfTrials} trials to guess. Let's start")
    for i in range(numberOfTrials):
        guessedNumber =  int(input(f"Trial - {i+1}, Enter a number: "))
        if 0 <= guessedNumber <= 100 :
            if guessedNumber == actualNumber:
                print("Whoooo.! You Hit That, The number is 19. Congratulations." )
                break
            elif guessedNumber > actualNumber:
                print(f"You are close!, Try another number less than {guessedNumber}")
            else:
                print(f"You are close!, Try another number greater than {guessedNumber}")
        else:
            print("Opps!, You entered a number outside the range, please guess a number between 0 and 20 ")
        if(i == numberOfTrials-1):
            print("Number of trials is finished !!. let's resart the game, Good Luck.")

def hello(to=""):
    print("Hello", to)


main()

