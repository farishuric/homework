import time 
target = 20
stringPosition = 0
for i in range(target):
    for j in range(target):
        if j == stringPosition:
            print("#")
        else:
            print("", end="")
        print("\r", end="")             
        stringPosition = stringPosition + 1  
        time.sleep(0.1)
        