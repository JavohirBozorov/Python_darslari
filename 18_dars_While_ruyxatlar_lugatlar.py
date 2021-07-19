# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:07:56 2021

18_18_dars_While_ruyxatlar_lugatlar

@author: Javohir Bozorov
"""

#ismlar = []
#print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
#n=1 # ismlarni sanash uchun o'zgaruvchi
#while True:
#    savol = f"{n}-do'stingiz ismini kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#    if javob =='ha':
#        n+=1
#        continue
#    else:
#        break
#print("Do'stlaringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())

#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingiz ismini kiriting: ")
#    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat    
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False
#
#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
#print(cars)

#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba] = baho

#uyga_vazifa
#1.Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini 
 #birma-bir qabul qilib, yangi ro'yxatga joylang.

#mahsulotlar = []
#print("Mahsulotlar ro'yxatini tuzamiz.")
#n=1 #mahsulot nomini sanovchi o'zgaruvchi
#while True:
#    savol = f"{n}-mahsulot nomini kiriting: "
#    mahsulot = input(savol)
#    mahsulotlar.append(mahsulot)
#    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#    if javob =='ha':
#        n+=1
#        continue
#    else:
#        break
#print("Mahsulotlar ro'yxati:")
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())

#2.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
 #dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va 
  #uning narhi) kiritishni so'rang

#print("\nBozorlik ro'yxati")
#bozorlik = {}
#ishora = True
#while ishora:
#    mahsulot = input("Mahsulot nomini kiriting: ")
#    narx = input("Mahsulot narxini kiriting:")
#    bozorlik[mahsulot] = int(narx)
#    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q) ")
#    if javob =="yo'q":
#        ishora  = False
#for mahsulot,narx in bozorlik.items():
#    print(f"\n{mahsulot.capitalize()}ning narxi {narx} so'm")

#3.Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
 #har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor 
  #ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa 
   #mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan 
    #xabarni ko'rsating.

bozorlik = {"kartoshka":2000,
            'sabzi':5000,
            'qalampir':12000,
            "sholg'om":7000,
            "olma":10000,
            'anor':13000,
            'nok':7000,
            'behi':13000,
            }
mahsulotlar = ["sabzi", 'qovun', "nok", 'behi', 'qalampir', 'gilos']
print("\nKerakli mahsulotlar nomini kiriting:")
while mahsulotlar:
    mahsulot = mahsulotlar.pop()
    if mahsulot in bozorlik.keys():
        narh = bozorlik[mahsulot]
        print(f"{mahsulot.title()} - {narh} so'm")
    else:
        print(f"Bizda {mahsulot} yo'q")



