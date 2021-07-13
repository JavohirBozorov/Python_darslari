# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 07:13:36 2021

11_darsIf_elif_else

@author: Javohir Bozorov 
"""

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    print('Sizga kirish bepul.')
#elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
#else:
#    print('Sizga kirish 10000 so\'m') 

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    price = 0
#elif yosh<=12:
#    price = 5000
#else:
 #   price = 10000
#    
#print(f"Sizga kirish {price} so'm")

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4: # yosh bolalarga bepul
#    price = 0
#elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#    price = 5000
#elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#    price = 10000
#else: # qariyalarga esa 8000 so'm
#   price = 8000
#print(f"Sizga kirish {price} so'm")

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    price = 0
#elif yosh<=12:
#    price = 5000
#elif yosh<65:
#    price = 10000
#elif yosh>=65:
#    price = 8000    
#print(f"Sizga kirish {price} so'm")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#    print("Uyda dam olamiz!")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("Cho'milgani ketdik!")
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#    print("Uyda dam olamiz!")

#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz
#
#print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000   
#print(f"Jami {narh} so'm")

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
#    print('Buyurtma qabul qilindi.')
#else:
#    print('Afsuski bizda bunday ovqat yo\'q')

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else: # agar ro'yxat bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son 
#kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni 
#chiqaring.

#son = int(input("Biror juft sonni kiriting: "))
#if son/2 == int() :
#    print("Rahmat")
#else:
#    print("Bu son juft emas")

#son = float(input("Juft son kiriting: "))
#if son%2:
#    print('Bu son juft emas.')
#else:
#    print("Rahmat!")



#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
 #quyidagicha chiqaring:
#    Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#    Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#    Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

#narx = int(input("Yoshingizni kiriting: "))
#if narx <= 4 or narx >= 60:
#    print("Sizga chipta bepul")
#elif narx <=18:
#    print("Chipta narxi 10 000 so'm")
#else:
#    print("Chipta narxi 20 000 so'm")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
#ularning teng yoki katta/kichikligi haqida xabarni chiqaring

#son1 = float(input("Birinchi sonn kiriting: "))
#son2 = float(input("Ikkinchi sonn kiriting: "))
#if son1 > son2:
#    print("Birinchi son katta")
#elif son1 == son2:
#    print("Sonlar teng ")
#else:
#    print("Ikkinchi son katta")
    
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
#5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar 
#ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot 
#do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
    
#mahsulotlar = ["kiob", "daftar", "kundalik", "bloknot", "umumiy daftar", "ruchka", "qalam", "marker", "list", "o'chirgich"]   
#savat = []
#savat.append(input("Savatingizga 1-mahsulotni kiriting: "))
#savat.append(input("Savatingizga 2-mahsulotni kiriting: "))
#savat.append(input("Savatingizga 3-mahsulotni kiriting: "))
#savat.append(input("Savatingizga 4-mahsulotni kiriting: "))
#savat.append(input("Savatingizga 5-mahsulotni kiriting: "))
#for mahsulot in savat:
#    if mahsulot.lower() in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else :
#       print(f"Kechirasiz {mahsulot} do'konimizda yo'q")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
 #              'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#for mahsulot in savat:#savat = []
#for n in range(5):

#    if mahsulot in mahsulotlar:
#        print(f"Savatingizdagi {mahsulot} bor ")
#    else:
#       print(f"Do'konimizda {mahsulot} yo'q ")


#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot 
#kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, 
#bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
#degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan 
#barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi 
#mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
#bor_mahsulotlar = []
#mavjud_emas = []
#
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)


#if mavjud_emas:#
#    print("\nDo'konimizda quidagi mahsulotlar yo'q: ")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("\nSiz so'ragan barcha mahsulotlar do'konimizda bor")

#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan 
#yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar 
#degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud 
#bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!"
# xabarini chiqaring.

#foydalanuvchilar = ["anvar", "baxrom", "doston", "elbek", "farruh", "javohir"]
#login = input("Yangi login tanlang: ")

#if login in foydalanuvchilar:
#    print("Login band, yangi login tanlang")
#else:
#    print("Xush kelibsiz foydalanuvchi!")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
#sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
#konsolga chiqaring.

#x = int(input("Biror butun sonni kiriting: "))

#if x%2==0:
 #   print(f"{x} soni 2ga qoldiqsiz bo'linadi")
#if x % 3 == 0:
#    print(f"{x} soni 3ga qoldiqsiz bo'linadi")
#if x%4 == 0:
#    print(f"{x} soni 4ga qoldiqsiz bo'linadi")
#if x%5 == 0:
#    print(f"{x} soni 5ga qoldiqsiz bo'linadi")
#if x%6 == 0:
#    print(f"{x} soni 6ga qoldiqsiz bo'linadi") 
#if x%7 == 0:
#    print(f"{x} soni 7ga qoldiqsiz bo'linadi")
#if x%8 == 0:
#    print(f"{x} soni 8ga qoldiqsiz bo'linadi")
#if x%9 == 0:
#    print(f"{x} soni 9ga qoldiqsiz bo'linadi")
#else:
#    print("Siz kiritgan son tub ekan")

son = int(input("istalgan son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n}ga qoldiqsiz bo'linadi")








