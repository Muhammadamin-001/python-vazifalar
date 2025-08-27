# -*- coding: utf-8 -*-
"""
Created on Sat May 24 17:18:54 2025

@author: Asus
"""

'''Robocontest #0009.Yolg'iz son'''

def single_n(N):
    sonlar=[]
    
    for m in range(1, N+1):
        sonlar.append(int(input()))
    if len(sonlar)==1:
        natija=1
    elif N>1:
        for i in range(N):
            c=0
            for j in range(N):
                if i != j and sonlar[i]==sonlar[j]:
                    c+=1
                    continue
                elif sonlar[i] !=sonlar[j]:
                    sana=sonlar[i]
                    
            if c==0:
                natija=sana
                break
    return natija         
    
N=int(input('N='))
if N>=1 and N<=100:
    print("->", single_n(N))
    




