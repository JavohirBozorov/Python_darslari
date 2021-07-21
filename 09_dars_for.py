# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:24:11 2021

09_dars_If

@author: Javohir Bozorov
"""
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va 
 #ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
#for ism in ismlar:
 #   print(f" Salom { ism}, Ahvollaring yaxshimi?")

#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan 
 #xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print("Kod 5marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
 #elementining kubini yangi qatordan konsolga chiqaring.
#toq_sonlar = list(range(11, 100, 2))
#for toq_son in toq_sonlar:
   # print(f"{toq_son}ning kubi {toq_son**3}ga teng")
    
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar 
 #degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
 
kinolar = [] 
#print("5ta Sizning eng sevimli filmingiz qaysilar: ")
#for n in range(5):
 #   kinolar.append(input(f"{n+1}-film nomini kiriting: "))
#print(kinolar)
     
#dostlar = [] # bo'sh ro'yxat
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
 #   dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
#print(dostlar)
     
 #Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
 #so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab 
 #ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
 
#people = []
#print("Bugun kimlar bilan ushrashdingiz? ")
#for n in range(5):
#    people.append(input(f"{n+1}-suhbatdoshingiz nomini kiriting"))
#print(people)

n_odamlar = int(input("Bugun necha kishi bilan uchrashdingiz? "))
ismlar = []
for n in range(n_odamlar):
       ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
#print(ismlar)
for ism in ismlar:
    print(ism.title())



