import unittest
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import os


class ServiceCatalogView_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_seach_input_field = "(//input[@class = 'border-input ring-offset-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-10 rounded-md border py-2 text-sm file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:border-primary focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 w-full border-none bg-transparent px-4 caret-blue-600 ring-0 focus-visible:ring-0'])[2]"
        self.click_database_technologies = "//button[text() = 'Database Technologies']"
        self.click_radiobtn = "(//input[@class = 'form-checkbox ml-3'])[1]"
        self.click_manufacturer = "//button[text() = 'Manufacturer']"
        self.click_manufacturer_radiobtn = "(//input[@class = 'form-checkbox ml-3'])[2]"
        self.click_viewbtn = "(//button[@class = 'inline-flex items-center justify-center bg-blue-100 text-blue-700 tracking-wide hover:bg-blue-200 focus:outline focus:outline-2 focus:outline-offset-2 focus:ring-indigo-500 px-[11px] py-[7px] text-xs btn-xs ml-3 rounded-full false'])[1]"
        self.scrollable_div = "//div[@class='ml-auto hidden flex-grow overflow-auto bg-gray-100 sm:block rtl:ml-0 rtl:mr-auto']"
        self.click_updatebtn = "(//button[@class = 'inline-flex items-center justify-center bg-blue-100 text-blue-700 tracking-wide hover:bg-blue-200 focus:outline focus:outline-2 focus:outline-offset-2 focus:ring-indigo-500 px-[11px] py-[7px] text-xs btn-xs ml-3 rounded-full false'])[2]"
        self.click_deletebtn = "(//button[@class = 'inline-flex items-center justify-center bg-blue-100 text-blue-700 tracking-wide hover:bg-blue-200 focus:outline focus:outline-2 focus:outline-offset-2 focus:ring-indigo-500 px-[11px] py-[7px] text-xs btn-xs ml-3 rounded-full false'])[3]"

    def Click_Delete(self):
        self.driver.find_element(by=By.XPATH, value=self.click_deletebtn).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value= "//button[text() = 'Delete']").click()


    def Click_UpdateBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_updatebtn).click()
        time.sleep(1)

    def ScrollDivUp(self, pixels=1000):
        element = self.driver.find_element(By.XPATH, self.scrollable_div)
        self.driver.execute_script("arguments[0].scrollTop -= arguments[1];", element, pixels)
        time.sleep(2)
        self.driver.find_element(By.XPATH, value="//div[text() = 'Service Catalog']").click()

    def ScrollDivDown(self, pixels=1000):
        element = self.driver.find_element(By.XPATH, self.scrollable_div)
        self.driver.execute_script("arguments[0].scrollTop += arguments[1];", element, pixels)
        print(f"Scrolled down {pixels}px inside the div ✅")


    def Click_ViewBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_viewbtn).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)

    def Click_Manufacturer_Radiobtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_manufacturer_radiobtn).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Connected Catalog']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[text() = 'Clear All']").click()
        time.sleep(1)

    def Click_Manufacturer(self):
        self.driver.find_element(by=By.XPATH, value=self.click_manufacturer).click()
        time.sleep(1)

    def Click_RadioButton(self):
        self.driver.find_element(by=By.XPATH, value=self.click_radiobtn).click()
        time.sleep(1)


    def Click_Database_Technologies(self):
        self.driver.find_element(by=By.XPATH, value=self.click_database_technologies).click()
        time.sleep(1)

    def ClickSeachInputField(self):
        self.driver.find_element(by=By.XPATH, value=self.click_seach_input_field).send_keys("Manan Test")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.click_seach_input_field).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
        time.sleep(1)

