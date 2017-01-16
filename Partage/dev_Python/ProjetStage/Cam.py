from tkinter import *
import picamera

class Cam(object):
	
		
	def __init__(self, **kwargs) :
		
		#Creation fenetre
		
		self.fenetre = Tk()
		self.fenetre.title('Configuration caméra')
		self.vP = StringVar()
		self.Balance = StringVar()
		self.vMeta = StringVar()
		self.Commande = StringVar()
		
		"""#Config Preview

		self.FramePreview = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FramePreview.pack()
		self.lb_Preview = Label(self.FramePreview, text="Preview")
		self.lb_Preview.pack(side=LEFT)
		self.rb_Preview = Radiobutton(self.FramePreview, text="Oui", variable=self.vP, value="true")
		self.rb_Preview.pack(side=LEFT)
		self.rb_Preview.select()
		self.rb_Preview2 = Radiobutton(self.FramePreview, text="Non", variable=self.vP, value="false")
		self.rb_Preview2.pack()"""
		
		#Config Netteté

		self.FrameNet = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameNet.pack()
		self.lb_Net = Label(self.FrameNet, text="Netteté (-100/100) : ")
		self.lb_Net.pack(side=LEFT)
		self.sb_Net = Spinbox(self.FrameNet, from_=-100, to=100,width=4)
		self.sb_Net.pack(side=RIGHT)
		
		#Config Contraste

		self.FrameCont = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameCont.pack()
		self.lb_Contraste = Label(self.FrameCont, text="Contraste (-100/100) : ")
		self.lb_Contraste.pack(side=LEFT)
		self.sb_Cont = Spinbox(self.FrameCont, from_=-100, to=100,width=4)
		self.sb_Cont.pack(side=RIGHT)
		
		#Config Luminosité

		self.FrameLumi = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameLumi.pack()
		self.lb_Lumi = Label(self.FrameLumi, text="Luminosité (0/100) : ")
		self.lb_Lumi.pack(side=LEFT)
		self.sb_Lumi = Spinbox(self.FrameLumi, from_=0, to=100,width=4, value = 50)
		self.sb_Lumi.pack(side=RIGHT)
		
		#Config Saturation

		self.FrameSat = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameSat.pack()
		self.lb_Sat = Label(self.FrameSat, text="Saturation  : (-100/100)")
		self.lb_Sat.pack(side=LEFT)
		self.sb_Sat = Spinbox(self.FrameSat, from_=-100, to=100,width=4)
		self.sb_Sat.pack(side=RIGHT)
		
		#Config Sensibilité ISO

		self.FrameISO = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameISO.pack()
		self.lb_ISO = Label(self.FrameISO, text="Sensibilité ISO (0/800) : ")
		self.lb_ISO.pack(side=LEFT)
		self.sb_ISO = Spinbox(self.FrameISO, from_=0, to=800,width=4)
		self.sb_ISO.pack(side=RIGHT)
		
		#Config AWB

		self.FrameAWB = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameAWB.pack()
		self.lb_AWB = Label(self.FrameAWB, text="Balance des blancs : ")
		self.lb_AWB.pack(side=LEFT)
		self.rb_AWB = Radiobutton(self.FrameAWB, text="Oui", variable=self.Balance, value = "auto", command = self.__Choix__)
		self.rb_AWB.pack(side=LEFT)
		self.rb_AWB.select()
		self.rb_AWB2 = Radiobutton(self.FrameAWB, text="Non", variable=self.Balance, value = "off", command = self.__Choix__)
		self.rb_AWB2.pack(side=RIGHT)
		
		#Config AWB gain

		self.FrameAWBReglage = Frame(self.fenetre, relief=GROOVE, pady = 3)
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

		self.FrameReso = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameReso.pack()
		self.lb_Taille = Label(self.FrameReso, text="Résolution : ")
		self.lb_Taille.pack(side=LEFT)
		self.Reso1 = Entry(self.FrameReso, width=5)
		self.Reso1.insert(0, 2592)
		self.Reso1.pack(side = LEFT)
		self.Reso2 = Entry(self.FrameReso, width=5)
		self.Reso2.insert(0, 1944)
		self.Reso2.pack(side = RIGHT)
		self.lb_X = Label(self.FrameReso, text="X")
		self.lb_X.pack(side = RIGHT)
		
		#Config Qualité

		self.FrameQual = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameQual.pack()
		self.lb_Qual = Label(self.FrameQual, text="Qualité (1/100) : ")
		self.lb_Qual.pack(side=LEFT)
		self.sb_Qual = Spinbox(self.FrameQual, from_=1, to=100,width=4, value = 100)
		self.sb_Qual.pack(side=RIGHT)
		
		"""#Config Métadonnées

		self.FrameMeta = Frame(self.fenetre, relief=GROOVE, pady = 3)
		self.FrameMeta.pack()
		self.lb_Meta = Label(self.FrameMeta, text="Métadonnées : ")
		self.lb_Meta.pack(side=LEFT)
		self.rb_Meta = Radiobutton(self.FrameMeta, text="Oui", variable=self.vMeta, value="-r")
		self.rb_Meta.pack(side=LEFT)
		self.rb_Meta2 = Radiobutton(self.FrameMeta, text="Non", variable=self.vMeta, value=" ")
		self.rb_Meta2.pack(side=RIGHT)
		self.rb_Meta2.select()"""

		#Valider/Annuler

		self.FrameChoix = Frame(self.fenetre, relief=GROOVE, pady = 10)
		self.FrameChoix.pack()
		self.btn_Valider = Button(self.FrameChoix, text="Valider")
		self.btn_Valider.pack(side=LEFT)
		self.btn_Annuler = Button(self.FrameChoix, text="Annuler")
		self.btn_Annuler.pack(side=RIGHT)

		self.fenetre.mainloop()
		
		
	def __Choix__(self):
		if self.Balance.get() == "True":
			self.AWBR.delete(0,END)
			self.AWBR.configure(state="disabled")
			self.AWBB.delete(0,END)
			self.AWBB.configure(state="disabled")
		elif self.Balance.get() == "False" :
			self.AWBR.configure(state="normal")
			self.AWBR.insert(END,1.5)
			self.AWBB.configure(state="normal")
			self.AWBB.insert(END,1.2)

if __name__ == '__main__':
	x = Cam()
