# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:45:23 2023

@author: Asus
"""

# Eng kichik tub sondan boshlab istalgan songacha faqat tub sonlarni chiqaradi

son=int(input("Musbat butun son kiriting:"))
tub_son=[]
sum=0

for n in range(2, son):
    for n1 in range(1, (n+1)):
        if n%n1==0:
            sum=sum+1
        
    if sum==2:
        tub_son.append(n)
        
    sum=0     
    
print(f"{son} sonigacha bo'lgan tub sonlar:", tub_son)
            