import os
from VueV2 import * 

class Photo(object):
	
	def __init__(self, unNumero, uneAnnee, unMois, unJour, uneHeure, uneMinute, uneEspece, unProgramme):
		self.__Numero = unNumero
		self.__Annee = uneAnnee
		self.__Mois = unMois
		self.__Jour = unJour
		self.__Heure = uneHeure
		self.__Minute = uneMinute
		self.__Espece = uneEspece
		self.__Programme = unProgramme
	
	def __PrendrePhoto__(self, **kwargs):
		print (self.__Heure)
		Fichier_Config = open("conf.txt", "r")
		Config = Fichier_Config.read()
		os.system("raspistill -o Photos/" + self.__Numero + self.__Espece + self.__Programme + ".jpg " + Config)

