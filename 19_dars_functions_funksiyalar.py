# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 06:54:36 2021

19_dars_functions_funksiyalar

@author: Javohir Bozorov
"""

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum!")
    
#def salom_ber(ism):
#    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")  
#print(salom_ber.__doc__)
    
#def salom_ber(ism):
#    """Fodyalanuvchi ismini qabul qilib, 
#        unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#print(salom_ber.__doc__)   
    
#def toliq_ism(ism, familiya):
#    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
#    
#print(toliq_ism('kamol','jamolov'))
    
#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
#print(yosh_hisobla('Javohir',1998))    
    
#def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#   print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#    
#tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#yosh_hisobla(tugilgan_yil)
    
#def yosh_hisobla(tugilgan_yil, joriy_yil):
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#
#yosh_hisobla(1993,2021)
    
#def salom_ber(ism):
#    """Salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, {ism.title()}!")
#print(salom_ber("hasan"))
    

#1.Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan 
 #funksiya yozing.
 
#def t_yil_hisobla(yosh, joriy_yil=2021):
#    """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini 
#          hisoblaydigan funksiya """
#    print(f"Siz {joriy_yil-yosh}yilda tug'ilgansiz.")
#yosh = int(input("Yoshingizni kiriting: "))
#t_yil_hisobla(yosh)
 
#2.Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi 
 #funksiya yozing.
 
#def sonning_kv_kub_hisobla(son):
#    """Son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#    print(f"{son}ning kvadrati {son**2}ga teng")
#    print(f"{son}ning kubi {son**3}ga teng")
#son = int(input("Xohlagan soningizni kiriting: "))
#print(sonning_kv_kub_hisobla(son))

#3.Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
 #funksiya yozing.
 
#def juft_toq_aniqla(son):
#    if son%2 == 0:
#        print("Kiritilgan son juft")
#    elif son==0:
#        print("0 juft ham, toq ham emas")
#    else:
#        print("Kiritilgan son toq")
#son = int(input("Xohlagan soningizni kiriting: "))
#print(juft_toq_aniqla(son))
 
#4.Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
 #funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
 
#def kattasini_chiqar(a,b):
#    if a>b:
#        print(f"Birinchi son katta {a}>{b}")
#    elif a==b:
#        print("Sonlar teng")
#    else:
#        print(f"Ikkinchi son katta {a}<{b}")
#a=int(input("Birinchi sonni kiriting: "))
#b=int(input("Ikkinchi sonni kiriting: "))
#print(kattasini_chiqar(a,b))
 
#5.Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.

#def daraja_hisobla(x,y):
#    print(f"{x**y}")
#x=int(input("x="))
#y=int(input("y="))
#print(daraja_hisobla(x,y))

#6.Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

#def daraja_hisobla(x, y=3):
#    print(f"{x**y}")
#x=int(input("x="))
#print(daraja_hisobla(7))


#7.Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
 #qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

#def qoldiqni_tekshir(x):
#    for n in range(2,11):
#        if not x%n:
#            print(f"{x} {n}ga qoldiqsiz bo'linadi")
#x= int(input("x="))
#print(qoldiqni_tekshir(x))
    
