# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:17:16 2021

08_dars_ro'yxatlar_bn_ishlash

@author: Javohir Bozorov
"""


#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ["USA", "UK", "Australia", "Uzbekistan", "Spain", "France", "Germany"]
print(countries)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(countries))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(countries))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(countries, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(countries)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
countries.reverse()
print(countries)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
print(list(range(120,1200,2)))

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(list(range(120,1200,2))))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
a = max(list(range(120,1200,2)))
b = min(list(range(120,1200,2)))
print(a-b)

#Ro'yxatdagi elementlar sonini hisoblang
print(len((list(range(120,1200,2)))))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 10 ta qiymatni konsolga chiqaring
c = list(range(120,1200,2))
print("Birinchi o'ntalik", c[0:10], "O'rtasidagi o'ntalik", c[265:275], "Oxirgi o'ntalik", c[-11:-1])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["palov", "sho'rva", "mastava", "pizza", "hot-dog"]

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("mastava")
del nonushta[1]
nonushta.append("quymoq")
nonushta.insert(1, "qahva")

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print("Nonushtadagi taomlar: ", nonushta)
print("Kechki ovqat uchun taomlar: " , taomlar)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta = list(nonushta)
nonushta.insert(0,'qaymoq va non')
nonushta = tuple(nonushta)
print(nonushta)
