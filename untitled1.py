# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 19:01:27 2025

@author: Asus
"""

'''Robocontest'''
 #1
def meets(n, a, b):
    if n>=b and b>=a:
        if (a+b)%2==0:
            natija='Yes'
        else:
            natija='No'
    else:
        natija='xatolik!'
    return natija

# n, a, b=map(int, input("Qimatlar:\t").split())
# print(meets(n, a, b))


 #2
def get_im(x, y, z):
    
     return lambda a: 'IM' if a>=x else 'IM emas'
   
# x, y, z=map(int, input('->').split())
# if 0<=x<=700 and y+z<=7:
#     if 0<=y<=7 and 0<=z<=7:
#         natija=get_im(x, y, z)
        
#         x1,x2,x3,x4,x5,x6,x7=map(int, input('->>').split())
#         adds=x1+x2+x3+x4+x5+x6+x7
        
#         print(natija(adds))


 #3  Eldor volybol turnirida
# def attempt(N, K):
#     sign=input('->>').lower()
#     if len(sign)!=N:
#         natija='No'
#     else:
#         c=0
#         ball=0
#         for n in sign:
                 
#             if n=='s':
#                 ball+=1
#                 c+=1 
#             elif n=='p':
#                 ball+=2
#                 c+=1 
#             elif n=='f':
#                 c=0
                
#             if c>K:
#                 natija='No'
#                 break
#             else:
#                 natija='Yes'
    
#     print(natija)
#     if natija!='No':
#         print(ball)
               
# N, K=map(int, input('->').split())
# attempt(N, K)
        

 #4. 
























 
 
 
 
 
 
 
 
 
 
 
 
 
 
 