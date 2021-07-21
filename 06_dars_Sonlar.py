# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:05:52 2021

06_dars_sonlar

@author: Javohir Bozorov
"""

#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

#son = input("Istalgan son kiriting:")
#sonning_kv = int(son)*int(son)
#print(son + "ning kvadrati " + str(sonning_kv) + "ga teng")
#sonning_kb = int(son)**3
#print(son + "ning kubi " + str(sonning_kb) +"ga teng")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab,
 #konsolga chiqaruvchi dastur

#yosh = input("Yoshingizni kiriting:")
#t_yil = 2021 - int(yosh)
#print("Siz "+ str(t_yil) + "da tug'ilgansiz")

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi,
#     ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

a = input("Birinchi sonni kiriting: ")
b = input("Ikkinchi sonni kiriting: ")
c = float(a) + float(b)
d = float(a) - float(b)
e = float(a) * float(b)
f = float(a) / float(b)
print( str(float(a)) + " + " + str(float(b)) + " = " + str(c))
print( str(float(a)) + " - " + str(float(b)) + " = " + str(d))
print( str(float(a)) + " * " + str(float(b)) + " = " + str(e))
print( str(float(a)) + " / " + str(float(b)) + " = " + str(f))

