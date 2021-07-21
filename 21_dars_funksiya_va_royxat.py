# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:16:24 2021

21-DARS.FUNKSIYA_VA_RO'YXAT

@author: Javohir Bozorov
"""

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=baho
#    return baholar

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar[:])
#print(talabalar)

#1.Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
 #birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def ozgartir(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].capitalize()   

ismlar = ['alining ukasi', 'vali', 'hasan', 'husan']
ozgartir(ismlar)
#print(ismlar)

#2.Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan 
#va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in baholar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

