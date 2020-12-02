numbers = (1,2,3,4,5,6,7,8,9)
num_even = 0
num_odd = 0
for i in numbers:
    if i%2==0:
        num_even = num_even + 1
print("Broj parnih je: ", num_even)
for j in numbers:
    if j%2!=0:
        num_odd = num_odd + 1
print("Broj neparnih je: ", num_odd)