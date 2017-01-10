from tkinter import *

class Vue(object):
	
	def __init__(self, **kwargs) :		
		#Creation Fenetre
		self.__fenetre = Tk()
		self.__fenetre['bg'] = 'white'
		self.__fenetre.title('Test')

		self.__v = IntVar()

		#Creation Panneau
		self.__p = PanedWindow(self.__fenetre, orient=VERTICAL)
		self.__p2 = PanedWindow(self.__fenetre, orient=VERTICAL)
		self.__p.pack(side=LEFT, expand=Y)
		self.__p2.pack(side=RIGHT, expand=Y, fill=BOTH)


		#frameNbJour

		self.__frameNbjour = Frame(self.__fenetre, borderwidth=2, relief=GROOVE)
		self.__frameNbjour.pack(side=TOP, padx=20, pady=20)

		self.__radBtn_jour = Radiobutton(self.__frameNbjour, text="Au nombre de jour", \
		variable=self.__v, value=1, command=self.__Choix__)
		
		self.__radBtn_jour.pack()

		self.__lb_JourSouhaite = Label(self.__frameNbjour, text="Nombre de jour souhaité")
		self.__lb_JourSouhaite.pack()
		self.__sb_jour = Spinbox(self.__frameNbjour, from_=0, to=10,width=2)
		self.__s_jour = self.__sb_jour.pack()

		self.__lb_freq = Label(self.__frameNbjour, text="Fréquence des prise de vue")
		self.__lb_freq.pack()
		self.__sb_freq = Spinbox(self.__frameNbjour, from_=0, to=10,width=2)
		self.__s_freq = self.__sb_freq.pack(side=LEFT)

		self.__lb_parH = Label(self.__frameNbjour, text="/h")
		self.__lb_parH.pack(side=LEFT)

		#Désactivation freq & jour
		self.__sb_jour.configure(state='disabled')
		self.__sb_freq.configure(state='disabled')

		#frameDateADate

		self.__frameDateADate = Frame(self.__fenetre, borderwidth=2, relief=GROOVE)
		self.__frameDateADate.pack(side=LEFT, padx=20, pady=20)

		self.__radBtn_Plage = Radiobutton(self.__frameDateADate, text="Sur une plage de jours", \
		variable=self.__v, value=2, command=self.__Choix__)
		
		self.__radBtn_Plage.pack()
		self.__lb_DateD = Label(self.__frameDateADate, text="Date de début")
		self.__lb_DateD.pack()
		self.__dateDebut = Entry(self.__frameDateADate, width=12)
		self.__dateDebut.pack()

		self.__lb_DateF = Label(self.__frameDateADate, text="Date de fin")
		self.__lb_DateF.pack()
		self.__dateFin = Entry(self.__frameDateADate, width=12)
		self.__dateFin.pack()
		self.__lb_freqD = Label(self.__frameDateADate, text="Fréquence des prise de vue")
		self.__lb_freqD.pack()

		#Désactivation des dates
		self.__dateDebut.configure(state='disabled')
		self.__dateFin.configure(state='disabled')

		#frameResume

		self.__frameResume = Frame(self.__fenetre, borderwidth=2, relief=GROOVE)
		self.__frameResume.pack(side=BOTTOM, padx=20, pady=20)
		self.__lb_TempsE = Label(self.__frameResume, text="Temps écoulé : ")
		self.__lb_TempsE.pack()
		self.__lb_NbPhoto = Label(self.__frameResume, text="Nombre de photo(s) : ")
		self.__lb_NbPhoto.pack()
		self.__lb_PhotoR = Label(self.__frameResume, text="Photo(s) réstante(s) : ")
		self.__lb_PhotoR.pack()
		self.__lb_TempsR = Label(self.__frameResume, text="Temps restants : ")
		self.__lb_TempsR.pack()

		#frameChoix

		self.__frameChoix = Frame(self.__fenetre, borderwidth=2, relief=GROOVE)
		self.__frameChoix.pack(side=LEFT, padx=20, pady=20)
		self.__btn_Valider = Button(self.__frameChoix, text="Valider")
		self.__btn_Valider.pack(side=LEFT)
		self.__btn_Quitter = Button(self.__frameChoix, text="Annuler", command = self.__RAZ__)
		self.__btn_Quitter.pack(side=RIGHT)

		self.__p.add(self.__frameNbjour)
		self.__p.add(self.__frameDateADate)
		self.__p.add(self.__frameChoix)
		self.__p2.add(self.__frameResume)
		
		self.__fenetre.mainloop()
		
		
	def __RAZ__(self):
		self.__sb_jour.delete(0, None)
		self.__sb_freq.delete(0, None)
		self.__dateDebut.delete(0, END)
		self.__dateFin.delete(0, END)
		
	def __Choix__(self):
		self.__va = self.__v.get()
		if self.__va == 1 :
			self.__dateDebut.delete(0, END)
			self.__dateFin.delete(0, END)
			self.__sb_jour.configure(state='normal')
			self.__sb_freq.configure(state='normal')
			self.__dateDebut.configure(state='disabled')
			self.__dateFin.configure(state='disabled')
		
		elif self.__va == 2 :
			self.__sb_jour.delete(0, None)
			self.__sb_freq.delete(0, None)
			self.__sb_jour.insert(0, 0)
			self.__sb_freq.insert(0, 0)
			self.__dateDebut.configure(state='normal')
			self.__dateFin.configure(state='normal')
			self.__sb_jour.configure(state='disabled')
			self.__sb_freq.configure(state='disabled')
	


	
