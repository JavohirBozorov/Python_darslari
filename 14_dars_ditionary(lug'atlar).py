# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 08:18:36 2021

14_dars_Lug'at(Dictionary)

@author: Javohir_Bozorov
"""

car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['model'])

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba_0['ism'].title()},\
 #{talaba_0['t_yil']}-yilda tug'ilgan,\
 #{talaba_0['yosh']} yoshda")
 
talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 

#print(talaba_0)

talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
#print(talaba_0)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
#print(telefonlar)

#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")

#phone = telefonlar['hasan']
#print(f"Hasanning telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)

phone = telefonlar.get('hasan')
#print(phone)

#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
 #haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va 
  #hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi
   # Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ism':'nayim', 
        't_yil':'1965', 
        't_shahri':'qarshi', 
        'manzil':'niyozmudin qishlog\'i'}
#print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, {otam['t_shahri'].title()} tumani {otam['manzil'].capitalize()}da tug'ilgan")

onam = {'ism':'dilorom', 
        't_yil':'1970', 
        't_shahri':'qarshi', 
        'manzil':'niyozmudin qishlog\'i'}
#print(f"Onamning ismi {onam['ism'].title()}, {onam['t_yil']}-yilda, {onam['t_shahri'].title()} tumani {onam['manzil'].capitalize()}da tug'ilgan")

#Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 
 #5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga
  #chiqaring: Alining sevimli taomi osh

taomlar = {'otam':"sho'rva", 
           'onam':'manti', 
           'nurbek':'shashlik', 
           'dilfuza':'qozonkabob', 
           'javohir':'moshkichri'}
#print(f"Otamning sevimli taomi {taomlar['otam']}")
#print(f"Onamning sevimli taomi {taomlar['onam']}")
#print(f"Nurbekning sevimli taomi {taomlar['nurbek']}")
#print(f"Dilfuzaning sevimli taomi {taomlar['dilfuza']}")
#print(f"Javohirning sevimli taomi {taomlar['javohir']}")

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
 #(atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har
  #birining qisqacha tarjimasini yozing.

lugat = {'int':'butun son',
         'float':'o\'nlik sonlar', 
         'str':'matn', 
         'list':'ro\'yxat', 
         'tuples':"o'zgarmas ro'yxat", 
         'for':'uchun', 
         'if':'agar', 
         "else":'aks holda'}
#print(lugat)
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi
 #lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z 
  #mavjud emas" degan xabarni chiqaring.

#kalit = input("Biror so'z kiriting: ").lower()  
#kalit = lugat.get(kalit,'Bunday so\'z mavjud emas')
#print(kalit)
  
#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga 
 #tushunarli ko'rinishda chiqaring
 
suz = input("Biror so'zni kiriting: ").lower()
if suz in lugat:
    print({lugat[suz]})
else:
    print("Bunday so'z mavjud emas")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

#kalit = input("Kalit so'z kiriting:").lower()
#print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

#kalit = input("Kalit so'z kiriting:").lower()
#tarjima = python_izohli_lugati.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    

