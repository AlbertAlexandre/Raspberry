from tkinter import *
import datetime
import time
import calendar
from Photo import *

class TempsDate(object):
	
	def __init__(self, uneDateDebut, uneDateFin, uneFreq):
		
		self.__DateDebut = uneDateDebut
		self.__DateFin = uneDateFin
		self.__Freq = uneFreq

	def __Debut__(self, **kwargs):
		a = 0
		Freq = float(self.__Freq)
		debut = datetime.datetime.strptime(str(self.__DateDebut), '%d-%m-%Y %H:%M:%S')
		fin = datetime.datetime.strptime(str(self.__DateFin), '%d-%m-%Y %H:%M:%S')
		debutSeconde = calendar.timegm(debut.utctimetuple())
		finSeconde = calendar.timegm(fin.utctimetuple())
		while time.time() < debutSeconde:
			1
		print("Lancement séquence")
		while time.time() < finSeconde :
			tour = time.time() + (3600/Freq)
			while time.time() < tour :
				1
			a = a + 1
			print(a)
			PH = Photo(str(a), datetime.datetime.now().year, datetime.datetime.now().month,
			 datetime.datetime.now().day,datetime.datetime.now().hour,
			 datetime.datetime.now().minute, datetime.datetime.now().second)
			PH.__PrendrePhoto__()
			print("Photo ok")
		print("Fin")
