def calculTempsJours():
	print("jour")
	nbJour = int(sb_jour.get())
	nbSeconde = nbJour * 86400
	tempsFin = time.time() + nbSeconde
	print(tempsFin)
	
	
def dateADate():
	print("date")
	print(tempsFin)

def Validation():
	val = v.get()
	if val == 1:
		calculTempsJours()
	elif val == 2:
		dateADate()
