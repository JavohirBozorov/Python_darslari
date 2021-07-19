# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:42:38 2021

15_dars_lug'atlar_bn_ishlash

@author: Javohir Bozorov
"""

talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat} \n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

#print(mahsulotlar.keys())

bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, do'koningizga {buyum} ham olib keling")

#print("Do'konimizdagi mahsulotlar:")    
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())

#print(telefonlar.values())

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#    print(tel)



#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
 #Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
   #ketma-ketligida chiroyli qilib konsolga chiqaring.

lugat = {'int':'butun son',
         'float':'o\'nlik sonlar', 
         'str':'matn', 
         'list':'ro\'yxat', 
         'tuples':"o'zgarmas ro'yxat", 
         'for':'uchun', 
         'if':'agar', 
         "else":'aks holda'}

#for key, value in sorted(lugat.items()):
#    print(f"{key.title()} - {value}")

#print("Python izohli lug'ati: ")
#for k in sorted(lugat):
#    print(k)
#print("\n")
#for q in sorted(lugat.values()):
#    print(q)

#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
 #keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

davlatlar = {'usa':"vashington",
             'uk':'london',
             'uzbekistan':'tashkent',
             'germany':'berlin',
             'russia':'moskva',
             'ispain':'madrid',
             'italy':'rim',
             'australia':'kanberra',
             'china':'bejing',
             'korea':'seul',
             'japan':'tokio',
             'france':'paris'
             }

#davlat = input("istalgan davlatni kiriting: \n").lower()
#tarjima = davlatlar.get(davlat)

#if tarjima == None:
 #   print("Bunday so'z mavjud emas")
#else:
 #   print(f"{tarjima.title()} capital of {davlat.title()} ")

#for key in sorted(davlatlar):
#    print(key)

#print("\n")    
#for q in sorted(davlatlar.values()):
#    print(q)

#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
 #konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
  #"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

#davlat = input("Istalgan davlatni kiriting: ")
#for davlat in davlatlar:
#if davlat in davlatlar and davlat == "usa" and "uk":
#    print(f"{davlatlar[davlat].capitalize()} is capital of {davlat.upper()}")
#elif davlat in davlatlar:
#    print(f"{davlatlar[davlat].capitalize()} is capital of {davlat.title()}")
#else:
#    print("Bizda bunday ma'lumot yo'q")
 
   

#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
 #Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
  #taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
   #aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

#print("3ta taom buyurtma qiling:")

menu = {"osh":15000,
         "sho'rva":12000,
         "mastava":11000,
         "shashlik":30000,
         "jiz":28000,
         'moshkichri':14000,
         'chuchvara':17000,
         'somsa':3000,
         'tandir':40000
        }
print("3ta taomga buyurtma bering")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-ovqat nomini kiriting: ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"\n{buyurtma} {menu[buyurtma]} so'm")
    else:
        print(f"\nBizda {buyurtma} mavjud emas")
        
        
#if ovqat == None:
 #   print("Bizda bunday ovqat yo'q")
#else:
 #   print(f"{ovqat}ning narxi {menu[ovqat]} so'm")



#    if ovqat in menu.keys():
#        print(f"{ovqat} {menu[ovqat]} so'm")
#    else:
#        print("Bizda bunday ovqat yo'q")

#ovqat1 = input("Birinchi ovqatni kiriting: ") 
#ovqat2 = input("Ikkinchi ovqatni kiriting: ") 
#ovqat3 = input("Uchinchi ovqatni kiriting: ") 

#f ovqat1 in menu:
#    print(f"{ovqat1}ning narxi {menu[ovqat1]} so'm")
#else:
#    print("Bizda bunday ovqat yo'q")
#if ovqat2 in menu:
#    print(f"{ovqat2}ning narxi {menu[ovqat2]} so'm")
#else:
#    print("Bizda bunday ovqat yo'q")
#if ovqat3 in menu:
#    print(f"{ovqat3}ning narxi {menu[ovqat3]} so'm")
#else:
#    print("Bizda bunday ovqat yo'q")


