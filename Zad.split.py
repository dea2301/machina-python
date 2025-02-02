#Zad s predacvanja riješen pomoću .split()
vrijeme = input ("Unesite vrijeme (HH:MM): ")
sati, minute = vrijeme.split(":")
print(f"Sati: {sati}, Minute: {minute}")
sati_int= int (sati)
minute_int= (int (minute))

if (8 <= sati_int < 11) or (sati_int == 11 and minute_int <= 30) or (sati_int == 14 and minute_int > 30) or (15 <= sati_int < 18):
    print('radi')
else:
    print('ne radi')