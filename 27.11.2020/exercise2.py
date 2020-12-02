import random  
random_number = random.randint(1,9)
userGuess = 0
print ("Random number is: ", random_number)
for i in range(10):
    userInput = int(input("Input your number: "))
    if i != random_number:
        userGuess = userGuess + 1
        print("You guessed the wrong number, try again. You tried: ", userGuess)
    else:
        print("You won.")
        break
    

