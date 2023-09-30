# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:45:23 2023

@author: Asus
"""

# Eng kichik tub sondan boshlab istalgan songacha faqat tub sonlarni chiqaradi

son=int(input("Musbat butun son kiriting:"))
tub_son=[] # Bo'sh ro'yxat yaratyapmiz
sum=0 # o'zgaruvchiga nol (0) qiymat berdik

for n in range(2, son):  # bu yerda 2 dan boshlab biz kiritgan songacha sikl aylanib davom etadi
    for n1 in range(1, (n+1)):  # n o'zlashtirgan sonni ham n1 orqali qo'llash uchun n+1 gacha chegara qo'ydik
        if n%n1==0: 
            sum=sum+1   # tub sonni topish uchun o'sha sonni faqat 1 ga va o'ziga bo'linishini tekshirish kerak
                        # sum shu qoldiqsiz bo'linishlarni sanaydi
    if sum==2:
        tub_son.append(n)
        
    sum=0    # bu yerda esa sum ni nol (0) ga teng qilib yana sanoqqa tayyorlaymiz
    
print(f"{son} sonigacha bo'lgan tub sonlar:", tub_son)
            
