# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:24:29 2025

@author: Asus
"""

def larger(num):
    max_num=num[0]
    c=0
    m=0
    placed=[]
    for i in range(len(num)):
        if max_num<num[i]:
            max_num=num[i]
            
    for k in num:
        m+=1
        if max_num==k:
            c+=1
            placed.append(m)
    
    result=f"\n {max_num}  {c} \n{' '.join(map(str, placed))}"
    return result

n=int(input('n='))
numbers=list(map(int, input().split()))

if n!=len(numbers):
    print('ortiqcha yoki kam son kiritildi')
else:
      print(larger(numbers))
      
      
      
      
      
      