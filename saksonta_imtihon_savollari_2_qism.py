# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 02:48:29 2025

@author: Asus
"""

'''#22. isPrime(N) mantiqiy funksiyasini hosil qilish, tublar sonini aniqlash'''
# def isPrime(N):
#     tub=True # buyerda tubga qiymat berish kerak ekan
#     if (N==1):
#         tub=False
#     elif (N==2):
#         tub=True
#     else:
#         for x in range(2, N):
#             if(N%x==0):
#                 tub=False
#     return tub

# sonlar=[]
# k=int(input('k=')) # k- bu kiritiladigan sonlar miqdori 
# for n in range(k):
#     n=int(input(f"{n+1}-son:"))
#     sonlar.append(n)
# tub_sonlar=[]  
# for n in sonlar:  
#     if isPrime(n) and n>0: #Buyerda funksiyaga murojaat qilinmoqda, 
#         tub_sonlar.append(n)   #n>0 sharti, 0 ni tub songa kiritmasligi uchun.
# print('Natija:', len(tub_sonlar))
    

'''#23. DigitCount(k) funksiya k ni raqamlari sonini qaytarsin'''
# def DigitCount(k):
#     qold=[]
#     while k:
#         if k>10:
#             qold.append(k%10)
#             k=int(k/10)
#         elif k==10:
#             qold.append(0)
#             k=1
#         else:
#             qold.append(k)
#             break
#     return len(qold) #qold massiv o'lchami orqali, raqamlar soni 

# print(DigitCount(10120)) # kiruvchi ma'lumot k ni funksiyaga kiritish


'''#24. k soni n-elementini qaytaruvchi function'''
# def DigitN(k, n):
#     qoldiq=[]
#     while k:
#         if(k>10):
#             qoldiq.append(k%10)
#             k=int(k/10)
#         elif(k==10):
#             qoldiq.append(0)
#             k=1
#         else:
#             qoldiq.append(k)
#             break
#     raqam=0 # o'zgaruvchi
#     raqamlar=[]
#     Natija=-1
#     l=len(qoldiq) # l buyerda massiv o'lchami
#     if l>=n:
#         for i in range(l):
#             raqam=qoldiq.pop() # pop metodi yordamida oxiridan sugirib olamiz
#             raqamlar.append(raqam) # va yangi massivga tartiblab qoshamiz
#         for j in raqamlar:
#             Natija=raqamlar[n-1]
            
#     return Natija
# k=int(input("K="))
# n=int(input("N="))
# print('Natija:',DigitN(k, n))
            
    
'''#25. palindrom son, o'ngdan va chapdan o'qilishi bir xil sonlar'''
# def DigitCount(k):
#     qold=[]
#     while k:
#         if k>10:
#             qold.append(k%10)
#             k=int(k/10)
#         elif k==10:
#             qold.append(0)
#             k=1
#         else:
#             qold.append(k)
#             break
#     return qold

# def isPalindrom(N):
#     palindrom=False
#     son=0      #o'zgaruvchi
#     sonlar=[]  #bo'sh massiv
#     raqamlar=[]
#     l=len(DigitCount(N))
#     for x in range(l):
#         son=DigitCount(N)[x]
#         raqamlar.append(son)
        
#     for i in range(l):
#         son=raqamlar.pop()
#         sonlar.append(son)
#     c=0
#     for x in range(l):
#         son=DigitCount(N)[x] # boshqa funksiya natijasidan elementni olib,
#         raqamlar.append(son) # yangi massivga berdik.
    
#     for i in range(l):
#         if sonlar[i]==raqamlar[i]:
#             c+=1
#     if l==c:
#         palindrom=True
#     return palindrom

# print("3 ta sondan nechtasi palindrom ekanini aniqlovchi dastur!")
# #print("(palindrom-bu sonni o'ngdan ham, chapdan ham o'qilishi bir xil b-di)")
# soni=[]
# son=0
# p=0
# for i in range(1, 4):
#     son=int(input(f"{i}-son:"))
#     soni.append(son)
# for N in soni:
#     if isPalindrom(N):
#         p+=1
# print(f"Natija:{p}")
    
            
'''#26. EKUB(A, B) funksiyasini hosil qilish'''
# def ekub(a, b):
#     buluvci=0
#     min=a
#     if(a>b):
#         min=b
#     for n in range(1, min+1):
#         if a%n==0 and b%n==0:
#             buluvci=n
#     return buluvci

# print('Natija:', ekub(24, 12))
    
    
'''#27. EKUK(A, B) funksiya'''
# def ekuk(a, b):
    
#     bulinuvci=(a*b)/ekub(a, b) # yuqoridagi ekub funksiya orqali ekukni topish
#     bulinuvci=int(bulinuvci)
#     return bulinuvci
    
# print('Natija:',ekuk(24, 18))
    
    
''' #28.EKUB3(A,B,C) funksiyasi'''
# def ekub3(a, b, c):
#     buluvci=0
#     min=a
#     if(a>b and b<c):
#         min=b
#     elif(a>c and b>c):
#         min=c
#     for n in range(1, min+1):
#         if a%n==0 and b%n==0 and c%n==0:
#             buluvci=n
#     return buluvci
# print('Natija:',ekub3(17, 37, 15))

'''#29.EKUB n ta son'''
# def ekub(n):
#     buluvci=0
#     sonlar=[]
#     for i in range(n):
#         sonlar.append(int(input(f"{i+1}-son:")))#sonlarni ro'yxatga qo'shib,
#     min=sonlar[0]                               # 
#     for a in sonlar:
#         if(a<min):
#             min=a
#     #sonlar to'plamini chiqarib, tasdiqlab olamiz
#     print("Siz kiritgan sonlarni tasdiqlang:\n",sonlar) 
#     ishora=input("(ha/yoq)>")
#     if ishora=="ha": #sonlarni to'g'ri kiritganini tasdiqlash u-n
#         for j in range(1, min+1):
#             c=0
#             for son in sonlar:
#                 if son%j==0:
#                     c+=1
#             if c==n:
#                 buluvci=j
#     else:
#         print("Iltimos! Nimadir xatoga o'xshayabdi,"
#               " sonlarni qaytadan kiriting..")
#     return buluvci

# print("Natija:", ekub(5))


'''#30.Kabisa yil'''
def isLeapYear(yil):
    javob=False
    if yil%100==0: #100 ga karrali yillar, 400 ga bo'linsa.
        if yil%400==0:
            javob=True
    elif yil%4==0: # 4 ga karrali b-sa kabisa yil.
        javob=True
    return javob

# kabisa=[]
# yillar=[]
# print("Kiritilgan yillardan nechtasi kabisa...yil kiriting:")
# for i in range(1, 4):
#     yillar.append(int(input(f"{i}-yil:")))
# for y in yillar:
#     if isLeapYear(y):
#         kabisa.append(y)
# print(f"Natija:{len(kabisa)}")


'''#31. kiritilgan yil oylarining kunini aniqlash'''
def MonthDays(month, year): # 30-masaladagi funksiyadan foydalanilgan
    day=0
    if isLeapYear(year) and month==2:
        day=29
    elif month==2:
        day=28
    elif month==4 or month==6 or month==9 or month==11: #shu tartibdagi 
        day=30                  #oylarda 30 kun bor
    else:    #qolgan oylar 31 kun ekan
        day=31
    return day

# print("yil va oy kiritib. shu oylarda necha kun borligini bil")
# yil=int(input("yil:"))
# months=[]
# for i in range(3):
#     months.append(int(input(f"M{i+1}:")))
# for m in months:
#     print(MonthDays(m, yil), end=' ')


'''#32. Berilgan sanadan oldingi sanani aniqlovchi dastur,'''
# def PrevDate(D, M, Y): # 31-masaladagi funksiyalar bilan ishlaydi
#     Natija=[]
#     if D==1: #kun 1 ga teng b-sa,
#         if M==1: # va oy ham 1 ga teng b-sa, oy va yil o'zgaradi.
#             M=12 #oy
#             Y=Y-1 #yil
#             Natija.append(MonthDays(M, Y)) #oldingi oydagi oxirgi kunni beradi
#             Natija.append(M)
#             Natija.append(Y)
#         else:
#             Natija.append(MonthDays(M-1, Y))
#             Natija.append(M-1)
#             Natija.append(Y)
#     elif isLeapYear(Y) ==False and M==2 and D==29:
#         Natija.append(f"Bunday sana yo'q (maybe:28/2/{Y})!)") #Fevral 28 kun b-sa.
#     elif D<=MonthDays(M, Y):
#         Natija.append(D-1)
#         Natija.append(M)
#         Natija.append(Y)
#     else:
#         Natija.append("Bunday sana yo'q (day:30/31)")  #kun xato kiritilsa                
#     return Natija

# print("Kun/oy/Yil shaklida to'ldiring")
# d=int(input("kun:"))
# m=int(input("oy:"))
# y=int(input("yil:"))
# if m<=12:
#     for n in PrevDate(d, m, y):
#         print(f"{n}", end='/')
# else:
#     print("Bunday sana yo'q (month<=12:)") #oy xato kiritilsa


'''#33.Berilgan sanadan keyingi sanani aniqlash'''
# def PrevDate(D, M, Y): # 31-masaladagi funksiyalar bilan ishlaydi
#     Natija=[]
#     if D==MonthDays(M, Y): #kun oyni oxiri b-sa,
#         if M==12: # va oy ham 12 ga teng b-sa, oy va yil o'zgaradi.
#             M=1 #oy
#             Y=Y+1 #yil
#             Natija.append(1) #keyingi oydagi birinchi kunni beradi
#             Natija.append(M)
#             Natija.append(Y)
#         else:
#             Natija.append(1)
#             Natija.append(M+1)
#             Natija.append(Y)
#     elif isLeapYear(Y) ==False and M==2 and D==29:
#         Natija.append(f"Bunday sana yo'q (maybe:28/2/{Y})!)") #Fevral 28 kun b-sa.
#     elif D<=MonthDays(M, Y):
#         Natija.append(D+1)
#         Natija.append(M)
#         Natija.append(Y)
#     else:
#         Natija.append("Bunday sana yo'q (day:30/31)")  #kun xato kiritilsa                
#     return Natija

# print("Kun/oy/Yil shaklida to'ldiring")
# d=int(input("kun:"))
# m=int(input("oy:"))
# y=int(input("yil:"))
# if m<=12:
#     for n in PrevDate(d, m, y):
#         print(f"{n}", end='/')
# else:
#     print("Bunday sana yo'q (month<=12:)") #oy xato kiritilsa


'''#34 massiv'''
# son_A=[]
# n=int(input("n=")) #n ta
# for i in range(n):
#     son_A.append(int(input(f"{i+1}->"))) #sonlarni qo'shamiz
# for j in range(n):
#     if n%2!=0: # Takrorlanmaslik u-n sonlar miqdori toq b-sa,
#         if son_A[j] ==son_A[n-j-1]:
#             print(son_A[j])
#             break
#     elif j!=0: # juft b-sa, 0 indeksdagi element hisobga kirmaydi.
#         if son_A[j-1]==son_A[n-j-1]:
#             break
#     print(son_A[j], end='; ')
#     print(son_A[n-j-1], end='; ')


'''#35. n ta element massiv'''
# son_A=[]
# n=int(input("n=")) #n ta
# for i in range(n):
#     son_A.append(int(input(f"{i+1}->"))) #sonlarni qo'shamiz
# j=0
# i=1
# while True:
    
#     print(son_A[j])
#     j+=1
#     print(son_A[j])
#     j+=1
#     if j+i>=n: #sonni ikki marta takrorlanmasligi u-n, 
#         print(son_A[j])
#         break
    
#     print(son_A[n-i])
#     i+=1
#     print(son_A[n-i])
#     i+=1
#     if i+j>=n:#son takrorlanmasligi u-n,
#         print(son_A[n-i])
#         break

'''#36'''