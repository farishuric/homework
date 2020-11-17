#print KM apoena
cash = float(input("Unesite količinu novca: "))
print()
tens = int(cash)//10
final = float(cash-tens*10)
fives = int(final)//5
twos = int(final-fives*5)//2
ones = int(final-fives*5-twos*2)//1
kf_50 = float(final-fives*5-twos*2-ones*1)//0.50
kf_20 = float(final-fives*5-twos*2-ones*1-kf_50*0.50)//0.20
kf_10 = float(final-fives*5-twos*2-ones*1-kf_50*0.50-kf_20*0.20)//0.10
kf_05 = float(final-fives*5-twos*2-ones*1-kf_50*0.50-kf_20*0.20-kf_10*0.10)//0.05

print ("Ukoliko želite isplatu u Konvertlnim Markama, isplata će biti u sljedećim apoenima:")
print ("Deset KM: ",tens)
print ("Pet KM: ", fives)
print ("Dva KM: ", twos)
print ("Jedan KM: ", ones)
print ("Pedeset feninga: ", int(kf_50))
print ("Dvadeset feninga: ", int(kf_20))
print ("Deset feninga: ", int(kf_10))
print ("Pet feninga: ", int(kf_05))
print()
print()
#print KM apoena


#eur/dollar valuta
eur = cash*1.95583
usd = cash*1.62
#print isplata
print("Ukoliko želite isplatu u eurima dobili bi ste",(round(eur,2)),"€")
print("Ukoliko želite isplatu u eurima dobili bi ste",(round(usd,2)),"$")
print()
print()


print("Novac u Euro valuti će vam biti isplaćen u sljedećim apoenima:")
#eur valuta
tens = int((round(eur,2)))//10
final = float(eur-tens*10)
fives = int(final)//5
twos = int(final-fives*5)//2
ones = int(final-fives*5-twos*2)//1
kf_50 = float(final-fives*5-twos*2-ones*1)//0.50
kf_20 = float(final-fives*5-twos*2-ones*1-kf_50*0.50)//0.20
kf_10 = float(final-fives*5-twos*2-ones*1-kf_50*0.50-kf_20*0.20)//0.10
kf_05 = float(final-fives*5-twos*2-ones*1-kf_50*0.50-kf_20*0.20-kf_10*0.10)//0.05
kf_01 = float(final-fives*5-twos*2-ones*1-kf_50*0.50-kf_20*0.20-kf_10*0.10-kf_05*0.05)//0.01
print ("Deset €: ",tens)
print ("Pet €: ", fives)
print ("Dva €: ", twos)
print ("Jedan €: ", ones)
print ("Pedeset centi: ", int(kf_50))
print ("Dvadeset centi: ", int(kf_20))
print ("Deset centi: ", int(kf_10))
print ("Pet centi: ", int(kf_05))
print ("Jedan cent: ",int(kf_01))
print()
#eur valuta
#dolar valuta
print("Novac u Dolar valuti će vam biti isplaćen u sljedećim apoenima:")
tens_usd = int((round(usd,2)))//10
final = float(usd-tens_usd*10)
fives_usd = int(final)//5
twos_usd = int(final-fives_usd*5)//2
ones_usd = int(final-fives_usd*5-twos_usd*2)//1
cents_50 = float(final-fives_usd*5-twos_usd*2-ones_usd*1)//0.50
cents_20 = float(final-fives_usd*5-twos_usd*2-ones_usd*1-cents_50*0.50)//0.20
cents_10 = float(final-fives_usd*5-twos_usd*2-ones_usd*1-cents_50*50-cents_20*0.20)//0.10
cents_05 = float(final-fives_usd*5-twos_usd*2-ones_usd*1-cents_50*50-cents_20*0.20-cents_10*0.10)//0.05
cents_01 = float(final-fives_usd*5-twos_usd*2-ones_usd*1-cents_50*50-cents_20*0.20-cents_10*0.10-cents_05*0.05)//0.01
print ("Deset $: ",tens_usd)
print ("Pet $ ", fives_usd)
print ("Dva $: ", twos_usd)
print ("Jedan $: ", ones_usd)
print ("Pedeset centi: ", int(cents_50))
print ("Dvadeset centi: ", int(cents_20))
print ("Deset centi: ", int(cents_10))
print ("Pet centi: ", int(cents_05))
print ("Jedan cent: ",int(cents_01))
#dolar valuta


