# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:37:46 2025

@author: Asus
"""
## Na'munalar:
    
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ismni qaytaruvchi funksiya"""
#     if otasining_ismi: #Otasining ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title() # qiymat qaytarish uchun return operatorini ishlatamiz
# talaba1=toliq_ism_yasa("Salim", "Shodiyev")
# talaba2=toliq_ism_yasa("Rasul", "Negmatov", "Hoshimovich")
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}.")

# def avto_info(kompaniyasi, modeli, rangi, karobkasi, yili, narhi=None):
#     avtocar={'kompaniya':kompaniyasi,
#               'model':modeli,
#               'rang':rangi,
#               'karobka':karobkasi,
#               'yil':yili,
#               'narh':narhi}
#     return avtocar
# avto1=avto_info('GM', 'Malibu 2', 'qora', 'avtomat', 2022)
# avto2=avto_info('GM', 'Cobalt', 'oq', 'meanika', 2021, 10000)
# avtolar=[avto1, avto2]
# print('Online bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh= "Noma'lum"
#     print(f"\t{avto['rang'].capitalize()} {avto['model']}. Narhi:{narh}")

# def oraliq(min, max, qadam=1):
#     sonlar=[] #Bo'sh royxat
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# print(oraliq(0, 21, 2))
# print(oraliq(10, 21))
    
# def avto_info(kompaniyasi, modeli, rangi, karobkasi, yili, narhi=None):
#     avtocar={'kompaniya':kompaniyasi,
#               'model':modeli,
#               'rang':rangi,
#               'karobka':karobkasi,
#               'yil':yili,
#               'narh':narhi}
#     return avtocar
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end=' ')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rang=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yil=input("Ishlab chiqarilgan yili: ")
#     narh=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# #Amaliyot

'''1,2.Foydalanuvchi ma'lumotlarini lug'at ko'rinishida qaytaruvchi dastur'''
# def custumor_info(ismi, familiyasi, tug_yili, tug_joyi, yoshi, e_manzili=' ', teli=None):
#     cinfo={'ism':ismi,
#             'familiya':familiyasi,
#             'tyil':tug_yili,
#             'tjoy':tug_joyi,
#             'yosh':2025-tyil,
#             'email':e_manzili,
#             'tel':teli}
#     return cinfo
# mijozlar=[]
# print("Foydalanuvchi ma'lumotlarini kiriting:")
# while True:
#     ism=input("Ismi:")
#     familiya=input("Familiyasi:")
#     tyil=int(input("tugilgan yili:"))
#     tjoy=input("tugilgan joyi:")
#     email=input("elektron manzili(ixtiyoriy!):")
#     tel=input("telefon raqami(ixtiyoriy!):")
#     mijozlar.append(custumor_info(ism, familiya, tyil, tjoy, email, tel))
#     javob=input("Yana foydalanuvchi qo'shasizmi(yes/no)?")
#     if javob!='yes':
#         break
    
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['tjoy'].capitalize()}da "
#           f"{mijoz['tyil']}-yilda tug'ilgan. emaili: {mijoz['email']} Telefon raqami:{mijoz['tel']}, ")
'''CHALA XATO! telefon raqam o'rniga, raqamni emailga saqladi'''


'''3.uchta sondan eng kattasini qaytar'''
# def kattasi(x, y, z):
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#           max=z
#     return max

# print("Uchta son kiriting:")
# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))
# print(kattasi(x, y, z))

'''4.radiusi...lug'at ko'rinishida qaytar funksiya'''
# def aylana_info(radius, pi=3.14159):
#     aylana={'radius':radius,
#             'diametr':2*radius,
#             'perimetr':2*pi*radius,
#             'yuzi':pi*radius**2}
#     return aylana

# r=int(input('Aylana radiusi:'))
# print(aylana_info(r))

'''5.Berilgan oraliqdagi tub sonlar qaytaruvchi funksiya'''
# def tubla(y, x=2):
#     tub=[]
#     for son in range(x, y):
#         count=0
#         for n in range(1, (son+1)):
#             if son%n==0:
#                 count+=1
#         if count==2:
#             tub.append(son)
#     return tub
# soni=int(input('Qaysi songacha tub bo\'lsin: '))
# print(tubla(soni))

'''Ustozni kodi:'''
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# print(tub_sonlar_top(1,20))

'''6.Fibonachi sonlar ro'yxatini qaytaruvchi funksiya'''
# def fibonacci(n):
#     fibolist=[]
#     for i in range(n):
#         if i==0 or i==1:
#             fibolist.append(1)
#         else:
#             fibolist.append(fibolist[i-1]+fibolist[i-2])
#     return fibolist

# print(fibonacci(10))
'''07.01.2025/ 20:59'''     
        

