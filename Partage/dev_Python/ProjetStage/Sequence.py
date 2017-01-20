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

	def __Photo__(self) :
		PH = Photo(str(self.Compteur), datetime.datetime.now().year, datetime.datetime.now().month,
		 datetime.datetime.now().day,datetime.datetime.now().hour, 
		 datetime.datetime.now().minute, self.__Espece, self.__Programme)
		PH.__PrendrePhoto__()
		print("Photo " + str(self.Compteur) + " OK")
		
	def __Debut__(self, **kwargs):
		
		NbSecJour = float(self.__NbJour) * 86400
		NbSecFreq = float(self.__Freq) * 60
		TSecPremiere = float(self.__Premiere) * 60
		Fin = time.time() + NbSecJour
		
		self.__Photo__()
		
		time.sleep(TSecPremiere)
		
		while time.time() < Fin :
			self.Compteur = self.Compteur + 1
			self.__Photo__()
			time.sleep(NbSecFreq)
			

