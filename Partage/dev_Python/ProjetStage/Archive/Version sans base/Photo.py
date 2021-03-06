import os
from VueV2 import * 
from Donnees_SQL import *

class Photo(object):
	
	def __init__(self, unNumero, uneAnnee, unMois, unJour, uneHeure, uneMinute, uneEspece, unProgramme, unChemin):
		self.__Numero = unNumero
		self.__Annee = uneAnnee
		self.__Mois = unMois
		self.__Jour = unJour
		self.__Heure = uneHeure
		self.__Minute = uneMinute
		self.__Espece = uneEspece
		self.__Programme = unProgramme
		self.__Chemin = unChemin
	
	def __PrendrePhoto__(self, **kwargs):
		
		##Nom##
		
		Esp = self.Espece10(self.__Espece)
		An = self.Annee2(str(self.__Annee))
		Mois = self.Chaine2(str(self.__Mois))
		Jour = self.Chaine2(str(self.__Jour))
		Heure = self.Chaine2(str(self.__Heure))
		Min = self.Chaine2(str(self.__Minute))
		Num = self.Chaine3(str(self.__Numero))
		
		##Connexion##
		
		ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
		donnees = Donnees_SQL(ConnexionString)
		donnees.SQL_projetEnCours()
		result = donnees.chargerLesDonnees_RequeteSQL()
		NumCam = str(result[0])
		NumCam = NumCam.replace(")","")
		NumCam = NumCam.replace("(","")
		NumCam = NumCam.replace(",","")
		NumCam = self.Chaine3(NumCam)
		
		##NomFichier##
		
		MaChaine = Esp + An + Mois + Jour + Heure + Min + "_" + NumCam + "_" + Num
		Fichier_Config = open("conf.txt", "r")
		Config = Fichier_Config.read()
		os.system("raspistill -o " + self.__Chemin + "/" + MaChaine + ".jpg " + Config)
		
		
	def Chaine3(self, uneChaine):
		while len(uneChaine)<3:
			uneChaine = "0" + uneChaine
		return(uneChaine)
		
	def Annee2(self, uneAnnee4):
		Annee2 = str(uneAnnee4)[2:4]
		return (Annee2)
		
	def Chaine2(self, uneChaine):
		while len(uneChaine)<2:
			uneChaine = "0" + uneChaine
		return(uneChaine)
		
	def Espece10(self, uneChaine):
		while len(uneChaine)<10:
			uneChaine = uneChaine + "_" 
		return(uneChaine)
