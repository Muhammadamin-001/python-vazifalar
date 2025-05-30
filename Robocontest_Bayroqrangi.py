# -*- coding: utf-8 -*-
"""
Created on Sat May 24 14:28:12 2025

@author: Asus
"""

'''#Bayroq ranglari b-n oyna bo'yash'''

def drawn(N):
    if N>=1 and N<=45:
        natija=2
        if N>2:
            natija=(N-1)*2
    return natija

n=int(input("N="))
print(drawn(n))

