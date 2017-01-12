from tkinter import *


fenetre = Tk()
fenetre.title('Configuration caméra')
vP = StringVar()
vAWB = StringVar()
vMeta = StringVar()
Commande = StringVar

def __Commande__():
	#Commande = vP.get() + " -sh " + sb_Net.get() + " -co " + sb_Cont.get() + " -br " + sb_Lumi.get() + " -sa " + sb_Sat.get() + " -ISO " + sb_ISO.get() + vAWB.get() + " -md " + str(listeReso.index(ACTIVE)) + " -q " + sb_Qual.get() + vMeta.get()
	#print(Commande)
	print("lol")

def __Choix__():
	if vAWB.get() == " -awb auto " :
		AWBR.configure(state="disabled")
		AWBB.configure(state="disabled")
	elif vAWB.get() == " -awb off " :
		AWBR.configure(state="normal")
		AWBB.configure(state="normal")

FramePreview = Frame(fenetre, relief=GROOVE, pady = 3)
FramePreview.pack()
lb_Preview = Label(FramePreview, text="Preview")
lb_Preview.pack(side=LEFT)
rb_Preview = Radiobutton(FramePreview, text="Oui", variable=vP, value=" -p ")
rb_Preview.pack(side=LEFT)
rb_Preview.select()
rb_Preview2 = Radiobutton(FramePreview, text="Non", variable=vP, value=" -n ")
rb_Preview2.pack()


FrameNet = Frame(fenetre, relief=GROOVE, pady = 3)
FrameNet.pack()
lb_Net = Label(FrameNet, text="Netteté (-100/100) : ")
lb_Net.pack(side=LEFT)
sb_Net = Spinbox(FrameNet, from_=-100, to=100,width=4)
sb_Net.pack(side=RIGHT)

FrameCont = Frame(fenetre, relief=GROOVE, pady = 3)
FrameCont.pack()
lb_Contraste = Label(FrameCont, text="Contraste (-100/100) : ")
lb_Contraste.pack(side=LEFT)
sb_Cont = Spinbox(FrameCont, from_=-100, to=100,width=4)
sb_Cont.pack(side=RIGHT)

FrameLumi = Frame(fenetre, relief=GROOVE, pady = 3)
FrameLumi.pack()
lb_Lumi = Label(FrameLumi, text="Luminosité (0/100) : ")
lb_Lumi.pack(side=LEFT)
sb_Lumi = Spinbox(FrameLumi, from_=0, to=100,width=4, value = 50)
sb_Lumi.pack(side=RIGHT)

FrameSat = Frame(fenetre, relief=GROOVE, pady = 3)
FrameSat.pack()
lb_Sat = Label(FrameSat, text="Saturation  : (-100/100)")
lb_Sat.pack(side=LEFT)
sb_Sat = Spinbox(FrameSat, from_=-100, to=100,width=4)
sb_Sat.pack(side=RIGHT)

FrameISO = Frame(fenetre, relief=GROOVE, pady = 3)
FrameISO.pack()
lb_ISO = Label(FrameISO, text="Sensibilité ISO (100/800) : ")
lb_ISO.pack(side=LEFT)
sb_ISO = Spinbox(FrameISO, from_=100, to=800,width=4, value = 100)
sb_ISO.pack(side=RIGHT)

FrameAWB = Frame(fenetre, relief=GROOVE, pady = 3)
FrameAWB.pack()
lb_AWB = Label(FrameAWB, text="Balance des blancs : ")
lb_AWB.pack(side=LEFT)
rb_AWB = Radiobutton(FrameAWB, text="Oui", variable=vAWB, value=" -awb auto ", command = __Choix__)
rb_AWB.pack(side=LEFT)
rb_AWB.select()
rb_AWB2 = Radiobutton(FrameAWB, text="Non", variable=vAWB, value=" -awb off ", command = __Choix__)
rb_AWB2.pack(side=RIGHT)

FrameAWBReglage = Frame(fenetre, relief=GROOVE, pady = 3)
FrameAWBReglage.pack()
lb_AWBReglage = Label(FrameAWBReglage, text="Réglage par cannal (Rouge,Bleu) : ")
lb_AWBReglage.pack()
lb_AWBR = Label(FrameAWBReglage, text="Rouge : ")
lb_AWBR.pack(side = LEFT)
AWBR = Entry(FrameAWBReglage, width=3)
AWBR.pack(side = LEFT)
AWBR.configure(state="disabled")
AWBB = Entry(FrameAWBReglage, width=3)
AWBB.pack(side = RIGHT)
AWBB.configure(state="disabled")
lb_AWBB = Label(FrameAWBReglage, text="Bleu : ")
lb_AWBB.pack(side = RIGHT)




FrameReso = Frame(fenetre, relief=GROOVE, pady = 3)
FrameReso.pack()
lb_Taille = Label(FrameReso, text="Résolution : ")
lb_Taille.pack(side=LEFT)
listeReso = Listbox(FrameReso)
listeReso.insert(END, "Défaut : (2592x1944 (4:3) 1-15 IPS)")
listeReso.insert(END, "1920x1080 (16:9) 1-30 IPS")
listeReso.insert(END, "2592x1944 (4:3) 1-15 IPS)")
listeReso.insert(END, "2592x1944 (4:3) 0.1666-1 IPS")
listeReso.insert(END, "1296x972 (4:3) 1-42 IPS")
listeReso.insert(END, "1296x730 (16:9) 1-49 IPS")
listeReso.insert(END, "640x480 (4:3) 42.1-60 IPS")
listeReso.insert(END, "640x480 (4:3) 60.1-90 IPS")
listeReso.config(height=8, width = 28)
listeReso.selection_set(0,None)
listeReso.pack()

FrameQual = Frame(fenetre, relief=GROOVE, pady = 3)
FrameQual.pack()
lb_Qual = Label(FrameQual, text="Qualité (1/100) : ")
lb_Qual.pack(side=LEFT)
sb_Qual = Spinbox(FrameQual, from_=1, to=100,width=4, value = 100)
sb_Qual.pack(side=RIGHT)

FrameMeta = Frame(fenetre, relief=GROOVE, pady = 3)
FrameMeta.pack()
lb_Meta = Label(FrameMeta, text="Métadonnées : ")
lb_Meta.pack(side=LEFT)
rb_Meta = Radiobutton(FrameMeta, text="Oui", variable=vMeta, value="-r")
rb_Meta.pack(side=LEFT)
rb_Meta2 = Radiobutton(FrameMeta, text="Non", variable=vMeta, value=" ")
rb_Meta2.pack(side=RIGHT)
rb_Meta2.select()

FrameChoix = Frame(fenetre, relief=GROOVE, pady = 10)
FrameChoix.pack()
btn_Valider = Button(FrameChoix, text="Valider", command = __Commande__())
btn_Valider.pack(side=LEFT)
btn_Annuler = Button(FrameChoix, text="Annuler", command = __Commande__())
btn_Annuler.pack(side=RIGHT)

fenetre.mainloop()



