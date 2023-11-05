# Amaliy vazifalar

# 1
'''python={
#         "print":'chop etish',
#         'for':'takror',
#         'title':"birinchisi katta",
#         'upper':'bosh harflar',
#         'lower':'kichik harflar',
#         'tuple':"o'zgarmas ro'yxat",
#         'list':"oddiy ro'yxat",
#         'if':"shart operatori",
#         'set':"takrorsiz",
#         'sorted':'saralash'
#         }
# for k, q in sorted(python.items()):
#     print(f"{k}-->{q}")  '''

# 2
'''davlatlar={
    'misr':"qohira",
    'Amerika q sh':'washington',
    'germaniya':"berlin",
    "rossiya":'moskva',
    'baa':"saudiya",
    'uzbekistan':'tashkent'
    }
print("Davlatlar:")
for davlat in sorted(davlatlar):
    print(davlat.title())
print("\nPoytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.capitalize())'''
    
# 3
'''davlatlar={
    'misr':"qohira",
    'amerika':'washington',
    'germaniya':"berlin",
    "rossiya":'moskva',
    'baa':"saudiya",
    'uzbekistan':'tashkent',
    'qirg\'iziston':'bishkek',
    'qozog\'iston':"dushanbe",
    'italiya':'rim',
    'ispaniya':'madrid'
    }
davlat=input("Birorta davlat kiriting:").lower()
poytaxt=davlatlar.get(davlat)
if poytaxt==None:
    print("Bunday qiymat mavjud emas")
else:  
    print(f"{davlat.title()}ning poytaxti {davlatlar[davlat].capitalize()}")'''

# 4
'''menu={
      'osh':20000,
      'salat':5000,
      'non':4000,
      'somsa':12000,
      'halisa':25000,
      'sho\'rva':15000,
      'shashlik':60000,
      "choy":2000,
      "kofe":3000,
      'tort':50000}
print("Birinchi 3 talik narsangizni buyuring:")
test=input(" ha \ yo'q  __>").lower()
if test=="ha":
        
    buyurtma=[]
    for n in range(3):
        buyurtma.append(input(f"{n+1}-buyurtmangiz:").lower())
        
    print("Javob:")
    for taom in buyurtma:
        if taom in menu:
            print(f"{taom} narxi-{menu[taom]} so'm")
        else:
            print(f"Bizda {taom} yo'q ekan")        
elif test=="yo'q":
    print("Bizni ajobiy taomlar menyusi bilan tanishib chiqishingiz mumkin!")
else:
    print("Noaniq buyruq berdingiz! Izltimos, nima xohlashingizni aniqroq aytsangiz\n..(ha yoki yo'q kiriting)")           
'''