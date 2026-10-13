from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base

class Payment_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)



    #locators
    button_finish = '//button[@id="finish"]'





    #Getters
    def get_button_finish(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_finish)))




    #Actions
    def click_button_finish(self):
        self.get_button_finish().click()
        print("Click button finish")


    #Method

    def payment(self):
        self.get_current_url()
        self.click_button_finish()
