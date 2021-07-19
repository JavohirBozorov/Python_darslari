# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 06:59:37 2021

16_dars_Nesting

@author: Javohir Bozorov
"""


car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }


#car = car0
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")

#car = car1
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")

#car = car2
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")  


cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang, "
#          f"{car['yil']}-yil, {car['narh']}$")


#print(cars[0])

#print(cars[0]['model'])

#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")


#malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
#for n in range(10):
#    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#        'model':'malibu',
 #       'rang':None, # rangi noaniq
  #      'yil':2020,
   #     'narh':None, # narhi belgilanmagan
    #    'km':0,
     #   'korobka':'avto'
      #  }
#    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz

#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
#for malibu in malibus:
#    if malibu['korobka']=='avto':
#        malibu['narh']=40000
#    else:
#        malibu['narh']=35000
#for malibu in malibus:
#    print(malibu)


dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(til.upper())

#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
  #  for til in tillar:
   #     print(f'{til.upper()} ', end='')


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

#for ism, info in hamkasblar.items():
 #   print(f"\n{ism.title()} {info['familiya'].title()}, "
  #        f"{info['tyil']}-yilda tug'ilgan. "
   #       f"Ma'lumoti: {info['malumot']}. \n"
    #      "Quyidagi dasturlash tillarini biladi:")
    #for til in info['tillar']:
     #   print(til.upper())


#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
 #ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
   #va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

person1 = { 'ism':'alisher navoiy',
           'tyil':1441,
           'vafot':1501,
           'yaratgan':"hamsa",
           'lavozimi':"bosh vazir",
           'asarlari':["hayrat-ul abror", "sabbai sayyor", 'saddi iskandariy', 'farhod va shirin', 'layli va majnun']
         }
person2 = { 'ism':'stive jobs',
          'tyil':1943,
          'vafot':2010,
          'yaratgan':'apple computer',
          'lavozimi':'kompaniya bosh derktori',
          'asarlari':["iphone1",'iphone2','iphone3']
        }
person3 = {  'ism':'bill gats',
            'tyil':1943,
            'vafot':"hali hayot",
            'yaratgan':'windows',
            'lavozimi':'kompaniya derektori',
            'asarlari':['windows 1.0', 'windows 2.0']
           }
person4 = {      'ism':'ozodbek nazarbekov',
                'tyil':1974,
                'vafot':"hali hayot",
                'yaratgan':'ko\'plab qo\'shiqlar',
                "lavozimi":'madaniyat vaziri',
                'asarlari':['atirgulim', 'qizg\'aldog\'im', 'jig\'i-jig\'i']
              }
people = [person1, person2, person3, person4]
#for person in people:
#    print(f"{person['ism'].title()} {person['tyil']}da tug\'ilgan "
#          f'{person["yaratgan"].title()}ni yaratgan '
#          f'{person["lavozimi"]} bo\'lib ishlagan')

#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham 
 #qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga
  #chiqaring
  
#for shaxs in people:
 #   ism = shaxs["ism"]
  #  asarlari = shaxs["asarlari"]
   # print(f"{ism.title()}ning asarlari:" )
    #for asar in asarlari:
     #   print(asar)

#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
 #Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
  #lug'artga saqlang. Natijani konsolga chiqaring

filmlar = { "ali":['Titanik', 'Mahallada duv-duv gap', 'Chinor ostidagi duel'],
            "vali":['Forsaj', 'Puaro', 'Sherlok Holms'],
            "hasan":['Yulduzlar jangi', 'Capitan Amerika', 'Avtobotlar']
           } 

#for key,filmlar in filmlar.items():
 #   print(f"\n{key.title()}ning sevimli filmlari: ", end=' ')
  #  for film in filmlar:
   #     print(film, end=' ')

#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
#ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni 
#konsolga chiqaring.

davlatlar = { 
       "o'zbekiston":{'poytaxt':'toshkent',
                      'maydoni':448900,
                      'aholisi':"33 mln",
                      'pul birligi':"so'm"
                      },
               "baa":{'poytaxt':'abu dabi',
                      'maydoni':82880,
                      'aholisi':"5 mln",
                      'pul birligi':'dirham'
                      },
         "germaniya":{'poytaxt':'berlin',
                      'maydoni':357021,
                      'aholisi':"83 mln",
                      'pul birligi':'yevro'
                       },
           "angliya":{'poytaxt':'london',
                      'maydoni':130279,
                      'aholisi':"56 mln",
                      'pul birligi':'funt'
                      },
          "ispaniya":{'poytaxt':'madrid',
                      'maydoni':505990,
                      'aholisi':"47.5 mln",
                      'pul birligi':'yevro'}
             }

#for davlat, info in davlatlar.items():
#    if davlat.lower() == "baa":
 #       davlat=davlat.upper()
  #  else:
   #     davlat=davlat.capitalize()
    #    
#    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()} ",
 #         f"\nMaydoni: {info['maydoni']} km kv",
  #        f"\nAholisi: {info['aholisi']} kishi",
   #       f'\nPul birligi: {info["pul birligi"]}')

#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
#lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan 
#xabarni chiqaring.

mamlakat = input("Mamlakat nomini kiriting: ").lower()
        
if mamlakat in davlatlar:
    info=davlatlar[mamlakat]
    if mamlakat.lower() == "baa":
        mamlakat=mamlakat.upper()
    else:
        mamlakat=mamlakat.capitalize()
    print(f"\n{mamlakat}ning poytaxti {info['poytaxt'].title()} ",
          f"\nMaydoni: {info['maydoni']} km kv",
          f"\nAholisi: {info['aholisi']} kishi",
          f'\nPul birligi: {info["pul birligi"]}')
else:    
    print("Bizda bu davlat haqida ma'lumot yo'q")





















