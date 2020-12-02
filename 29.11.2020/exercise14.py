from datetime import datetime

#datumi

dateOne = input("Enter your first date in 'dd.mm.yyyy' format: ")
dateTwo = input("Enter your second date in 'dd.mm.yyyy' format: ")
dateOne_format = datetime.strptime(dateOne, "%d.%m.%Y")
dateTwo_format = datetime.strptime(dateTwo, "%d.%m.%Y")

#datumi

#postavljam uslov da je finalni datum koji mi treba jednak 0, da bih kasnije dobio finalni datum kao razliku unesenih datuma

finalDate = 0

if dateOne_format>dateTwo_format:
    print("First date is greater.")
    finalDate = dateOne_format - dateTwo_format
else:
    print("Second date is greater.")
    finalDate = dateTwo_format - dateOne_format
print(f"Difference is {finalDate.days} days.")




