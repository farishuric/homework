userNumber = int(input("Enter your number: "))
digitsCount = 0
while userNumber != 0:
    userNumber = userNumber // 10
    digitsCount = digitsCount + 1
print(f"Total digits are {digitsCount}")