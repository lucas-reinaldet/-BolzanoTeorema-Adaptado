#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:31:44 2021

@author: lucas-reinaldet
"""

def f(x):
    return x ** 3 + (3 * x) - 1

import math

a = 0
b = 3
e= 0.01

qtd_repeticoes = 0
#Teorema de Bolzano
if f(a) * f(b) < 0:
    while (math.fabs(b-a)/2 > e):
        qtd_repeticoes += 1
        xi = (a+b)/2
        if f(xi) == 0:
            print('A raiz é : ',xi)
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print('Valor da raiz é: ', xi)
else:
    print('Não há raiz neste intervalo')

print(f"Quantidade de repetições = {qtd_repeticoes}")
