# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait #bekleme süresini ayarlar
# from selenium.webdriver.support import expected_conditions as ec  #bekleme şartını sağlar
# from selenium.webdriver.common.action_chains import ActionChains
# class Test_Sauce:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.saucedemo.com/")
#     def test_invalid_login(self): # Bu metod, geçersiz bir giriş yapmaya çalışarak kullanıcının karşılaşacağı davranışı test eder..
#         WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #en fazla 5 sn oalcak şekilde user-name id'li elementin görünmesini bekle
#         userNameInput= self.driver.find_element(By.ID,"user-name")
#         WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
#         passwordInput = self.driver.find_element(By.ID,"password")
#         userNameInput.send_keys("1")
#         passwordInput.send_keys("1")
#         userNameInput= self.driver.find_element(By.ID,"user-name")
#         passwordInput = self.driver.find_element(By.ID,"password")
#         loginButon = self.driver.find_element(By.ID,"login-button") #giriş yap tılattık
#         loginButon.click()
#         erorMesage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
#         testResult = erorMesage.text =="Epic sadface: Username and password do not match any user in this service"
#         print(f"TEST SONUCU :{testResult}")

#     def test_valid_login(self):
#         self.driver.get("https://www.saucedemo.com/")
#         WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #en fazla 5 sn oalcak şekilde user-name id'li elementin görünmesini bekle
#         userNameInput= self.driver.find_element(By.ID,"user-name")
#         WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
#         passwordInput = self.driver.find_element(By.ID,"password")
#         actions= ActionChains(self.driver) # farklı eylemleri bir araya getirmemize ve ardından bunları gerçekleştirmemize olanak tanır.
#         actions.send_keys_to_element(userNameInput,"standard_user") # kullanıcı adı alanına "standard_user" metnini girmemizi sağlar
#         actions.send_keys_to_element(passwordInput,"secret_sauce") # şifre alanına "secret_sauce" metnini girmemizi sağlar
#         actions.perform() #Bu yöntem, önceki adımlarda tanımladığımız eylemleri gerçekleştirir. 
#         loginButon = self.driver.find_element(By.ID,"login-button") #giriş yap tılattık
#         loginButon.click()
# 

#         self.driver.execute_async_script("window.scrollTo(0,500)") #js çağırarak 0 500 kooridinatlarına gitti
        
# testClass= Test_Sauce() # sınıfından bir örnek oluşturur.
# testClass.test_invalid_login() 
# testClass.test_valid_login()

#acition cahains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.execute_async_script("window.scrollTo(0,500)")

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()