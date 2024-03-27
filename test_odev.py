from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ce
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_Demo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
       
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_userNameisEmpty(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton() 
        
        nameErrorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-emptyusername-login-{username}-{password}.png")
        assert nameErrorMessage.text == ("Epic sadface: Username is required")

    @pytest.mark.parametrize("username,password",[("asdfg","")])
    def test_passwordisEmpty(self,username,password):
            
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()

        passwordErrorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-emptypassword-login-{username}-{password}.png")
        assert passwordErrorMessage.text == ("Epic sadface: Password is required")

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_senario3(self,username,password):
            
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()

        senario3ErrorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-senario3-login-{username}-{password}.png")
        assert senario3ErrorMessage.text == ("Epic sadface: Sorry, this user has been locked out.")
        
    @pytest.mark.parametrize("username,password",[("","")])
    def test_senario4(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()
        
        errorButton = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        self.driver.save_screenshot(f"{self.folderPath}/test-senario4_1-login-{username}-{password}.png")
        errorButton.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-senario4_2-login-{username}-{password}.png")
            
    
   
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_senario5(self,username,password):

            
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()

        self.driver.get("https://www.saucedemo.com/inventory.html")
    
        numberOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-senario5-login-{username}-{password}.png")
        assert 6 == len(numberOfProducts)

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])    
    def test_multiLogin(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()

        self.driver.save_screenshot(f"{self.folderPath}/test-multiplelogin-{username}-{password}.png")
        numberOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert 6 == len(numberOfProducts)
        

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_addtoCartandDelete(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()
        addToCartButton = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCartButton.click()

        self.driver.get("https://www.saucedemo.com/cart.html")
        
        addToCartButton = self.driver.find_element(By.ID,"remove-sauce-labs-backpack")
        addToCartButton.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")

        self.driver.save_screenshot(f"{self.folderPath}/test-addtoCartandDeletetoCart-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_problemUser(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
          
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.clickLoginButton()

        dogImage = self.driver.find_element(By.CLASS_NAME,"inventory_item_img")
        dogImage.click()

        wrongProductDescription = self.driver.find_element(By.CLASS_NAME,"inventory_details_desc.large_size")
        assert wrongProductDescription.text != "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        
        self.driver.save_screenshot(f"{self.folderPath}/test-problemuser-login-{username}-{password}.png")

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ce.visibility_of_element_located(locator))

    def clickLoginButton(self):
        loginButton = self.driver.find_element(By.ID,"login-button")    
        loginButton.click() 



           

            