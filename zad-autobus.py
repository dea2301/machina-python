#Zad1
# Napiši program koji će učitati broj učenika koji idu na ekskurziju
# veličinu busa i odrediti koliko buseva je potrebno unajmiti:

import math
broj_učenika = int (input("Unesi broj učenika: "))
veličina_autobusa = int (input ("Unesi veličinu autobusa: "))
broj_autobusa = print ("Potreban broj autobusa: ", math.ceil (broj_učenika/veličina_autobusa))

#L2

broj_učenika = int (input("Unesi broj učenika: "))
veličina_autobusa = int (input ("Unesi veličinu autobusa: "))
broj_autobusa = int (broj_učenika//veličina_autobusa)
if broj_učenika % veličina_autobusa != 0:
    print ("Potreban broj autobusa", broj_autobusa + 1)
    
if broj_učenika == 0:
    print ("Nije potreban niti jedan bus")