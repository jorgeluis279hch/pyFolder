#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# Created by Jorge l.


from random import randint as rint
from datetime import datetime


def gD():

	#genera_fechas
	in_date = input('Fecha inicio_dd/mm/aaaa: ')
	x 		= int(input('Cantidad: '))
	a, b, c = in_date.split('/')
	año 	= datetime.now().year
	mes 	= datetime.now().month
	dia 	= datetime.now().day
	Dates	= [[str(rint(int(a), dia)), str(rint(int(b), mes)), str(rint(int(c), año))] for _ in range(x)]


	for n in Dates:
		print('/'.join(n))

 
if __name__ == '__main__':
	from colores import c
	print(f'{c.R}Run the {c.B}main{c.E} {c.R}script...{c.E}')