#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

eleman = int(input("Lütfen 20 veya 20'den buyuk bir eleman sayisi giriniz: "))

fibonacci = [1, 1]  # İlk iki elemanı 1 olan Fibonacci serisi

while len(fibonacci) < eleman:  # En az 20 elemanlı olana kadar devam et
    next_fib = fibonacci[-1] + fibonacci[-2]  # Son iki elemanın toplamı
    fibonacci.append(next_fib)  # Yeni Fibonacci sayısını listeye ekle

print(fibonacci)

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = int(input("Lütfen bir sayi giriniz: "))

toplam = 0

for x in range(1, sayi + 1):
    if sayi % x == 0: #pozitif bolenleri bulma
        toplam += x

if(sayi == toplam / 2):
    print("Mukemmel sayidir.")
else:
    print("Mukemmel sayi degildir.")

#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

a = int(input("Birinci Sayıyı Giriniz : "))
b = int(input("İkinci Sayıyı Giriniz : "))
 
if (a > b):
    kucuksayi = b
else:
    kucuksayi = a
for i in range(1,kucuksayi+1):
    if (a  % i==0) and (b %i ==0):
        ebob = i
        ekok = (a*b)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi = int(input("Lütfen bir sayi giriniz: "))
if sayi > 1:
    for i in range (2,sayi):
       if (sayi % i) == 0: #tam bolen
           print(sayi," Asal Sayi Değildir.")
           break
    else:
       print(sayi," Asal Sayidir.")
else:
   print(sayi," Asal Sayi Değildir.")       

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
   
sayi = int(input("Lütfen Bir sayi giriniz: "))
bölen = 2
for i in range (1,sayi):
    if(sayi % bölen == 0):
        print(bölen)
        sayi /= bölen
    else:
        bölen += 1