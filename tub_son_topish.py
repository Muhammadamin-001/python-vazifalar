# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:37:07 2023

@author: Asus
"""
#Pytonda Tub son topish dasturi
son=int(input("son kiriting:"))
sum=0
for n in range(1,(son+1)):
    if son%n==0:
        sum=sum+1
        
if sum==2:
    print("bu son tub")
    
else:
    print("bu son tub emas!")
    print(f"chunki bo'luvchilari {sum} ta")