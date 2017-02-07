from tkinter import *
from tkinter.messagebox import *
import datetime
import time
from Sequence import *
from Photo import *
from ConfigCamera import *
from tkinter.filedialog import *
import os

class VueV2(object):
	
	def __init__(self) :
		
				
		#Creation Fenetre
		
		self.__root = Tk()
		self.__root['bg'] = 'white'
		self.__root.title('Configuration Séquence')
		self.CreateWidgets()
		self.__root.mainloop()
		
	def CreateWidgets(self):
		#Place les textbox, les labels, ect
		
		#Creation Panneau
		
		self.__p = PanedWindow(self.__root, orient=VERTICAL)
		self.__p2 = PanedWindow(self.__root, orient=HORIZONTAL)
		self.__p.pack(side=LEFT, expand=Y, fill=BOTH)
		self.__p2.pack(side=RIGHT, expand=Y, fill=BOTH)


		#frameNbJour

		self.__frameNbjour = Frame(self.__root)
		self.__frameNbjour.pack(side=TOP)

		self.__lb_JourSouhaite = Label(self.__frameNbjour, text="Nombre de jours souhaités")
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
		
		#frameDateDebut
		
		self.__frameDebut = Frame(self.__root)
		self.__frameDebut.pack(side=TOP)

		self.__lb_Debut = Label(self.__frameDebut, text="Heure début nuit (HH)")
		self.__lb_Debut.pack()
		self.__sb_Debut = Entry(self.__frameDebut, width=3)
		self.__sb_Debut.pack()
		
		#frameDateDebut
		
		self.__frameFin = Frame(self.__root)
		self.__frameFin.pack(side=TOP)

		self.__lb_Fin = Label(self.__frameFin, text="Heure fin nuit (HH)")
		self.__lb_Fin.pack()
		self.__sb_Fin = Entry(self.__frameFin, width=3)
		self.__sb_Fin.pack()

		
		#frameResume
		
		#Partie abandonné résumant l'avancé de la séquence

		"""self.__frameResume = Frame(self.__root, borderwidth=2, relief=GROOVE)
		self.__frameResume.pack(side=BOTTOM, padx=20, pady=20)
		self.__lb_TempsE = Label(self.__frameResume, text="Temps écoulé : ")
		self.__lb_TempsE.pack()
		self.__lb_NbPhoto = Label(self.__frameResume, text="Nombre de photo(s) : ")
		self.__lb_NbPhoto.pack()
		self.__lb_PhotoR = Label(self.__frameResume, text="Photo(s) réstante(s) : ")
		self.__lb_PhotoR.pack()
		self.__lb_TempsR = Label(self.__frameResume, text="Temps restants : ")
		self.__lb_TempsR.pack()"""
		
		#Frame Info
		
		self.__frameEP = Frame(self.__root)
		self.__frameEP.pack(side=LEFT, fill=BOTH)

		self.__lb_Espece = Label(self.__frameEP, text="Espèce : ")
		self.__lb_Espece.pack()
		self.__tb_Espece = Entry(self.__frameEP)
		self.__tb_Espece.pack()
		
		self.__lb_Programme = Label(self.__frameEP, text="Programme : ")
		self.__lb_Programme.pack()
		self.__tb_Programme  = Entry(self.__frameEP)
		self.__tb_Programme.pack()
		
		self.__lb_Tempe = Label(self.__frameEP, text="Temperature : ")
		self.__lb_Tempe.pack()
		self.__tb_Tempe  = Entry(self.__frameEP)
		self.__tb_Tempe.pack()
		
		self.__lb_Meth = Label(self.__frameEP, text="Methode : ")
		self.__lb_Meth.pack()
		self.__tb_Meth  = Entry(self.__frameEP)
		self.__tb_Meth.pack()
		
		self.__lb_ID = Label(self.__frameEP, text="ID échantillon : ")
		self.__lb_ID.pack()
		self.__tb_ID  = Entry(self.__frameEP)
		self.__tb_ID.pack()
		
		
		
		self.__frameSUITE = Frame(self.__root)
		self.__frameSUITE.pack(side=RIGHT, fill=BOTH)
		
		self.__lb_Rep = Label(self.__frameSUITE, text="Répétition / sous-répétition : ")
		self.__lb_Rep.pack()
		self.__tb_Rep = Entry(self.__frameSUITE)
		self.__tb_Rep.pack()
		
		self.__lb_Mod = Label(self.__frameSUITE, text="Modalité : ")
		self.__lb_Mod.pack()
		self.__tb_Mod  = Entry(self.__frameSUITE)
		self.__tb_Mod.pack()
		
		self.__lb_Num = Label(self.__frameSUITE, text="Numéro de module : ")
		self.__lb_Num.pack()
		self.__tb_Num  = Entry(self.__frameSUITE)
		self.__tb_Num.pack()
		
		self.__lb_Empl = Label(self.__frameSUITE, text="Emplacement dans le module : ")
		self.__lb_Empl.pack()
		self.__tb_Empl  = Entry(self.__frameSUITE)
		self.__tb_Empl.pack()
		
		self.__lb_Autre = Label(self.__frameSUITE, text="Autre : ")
		self.__lb_Autre.pack()
		self.__tb_Autre  = Entry(self.__frameSUITE)
		self.__tb_Autre.pack()
		
		self.__btn_Config = Button(self.__frameSUITE, text="Configuration caméra", command = self.__InterfaceConfig__)
		self.__btn_Config.pack()

		
		self.__btn_Parcourir= Button(self.__frameEP, text="Parcourir...", command = self.__Chemin__)
		self.__btn_Parcourir.pack()

		
		#frameChoix

		self.__frameChoix = Frame(self.__root, borderwidth=10)
		self.__frameChoix.pack(side=LEFT)
		self.__btn_Valider = Button(self.__frameChoix, text="Valider", command = self.__Valider__)
		self.__btn_Valider.pack(side=LEFT)
		self.__btn_Quitter = Button(self.__frameChoix, text="Effacer", command = self.__RAZ__)
		self.__btn_Quitter.pack(side=LEFT)


		self.__p.add(self.__frameNbjour)
		self.__p.add(self.__frameDebut)
		self.__p.add(self.__frameFin)
		self.__p2.add(self.__frameEP)
		self.__p2.add(self.__frameSUITE)
		self.__p.add(self.__frameChoix)
		#self.__p2.add(self.__frameResume)
		
	def __Chemin__(self):
		
		#Recupere s'il existe le dernier chemin enregistré
		
		FichierChemin = open("Chemin.txt", "r")
		AncienChemin = FichierChemin.read()
		dossier = askdirectory(initialdir = AncienChemin)
		try:
			if len(dossier) != 0:
				chemin = open("Chemin.txt", "w")
				chemin.write(dossier)
				chemin.close()
		except:
			pass #0.000694444
		
	def __RAZ__(self):
		#vide les champs
		
		self.__sb_jour.delete(0, 100)
		self.__sb_jour.insert(0, 0)
		self.__sb_freq.delete(0, 100)
		self.__sb_freq.insert(0, 0)
		self.__sb_TempsPrise1.delete(0, 100)
		self.__sb_TempsPrise1.insert(0, 0)
		self.__tb_Espece.delete(0, 100)
		self.__tb_Programme.delete(0, 100)
		self.__tb_Tempe.delete(0, 100)
		self.__tb_ID.delete(0, 100)
		self.__tb_Rep.delete(0, 100)
		self.__tb_Mod.delete(0, 100)
		self.__tb_Num.delete(0, 100)
		self.__tb_Empl.delete(0, 100)
		self.__tb_Autre.delete(0, 100)
		self.__tb_Meth.delete(0, 100)

	def __Valider__(self):
		#Ouvre une fenetre pour demander l'avis de l'utilisateur et lance la séquence si la répond est "oui"
		
		reponse = askyesno("Confirmation", "Voulez-vous lancer la séquence ?")
		self.__root.update()
		if reponse == True:
			self.__root.update()
			SQ = Sequence(self.__sb_jour.get(), self.__sb_TempsPrise1.get(), self.__sb_freq.get(), self.__tb_Espece.get(), self.__tb_Programme.get(), self.__tb_Tempe.get(), self.__tb_Meth.get(), self.__tb_ID.get(), self.__tb_Rep.get(), self.__tb_Mod.get(), self.__tb_Num.get(), self.__tb_Empl.get(), self.__tb_Autre.get(), self.__sb_Debut.get(), self.__sb_Fin.get())
			self.__root.update()
			SQ.__Debut__()
			
	"""def __PrisePhotos__(self):
		self.__root.update()
		SQ = Sequence(self.__sb_jour.get(), self.__sb_TempsPrise1.get(), self.__sb_freq.get(), self.__tb_Espece.get(), self.__tb_Programme.get(), self.__tb_Tempe.get(), self.__tb_Meth.get(), self.__tb_ID.get(), self.__tb_Rep.get(), self.__tb_Mod.get(), self.__tb_Num.get(), self.__tb_Empl.get(), self.__tb_Autre.get())
		self.__root.update()
		SQ.__Debut__()"""
			
	def __InterfaceConfig__(self):
		#Ouvre l'interface caméra
		__rootNew = Toplevel()
		self.__new = ConfigCamera(__rootNew )
		


if(__name__ == '__main__'):
	interface = VueV2()
