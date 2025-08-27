# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 00:13:58 2025

@author: Asus
"""

class user:
    def __init__(self,username,ism,email,tyil):
        self.uname=username
        self.ism=ism
        self.mail=email
        self.tyil=tyil
        
    def get_info(self):
        return f"Foydalanuvchi:{self.uname}; ismi: {self.ism}; email:{self.mail}"
    
    def get_age(self,yil=2025):
        if yil-self.tyil>=18:
            result="Foydalanuvchi yetarli yoshda"
        else:
            result="Foydalanuvchi 18 yoshga to'lmagan!"
    
        return result
    
user1=user('ali_7707', "Alisher Sobirov", "alisobirov07@gmail.ru",2002)
user2=user('Olimboy02', "Olim Nabiyev", "nabiyevolim212@gmail.com",2004)
user3=user('Hasan03', "Hasan Husanov", "hasanhusan003@gmail.com",2007)
user4=user('sobir_04', "Sobir Qodirov", "Olimovich_204@gmail.com",2009)



