# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:36:31 2024

@author: Asus
"""

''' $ Functions'''

# def salom_ber(ism):
#     """ Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya """
#     print(f"Assalomu aleykum, hurmatli {ism.title()}")

# salom_ber("hasan")
# salom_ber('husan')

''' 1.foydalanuvchi ismi va yoshini so'rab,
   tugilgan yilini chiqaruvchi dastur'''
   
# def tug_yil(ism, yosh):
#     """ ismi va yoshini so'raymiz 
#     va tugulgan yilini chiqaramiz"""
#     print(f"{ism.title()} siz {2024-yosh}-yilda tugulgansiz..")

# tug_yil('suraj', 22)
# tug_yil('ziyodulla', 23)

''' 2. kvadrati, kubi'''
# def darajala(son):
#     """ foydalanuvchidan sonni qabul qilib,
#     son kvadrati va kubini chiqaruvchi funksiya"""
#     print(f"{son} ni kvadrati:{(son)**2}, kubi:{(son)**3} ")
# darajala(-4)
 
''' 3. juft, toqligi'''
# def juftmi(son):
#     """ sonni juft yoki toqligini aniqlash"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         if son!=0:
#             print(f"{son} juft son")
#         else:
#             print(son, 'juft ham toq ham emas,',son, 'qiymatga ega emas!')

# juftmi(56)
# juftmi(157)
# juftmi(0)

''' 4. kattasini topish'''
# def solishtir(x, y):
#     """ ikkita sonni qabul qilib,
#     sonni kattasini chiqaradi yoki tengligini"""
#     if x>y:
#         print(f"{x}>{y}")
#     else:
#         if y>x:
#             print(x,'<',y)
#         else:
#             print(x,'=',y)
# solishtir(2**10, 5**3)
# solishtir(4**3, 9*8)
# solishtir(8*3, 6*4)

''' 5-6. x^y '''
# def darajala(x, y=2):
#     """ x ni y darajaga ko'tarish"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")

# darajala(5, 3)
# darajala(6, 4)
# darajala(3, 9)
# darajala(9)

''' 7. sonni 10 gacha bo'linishi'''
# def bulinishi(x):
#     """ foydalanuvchidan son qabul qilib,
#     2 dan 10 gacha qoldiqsiz bo'linishi.."""
#     print(f"{x} qoldiqsiz bo'linadi:")
#     for n in range(2, 11):
#         if not x%n:
#             print(f" {n}",end=';')
#     print('\n')
# bulinishi(20)
# bulinishi(32)










