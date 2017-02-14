from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import *
import os
from Donnees_SQL import *


class ConfigCamera(object):
	
		
	def __init__(self, boss = None) :
		
		#Creation fenetre
		if boss :
			self.__root = boss
		else : 
			self.__root = Tk()
		
		self.__root.title('Configuration Caméra')
		self.CreateWidgets()
		self.__Recup__()
		self.__aff_LaListeDesModes()
		self.__root.mainloop()
		
	def CreateWidgets(self):
		#Création des champs, labels, ect
		
		self.vP = IntVar()
		self.Balance = IntVar()
		self.vMeta = IntVar()
		self.Commande = StringVar()
		self.Exp = StringVar()
		self.laSelection = StringVar()
		self.CurrentIndexListe = 0
		
		#Mode
		
		self.FrameMode = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameMode.pack()
		
		self.cb_Mode = Combobox(self.FrameMode, textvariable = self.laSelection)
		self.cb_Mode.bind('<<ComboboxSelected>>', self.loadConfiguration)
		self.cb_Mode.pack()

		
		#Config Preview

		self.FramePreview = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FramePreview.pack()
		self.lb_Preview = Label(self.FramePreview, text="Preview : ")
		self.lb_Preview.pack(side=LEFT)
		self.rb_Preview = Radiobutton(self.FramePreview, text="Oui", variable=self.vP, value=1)
		self.rb_Preview.pack(side=RIGHT)
		self.rb_Preview.select()
		self.rb_Preview2 = Radiobutton(self.FramePreview, text="Non", variable=self.vP, value=2)
		self.rb_Preview2.pack(side=RIGHT)
		
		#Config Netteté

		self.FrameNet = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameNet.pack()
		self.lb_Net = Label(self.FrameNet, text="Netteté (-100/100) : ", padx = 23)
		self.lb_Net.pack(side=LEFT)
		self.sb_Net = Spinbox(self.FrameNet, from_=-100, to=100,width=4)
		self.sb_Net.pack(side=RIGHT)
		
		#Config Contraste

		self.FrameCont = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameCont.pack()
		self.lb_Contraste = Label(self.FrameCont, text="Contraste (-100/100) : ", padx = 16)
		self.lb_Contraste.pack(side=LEFT)
		self.sb_Cont = Spinbox(self.FrameCont, from_=-100, to=100,width=4)
		self.sb_Cont.pack(side=RIGHT)
		
		#Config Luminosité

		self.FrameLumi = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameLumi.pack()
		self.lb_Lumi = Label(self.FrameLumi, text="Luminosité (0/100) : ", padx = 24)
		self.lb_Lumi.pack(side=LEFT)
		self.sb_Lumi = Spinbox(self.FrameLumi, from_=0, to=100,width=4)
		self.sb_Lumi.pack(side=RIGHT)
		
		#Config Saturation

		self.FrameSat = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameSat.pack()
		self.lb_Sat = Label(self.FrameSat, text="Saturation  : (-100/100)", padx = 15)
		self.lb_Sat.pack(side=LEFT)
		self.sb_Sat = Spinbox(self.FrameSat, from_=-100, to=100,width=4)
		self.sb_Sat.pack(side=RIGHT)
		
		#Config Sensibilité ISO

		self.FrameISO = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameISO.pack()
		self.lb_ISO = Label(self.FrameISO, text="Sensibilité ISO (100/800) : ", padx = 6)
		self.lb_ISO.pack(side=LEFT)
		self.sb_ISO = Spinbox(self.FrameISO, from_=0, to=800,width=4)
		self.sb_ISO.pack(side=RIGHT)
		
		#Compensation EV
		
		self.FrameEV = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameEV.pack()
		self.lb_EV = Label(self.FrameEV, text="Compensation EV (-10/10) : ")
		self.lb_EV.pack(side=LEFT)
		self.sb_EV = Spinbox(self.FrameEV, from_=-10, to=10,width=4)
		self.sb_EV.pack(side=RIGHT)
		
		#Exposition
		
		self.FrameExp = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameExp.pack()
		self.lb_Exp = Label(self.FrameExp, text=" Temps d'exposition:\n\nEn µs Max 6s (6 000 000µs), 0 = par défaut")
		self.lb_Exp.pack()
		self.sb_Exp = Spinbox(self.FrameExp, from_=0, to=6000000,width=8)
		self.sb_Exp.pack()
		
		#Config AWB

		self.FrameAWB = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameAWB.pack()
		self.lb_AWB = Label(self.FrameAWB, text="Balance des blancs : ")
		self.lb_AWB.pack(side=LEFT)
		self.rb_AWB = Radiobutton(self.FrameAWB, text="Oui", variable=self.Balance, value = 1,
		 command = self.__Choix__)
		self.rb_AWB.pack(side=LEFT)
		self.rb_AWB.select()
		self.rb_AWB2 = Radiobutton(self.FrameAWB, text="Non", variable=self.Balance, value = 2,
		 command = self.__Choix__)
		self.rb_AWB2.pack(side=RIGHT)
		
		#Config AWB gain

		self.FrameAWBReglage = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameAWBReglage.pack()
		self.lb_AWBReglage = Label(self.FrameAWBReglage, text="Réglage par cannal (Rouge,Bleu) : ")
		self.lb_AWBReglage.pack()
		self.lb_AWBR = Label(self.FrameAWBReglage, text="Rouge : ")
		self.lb_AWBR.pack(side = LEFT)
		self.AWBR = Entry(self.FrameAWBReglage, width=3)
		self.AWBR.pack(side = LEFT)
		self.AWBR.configure(state="disabled")
		self.AWBB = Entry(self.FrameAWBReglage, width=3)
		self.AWBB.pack(side = RIGHT)
		self.AWBB.configure(state="disabled")
		self.lb_AWBB = Label(self.FrameAWBReglage, text="Bleu : ")
		self.lb_AWBB.pack(side = RIGHT)
		
		#Config Taille

		self.FrameReso = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameReso.pack()
		self.lb_Taille = Label(self.FrameReso, text="Résolution : ")
		self.lb_Taille.pack(side=LEFT)
		self.listeReso = Listbox(self.FrameReso)
		self.listeReso.insert(END, "Défaut : (2592x1944 (4:3) 1-15 IPS)")
		self.listeReso.insert(END, "1920x1080 (16:9) 1-30 IPS")
		self.listeReso.insert(END, "2592x1944 (4:3) 1-15 IPS)")
		self.listeReso.insert(END, "2592x1944 (4:3) 0.1666-1 IPS")
		self.listeReso.insert(END, "1296x972 (4:3) 1-42 IPS")
		self.listeReso.insert(END, "1296x730 (16:9) 1-49 IPS")
		self.listeReso.insert(END, "640x480 (4:3) 42.1-60 IPS")
		self.listeReso.insert(END, "640x480 (4:3) 60.1-90 IPS")
		self.listeReso.config(height=8, width = 28)
		self.listeReso.pack()
		
		#Config Qualité

		self.FrameQual = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameQual.pack()
		self.lb_Qual = Label(self.FrameQual, text="Qualité (1/100) : ")
		self.lb_Qual.pack(side=LEFT)
		self.sb_Qual = Spinbox(self.FrameQual, from_=1, to=100,width=4)
		self.sb_Qual.pack(side=RIGHT)
		
		#Config Métadonnées

		self.FrameMeta = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameMeta.pack()
		self.lb_Meta = Label(self.FrameMeta, text="Métadonnées : ")
		self.lb_Meta.pack(side=LEFT)
		self.rb_Meta = Radiobutton(self.FrameMeta, text="Oui", variable=self.vMeta, value=1)
		self.rb_Meta.pack(side=LEFT)
		self.rb_Meta2 = Radiobutton(self.FrameMeta, text="Non", variable=self.vMeta, value=2)
		self.rb_Meta2.pack(side=RIGHT)
		self.rb_Meta2.select()

		#Valider/Annuler/RAZ

		self.FrameChoix = Frame(self.__root, relief=GROOVE, pady = 10)
		self.FrameChoix.pack()
		self.btn_Valider = Button(self.FrameChoix, text="Valider", command = self.__Commande__)
		self.btn_Valider.pack(side=LEFT)
		self.btn_RAZ = Button(self.FrameChoix, text="Par défaut", command = self.__RAZ__)
		self.btn_RAZ.pack(side=RIGHT)
		self.btn_Annuler = Button(self.FrameChoix, text="Annuler", command = self.__FermerFenetre__)
		self.btn_Annuler.pack(side=LEFT)
		self.btn_Save = Button(self.FrameChoix, text="Sauvegarder", command = self.__Sauvegarde__)
		self.btn_Save.pack(side=RIGHT)
		
	def __FermerFenetre__(self):
		#Ferme la fenetre
		self.__root.destroy()

	def loadConfiguration(self, event):
		ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
		donnees = Donnees_SQL(ConnexionString)
		donnees.SQL_loadLeMode(self.cb_Mode.get())
		result = donnees.chargerLesDonnees_RequeteSQL()
		result = str(result).replace("bytearray", "")
		result = result.replace("(", "")
		result = result.replace(")", "")
		result = result.replace("b'", "")
		result = result.replace("'", "")
		result = result.replace("[", "")
		result = result.replace("]", "")
		result = result.replace(" ", "")
		print(result)
		listResult = result.split(",")
		print(listResult)
		self.ModifLoad(listResult)
		
	def ModifLoad(self, uneListe):
		self.vP.set(uneListe[2])
		self.sb_Net.delete(0, 100)
		self.sb_Net.insert(0, uneListe[3])
		self.sb_Cont.delete(0, 100)
		self.sb_Cont.insert(0, uneListe[4])
		self.sb_Lumi.delete(0, 100)
		self.sb_Lumi.insert(0, uneListe[5])
		self.sb_Sat.delete(0, 100)
		self.sb_Sat.insert(0, uneListe[6])
		self.sb_ISO.delete(0, 100)
		self.sb_ISO.insert(0, uneListe[7])
		self.sb_EV.delete(0, 100)
		self.sb_EV.insert(0, uneListe[8])
		self.sb_Exp.delete(0, 100)
		self.sb_Exp.insert(0, uneListe[9])
		self.Balance.set(uneListe[10]) 
		if self.Balance.get() == 1 :
			self.AWBR.delete(0, 100)
			self.AWBB.delete(0, 100)
			self.AWBR.configure(state="disabled")
			self.AWBB.configure(state="disabled")
		elif self.Balance.get() == 2 :
			self.AWBR.configure(state="normal")
			self.AWBB.configure(state="normal")
		self.AWBR.delete(0, 100)
		self.AWBR.insert(0, uneListe[11])
		self.AWBB.delete(0, 100)
		self.AWBB.insert(0, uneListe[12])
		self.listeReso.selection_set(uneListe[13], None)
		self.listeReso.activate(uneListe[13])
		self.sb_Qual.delete(0, 100)
		self.sb_Qual.insert(0, uneListe[14])
		self.vMeta.set(uneListe[15]) 
		
	def __aff_LaListeDesModes(self):
		ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
		donnees = Donnees_SQL(ConnexionString)
		""" affiche la liste des joueurs existants de la base de données dans le Combobox..."""
		LaListeDesModes = []
		# -- on renseigne le code de la requête SQL
		donnees.SQL_loadListedesModes()
		# -- on rempli la liste des joueurs...
		LaListeDesModes = donnees.chargerLesDonnees_RequeteSQL()
		# -- si la liste existe...
		laListe  = [""]
		# -- on met en forme la liste à afficher dans la Combobox
		for row in LaListeDesModes:
			a = str(row).replace("bytearray", "")
			a = a.replace("(", "")
			a = a.replace(")", "")
			a = a.replace("b'", "")
			a = a.replace("'", "")
			a = a.replace(",", "")
			laListe.append(a)
		# -- on sélectionne la première occurence de la liste.
		self.laSelection.set(laListe[self.CurrentIndexListe])
		# -- on renseigne la combobox avec la liste mis en forme
		self.cb_Mode.config( values = laListe , state = NORMAL )
		#aff_individu()
	
	
	def __Choix__(self):
		#Agit sur les champ en fonction du radiobutton
		if self.Balance.get() == 1 :
			self.AWBR.delete(0,END)
			self.AWBR.configure(state="disabled")
			self.AWBB.delete(0,END)
			self.AWBB.configure(state="disabled")
		elif self.Balance.get() == 2 :
			self.AWBR.configure(state="normal")
			self.AWBR.insert(END,1.5)
			self.AWBB.configure(state="normal")
			self.AWBB.insert(END,1.2)
			
	def __Commande__(self):
		
		self.__CreationCommande__()
		self.__CreationEtat__()
		self.__root.destroy()

		
	def __CreationCommande__(self):
		
		#Enregistre la commande utilisé lors des prises de vues
		
		if self.vP.get() == 2:
			Commande = "-n "
		else:
			Commande = ""
		
		Commande = Commande + "-sh " + self.sb_Net.get() + " -co " + self.sb_Cont.get() \
		+ " -br " + self.sb_Lumi.get() + " -sa " + self.sb_Sat.get() + " -ISO " + self.sb_ISO.get()\
		 + " -ev " + self.sb_EV.get() + " -ss " + self.sb_Exp.get()
		   
		if self.Balance.get() == 2 :
			Commande = Commande + " -awb off -awbg " + self.AWBR.get() + "," + self.AWBB.get()   
		   
		Commande = Commande +   " -md " + str(self.listeReso.index(ACTIVE)) + " -q " + self.sb_Qual.get() 
		
		if self.vMeta.get() == 1:
			Commande = Commande + " -r"
		
		print(Commande)
		Conf = open("conf.txt", "w")
		Conf.write(Commande)
		Conf.close()
		
	def __CreationEtat__(self):
		#Sauvegarde l'état pour le conserver lors de l'ouverture de cette fenetre
		if self.vP.get() == 2:
			Etat = "2;"
			
		else:
			Etat = "1;"
		
		Etat = Etat + self.sb_Net.get() + ";" + self.sb_Cont.get() +\
		 ";" + self.sb_Lumi.get() + ";" + self.sb_Sat.get() + ";" + self.sb_ISO.get()\
		   + ";" + self.sb_EV.get() + ";" + self.sb_Exp.get() + ";"
		   
		if self.Balance.get() == 2 :
			Etat = Etat + "2;" + self.AWBR.get() + ";" + self.AWBB.get() +";"
			
			
		else:
			Etat = Etat + "1;;;"
		   
		   
		Etat = Etat + str(self.listeReso.index(ACTIVE)) + ";" + self.sb_Qual.get()
			
		if self.vMeta.get() == 1:
			Etat = Etat + ";1"
		
		else:
			Etat = Etat + ";2"
		
		print(Etat)
		Statut = open("Etat.txt", "w")
		Statut.write(Etat)
		Statut.close()
	
	def __Sauvegarde__(self):
		
		Config = [self.cb_Mode.get(), self.vP.get(), self.sb_Net.get(), self.sb_Cont.get(), self.sb_Lumi.get(), self.sb_Sat.get(), self.sb_ISO.get(), self.sb_EV.get(), self.sb_Exp.get(), self.Balance.get(), self.AWBR.get(), self.AWBB.get(), str(self.listeReso.index(ACTIVE)), self.sb_Qual.get(), self.vMeta.get()]
		ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
		donnees = Donnees_SQL(ConnexionString)
		donnees.SQL_insertUneCommande(Config)
		result = donnees.executerlaRequeteSQL()
		showinfo("Information","Configuration sauvegardée")
		self.__aff_LaListeDesModes()
		
	def __Recup__(self):
		#Recupere les valeurs des champs
		
		Liste = []
		Fichier_Etat = open("Etat.txt", "r")
		AncienEtat = Fichier_Etat.read()
		for x in AncienEtat.split(";"):
			Liste.append(x)
			
		self.vP.set(Liste[0]) 
		self.sb_Net.delete(0, 100)
		self.sb_Net.insert(0, Liste[1])
		self.sb_Cont.delete(0, 100)
		self.sb_Cont.insert(0, Liste[2])
		self.sb_Lumi.delete(0, 100)
		self.sb_Lumi.insert(0, Liste[3])
		self.sb_Sat.delete(0, 100)
		self.sb_Sat.insert(0, Liste[4])
		self.sb_ISO.delete(0, 100)
		self.sb_ISO.insert(0, Liste[5])
		self.sb_EV.delete(0, 100)
		self.sb_EV.insert(0, Liste[6])
		self.sb_Exp.delete(0, 100)
		self.sb_Exp.insert(0, Liste[7])
		self.Balance.set(Liste[8]) 
		if self.Balance.get() == 1 :
			self.AWBR.configure(state="disabled")
			self.AWBB.configure(state="disabled")
		elif self.Balance.get() == 2 :
			self.AWBR.configure(state="normal")
			self.AWBB.configure(state="normal")
		self.AWBR.delete(0, 100)
		self.AWBR.insert(0, Liste[9])
		self.AWBB.delete(0, 100)
		self.AWBB.insert(0, Liste[10])
		self.listeReso.selection_set(Liste[11], None)
		self.listeReso.activate(Liste[11])
		self.sb_Qual.delete(0, 100)
		self.sb_Qual.insert(0, Liste[12])
		self.vMeta.set(Liste[13]) 
		
		
	def __RAZ__(self):
		#Vide les champs
		self.vP.set(1) 
		self.sb_Net.delete(0, 10)
		self.sb_Net.insert(0, 0)
		self.sb_Cont.delete(0, 10)
		self.sb_Cont.insert(0, 0)
		self.sb_Lumi.delete(0, 10)
		self.sb_Lumi.insert(0, 50)
		self.sb_Sat.delete(0, 10)
		self.sb_Sat.insert(0, 0)
		self.sb_ISO.delete(0, 10)
		self.sb_ISO.insert(0, 0)
		self.sb_EV.delete(0, 10)
		self.sb_EV.insert(0, 0)
		self.sb_Exp.delete(0, 10)
		self.sb_Exp.insert(0, 0)
		self.Balance.set(1)
		self.AWBR.delete(0,END)
		self.AWBR.configure(state="disabled")
		self.AWBB.delete(0,END)
		self.AWBB.configure(state="disabled")
		self.listeReso.selection_clear(0,10)
		self.listeReso.selection_set(0, None)
		self.listeReso.activate(0)
		self.sb_Qual.delete(0, 4)
		self.sb_Qual.insert(0, 100)
		self.vMeta.set(2) 

	

if __name__ == '__main__':
	x = ConfigCamera()
