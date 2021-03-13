
questions = [

    "Q1= Python da listede kaç elaman olduğunu, karakter sayısını vb. veren komut? ",
    "Q2= Ekrana yazı yazdırılmasını sağlayan komut? ",
    "Q3= Sayısal bir ifadeyi Metinsel bir ifadeye çevirmek için hangi komutu kullanırız? ",
    "Q4= Kullanıcıdan veri alınması gereken durumlarda kullanılması gereken komut? ",
    "Q5= Python’da bir nesneyi kopyalayabilir miyiz? (E/H) ",
    "Q6= Python yorumlanan bir programlama dili midir?(E/H) ",
    "Q7= Pythonda belirli aralıktaki sayıları kullanmak için hangi fonksiyonu kullanırız? ",
    "Q8= Öğeleri listenin istediğimiz bir konumuna yerleştirmek için kullandığımız method? ",
    "Q9= Bir değerin, değişkenin türünü bulmamıza yarayan komut? ",
    "Q10 list1 = ['banana', 'apple', 'orange'] \n  print (list1[1])? "
]

answers=[
    "len()", "print()", "str()", "input()","e", "e", "range()", "insert()","type()", "apple"
]

count=0

for i in range(10):
   s1 = input(questions[i])
   if s1.lower() == answers[i]:
       count= count+10


if count>50:
    print("Puanınız: {}, Başarılı :) ".format(count))
else:
    print("Puanınız: {}, Başarısız :( ".format(count))