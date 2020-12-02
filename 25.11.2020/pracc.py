print("If you need help, type 'help'.")
userInput = input("> ")
 userInput == "help":
    print("Type 'start' to start the car.")
    print("Type 'stop' to stop the car.")
    print("Type 'quit' to quit the program.")
else:
    print("I can not understand that.")
while userInput == "start":
    print("Car started... Ready to go!")
    userInput = input("> ")
while userInput == "stop":
    print("Car stopped.")
else:
    print("I can not understand that")
