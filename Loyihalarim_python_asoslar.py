# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 01:00:19 2025

@author: Asus
"""
'''1-loyiha: sonni topish o'yini'''

# loyiha=True #o'yinni davomli o'ynash uchun,
# while loyiha: # sikldan foydalanamiz.
#     game=input("Son o'yini o'ynaysizmi? (sure/not) bosing!\n>")
#     if game=='sure' or game=='ha' or game=='yes': #user' fikrini bilish
#         print("Men bir son o'yladim, u [1-10] orasida, qancha taxmin bilan toparkansiz!")
        
#         import random as r
#         son=r.randint(1, 10)
        
#         print("tahminiy son ayting:")
#         count=0 #foydalanuvchi urinishlari soni
    
#         while True:
#             try:
#                 tahmin=int(input(">>"))
#                 count+=1
                
#                 if son==tahmin:
#                     break #taxmin va o'ylangan son mos kelsa, sikl tugaydi.
#                 elif son>tahmin: # mos kelmasa, yo'naltirilib, urinish hisoblanadi!
#                    print('bundan kattaroq son o\'ylang:')
#                 else:
#                     print('bundan kichikroq son o\'ylang:')
#             except ValueError:
#                 print("matn emas son kiriting!")
        
#         print(f"\nSiz sonni {count} ta urinishda topdingiz!"
#               "\nEndi siz [1-10] orasida son o'ylang men topaman..")
#         fikri=input("o'yladizmi(ha/yoq):") 
#                     #user o'ylashiga vaqt beriladi
#         if fikri=='ha':
#             ishora=True
#             c=0    #kompyuter urinishlari soni
#             belg1=1
#             belg2=10
#             taxmini=r.randint(1, 10) #dastur taxmin qiladi.
#             while ishora:
#                 try:
#                     print('\ntaxminim:', taxmini) #aytadi
#                     natija=input("Taxminim to'g'ri bo'lsa(t), bundan katta bo'lsa(+), bundan kichik bo'lsa(-) bosing!\n>>")
#                     c+=1
                    
#                     if natija=='t':
#                         ishora=False#Taxmini mos kelsa, sikl tugaydi.
#                     elif natija=='-': #son taxmindan kichik  bo'lsa, maksimallik chegarasi
#                         belg2=taxmini-1 #bittaga kamayadi.
#                         taxmini=r.randint(belg1, belg2)
                        
#                     elif natija=='+': #Son taxminidan katta bo'lsa,
#                         belg1=taxmini+1 #minimallik chegarasi bittaga ortadi.
#                         taxmini=r.randint(belg1, belg2)
                    
#                 except ValueError:
#                     print("EROR! /404")
                
                 
#             print(f"\nmen sonni {c} ta urinishda topdim!")
#             if count<c:
#                 print(f"siz({count}) g'olib!")
#             elif count==c:
#                 print("kuchlar teng!")
#             else:
#                 print(f"siz yaxshi o'ynadingiz({count}), lekin ustunlik menda..!")
#         print("\n")
#     else:
#         loyiha=False


        





