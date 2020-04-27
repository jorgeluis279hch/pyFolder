#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# Created by Jorge l.

  
import argparse

from src.colores import c
from src.fechas import *
from random import randint as rint


#Change the code your country
prefix = '+51' 
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cantidad", help = "Cuantos numeros desea generar: # default[0]", type = int) 
parser.add_argument("-f", "--fechas", help = "Genera Fechas recibe como parametro el simbolo de \'y\'", type = str) 
args   = parser.parse_args()


def num_ale():
    #genera numeros de celular aleatorios
    print('Generating numbers...')
    x = [[str(9) + str(rint(20, 99)), str(rint(110, 989)), str(rint(110, 989))] for i in range(args.cantidad)]
    return x
 

if args.cantidad: 
    r = num_ale()
    for i in r:
        print(prefix + ' ' + ' '.join(i)) 

elif bool(args.cantidad) == False and args.fechas:
	gD()

elif bool(args.cantidad) == False:
    print(f'{c.R}[*] Argument not found, type {c.Y}\'main.py -h\'{c.E} {c.R}for more information...{c.E}')
