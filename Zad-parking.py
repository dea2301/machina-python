#Parkiralište u Ericssonu je otvoreno između 8:45 i 10h. Napiši program koji će za unešeno vrijeme u formatu HH:MM vratiti je li parkiralište otvoreno.

#pretpostavimo da parking radi samo radnimm danima od pon do petka od 8:45 do 10h
#prvo provjeri koji je dan u tjednu, ako zadovljava uvjet korisnik unosi vrijeme 



import datetime as dt
datum = input ("Unesite datum (YYYY-MM-DD) za koji želite provjeriti radno vrijeme: ")
datum = dt.datetime.strptime(datum, "%Y-%m-%d")
dan_u_tjednu = datum.weekday()

if (dan_u_tjednu >= 5):
    print ("Parking ne radi vikendom!")
else: 
    print ("Parking radi! Provjeri radno vrijeme!")
    vrijeme = input ("Unesi vrijeme (HH:MM) koje želiš provjeriti: ")
    vrijeme = dt.datetime.strptime (vrijeme, "%H:%M").time()
    početak_rada = dt.time (8, 45)
    kraj_rada = dt.time (10, 0)
    if not (početak_rada < vrijeme < kraj_rada):
        print ("Parking ne radi!")
    else:
        print ("Parking radi!")
    
