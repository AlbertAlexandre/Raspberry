import os
from VueV2 import * 

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
		Fichier_Config = open("conf.txt", "r")
		Config = Fichier_Config.read()
		os.system("raspistill -o Photos/" + self.__Nom + ".jpg " + Config)

	def _test(self):
		print(VueV2.__lb_Programme)
