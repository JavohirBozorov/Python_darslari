# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:34:36 2021

20_dars_qiynmat_qaytaruvchi_funksiya

@author: Javohir Bozorov
"""

#def toliq_ism_yasa(ism, familiya):
#    """Toliq isma qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
#talaba1 = toliq_ism_yasa('olim','hakimov')
#talaba2 = toliq_ism_yasa('hakim','olimov')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#    """Toliq isma qaytaruvchi funksiya"""
#    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()
#talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
#talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rang':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narh':narhi}
#    return avto

#avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
#avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
#avtolar = [avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
#    if avto['narh']:
#        narh = avto['narh']
#    else:
#        narh = "Noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
#avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting",end='')
#    kompaniya=input("Ishlab chiqaruvchi: ")
#    model=input("Modeli: ")
#    rangi=input("Rangi: ")
#    korobka=input("Korobka: ")
#    yili=input("Ishlab chiqarilgan yili: ")
#    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
#    javob = input("Yana avto qo'shasizmi? (yes/no): ")
#    if javob=='no':
#        break

#UYGA_VAZIFALAR

#kichik uy vazifasi qadamni ham qo'shish
#def oraliq(min,max,qadam=""): 
#    sonlar = [] # bo'sh ro'yxat
#    while min<max:
#        sonlar.append(min)
#        if qadam:
#            min += qadam
#        else:
#            min += 1
#    return sonlar
#print(oraliq(0,10))
#print(oraliq(10,21,5))

#1.Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili 
 #va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
  #Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni 
   #ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
#2.Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan
 #ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring

#def foydalanuvchi(ismi, familiyasi, t_yili, t_joyi, e_manzili='' , tel_raqami=None):
#    malumot = {'ism':ismi,
#               'familiya':familiyasi,
#               't_yil':t_yili,
#               't_joy':t_joyi,
#               'e_manzil':e_manzili,
#               'tel_raqam':tel_raqami
#              }
#    return malumot
#
#print("\nFoydalanuvchi malumotlarini shakillantiramiz:")
#malumotlar = []
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting", end='')
#    ismi = input("Ismingizni kiriting: ")
#    familiyasi = input("Familiyangizni kiriting: ")
#    t_yili = input("Tug'ilgan yilingizni kiriting: ")
#    t_joyi = input("Tug'ilgan joyingizni kiriting: ")
#    e_manzili = input("Elektron pochta manzilingizni kiriting: ")
#    tel_raqami = input("Telefon raqamingizni kiriting: ")
#    
#    malumotlar.append(foydalanuvchi(ismi, familiyasi, t_yili, t_joyi, e_manzili, tel_raqami))
#    
#    javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
#    if javob=='no':
#        break 
#print("Malumotlar: ")  
#for malumot in malumotlar:
#    print(f"{malumot['ism'].title()} {malumot['familiya'].title()} {malumot['t_yil']}-yil "
#          f"{malumot['t_joy'].title()}da tug'ilgan. E-maili:{malumot['e_manzil']} "
#          f"Tel:{malumot['tel_raqam']}")
               
#3.Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def max_chiqar(x,y,z):
    '''sonlarning maximumini chiqaruvchi dastur'''
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max
print(max_chiqar(13,-314,5))

#4.Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
 #perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
def aylanani_hisobla(r,pi=3.14):
    '''Radiusni olib aylananing parametrlarini chiqaruvchi dastur'''
    parametr={'radius':r,
              'diametr':2*r,
              'peremetr':2*r*pi,
              'yuzi':(r**2)*pi
              }
    return parametr
print(aylanani_hisobla(3))

#5.Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub 
 #sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

print(tub_sonlar_top(15,45))

#6.Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-
#ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi 
#o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
#Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb 
#olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))
    
    












