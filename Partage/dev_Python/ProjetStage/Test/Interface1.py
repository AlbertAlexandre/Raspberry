from tkinter import *
import time 

def RAZ():
	sb_jour.delete(0, None)
	sb_freq.delete(0, None)
	dateDebut.delete(0, END)
	dateFin.delete(0, END)
	
def Choix():
	va = v.get()
	if va == 1 :
		dateDebut.delete(0, END)
		dateFin.delete(0, END)
		sb_jour.configure(state='normal')
		sb_freq.configure(state='normal')
		dateDebut.configure(state='disabled')
		dateFin.configure(state='disabled')
	
	elif va == 2 :
		sb_jour.delete(0, None)
		sb_freq.delete(0, None)
		dateDebut.configure(state='normal')
		dateFin.configure(state='normal')
		sb_jour.configure(state='disabled')
		sb_freq.configure(state='disabled')
		
#Creation Fenetre
fenetre = Tk()
fenetre['bg'] = 'white'
fenetre.title('Test')

v = IntVar()

#Creation Panneau
p = PanedWindow(fenetre, orient=VERTICAL)
p2 = PanedWindow(fenetre, orient=VERTICAL)
p.pack(side=LEFT, expand=Y)
p2.pack(side=RIGHT, expand=Y, fill=BOTH)


#frameNbJour

frameNbjour = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameNbjour.pack(side=TOP, padx=20, pady=20)

radBtn_jour = Radiobutton(frameNbjour, text="Au nombre de jour", variable=v, value=1, command=Choix)
radBtn_jour.pack()

Label(frameNbjour, text="Nombre de jour souhaité").pack()
sb_jour = Spinbox(frameNbjour, from_=0, to=10,width=2)
s_jour = sb_jour.pack()

Label(frameNbjour, text="Fréquence des prise de vue").pack()
sb_freq = Spinbox(frameNbjour, from_=0, to=10,width=2)
s_freq = sb_freq.pack(side=LEFT)

Label(frameNbjour, text="/h").pack(side=LEFT)

#Désactivation freq & jour
sb_jour.configure(state='disabled')
sb_freq.configure(state='disabled')

#frameDateADate

frameDateADate = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameDateADate.pack(side=LEFT, padx=20, pady=20)

radBtn_Plage = Radiobutton(frameDateADate, text="Sur une plage de jours", variable=v, value=2)
radBtn_Plage.pack()
Label(frameDateADate, text="Date de début").pack()
dateDebut = Entry(frameDateADate, width=12)
dateDebut.pack()

Label(frameDateADate, text="Date de fin").pack()
dateFin = Entry(frameDateADate, width=12)
dateFin.pack()
Label(frameDateADate, text="Fréquence des prise de vue").pack()

#Désactivation des dates
dateDebut.configure(state='disabled')
dateFin.configure(state='disabled')

#frameResume

frameResume = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameResume.pack(side=BOTTOM, padx=20, pady=20)
Label(frameResume, text="Temps écoulé : ").pack()
Label(frameResume, text="Nombre de photo(s) : ").pack()
Label(frameResume, text="Photo(s) réstante(s) : ").pack()
Label(frameResume, text="Temps restants : ").pack()

#frameChoix

frameChoix = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameChoix.pack(side=LEFT, padx=20, pady=20)
btn_Valider = Button(frameChoix, text="Valider")
btn_Valider.pack(side=LEFT)
btn_Quitter = Button(frameChoix, text="Annuler", command = RAZ)
btn_Quitter.pack(side=RIGHT)

p.add(frameNbjour)
p.add(frameDateADate)
p.add(frameChoix)
p2.add(frameResume)

fenetre.mainloop()
