''' Masalalar to'plami'''
# #1.
# print("Uchta sonni kichigini chiqaruvchi dastur!")
# min=0
# sonlar=[]
# for raqam in range(1,4):
#     son=input(f"{raqam}-son:")
#     son=float(son)
#     sonlar.append(son)
# for n in range(3):
#     min=sonlar[0]
#     if min>=sonlar[n]:
#         min=sonlar[n]
# print(f"Natija: {min}")


'''2. Kiritigan yilda jami necha kun borligini chiqaruvchi dastur'''
# yil=int(input("yil:"))
# n="Natija:"
# if yil%100==0:
#     if yil%400==0:
#         print(f"{n}366 kun")
#     else:
#         print(f"{n}365 kun")
# else:
#     if yil%4==0:
#         print(f"{n}366 kun")
#     else:
#         print(f"{n}365 kun")


'''#3. 2 ta sonni kichigi yigindilarini 2 ga bo'linganiga,
kattasi ko'paytmalari ikkilanganiga almashtirilsin.'''
# x, y = 0, 0
# x=float(input("x="))
# y=float(input("y="))
# a, b = x, y
# if x<y:
#     x=(a+b)/2
#     y=2*a*b
# elif x>y:
#     y=(a+b)/2
#     x=2*a*b
# print(x, y)


'''#4. Ikkita butun son berilgan kun, oy (kabisa bolmagan yil sanasi kiritiladi)
#Berilgan sanadan keyingi sanani ifodalovchi dastur tuzing.'''
# day=int(input("kun:"))
# month=int(input("oy:"))
# if month== 1 or month==3 or month==5 or month==month==7 or month==8 or month==10 or month==12:
#     #day=31
#     if day==31:
#         day=1
#         month+=1
#     elif day<31:
#         day+=1
# elif month== 4 or month== 6 or month==9 or month==11:
#     #day=30
#     if day==30:
#         day=1
#         month+=1
#     elif day<30:
#         day+=1
# elif month== 2:
#     #day=28
#     if day==28:
#         day=1
#         month+=1
#     elif day<28:
#         day+=1   
# print(f"{day} {month}")


'''#5.Mukammal son'''
#N=int(input("Son kiriting, men ungacha bo'lgan mukammal sonlarni topib beraman!\n son>>"))
# m_son=[]
# if N<=1:
#     print("Iltimos, Qaytadan kiriting, ko'zda tutilmagan raqam...")
# else:   
#     for m in range(1,N):
#         son=0
#         for r in range(1,m):
#             if m % r ==0:
#                 son+=r
#         if m==son:
#             m_son.append(m)
# print(f"{N} gacha Mukammal sonlar: {m_son}")


'''#6. tub son'''
# t_son=[]
# soni=int(input("son:"))
# c=0
# for son in range(2,soni):
#     sum=0
#     for n in range(1,(son+1)):
#         if son % n==0:
#             sum+=1
#     if sum==2:
#         t_son.append(son)
#         c+=1
# print(f"Tub sonlar: {t_son} -> {c} ta")


''' #7. Do'st sonlar'''
# N=int(input("N="))
# sonlar=[]
# if N <= 284:
#     print("Bu oraliqda siz izlagan son yo'q, tavsiya 285+...")
# else:
#     for son in range(220, N):
#         summ=0
#         for n in range(1,son):
#             if son%n==0:
#                 summ+=n 
#         count=0
#         for n in range(1,summ):
#             if summ%n==0:
#                 count+=n
#         if son==count and son<summ:
#             sonlar.append(son)
#             sonlar.append(summ)
# c=0
# for i in sonlar:
#     c+=1
#     if c==2:
#         print(i)
#         c=0
#     else:
#         print(i, end=' ')


''' #8. Bankka qo'yilgan summa k-oyda ikki marta ko'payadi.'''

# pul=float(input("pul kiriting (so'mda):..>"))
# p=float(input("necha foiz (12% gacha):"))
# if p>12:
#     print("Iltimos, 12% gacha kirita olasiz!")
# else:
#     p=p/100
#     ishora=True
#     pull=2*pul
#     k=0
#     while ishora:
#         if pul == pull or pul > pull:
#             ishora=False
#         else:
#             pul=pul+pul*p
#             k+=1
#     print(f"{k} oyda {pul} so'm")
    

'''   #9. sonni raqamlari nechta va raqamlari yig'indisi'''
# n=int(input("son:"))
# m=0
# c=0
# while n>0:
#     m+=n%10
#     n=n//10
#     c+=1
# print(c, m)


''' #10. EKUB(a, b)'''
# a=int(input("a="))
# b=int(input("b="))
# m=0
# abb=[]
# if a>b: min=b 
# else: min=a

# for n in range(1, (min+1)):
#     if a %n ==0 and b %n ==0:
#         abb.append(n)
# print(abb[-1])


'''   #11. N ni M ga (%, /) ishoralarsiz bo'ish, qolding va butun qismini toping.'''
# print("N-bo'linuvchi, M-bo'luvchi")
# N=int(input("N="))
# M=int(input("M="))
# q=0
# b=1
# m=M
# while N>M:
#     M+=m
#     b+=1
# if M>N:
#     b-=1
#     q=N-b*m
# print(q, b)
 

'''   #12. Eng katta va eng kichik.'''
# n=int(input("nechta son:"))
# son={}
# for m in range(1, (n+1)):
#     son[m]=int(input(""))
    
# max=son[1]
# min=son[1]  
# for m in range(1,(n+1)):
#     if max<=son[m]:
#         if son[m]>max and min>max:
#             min=max
#         max=son[m]
#     else:
#         if min>=son[m]:
#             min=son[m] 
# print(min, max)


'''  #13 eng kichik son va uning o'rni'''
# n=int(input("nechta son:"))
# son={}
# for m in range(1,(n+1)):
#     son[m]=int(input())

# min=son[1]
# for m in range(1, (n+1)):
#     if min>son[m]:
#         min=son[m]
# c=0
# for m in range(1, (n+1)):        
#     if min==son[m]:
#         c=m
# print(min, c)


'''  #14.Birinchi uchragan eng kichik, oxirgi eng katta''' 
# n=int(input("nechta son:"))
# son={}
# for m in range(1, (n+1)):
#     son[m]=int(input(""))
    
# max=son[1]
# min=son[1]  
# for m in range(1,(n+1)):
#     if max<=son[m]:
#         if son[m]>max and min>max:
#             min=max
#         max=son[m]
#     else:
#         if min>=son[m]:
#             min=son[m] 
# c=0
# d=0
# for m in range(1,(n+1)):
#     if min==son[m]:
#         c=m
#         break
# for m in range(1,(n+1)):
#     if max==son[m]:
#         d=m
# print(min, c,";", max, d)


''' #15. Ekstremal element'''
# n=int(input("nechta son:"))
# son={}
# for m in range(1, (n+1)):
#     son[m]=int(input(""))
    
# max=son[1]
# min=son[1]  
# for m in range(1,(n+1)):
#     if max<=son[m]:
#         if son[m]>max and min>max:
#             min=max
#         max=son[m]
#     else:
#         if min>=son[m]:
#             min=son[m] 
# c=0
# d=0
# for m in range(1,(n+1)):
#     if min==son[m]:
#         c=m
#         break
# for m in range(1,(n+1)):
#     if max==son[m]:
#         d=m
#         break
# if c<d:
#     print(min, c)
# else:
#     print(max, d)


'''  #16. oxirgi ekstremal son.'''
# n=int(input("nechta son:"))
# son={}
# for m in range(1, (n+1)):
#     son[m]=int(input(""))
    
# max=son[1]
# min=son[1]  
# for m in range(1,(n+1)):
#     if max<=son[m]:
#         if son[m]>max and min>max:
#             min=max
#         max=son[m]
#     else:
#         if min>=son[m]:
#             min=son[m] 
# c=0
# d=0
# for m in range(1,(n+1)):
#     if min==son[m]:
#         c=m

# for m in range(1,(n+1)):
#     if max==son[m]:
#         d=m
# if c>d:
#     print(min, c)
# else:
#     print(max, d)


'''   #17. eng kichik musbat son.'''
# n=int(input("Nechta son:"))
# Dson={}
# for m in range(1, (n+1)):
#     Dson[m]=int(input(' '))

# max=Dson[1]
# min=Dson[1]
# for m in range(1, (n+1)):
#     if min<0:
#         min=Dson[m]
#     else:     
#         if min>Dson[m] and Dson[m]>0:
#             min=Dson[m]
# if min<0:
#     min=0
# print(min)


'''  #18 birinchi uchragan eng katta toq son va tartib raqami'''
# n=int(input("Nechta son:"))
# sonlar={}
# for m in range(1, (n+1)):
#     sonlar[m]=int(input(' '))

# t_max=0
# for m in range(1, (n+1)):
#     if t_max<sonlar[m] and (sonlar[m]+1)%2==0:
#         t_max=sonlar[m]
# c=0
# for m in range(1, (n+1)):
#     if t_max==sonlar[m]:
#         c=m
#         break
# if t_max==0:
#     print(0)
# else:
#     print(t_max, c)       
        

'''  #19. oxirgi eng katta element va undan keyin turgan elementlar soni'''
# n=int(input("Nechta son:"))
# son={}
# for m in range(1, (n+1)):
#     son[m]=int(input(' '))
# max=son[1]
# for m in range(1, (n+1)):
#     if max<son[m]:
#         max=son[m]
# c=0
# for m in range(1, (n+1)):
#     if max==son[m]:
#         c=m
# c=n-c
# print(max, c)


''' #20. eng kichik 2 ta qiymat '''
# N=int(input("Nechta element(2+):"))
# if N>2:
#     son=[]
#     for m in range(N):
#         son.append(int(input("")))
#     min=son[0]
#     min1=son[0]
#     for m in range(N):
#         if min>son[m]:
#             min=son[m]
#     for m in range(N):
#         if min!=son[m] and min1>son[m]:
#             min1=son[m] 
#         else:
#             if min!=son[m] and min==min1:
#                 min1=son[m]
#     print(min," ",min1)
# else:
#     print("2 tadan ko'p element tanlang, iltimos!")
    

''' #21. ikkita qo'shni son yigindisining eng katta qiymati'''  
# N=int(input("Elementlar soni:"))
# if N>1:
#     Dson={}
#     for m in range(1, (N+1)):
#         Dson[m]=int(input(''))
#     max=0
#     adds=0
#     for m in range(1, (N+1)):
#         if m==N:
#             break
#         else:
#             adds=Dson[m]+Dson[m+1]
#             if max<adds:
#                 max=adds
#     print("->",max)
# else:
#     print('N>1')

           
                    
    







    
    
