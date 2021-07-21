# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:29:36 2021

22_dars_moslashuvchan_funksiyalar

@author: Javohir Bozorov
"""

#def summa(*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    yigindi = 0
#   for son in sonlar:
#        yigindi += son
#    return yigindi

#def summa(x,y,*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    return x+y+sum(sonlar)

#def avto_info(kompaniya,model,**malumotlar):
#    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#    malumotlar['kompaniya']=kompaniya
#    malumotlar['model']=model
#    return malumotlar

#avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
#avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
#print(avto1)

#1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

#def kopaytir(*sonlar):
#    a = 1
#    for son in sonlar:
#        a *= son
#    return a

#2.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya 
#yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa
#ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism,familiya,**malumotlar):
    malumotlar["ism"]=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talaba_info("ali", 'halimov', yoshi='21', oilaviy_ahvoli="bo'ydoq")


