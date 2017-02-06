from tkinter import * 
from tkinter.ttk import *
from Donnees_SQL import *

def main():
	
			
	root = Tk()
	root['bg'] = 'white'
	root.title('Configuration Séquence')
	laSelection = StringVar()
	CurrentIndexListe = 0
	
	lb_JourSouhaite = Combobox(root, textvariable = laSelection)
	lb_JourSouhaite.pack()
	__aff_LaListeDesJoueurs(laSelection, CurrentIndexListe)
	root.mainloop()
	
	return 0
	
def __aff_LaListeDesJoueurs(laSelection, CurrentIndexListe):
	ConnexionString = {'user': 'newuser' ,'password': 'newuser.56' ,'host': '172.16.22.107' ,'database': 'base_projets'}
	donnees = Donnees_SQL(ConnexionString)
	""" affiche la liste des joueurs existants de la base de données dans le Combobox..."""
	LaListeDesJoueurs = []
	# -- on renseigne le code de la requête SQL
	donnees.SQL_loadListedesJoueurs()
	# -- on rempli la liste des joueurs...
	LaListeDesJoueurs = donnees.chargerLesDonnees_RequeteSQL()
	# -- si la liste existe...
	if LaListeDesJoueurs:
		laListe  = []
	# -- on met en forme la liste à afficher dans la Combobox
	#for row in LaListeDesJoueurs:
	#	laListe.append("{:^8}".format(row[0]) + ' - ' + row[1])
	# -- on sélectionne la première occurence de la liste.
	laSelection.set(LaListeDesJoueurs[CurrentIndexListe])
	# -- on renseigne la combobox avec la liste mis en forme
	lb_JourSouhaite.config( values = laListe , state = NORMAL )
	aff_individu()

if __name__ == '__main__':
	main()

