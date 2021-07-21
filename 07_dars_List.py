# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:28:11 2021

06_dars_Listlar

@author: Javohir Bozorov
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
#print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
#print(narhlar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
#print(mevalar)

cars = [] # bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
#print(cars)

cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
#print(cars)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
#print(mevalar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
#print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
#print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
#print("Men " + mahsulot + " sotib oldim")
#print("Olinmagan mahsulotlar: ", bozorlik)

#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#print("Birinchi meva: ", mevalar[0])
#print("Ikkinchi meva: ", mevalar[1])

#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
#print("Birinchi meva: ", mevalar[0].title())
#print("Ikkinchi meva: ", mevalar[1].upper())

narhlar = [12000, 18000, 10900, 22000]
#print(narhlar[2] + narhlar[3])

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

names = ['rustam' , 'anvar', "zubaydulla", "suxrob"]

#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

#salom name, bugun choyxona bormi?
#print("Salom " + names[0].title() + ', bugun choyxona bormi?')
#print(names[2].capitalize() + ', choyxonaga boramizmi?')

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

sonlar = []
sonlar.append(2390)
sonlar.insert(0, 8097)
sonlar.append(4563)
#print(sonlar[2] // sonlar[0])
#print(sonlar[1] % sonlar[0])
#print(sonlar)
sonlar[-1] = 6742
sonlar[1] = sonlar[1] + 70_000
#print(sonlar)

#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz
#eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

t_shaxslar = ["amir temur", "alisher navoiy", 'mirzo ulug\'bek']
z_shaxslar = ["bill gates", "jef bezos", 'mark sucerberg', 'jeck ma']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib 
#(.pop()), quyidagi ko'rinishda chiqaring:

shaxs1 = t_shaxslar.pop(1)
shaxs2 = z_shaxslar.pop(-2)
#print('Men tarixiy shaxslardan ' + shaxs1.title() + ' bilan, zamonaviy shaxslardan esa ' + shaxs2.title() + " bilan suxbat qilishni istar edim")

#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

friends = []
friends.append('shahzod')
friends.append("dilshod")
friends.append('sanjar')
friends.append('halim')
friends.append('doston')
#print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.  

friends.remove("doston")

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.insert(0, "jasur")
friends.insert(6, 'ulug\'bek')
friends.insert(4, 'baxrom')
#print(friends)

#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(4))
print(mehmonlar)







