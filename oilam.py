# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:20:04 2023

@author: Asus
"""
print("Bu siz haqingizda va oila a'zolaringiz haqida tanishtiruvchi dastur iltimos ma'lumotlarni to'g'ri kiriting! ")
oila=["Dadam", "Onam", "Singlim", "men"]
kishilar=[]

kishilar.append(oila.pop(0))
kishilar.append(oila.pop(0))
kishilar.append(oila.pop(0))
kishilar.append(oila.pop(0))

oila.insert(0, input("Dadam: "))
oila.insert(1, input("Onam: "))
oila.insert(2, input("Singlim: "))
oila.insert(3, input("men: "))

print("Assalomu aleykum mening ismim "+oila[3].title()+". Biz oilada to'rt kishimiz."+kishilar[0]+' '+oila[0].title()+" ayni paytda pensiya yoshidalar.")
print(kishilar[1]+' '+oila[1].title()+" obodon xodimi bo'lib ishlaydilar. "+kishilar[2]+' '+oila[2].title()+" ABCO akademiyasida o'qiydi. Va "+kishilar[3]+" BuxDu da o'qiyman.")


