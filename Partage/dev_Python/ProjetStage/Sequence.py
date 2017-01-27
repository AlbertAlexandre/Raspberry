from datetime import *
import datetime
import time
import os
from Photo import *

class Sequence(object):
	
	def __init__(self, unNbJour, unePremiere, uneFreq, uneEspece, unProgramme, uneTemperature, uneMethode, unID, uneRep, uneMod, unNum, unEmp, unAutre):
		
		self.__NbJour = unNbJour
		self.__Premiere = unePremiere
		self.__Freq = uneFreq
		self.__Espece = uneEspece
		self.__Programme = unProgramme
		self.__Temperature = uneTemperature
		self.__Methode = uneMethode
		self.__ID = unID
		self.__Repetition = uneRep
		self.__Modalite = uneMod
		self.__NumMod = unNum
		self.__Emplacement = unEmp
		self.__Autre = unAutre
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
		
		datedebut = str(datetime.datetime.now())
		
		self.__Photo__(Chemin)
		
		time.sleep(TSecPremiere)
		
		date1 = str(datetime.datetime.now())
		
		while time.time() < Fin :
			self.Compteur = self.Compteur + 1
			self.__Photo__(Chemin)
			time.sleep(NbSecFreq)
		date2 = str(datetime.datetime.now())
		self.__CreationFichierResume__(Chemin, date1, date2, datedebut)
			
	def CreerDossier(self):
		NumDossier = 0
		Fichier_Chemin = open("Chemin.txt", "r")
		LeChemin = Fichier_Chemin.read()
		ChaineDossier = LeChemin + "/" + self.Annee2(str(datetime.datetime.now().year))\
		 + "_" + self.Chaine2(str(datetime.datetime.now().month)) + "_" + self.Chaine2(str(datetime.datetime.now().day)) \
		 + "_" + self.__Programme + "_" + self.__Espece + "_" + str(self.NumCam()) + "_" + self.Chaine2(str(NumDossier))
		
		while os.path.exists(ChaineDossier):
			NumDossier = NumDossier + 1
			ChaineDossier =  LeChemin + "/" + self.Annee2(str(datetime.datetime.now().year))\
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
		
	def __CreationFichierResume__(self, unChemin, uneDate1, uneDate2, uneDateDebut):
		
		freq = float(self.__Freq) * 60
		tot = float(self.__NbJour) * 86400
		prem = float(self.__Premiere) * 60
		
		Fichier = "Periode : " + str(freq) + "\n" +\
		"Durée Totale : " + str(tot) + "\n" +\
		"Durée avant 1ere prise : " + str(prem) + "\n" +\
		"Date 1er fichier : " + uneDate1 + "\n" +\
		"Date dernier fichier : " + uneDate2 + "\n" +\
		"Nombre de photos total : " + str(self.Compteur + 1) + "\n" +\
		"Date de debut : " + uneDateDebut + "\n" +\
		"Espece : " + self.__Espece + "\n" +\
		"Temperature : " + self.__Temperature + "\n" +\
		"Méthode : " + str(self.__Methode) + "\n" +\
		"Identifiant de l'échantillon : " + str(self.__ID) + "\n" +\
		"Numero de répétition ou sous-répétition : " + str(self.__Repetition) + "\n" +\
		"Modalité : " + str(self.__Modalite) + "\n" +\
		"Numéro de module : " + str(self.__NumMod) + "\n" +\
		"L'emplacement dans le module : " + str(self.__Emplacement) + "\n" +\
		"Autre : " + str(self.__Autre)
		
		
		Resume = open(unChemin + "/Resume.txt", "w")
		Resume.write(Fichier)
		Resume.close()
		
		
