from datetime import *
import time
import os
from Photo import *
from Vue import *

class TempsJour(object):
	
	def __init__(self, unNbJour, uneFreq):
		
		self.__NbJour = unNbJour
		self.__Freq = uneFreq
		
	def __Debut__(self, **kwargs):
		
		NbSecJour = float(self.__NbJour) * 86400

		Freq = float(self.__Freq)
		heure = float(time.time())
		fin = heure + NbSecJour
		a = 0

		while time.time() < fin :
			tour = time.time() + (3600/Freq)
			while time.time() < tour :
				1
			a = a + 1
			print(a)
			PH = Photo(str(a), datetime.datetime.now().year, datetime.datetime.now().month,
			 datetime.datetime.now().day,datetime.datetime.now().hour, 
			 datetime.datetime.now().minute, datetime.datetime.now().second)
			PH.__PrendrePhoto__()
			print("photo ok")
			

		
		
