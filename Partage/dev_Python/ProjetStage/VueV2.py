from tkinter import *
from tkinter.messagebox import *
import datetime
import time
from Sequence import *
from Photo import *
from ConfigCamera import *

class VueV2(object):
	
	def __init__(self) :
		
				
		#Creation Fenetre
		
		self.__root = Tk()
		self.__root['bg'] = 'white'
		self.__root.title('Configuration Séquence')
		self.CreateWidgets()
		self.__root.mainloop()
		
	def CreateWidgets(self):
		
		#Creation Panneau
		
		self.__p = PanedWindow(self.__root, orient=VERTICAL)
		self.__p2 = PanedWindow(self.__root, orient=VERTICAL)
		self.__p.pack(side=LEFT, expand=Y, fill=BOTH)
		self.__p2.pack(side=RIGHT, expand=Y, fill=BOTH)


		#frameNbJour

		self.__frameNbjour = Frame(self.__root)
		self.__frameNbjour.pack(side=TOP, padx=20, pady=20)

		self.__lb_JourSouhaite = Label(self.__frameNbjour, text="Nombre de jour souhaité")
		self.__lb_JourSouhaite.pack()
		self.__sb_jour = Spinbox(self.__frameNbjour, from_=0, to=10,width=3)
		self.__sb_jour.pack()
		
		self.__lb_TempsPrise1 = Label(self.__frameNbjour, text="Temps avant première prise\n(en minute)")
		self.__lb_TempsPrise1.pack()
		self.__sb_TempsPrise1  = Spinbox(self.__frameNbjour, from_=0, to=10,width=3)
		self.__sb_TempsPrise1.pack()

		self.__lb_freq = Label(self.__frameNbjour, text="Fréquence des prises de vues\n(Toutes les n minutes)")
		self.__lb_freq.pack()
		self.__sb_freq = Spinbox(self.__frameNbjour, from_=0, to=600,width=3)
		self.__sb_freq.pack()

		
		#frameResume

		self.__frameResume = Frame(self.__root, borderwidth=2, relief=GROOVE)
		self.__frameResume.pack(side=BOTTOM, padx=20, pady=20)
		self.__lb_TempsE = Label(self.__frameResume, text="Temps écoulé : ")
		self.__lb_TempsE.pack()
		self.__lb_NbPhoto = Label(self.__frameResume, text="Nombre de photo(s) : ")
		self.__lb_NbPhoto.pack()
		self.__lb_PhotoR = Label(self.__frameResume, text="Photo(s) réstante(s) : ")
		self.__lb_PhotoR.pack()
		self.__lb_TempsR = Label(self.__frameResume, text="Temps restants : ")
		self.__lb_TempsR.pack()
		
		#Frame espece/programme
		
		self.__frameEP = Frame(self.__root)
		self.__frameEP.pack(side=TOP, fill=BOTH)

		self.__lb_Espece = Label(self.__frameEP, text="Espèce : ")
		self.__lb_Espece.pack()
		self.__tb_Espece = Entry(self.__frameEP)
		self.__tb_Espece.pack()
		
		self.__lb_Programme = Label(self.__frameEP, text="Programme : ")
		self.__lb_Programme.pack()
		self.__tb_Programme  = Entry(self.__frameEP)
		self.__tb_Programme.pack()

		#frameChoix

		self.__frameChoix = Frame(self.__root, borderwidth=10)
		self.__frameChoix.pack(side=LEFT, padx=10, pady=10)
		self.__btn_Valider = Button(self.__frameChoix, text="Valider", command = self.__Valider__)
		self.__btn_Valider.pack(side=LEFT)
		self.__btn_Quitter = Button(self.__frameChoix, text="Annuler", command = self.__RAZ__)
		self.__btn_Quitter.pack(side=LEFT)
		self.__btn_Config = Button(self.__frameChoix, text="Configuration camera", command = self.__InterfaceConfig__)
		self.__btn_Config.pack(side=LEFT)

		self.__p.add(self.__frameNbjour)
		self.__p.add(self.__frameEP)
		self.__p.add(self.__frameChoix)
		self.__p2.add(self.__frameResume)
		
		
	def __RAZ__(self):
		self.__sb_jour.delete(0, None)
		self.__sb_jour.insert(0, 0)
		self.__sb_freq.delete(0, None)
		self.__sb_freq.insert(0, 0)
		self.__sb_TempsPrise1.delete(0, None)
		self.__sb_TempsPrise1.insert(0, 0)

	def __Valider__(self):
		reponse = askyesno("Confirmation", "Voulez-vous lancer la séquence ?")
		self.__root.update()
		if reponse == True:
			self.__PrisePhotos__()
			
	def __PrisePhotos__(self):
		self.__root.update()
		SQ = Sequence(self.__sb_jour.get(), self.__sb_TempsPrise1.get(), self.__sb_freq.get(), self.__tb_Espece.get(), self.__tb_Programme.get())
		self.__root.update()
		SQ.__Debut__()
			
	def __InterfaceConfig__(self):
		__rootNew = Toplevel()
		self.__new = ConfigCamera(__rootNew )
		
from tkinter import *
import os

if(__name__ == '__main__'):
	interface = VueV2()
