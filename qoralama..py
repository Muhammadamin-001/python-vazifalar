# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:26:44 2024

@author: Asus
"""

sohalar={"Adabiyot":"she'riyat, ma'naviyat","Iqtisodiyot":"islom iqtisodiyoti, Istihora","Texnologiya":"qobiliyat, qiziqish"}
soham=input("Qaysi soha qiziq?\n>..")

for soha, sifat in sohalar.items():
    if soham.lower()==soha.lower():
        print(f"{soha} yo'nalishi sizga {sifat} sifatida tanish")
    
    