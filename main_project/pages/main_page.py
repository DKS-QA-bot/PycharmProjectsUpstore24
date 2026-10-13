import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base

class Main_page(Base):
    """ Класс содержащий локаторы и методы для главной страницы"""



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)
        self.sleep = 1.5


    #locators
    hamburger = '//*[@class="hamburger__title"]'
    select_pc = '(//*[@data-nav-item="18771934"])[2]'
    select_products_pc = '(//*[normalize-space()="Apple Mac Studio 2026"])[1]'
    cart = '//*[@data-test="shopping-cart-link"]'
    burger = '//button[@id="react-burger-menu-btn"]'
    button_about = '//a[@id="about_sidebar_link"]'
    url = 'https://upstore24.ru/'
    price_min = '(//*[@class="noUi-touch-area"])[1]'
    price_max = '(//*[@class="noUi-touch-area"])[2]'
    checkbox_apple = '//*[@for="filter-item-109849115"]'
    checkbox_orange = '//*[@for="filter-item-109849221"]'
    filter_count = '//*[@data-filter-submit]'
    filter_ram = '//*[@for="filter-item-109849128"]'
    platform = '//*[@for="filter-item-109849269"]'
    processor = '//*[@for="filter-item-247481722"]'





    #Getters
    def get_platform(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.platform)))

    def get_filter_ram(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_ram)))


    def get_filter_count(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_count)))

    def get_checkbox_orange(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_orange)))


    def get_checkbox_apple(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_apple)))


    def get_price_max(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.price_max)))


    def get_price_min(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.price_min)))


    """retun hamburger menu"""
    def get_select_hamburger(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hamburger)))


    def get_select_pc(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_pc)))


    def get_select_product_pc(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_products_pc)))


    def get_cart(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.burger)))

    def get_button_about(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_about)))


    #Actions
    def click_platform(self):
        try:
            self.get_platform().click()
            print("Click platform")
        except Exception as e:
            self.get_platform().click()
            print("Click platform")
    def move_to_window(self):
        try:
            self.driver.execute_script("window.scrollTo(0,700)")
            print('move')
        except Exception as e:
            self.driver.execute_script("window.scrollTo(0,700)")
            print('move1')

    def click_filter_ram(self):
        try:
            self.get_filter_ram().click()
            print("Click filter ram")
        except Exception as e:
            self.get_filter_ram().click()

    def click_filter_count(self):
        try:
            self.get_filter_count().click()
            print("Click filter count")
        except Exception as e:
            self.get_filter_count().click()


    def click_to_orange(self):
        # self.move_to_orange()
        try:
            self.get_checkbox_orange().click()
            print("Click orange")
        except Exception as e:
            self.get_checkbox_orange().click()
            print("Click orange")


    def click_select_hamburger(self):
        try:
            self.get_select_hamburger().click()
            print("Click hamburger")
        except Exception as e:
            self.get_select_hamburger().click()
            print("Click hamburger")

    def click_select_pc(self):
        try:
            self.get_select_pc().click()
            print("Click select product")
        except Exception as e:
            self.get_select_pc().click()
            print("Click select product")

    def click_select_product_pc(self):
        try:
            self.get_select_product_pc().click()
            print("Click select product")
        except Exception as e:
            self.get_select_product_pc().click()
            print("Click select product")

    def select_price_min(self):
        self.actions.click_and_hold(self.get_price_min()).move_by_offset(50,0).release().perform()

    def select_price_max(self):
        self.actions.click_and_hold(self.get_price_max()).move_by_offset(-50,0).release().perform()

    def click_checkbox_apple(self):
        try:
            self.get_checkbox_apple().click()
            print("Click checkbox apple")
        except Exception as e:
            self.get_checkbox_apple().click()
            print("Click checkbox apple")


    #Method
    def select_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_select_hamburger()
        time.sleep(self.sleep)
        self.click_select_pc()
        time.sleep(self.sleep)
        self.select_price_min()
        time.sleep(self.sleep)
        self.select_price_max()
        time.sleep(self.sleep)
        self.click_checkbox_apple()
        time.sleep(self.sleep)
        self.click_filter_count()
        time.sleep(self.sleep)
        self.click_to_orange()
        time.sleep(self.sleep)
        self.click_filter_ram()
        time.sleep(self.sleep)
        self.move_to_window()
        time.sleep(self.sleep)
        self.click_platform()
        time.sleep(20)

