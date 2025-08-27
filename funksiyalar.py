# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:24:15 2025

@author: Asus
"""
''' #26 So'z topish o'yini'''
#Kerakli funksiyalar:
    #get_word()-tasodifiy so'zlarni tanlaydi
    #display('qabc','qurilma')
    #q....a

#from uzwords import words
from random import randint
from uzwords2 import words
def get_word(word):
    
    n=int(randint(1, len(word)-1))
    return word[n]



from collections import Counter

def display(s1, s2):
    s1_count = Counter(s1)  # Harflar sonini hisoblab olamiz
    result = ''
    
    for c in s2:
        if s1_count[c] > 0:
            result += c
            s1_count[c] -= 1  # Harfni ishlatdik, 1 taga kamaytiramiz
        else:
            result += '-'
    return result

input("So'z o'yini o'ynang, so'z harflarini tahmin qiling, istalgan tugma+enter boshlaydi.>>.")
word=get_word(words)
#print(word)
harflar=[]
bor_harflar=[]
soni=len(word)
copy=word[:] #so'zimizni nusxasini oldik
dict_c=Counter(copy) #funksiya orqali {harflar:soni} shaklda lug'at
print("Tahminiy harf yozing. Qani ketdik!")
while True:
    harf=input('>>>')
    
    if harf in word:
        
        if dict_c[harf]>0:
            print(f"{harf} harfi to'g'ri")
            bor_harflar.append(harf)
            dict_c[harf]-=1
            soni-=1
        else:
            print("Bu harfdan foydalangansiz.")
    else:
        print("Bunday harf yo'q")
    harflar.append(harf)
    print(display(bor_harflar, word))
    print(f"Shu vaqtgacha kiritgan harflaringiz:{harflar}\n")
    
    if soni==0:
        print(f"Siz {len(harflar)} ta urinishda topdingiz."
              f"\tO'sha so'z: ->>{word.upper()}-<< edi!")
        break










