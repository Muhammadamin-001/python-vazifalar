# -*- coding: utf-8 -*-
"""
Created on Wed May 21 15:36:12 2025

@author: Asus
"""
'''# Dasturchilar kunini aniqlash dasturi'''

from saksonta_imtihon_savollari_2_qism import MonthDays as date
year=int(input("Yil:"))
days=256 #256-kuni kerak
month=0

for m in range(1, 13):
    days-= date(m, year) #yil orqali oldingi oyda necha kun borligini bilib,
    month=m               #256 dan ayirib boramiz! m-bu yerda oy hisoblanadi
    if days<=0: #kunlar tugagach sana o'tib ketgan hisoblanadi.
        day=date(m, year)-(-days) #manfiy o'tgan kunni ayirib topamiz
        break

print(f"{str(day).zfill(2)}/{str(month).zfill(2)}/{str(year).zfill(4)}")
 #.zfill(n)-bu funksiya n xonali son u-n, nol raqam orqali to'ldiradi.

 