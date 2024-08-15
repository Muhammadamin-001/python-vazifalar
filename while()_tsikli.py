
# &While tsikli

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
#  Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
'''
print("Sizga yoqadigan kitoblarni kiriting",end='')
print("(barchasini kiritib bo'lgach 'stop' so'zini kiriting!)")
javob=">>:"
while True:
    kitob=input(f"{javob}")
    if kitob.lower()=="stop":
        break
print("Rahmat!")
'''
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
#  Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring). 
'''
savol="yoshingizni kiriting\n>:"
izoh="(Dasturni to'xtatish uchun 'exit' yoki 'quit' buyurug'laridan birini kiriting)"
while True:
    qiymat=input(f"{savol}")
    if qiymat=="exit" or qiymat=="quit":
        break
    yosh=int(qiymat)
    if yosh<7:
        narh=2000
    elif yosh<18:
        narh=3000      
    elif yosh<65:
        narh=10000
    else:
        narh=0
    if narh==0:
        print("sizga chipta bepul","\n",izoh)
    else:
        print(f"sizga chipta narhi {narh} so'm","\n",izoh)
'''
#abadiy tsikl xatosini topish
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

   #JAVOBIM
'''savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing)\n>: "

while True:
    qiymat = input(savol)
    if qiymat.title()=='Exit':
        break
    ildiz = float(qiymat)
    if ildiz<0:
        continue
    else:
        print(f"{qiymat} ning ildizi {ildiz**(0.5)} ga teng")
'''


