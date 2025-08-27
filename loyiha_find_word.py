# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:24:15 2025

@author: Asus
"""
''' #2-loyiha: 26 So'z topish o'yini'''
#Kerakli funksiyalar:
    #get_word()-tasodifiy so'zlarni tanlaydi
    #display('qabc','qurilma')
    #q....a

#from uzwords import words #krillcha
from random import randint
#from uzwords_lotin import words #lotincha yozuvda
from uzwords import words
from transliterate import to_latin
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


def yordam(w, dcount, bor):
    ishora=True
    while ishora:
        i=randint(0, len(w)-1)
        n=w[i]
        if dcount[n]>0:
            bor.append(n)
            dcount[n]-=1
            ishora=False
    return 0

input("So'z o'yini o'ynang, so'z harflarini tahmin qiling, istalgan tugma+enter boshlaydi.>>.")
word=to_latin(get_word(words))
#print(word)
harflar=[]
bor_harflar=[]
soni=len(word)
copy=word[:] #so'zimizni nusxasini oldik
dict_count=Counter(copy) #funksiya orqali {harflar:soni} shaklda lug'at
c=0 #inkorlar soni
s=0 #yordamlar soni
print("Tahminiy harf yozing. Qani ketdik!")
while True: #kiritilgan harf so'zda bo'lsa inobatga oladi,'finish, support', so'z topilgach tugaydi. 
    harf=input('>>>')
    
    if harf=='finish':
        print(word)
        break
    
    elif harf=='support' and s<4:
        yordam(word, dict_count, bor_harflar)
        soni-=1
        s+=1
        
    elif harf in word:
        if dict_count[harf]>0:
            print(f"{harf} harfi to'g'ri")
            bor_harflar.append(harf)
            dict_count[harf]-=1
            soni-=1
        #print(dict_count)
        else:
            print("Bu harfdan foydalangansiz.")
            c+=1
    else:
        print("Bunday harf yo'q")
        c+=1
        
    harflar.append(harf)
    print(display(bor_harflar, word))
    print(f"Shu vaqtgacha kiritgan harflaringiz:{harflar}\n")
    if c>=10 and c%5==0:
            print("Tugatish uchun 'finish' deb kiriting.")
            if s<4:
                print(f"Yordam olish uchun 'support' deb kiriting, qolgan urinish:({4-s})")
        
    if soni==0:
        print(f"Siz {len(harflar)} ta urinishda topdingiz."
              f"\tO'sha so'z: ->*{word.upper()}*< edi!")
        break











