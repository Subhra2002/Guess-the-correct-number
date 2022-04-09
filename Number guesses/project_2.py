import random
randomNumber = random.randint(1, 100)
# print(randomNumber)
userGuess = None
guesses = 0
while(userGuess != randomNumber):
    try:
        userGuess = int(input("Enter your guess number:"))
        guesses += 1
 
        if(userGuess == randomNumber):
         print("You are right!")

        else:
            if(userGuess > randomNumber):
                print("your guess is Wrong! samller number please")
            else:
                 print("your guess is Wrong! higher number please")
    except Exception as e:
        print("Make sure you Enetr a valid number")
print(f"you guess is correct in {guesses} attempt")
