# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:37:17 2025

@author: Asus
"""

''' Modullar'''

# from ruxat_qaytar_funks import katta
# talabalar=['ali', 'vali', 'nabi', 'nodir', 'qodir']
# ismlar=katta(talabalar)
# print(ismlar)


''' Boshqa Modul ichidagi funksiya yordamida kabisa yillarni aniqlash'''
from saksonta_imtihon_savollari_2_qism import isLeapYear as year #yilni kabisa bo'lsa, 
                                                #True qaytaruvchi funsiyaga murojaat qildik
print("Yillar oralig'ini kiriting va"
      " shu oraliqdagi kabisa(366 kun) bo'lgan yillarni aniqlang")
kabisa=[]
y1=int(input('boshlanishi:'))
y2=int(input('tugashi:'))
for n in range(y1, y2):
    if year(n): # Moduldan olgan funksiyamiz orqali yillarni tekshiramiz
        kabisa.append(n)
        
print(f"Quyidagi yillar 366 kundan iborat:{kabisa}\n"
      f"Bu oraliqda {len(kabisa)} ta yil kirdi.")



