# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:04:14 2025

@author: Asus
"""

def isLeapYear(yil):
    javob=False
    if yil%100==0: #100 ga karrali yillar, 400 ga bo'linsa.
        if yil%400==0:
            javob=True
    elif yil%4==0: # 4 ga karrali b-sa kabisa yil.
        javob=True
    return javob

def MonthDays(month, year): # 30-masaladagi funksiyadan foydalanilgan
    day=0
    if isLeapYear(year) and month==2:
        day=29
    elif month==2:
        day=28
    elif month==4 or month==6 or month==9 or month==11: #shu tartibdagi 
        day=30                  #oylarda 30 kun bor
    else:    #qolgan oylar 31 kun ekan
        day=31
    return day

year=int(input("Yil:"))
days=256 #256-kuni kerak
month=0

for m in range(1, 13):
    days-= MonthDays(m, year) #yil orqali oldingi oyda necha kun borligini bilib,
    month=m               #256 dan ayirib boramiz! m-bu yerda oy hisoblanadi
    if days<=0: #kunlar tugagach sana o'tib ketgan hisoblanadi.
        day=MonthDays(m, year)-(-days) #manfiy o'tgan kunni ayirib topamiz
        break

print(f"{str(day).zfill(2)}/{str(month).zfill(2)}/{str(year).zfill(4)}")






