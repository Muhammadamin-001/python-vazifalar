
    
# Amaliy vazifalar

#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
#va Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
'''
allomalar=[]
navoiy={
    'ismi':'Alisher Navoiy',
    'sohasi':'shoir',
    'tyil':1441,
    'kitobi':['hamsa','lison ut-tayr','vaqfnoma'],
    'shahri':'hirot',
    'otasi':"g'iyosiddin"
    }   
temur={
    'ismi':'Amir Temur',
    'sohasi':"sarkarda",
    'tyil':1336,
    'kitobi':'temur tuzuklari',
    'shahri':'shahrisabz',
    'otasi':"tarag'ay"
    }   
    
bobur={
    'ismi':'Zahriddin Muhammad Bobur',
    'sohasi':['shoh','shoir'],
    'tyil':1483,
    'kitobi':['boburnoma','ga\'zallari'],
    'shahri':'andijon',
    'otasi':"umarshayx"
    }   
xorazmiy={
    'ismi':'al Xorazmiy',
    'sohasi':['matematik','astranom'],
    'tyil':783,
    'kitobi':['aljabr val muqobala','asatranomiya'],
    'shahri':'xiva',
    'otasi':"ja'far"
    }   
allomalar=[navoiy,temur,bobur,xorazmiy]
for shaxs in allomalar:
    ism=shaxs['ismi']
    sohalar=shaxs['sohasi']
    tyil=shaxs['tyil']
    asarlar=shaxs['kitobi']
    shahar=shaxs['shahri']
    ota=shaxs['otasi']
    print(f"{ism},",end=' ')
    if type(sohalar)==str:
        print(f"{sohalar}",end=' ')
    else:
        for soha in sohalar:
            print(f"{soha}",end=' ')
    print(f"{tyil}-yilda {shahar.capitalize()} shahrida tavallud topgan.\n"
          f"Otasi {ota.capitalize()}. Eng mashhur kitoblari:",end='')
    if type(asarlar)==str:
        print(f"\"{asarlar.capitalize()}\"",end=' ')
    else:
        for asar in asarlar:   
            print(f"\"{asar.capitalize()}\"",end=' ')
    print('.\n')
'''

#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.
#Natijani konsolga chiqaring.
'''
kino={
      'jamshid':['pavarot ne tuda','urush va tinchlik','bevalar'],
      'jalol':['who am i','maqsad','avatar'],
      'suxrob':['intelsteller','tubsizlik maxluqi','monk'],
      'ruslan':['king kong','terminator','gadzila']
      }
for ism, kinolar in kino.items():
    print(f"\n{ism.title()}ning sevimli filmlari:")
    for film in kinolar:
        print(f"\"{film.title()}\"")
'''

#Davlatlar degan lug'at yarating, 
#lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
#Har bir davlat haqida ma'lumotni konsolga chiqaring.

#Va Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
#Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
#"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
'''
davlatlar={
    'uzbekistan':{'poytaxti':'toshkent',
                  'maydoni':448.9,
                  'joylashuvi':'markaziy osiyo',
                  'aholisi':36},
    'qozoqiston':{'poytaxti':'astana',
                  'maydoni':2724.9,
                  'joylashuvi':'yevro-osiyo',
                  'aholisi':19.879},
    'rossiya':{'poytaxti':'moskva',
                  'maydoni':17100,
                  'joylashuvi':'yevropa',
                  'aholisi':145.3}
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()}:\npoytaxti:{info['poytaxti'].capitalize()}\nmaydoni:{info['maydoni']} ming km kv\n"
          f"joylashuvi:{info['joylashuvi']}\naholisi:{info['aholisi']} mln")
'''

#Va Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
#Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
#"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
'''
davlatlar={
    'uzbekistan':{'poytaxti':'toshkent',
                  'maydoni':448.9,
                  'joylashuvi':'markaziy osiyo',
                  'aholisi':36},
    'qozoqiston':{'poytaxti':'astana',
                  'maydoni':2724.9,
                  'joylashuvi':'yevro-osiyo',
                  'aholisi':19.879},
    'rossiya':{'poytaxti':'moskva',
                  'maydoni':17100,
                  'joylashuvi':'yevropa',
                  'aholisi':145.3}
    }
request=input("Qaysi davlat haqida ma'lumot qidiryapsiz?\n>>")
request=request.lower()
if request in davlatlar:
    info=davlatlar[request]
    print(f"\n{request.title()}:\npoytaxti:{info['poytaxti'].capitalize()}\nmaydoni:{info['maydoni']} ming km kv\n"
          f"joylashuvi:{info['joylashuvi']}\naholisi:{info['aholisi']} mln")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    