# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:49:10 2021

10dars If else

@author: Javohir Bozorov
"""
avtolar = ['hyundai', 'bmw', 'gm']
#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
        
#ism = input('Ismr() != 'ali'ingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
#if ism.lowe: # Agar ism Aliga teng bo'lmasa ...
 #   print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
#else:
#    print("Salom, Ali")
        
#javob = float(input("12x6 nechiga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")
        
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#    print('Xush kelibsiz!')
#else: # ask holda
#    print('Kirish mumkin emas!')
    
#login = input("Yangi login tanlang:")
#if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")  
    
#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2020-yil}da ekan.\nKirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")    
    
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=65: print("Siz COVID-19 risk guruhida ekansiz")   
        


#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
 #ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM 
 #uchun ikkala harfni katta qiling.

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
 #   if car == 'gm' :
 #       print(car.upper())
 #   else :
 #       print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

#    if car != "gm":
     #    print(car.title())
#    else :
#         print(car.upper())

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz,
 #Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
 #Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

#log = input("Iltimos, loginingizni kiriting " )
#if log == Admin:
#    print('Xush kelibsiz Admin. Foydalanuvchilar ro\'yxatini k\'rasizmi?')
#else:
 #   print(f"Xush kelibsiz, {log}")
    
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng 
 #bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

#a = float(input("Birinchi sonni kiriting: "))
#b = float(input("Ikkinchi sonni kiriting: "))
#if a == b:
#    print("Sonlar teng")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa 
 #konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

#a = float(input("Xohlagan soningizni kiriting: "))
#if a > 0 :
 #   print("Musbat son")
#else:
 #   print("Manfiy son")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
 #ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son 
 #kiriting" degan xabarni chiqaring.

#a = float(input("Biror sonni kiriting: "))
#if a >= 0 :
 #   print(float(a**0.5))
#else :
 #   print("Musbat son kiriting.")