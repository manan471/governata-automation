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

class ServiceCatalog_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_servicecatalog = "//span[text() = 'Service Catalog']"
        self.click_add_servicecatalog = "//button[text() = 'Add Service Catalog']"
        self.enter_titlename = "title"
        self.detectservicecatalogpage = "//p[text() = 'Number of Catalog']"
        self.enterapplicationtechnology = "application_technology"
        self.clickdatabasetechnologiesdropdown_input = "react-select-2-input"
        self.clickdatabasedition= "database_edition"
        self.clickdatabaseversion = "database_version"
        self.clickapplicationinterface = "react-select-3-input"
        self.clicklicenses = "react-select-4-input"
        self.clicklicenserenewaldate = "//span[text() = 'License Renewal Date']"
        self.clickproductiondate    ="//span[text() = 'Production Date']"
        self.clicknextbtn = "//button[text() = 'Next']"
        self.entermanufacturer = "react-select-5-input"
        self.enterrole  = "react-select-10-input"
        self.enterdepartment = "react-select-11-input"
        self.submitbtn = "//button[text() = 'Submit']"






    def ClickSubmitBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.submitbtn).click()
        try:
            self.driver.find_element(by=By.XPATH, value="//button[@class = 'absolute right-1.5 top-1.5 rounded-md bg-[#F3F4F6] p-2 text-gray-900 transition-all duration-200 ease-in-out hover:bg-[#E5E7EB] hover:text-black focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 active:bg-[#D1D5DB] disabled:pointer-events-none dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600 rtl:left-4 rtl:right-auto']").click()
            time.sleep(2)
        except:
            time.sleep(2)

    def EnterDepartment(self):
        self.driver.find_element(by=By.ID, value=self.enterdepartment).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.enterdepartment).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def EnterRole(self):
        self.driver.find_element(by=By.ID, value=self.enterrole).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.enterrole).send_keys(Keys.ARROW_DOWN+Keys.ENTER)



    def EnterManufacturer(self):
        self.driver.find_element(by=By.ID, value=self.entermanufacturer).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.entermanufacturer).send_keys(Keys.ARROW_DOWN+Keys.ENTER)

    def ScrollUp(self):
        scroll_div = self.driver.find_element(By.XPATH, "//div[contains(@class, 'layout-container') and contains(@class, 'overflow-auto')]")
        self.driver.execute_script("arguments[0].scrollTop = 0;", scroll_div)


    def ScrollDown(self):
        scroll_div = self.driver.find_element(By.XPATH,"//div[contains(@class, 'layout-container') and contains(@class, 'overflow-auto')]")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_div)

    def ClickNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.clicknextbtn).click()
        time.sleep(1)

    def EnterProductionDate(self):
        self.driver.find_element(by=By.XPATH, value=self.clickproductiondate).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//button[text() = '30'])[2]").click()

    def EnterlicenseRenewalDate(self):
        self.driver.find_element(by=By.XPATH, value=self.clicklicenserenewaldate).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//button[text() = '30'])[2]").click()


    def EnterLicenses (self):
        self.driver.find_element(by=By.ID, value=self.clicklicenses).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.clicklicenses).send_keys(Keys.ARROW_DOWN+Keys.ENTER)

    def EnterApplicationInterface(self):
        self.driver.find_element(by=By.ID, value=self.clickapplicationinterface).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.clickapplicationinterface).send_keys(Keys.ARROW_DOWN+Keys.ENTER)


    def EnterDatabaseVersion(self):
        self.driver.find_element(by=By.NAME, value=self.clickdatabaseversion).send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)

    def EnterDatabaseEdition(self):
        self.driver.find_element(by=By.NAME, value=self.clickdatabasedition).send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)

    def EnterDatabaseTechnology(self):
        self.driver.find_element(by=By.ID, value=self.clickdatabasetechnologiesdropdown_input).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.clickdatabasetechnologiesdropdown_input).send_keys(Keys.ARROW_DOWN+Keys.ENTER)
        time.sleep(1)



        # # Get all options
        # options = self.driver.find_elements(*self.dropdown_options)
        #
        # # Select a random option
        # random.choice(options).click()
        #
        # # self.driver.find_element(by=By.XPATH, value=self.databasetechnology).click()
        # # time.sleep(2)


    def EnterApplicationTechnology(self):
        self.driver.find_element(by=By.NAME, value=self.enterapplicationtechnology).send_keys("Test Manan" + ''.join(random.choice(string.ascii_lowercase) for i in range(2)))
        time.sleep(2)


    def DetectServiceCatalogPage(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detectservicecatalogpage))):
            return True
        else:
            return False

    def Enter_Titlename(self):
        self.driver.find_element(by=By.NAME, value=self.enter_titlename).send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(2)

    def Click_ServiceCatalog(self):
        self.driver.find_element(by=By.XPATH, value=self.click_servicecatalog).click()
        time.sleep(2)

    def Click_AddServiceCatalog(self):
        self.driver.find_element(by=By.XPATH, value=self.click_add_servicecatalog).click()
        time.sleep(2)


