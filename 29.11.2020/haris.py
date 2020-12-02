from datetime import datetime
datum1=input("Unesi prvi datum u 'dd-mm-yyyy' formatu:")
datum2=input("Unesi drugi datum u 'dd-mm-yyyy' formatu:")
datum1_format=datetime.strptime(datum1,"%d-%m-%Y")
datum2_format=datetime.strptime(datum2,"%d-%m-%Y")
 
razlikadatuma=0
 
if datum1_format>datum2_format:
    print("prvi datum je veci")
    razlikadatuma=datum1_format-datum2_format
else:
    razlikadatuma=datum2_format-datum1_format
print(f"Razlika datuma je {razlikadatuma.days} dana.")
