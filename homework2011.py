year = int(input("Unesite svoje godište: "))
if year%4==0 & (year%100!=0 | year%400==0):
    print("Vaša godina rođenja je prestupna.")
    print()
    name = input("Unesite vaše ime: ")
    if (name=="Mujo"):
            import datetime
            datum = datetime.datetime.now()
            print ("Današnji datum je", datum)

    else:
        print("Mujo zakasnio si.")
        print()
else:
    print("Vaša godina rođenja nije prestupna.")
    print()
    maleName=input("Unesite muško ime:")
    femaleName=input("Unesite žensko ime:")
    if len(maleName)>4:
        print("Volim kratke muškarce.")
    else:
        print("Izvini imam dečka")
print()
numberOne=int(input("Unesite prvi broj: "))
numberTwo=int(input("Unesite drugi broj: "))   
numberThree=int(input("Unesite treći broj: "))  
print()
if numberOne>numberTwo and numberOne>numberThree:
    print(numberOne, "je najveći broj.")
elif numberTwo>numberOne and numberTwo>numberThree:
    print(numberTwo, "je najveći broj.")
else:
    print(numberThree, "je najveći broj.")
print()
arr=[1,2,3,4,5]
if (numberOne and numberTwo and numberThree in arr):
    print("Ispravno")
else:
    print("Neispravno.")
print()
bored = input("Da li ti je dosadno? (odgovoriti sa 'Da' ili 'Ne'): ")
if bored == "Da":
    print("Pošalji Atifu mail.")    
elif bored == "Ne":
    print("Vidimo se u četvrtak.")
else:
    print("Unesite ispravan odgovor.")