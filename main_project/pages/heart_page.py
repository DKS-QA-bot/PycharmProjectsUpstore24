from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base

class Client_information_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""





    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)



    #locators
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    button_continue = '//input[@data-test="continue"]'


    #Getters
    def get_first_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.postal_code)))

    def get_button_continue(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,self.button_continue)))


    #Actions
    def input_first_name(self,first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")


    def input_last_name(self,last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")


    def input_postal_code(self,postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click continue button")



    #Method
    def input_information(self):

        self.get_current_url()
        self.input_first_name('Ivan')
        self.input_last_name('Ivanov')
        self.input_postal_code('1234')
        self.click_button_continue()