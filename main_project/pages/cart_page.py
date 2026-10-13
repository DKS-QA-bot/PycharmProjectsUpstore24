from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base

class Cart_page(Base):
    """ Класс содержащий локаторы и методы для страницы Магазина"""



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)



    #locators
    button_logout = '//button[@id="checkout"]'


    #Getters
    def get_button_logout(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_logout)))



    #Actions
    def click_button_logout(self):
        self.get_button_logout().click()
        print("Click button logout")


    #Method
    def product_confirmation(self):
        self.get_current_url()
        self.click_button_logout()