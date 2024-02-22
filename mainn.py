import ogrenci
import ogretmen

a=int(input("Öğrenci bilgileri için 1 e basınız \nÖgretmen bilgileri için 2 ye basınız.\n "))
if a==1 :
    kac = int(input("Kaç öğrenci bilgisi girilecek: "))
    ogrenciBilgisi = []
    i = 1

    while i <= kac:
        ogrenciObj = ogrenci.OgrenciClass()
        ogrenciObj.ogrenciBilgileri()
        ogrenciBilgisi.append(ogrenciObj.ogrenciBilgi())
        i += 1

    print(ogrenciBilgisi)
else:
    o_kac = int(input("Kaç öğretmen bilgisi girilecek: "))
    ogretmenBilgisi = []
    i = 1

    while i <= o_kac:
        ogretmenObj = ogretmen.OgretmenClass()
        ogretmenObj.ogretmenBilgileri()
        ogretmenBilgisi.append(ogretmenObj.ogretmenBilgi())
        i += 1

    print(ogretmenBilgisi)

