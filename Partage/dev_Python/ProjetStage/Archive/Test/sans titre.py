import time

NbJour = float(input("Choisir nb jour\n"))
NbSecJour = NbJour * 86400

Freq = float(input("Choisir une fréquence\n"))

heure = time.time() 
fin = heure + NbSecJour
a = 0

while time.time() < fin :
	tour = time.time() + (3600/Freq)
	while time.time() < tour :
		1
	a = a + 1
	print(a)
