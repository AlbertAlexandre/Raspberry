from tkinter import *
import os

class ConfigCamera(object):
	
		
	def __init__(self, boss = None) :
		
		#Creation fenetre
		if boss :
			self.__root = boss
		else : 
			self.__root = Tk()
		
		self.__root.title('Configuration Caméra')
		self.vP = StringVar()
		self.Balance = StringVar()
		self.vMeta = StringVar()
		self.Commande = StringVar()
		self.Exp = StringVar()
		
		#Config Preview

		self.FramePreview = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FramePreview.pack()
		self.lb_Preview = Label(self.FramePreview, text="Preview")
		self.lb_Preview.pack(side=LEFT)
		self.rb_Preview = Radiobutton(self.FramePreview, text="Oui", variable=self.vP, value=" ")
		self.rb_Preview.pack(side=LEFT)
		self.rb_Preview.select()
		self.rb_Preview2 = Radiobutton(self.FramePreview, text="Non", variable=self.vP, value=" -n ")
		self.rb_Preview2.pack()
		
		#Config Netteté

		self.FrameNet = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameNet.pack()
		self.lb_Net = Label(self.FrameNet, text="Netteté (-100/100) : ")
		self.lb_Net.pack(side=LEFT)
		self.sb_Net = Spinbox(self.FrameNet, from_=-100, to=100,width=4)
		self.sb_Net.pack(side=RIGHT)
		
		#Config Contraste

		self.FrameCont = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameCont.pack()
		self.lb_Contraste = Label(self.FrameCont, text="Contraste (-100/100) : ")
		self.lb_Contraste.pack(side=LEFT)
		self.sb_Cont = Spinbox(self.FrameCont, from_=-100, to=100,width=4)
		self.sb_Cont.pack(side=RIGHT)
		
		#Config Luminosité

		self.FrameLumi = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameLumi.pack()
		self.lb_Lumi = Label(self.FrameLumi, text="Luminosité (0/100) : ")
		self.lb_Lumi.pack(side=LEFT)
		self.sb_Lumi = Spinbox(self.FrameLumi, from_=0, to=100,width=4)
		self.sb_Lumi.insert(INSERT,5)
		self.sb_Lumi.pack(side=RIGHT)
		
		#Config Saturation

		self.FrameSat = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameSat.pack()
		self.lb_Sat = Label(self.FrameSat, text="Saturation  : (-100/100)")
		self.lb_Sat.pack(side=LEFT)
		self.sb_Sat = Spinbox(self.FrameSat, from_=-100, to=100,width=4)
		self.sb_Sat.pack(side=RIGHT)
		
		#Config Sensibilité ISO

		self.FrameISO = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameISO.pack()
		self.lb_ISO = Label(self.FrameISO, text="Sensibilité ISO (100/800) : ")
		self.lb_ISO.pack(side=LEFT)
		self.sb_ISO = Spinbox(self.FrameISO, from_=100, to=800,width=4)
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
		self.rb_AWB = Radiobutton(self.FrameAWB, text="Oui", variable=self.Balance, value = " -awb auto ",
		 command = self.__Choix__)
		self.rb_AWB.pack(side=LEFT)
		self.rb_AWB.select()
		self.rb_AWB2 = Radiobutton(self.FrameAWB, text="Non", variable=self.Balance, value = " -awb off ",
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
		self.listeReso.selection_set(0,None)
		self.listeReso.pack()
		
		#Config Qualité

		self.FrameQual = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameQual.pack()
		self.lb_Qual = Label(self.FrameQual, text="Qualité (1/100) : ")
		self.lb_Qual.pack(side=LEFT)
		self.sb_Qual = Spinbox(self.FrameQual, from_=1, to=100,width=4, value = 100)
		self.sb_Qual.pack(side=RIGHT)
		
		#Config Métadonnées

		self.FrameMeta = Frame(self.__root, relief=GROOVE, pady = 3)
		self.FrameMeta.pack()
		self.lb_Meta = Label(self.FrameMeta, text="Métadonnées : ")
		self.lb_Meta.pack(side=LEFT)
		self.rb_Meta = Radiobutton(self.FrameMeta, text="Oui", variable=self.vMeta, value=" -r ")
		self.rb_Meta.pack(side=LEFT)
		self.rb_Meta2 = Radiobutton(self.FrameMeta, text="Non", variable=self.vMeta, value=" ")
		self.rb_Meta2.pack(side=RIGHT)
		self.rb_Meta2.select()

		#Valider/Annuler

		self.FrameChoix = Frame(self.__root, relief=GROOVE, pady = 10)
		self.FrameChoix.pack()
		self.btn_Valider = Button(self.FrameChoix, text="Valider", command = self.__Commande__)
		self.btn_Valider.pack(side=LEFT)
		self.btn_Annuler = Button(self.FrameChoix, text="Annuler", command = self.__FermerFenetre__)
		self.btn_Annuler.pack(side=RIGHT)

		self.__root.mainloop()
		
	def __Choix__(self):
		if self.Balance.get() == " -awb auto " :
			self.AWBR.delete(0,END)
			self.AWBR.configure(state="disabled")
			self.AWBB.delete(0,END)
			self.AWBB.configure(state="disabled")
		elif self.Balance.get() == " -awb off " :
			self.AWBR.configure(state="normal")
			self.AWBR.insert(END,1.5)
			self.AWBB.configure(state="normal")
			self.AWBB.insert(END,1.2)
			
	def __Commande__(self):
		Commande = self.vP.get() + "-sh " + self.sb_Net.get() + " -co " + self.sb_Cont.get() +\
		 " -br " + self.sb_Lumi.get() + " -sa " + self.sb_Sat.get() + " -ISO " + self.sb_ISO.get()\
		  + self.Balance.get() + "-md " + str(self.listeReso.index(ACTIVE)) + " -q " + self.sb_Qual.get()\
		   + self.vMeta.get() + self.Exp.get() + "-ev " + self.sb_EV.get() + " -ss " + self.sb_Exp.get()
		if self.Balance.get() == " -awb off " :
			Commande = Commande + " -awbg " + self.AWBR.get() + "," + self.AWBB.get()
		print(Commande)
		Conf = open("conf.txt", "w")
		Conf.write(Commande)
		Conf.close()
		chaine = open("conf.txt", "r")

	def __FermerFenetre__(self):
		self.__root.destroy()

if __name__ == '__main__':
	x = ConfigCamera()
