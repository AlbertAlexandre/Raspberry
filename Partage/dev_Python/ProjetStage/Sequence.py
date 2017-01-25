from datetime import *
import datetime
import time
import os
from Photo import *

class Sequence(object):
	
	def __init__(self, unNbJour, unePremiere, uneFreq, uneEspece, unProgramme):
		
		self.__NbJour = unNbJour
		self.__Premiere = unePremiere
		self.__Freq = uneFreq
		self.__Espece = uneEspece
		self.__Programme = unProgramme
		self.Compteur = 0

	def __Photo__(self, Chemin) :
		
		PH = Photo(str(self.Compteur), datetime.datetime.now().year, datetime.datetime.now().month,
		 datetime.datetime.now().day,datetime.datetime.now().hour, 
		 datetime.datetime.now().minute, self.__Espece, self.__Programme, Chemin)
		PH.__PrendrePhoto__()
		print("Photo " + str(self.Compteur) + " OK")
		
	def __Debut__(self, **kwargs):
		Chemin = self.CreerDossier()
		NbSecJour = float(self.__NbJour) * 86400
		NbSecFreq = float(self.__Freq) * 60
		TSecPremiere = float(self.__Premiere) * 60
		Fin = time.time() + NbSecJour
		
		self.__Photo__(Chemin)
		
		time.sleep(TSecPremiere)
		
		while time.time() < Fin :
			self.Compteur = self.Compteur + 1
			self.__Photo__(Chemin)
			time.sleep(NbSecFreq)
			
	def CreerDossier(self):
		NumDossier = 0
		ChaineDossier = "/home/pi/Partage/dev_Python/ProjetStage/Photos/" + self.Annee2(str(datetime.datetime.now().year))\
		 + "_" + self.Chaine2(str(datetime.datetime.now().month)) + "_" + self.Chaine2(str(datetime.datetime.now().day)) \
		 + "_" + self.__Programme + "_" + self.__Espece + "_" + str(self.NumCam()) + "_" + self.Chaine2(str(NumDossier))
		
		while os.path.exists(ChaineDossier):
			NumDossier = NumDossier + 1
			ChaineDossier = "/home/pi/Partage/dev_Python/ProjetStage/Photos/" + self.Annee2(str(datetime.datetime.now().year))\
			+ "_" + self.Chaine2(str(datetime.datetime.now().month)) + "_" + self.Chaine2(str(datetime.datetime.now().day)) \
			+ "_" + self.__Programme + "_" + self.__Espece + "_" + str(self.NumCam()) + "_" + self.Chaine2(str(NumDossier))
		os.mkdir(ChaineDossier)
		return(ChaineDossier)
		
	def Annee2(self, uneAnnee4):
		Annee2 = str(uneAnnee4)[2:4]
		return (Annee2)
		
	def Chaine2(self, uneChaine):
		while len(uneChaine)<2:
			uneChaine = "0" + uneChaine
		return(uneChaine)
		
	def Chaine3(self, uneChaine):
		while len(uneChaine)<3:
			uneChaine = "0" + uneChaine
		return(uneChaine)
		
	def NumCam(self):
		ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
		donnees = Donnees_SQL(ConnexionString)
		donnees.SQL_projetEnCours()
		result = donnees.chargerLesDonnees_RequeteSQL()
		NumCam = str(result[0])
		NumCam = NumCam.replace(")","")
		NumCam = NumCam.replace("(","")
		NumCam = NumCam.replace(",","")
		NumCam = self.Chaine3(NumCam)
		return(NumCam)
