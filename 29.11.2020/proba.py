from datetime import datetime

date_1 = datetime(2020,2,25).date()
date_2 = datetime(2020,9,17).date()

delta = None

if date_1>date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print(f"Difference is {delta.days} days")