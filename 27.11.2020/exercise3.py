h = 10
a = 0
b = 10
for i in range(h):
    for j in range(a):
        print ("*", end="")
    a = a + 1
    print()
for k in range(h):
    for l in range(b):
        print ("*", end="")
    b = b - 1
    print()