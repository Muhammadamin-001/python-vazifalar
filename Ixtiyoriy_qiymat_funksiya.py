# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:46:10 2025

@author: Asus
"""

''' *args & **kwargs'''

'''#1.istalgan sonni ko'paytmasini topish'''
# def kopay(*sonlar): # *args-istalgancha argument kiritish mumkin
#     Natija=1
#     for son in sonlar:
#         Natija*=son
#     return Natija
# print(kopay(1,2,3,4,5,6,10))


'''#2.Talaba haqidagi ma'lumotlarni lug'at ko'rinishida saqlash'''
# def talaba_info(ism, familiya, **axborot):
#     axborot['ism']=ism
#     axborot['familiya']=familiya
#     return axborot

# talaba=talaba_info('Ali', 'Ikromov', oliygoh='TATU', fakultet='Dasturiy injeniring', kurs=3, yonalish='AX')
# print(talaba)


'''lambda- nomsiz funksiya'''

# def daraja(n):
#     return lambda x: x**n

# kvadrat=daraja(2)
# kub=daraja(3)
# son=int(input("son:"))
# print(f"{son} ning kvadrati-{kvadrat(son)}, kubi-{kub(son)} ga teng.")

'''#Matndan harflar sonini topish'''
# def search(s):
#     matn=s
#     qidir=input("search:")
#     count=0
#     for word in matn:
#         if qidir==word:
#             count+=1
#     return count
# m=str("men kim mulki turon saltanati guliston yurt farzandiman")
# print(search(m))



