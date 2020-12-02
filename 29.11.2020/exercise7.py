suma = 0
userInput = input("Enter number:")
while userInput.isnumeric():
    suma = int(userInput) + suma
    userInput = input("Enter number:")
    if userInput == "":
        print(f"Your total result is {suma}")
        userInput = input("Enter number:")
    if not userInput.isnumeric():
        print("Value is not numeric.")
        userInput = input("Enter number:")
