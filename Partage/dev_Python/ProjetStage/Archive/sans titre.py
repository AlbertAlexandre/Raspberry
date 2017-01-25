#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sans titre.py
#  
#  Copyright 2017  <pi@raspi_tv07>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	def Chaine3(uneChaine):
		while len(uneChaine)<3:
			uneChaine = "0" + uneChaine
		print(uneChaine)
		
	def Annee2(uneAnnee4):
		Annee2 = str(uneAnnee4)[2:4]
		print (Annee2)
		
	def Chaine2(uneChaine):
		while len(uneChaine)<2:
			uneChaine = "0" + uneChaine
		print(uneChaine)
		
	def Espece10(uneChaine):
		while len(uneChaine)<10:
			uneChaine = uneChaine + "_" 
		print(uneChaine)
	
	
	x = "1"
	Chaine3(x)
	an = 2017
	Annee2(an)
	y = "1"
	Chaine2(y)
	esp = "colza"
	Espece10(esp)
	
	
	
	
	return 0
if __name__ == '__main__':
	main()

