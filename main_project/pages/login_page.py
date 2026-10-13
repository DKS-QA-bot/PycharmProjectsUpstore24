import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base

class Login_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""


    url = 'https://upstore24.ru/'


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)



    #locators
    user_icon = '(//span[@data-icon="user"])[1]'
    user_email = '//*[@id="input-15"]'
    button_continue = '//button[@type="button"]'
    password = '//input[@type="password"]'
    button_enter = '//button[normalize-space()="Войти"]'




    #Getters
    def get_button_enter(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))
    def get_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_user_icon(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_icon)))

    def get_user_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_button_continue(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.button_continue)))


    #Actions
    def click_button_enter(self):
        self.get_button_enter().click()
        print('click enter')

    def click_user_icon(self):
        self.get_user_icon().click()
        print("Click icon user")


    def input_user_email(self,email):
        self.get_user_email().send_keys(email)
        print("Input email")

    def click_go(self):
        self.get_button_continue().click()
        print('click go')

    def input_password(self,password):
        self.get_password().send_keys(password)
        print("Input password")


    #Method

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_user_icon()
        self.input_user_email('dmitrij.kryukov.1986@list.ru')
        self.click_go()
        self.input_password('321123')
        self.click_button_enter()
        time.sleep(5)