# Test Caseler;

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class test_Sauce:
    def onkosul (self):
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        return driver #driveri döndür.
    
    def bosgiris (self):
        driver= self.onkosul() #driveri çağırdık.
        loginButton=driver.find_element(By.ID,"login-button") # find elemnt: elementi bul, by: neyinden 
        loginButton.click()
        erorMesaji=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3") #eror mesajını bulduk.
        testResult = erorMesaji.text ==  "Epic sadface: Username is required" #eror msajının verilene eşitmi bakalıcak
        print(f"Test Sonucu:{testResult}") 
        
    
    def sifrebos (self):
        driver= self.onkosul()
        kullaniciAdi=driver.find_element(By.ID,"user-name")
        kullaniciAdi.send_keys("gnc") #kullanici adına gnc yaz
        loginButton=driver.find_element(By.ID,"login-button") # find elemnt: elementi bul, by: neyinden 
        loginButton.click() 
        erorMesaji2=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3") #eror mesajını bulduk.
        testResult2 = erorMesaji2.text ==  "Epic sadface: Password is required" #eror msajının verilene eşitmi bakalıcak
        print(f"Test Sonucu:{testResult2}")

    def yasakliKullanici (self):
        driver= self.onkosul()
        kullaniciAdi=driver.find_element(By.ID,"user-name")
        kullaniciAdi.send_keys("locked_out_user")
        sifre=driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        erorMesaji3=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult3=erorMesaji3.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu : {testResult3}")
        

testClass=test_Sauce() # classı değişkene atıyoruz.
testClass.onkosul() # değişkenle fonksiyonu çalıştırıyoruz.
testClass.bosgiris() #değişkenle bosgirişi çalıştır.
testClass.sifrebos() #değişkenle bosgirişi çalıştır.
testClass.yasakliKullanici()
