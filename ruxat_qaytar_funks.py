# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:43:39 2025

@author: Asus
"""

'''Amaliy: ro'yxat qaytaruvchi funsiyalar:'''

def katta(ismlar):     #Berilgan matnli ro'yxat elementlarini birinchi
    ismlar=ismlar[:]     #harfini katta qilib beruvchi funksiya
    for i in range(len(ismlar)):         
        ismlar[i]=ismlar[i].title()
    return ismlar
# talabalar=['ali', 'vali', 'nabi', 'nodir', 'qodir']
# ismlar=katta(talabalar)
# print(ismlar)
# print(talabalar)


def bahola(ismlar):
  
    baholar = {}
    for ism in ismlar: # pop() metodidan foydalanmasdan bajarish
        
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)






