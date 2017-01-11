from datetime import *
import time
import os
from Photo import *
from Vue import *

class Sequence(object):
	
	def __init__(self, unNbJour, unePremiere, uneFreq):
		
		self.__NbJour = unNbJour
		self.__Premiere = unePremiere
		self.__Freq = uneFreq
		self.Compteur = 0

	def __Photo__(self) :
		PH = Photo(str(self.Compteur), datetime.datetime.now().year, datetime.datetime.now().month,
		 datetime.datetime.now().day,datetime.datetime.now().hour, 
		 datetime.datetime.now().minute, datetime.datetime.now().second)
		PH.__PrendrePhoto__()
		print("Photo " + str(self.Compteur) + " OK")
		
	def __Debut__(self, **kwargs):
		
		NbSecJour = float(self.__NbJour) * 86400
		NbSecFreq = float(self.__Freq) * 60
		TSecPremiere = float(self.__Premiere) * 60
		Fin = time.time() + NbSecJour
		self.__Photo__()
		
		time.sleep(TSecPremiere)
		
		self.Compteur = self.Compteur + 1
		self.__Photo__()
		
		while time.time() < Fin :
			time.sleep(NbSecFreq)
			self.Compteur = self.Compteur + 1
			self.__Photo__()
			
			

		
