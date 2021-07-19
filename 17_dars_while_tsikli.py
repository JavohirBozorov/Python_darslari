# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:28:03 2021

17_dars_while_tsikli

@author: Javohir bozorov
"""

#ism = input("Ismingiz nima? ")
#print(f'Salom, {ism.title()}')

#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)

#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh) # yosh ni butun songa o'tkazamiz
#height = input("Bo'yingiz necha metr? ")
#height = float(height) # bo'yni o'nlik songa o'tkazamiz

#while
#son = 1 # son ga 1 qiymatini beramiz
#while son<=5: # toki son 5 dan kichik yoki teng ekan...
#    print(son, end=' ') # son ni konsolga chiqaramiz,
#    son = son+1 # songa 1 qo'shamiz.

#while and input
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl
 #   qiymat = input(savol)
  #  if qiymat == 'exit':
   #     break # tsiklni to'xtatish
    #else:
     #   print(float(qiymat)**2)
    
#sonlar = list(range(1,11))
#for son in sonlar: 
#   if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")

#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)

# infinite loop
#son = 0
#while son<10:
#    if son%2!=0:
#        continue
#    else:
#        print(son)

#uyga_vazifalarim
#1.Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi 
 #stop so'zini yozishi bilan dasturni to'xtating

#print("Yoqtirgan kitoblaringiz ro'yxatini chiqaruvchi dastur.")
#savol = "Yoqtirgan kitobingizni kiriting "
#savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "
#qiymat = ''
#while qiymat != 'stop':
#    qiymat = input(savol)
#    if qiymat != 'stop':
#       print(qiymat.capitalize())

#2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 
#2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga 
#bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
#chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
#to'xtasin (ikkita shartni ham tekshiring).
#Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

#savol = "Yoshingizni kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
 #   qiymat = input(savol)
  #  if qiymat == 'exit':
   #     ishora = False
    #elif int(qiymat)<=7:
     #   print("Chiptangiz narxi 2 000 so'm")
#    elif int(qiymat)<=18:
 #       print("Chiptangiz narxi 3 000 so'm")
  #  elif int(qiymat)<=65:
   #     print("Chiptangiz narxi 10 000 so'm")
    #else:
     #   print("Chiptangiz bepul")

#savol = "Yoshingizni kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#while True:
 #   qiymat = input(savol)
  #  if qiymat == 'exit':
   #     break
    #elif int(qiymat) <= 7:
#     #   print("Chiptangiz narxi 2 000 so'm")
 #   elif int(qiymat)<=18:
  #      print("Chiptangiz narxi 3 000 so'm")
   # elif int(qiymat)<=65:
    #    print("Chiptangiz narxi 10 000 so'm")
    #elif int(qiymat)>65:
     #   print("Chiptangiz bepul")
    
#3.Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda
 #tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?

#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
 #   qiymat = input(savol)
  #  if qiymat=='exit':
   #     break
    #elif float(qiymat)<0:
     #   continue
   # else:
    #    ildiz = float(qiymat)**(0.5)
     #   print(f"{qiymat} ning ildizi {ildiz} ga teng")


























