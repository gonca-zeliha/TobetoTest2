class OgrenciClass :
    isim=""
    soyisim=""
    bolum=""
    okulNo=0
    bolum=""
    ders=""
    
    def ogrenciBilgi (self):
        return " İsim: {} Soyisim: {} Okul No: {} bolum: {} Ders: {}".format(self.isim,self.soyisim,self.bolum,self.bolum,self.okulNo,self.ders)
    def ogrenciBilgileri(self):
        self.isim = input("Lütfen öğrenci adını giriniz: ")
        self.soyisim = input("Lütfen öğrenci soyadını giriniz: ")
        self.okulNo = input("Lütfen öğrenci numarasını giriniz: ")
        self.bolum = input("Lütfen öğrenci bölümünü giriniz: ")
        self.ders = input("Lütfen öğrenci dersini giriniz: ")
        return self