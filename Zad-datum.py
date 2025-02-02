#Napiši program koji će za svaki unešeni datum (u bilo kojem obliku koji vam padne na pamet(jedan string)) vratiti koji je bio dan 

import datetime as dt
datum = input ("Unesite datum (DD.MM.YYYY) za koji želite provjeriti : ")
datum = dt.datetime.strptime(datum, "%d.%m.%Y")
dan_u_tjednu = datum.strftime ("%A")
print ("Ovaj datum je:",dan_u_tjednu)