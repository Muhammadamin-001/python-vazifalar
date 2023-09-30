# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:05:36 2023

@author: Asus
"""
""" 1.
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
(ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring:
Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""
# otam={'ismi':'Baxshullo','t_yil':1963,'shahri':"Buxoro",'faoliyati':'pensioner'}
# onam={'ismi':'Sanobar','t_yil':1976,'shahri':"Navoiy",'faoliyati':"obodon xodimasi"}
# singlim={'ismi':'Matuna','t_yil':2004,'shahri':"Vobkent",'faoliyati':'talaba'}
# print(f"Otamning ismi {otam['ismi']}, {otam['t_yil']}-yilda, {otam['shahri']} viloyatida tug'ilgan. Hozirda {otam['faoliyati']} hisoblanadi.")
# print(f"Onamning ismi esa {onam['ismi']}, {onam['t_yil']}-yilda, {onam['shahri']} viloyatida tug'ilgan. Hozirda {onam['faoliyati']} hisoblanadi.")
# print(f"Mening singlimni ismi {singlim['ismi']}, {singlim['t_yil']}-yilda, {singlim['shahri']} tumanida tug'ilgan. Hozirda {singlim['faoliyati']} hisoblanadi.")

""" 2.
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
 Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh 
 """
# sev_taom={'otam':'osh','onam':'somsa','akam':'chuchvara','singlim':'manti','men':'kabob'}
# print(f"Otamning sevimli taomlari {sev_taom['otam']}. chunki har doim {sev_taom['otam']} tayyorlaydilar.\n\
# Onam esa doim bizlarga {sev_taom['onam']} pishirib beradilar, singlim {sev_taom['singlim']}ni yoqtiradi. Menga esa {sev_taom['men']} yoqadi")
      
""" 3.
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
(masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""
izohli={
        'print':"chop etmoq",'string':'matn','int':'integer-butun son',
        'float':"o'nlik son",'list':'ruyxat','tuple':"o'zgarmas ruyxat",
        'if':'shart operatori','else':'yoki bo\'lmasa','for':'takrorlanuvchi funksiya','input':'kirituvchi operator'
        }

""" 4.
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
 Agar so'z lu'gatda mavjud bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring."""

kalit=input("Kalit so'z kiriting: >").lower()
# print(izohli.get(kalit,"Bunday so'z mavjud emas"))

""" 5.
Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring."""
""" #1 """
# if kalit in izohli:
#     print(f"{kalit}: '{izohli[kalit]}' ma'nosida ishlatiladi")
# else:
#     print("Bunday so'z mavjud emas")
 
""" #2 """
# tarjima=izohli.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")







