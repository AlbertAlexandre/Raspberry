import os

class Photo(object):
	
	def __init__(self, unNom, uneAnnee, unMois, unJour, uneHeure, uneMinute, uneSeconde):
		self.__Nom = unNom
		self.__Annee = uneAnnee
		self.__Mois = unMois
		self.__Jour = unJour
		self.__Heure = uneHeure
		self.__Minute = uneMinute
		self.__Seconde = uneSeconde
	
	def __PrendrePhoto__(self, **kwargs):
		os.system("raspistill -o Photos/" + self.__Nom + ".jpg -awb off -awbg 1.15,1.6")
