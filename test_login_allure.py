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
import openpyxl
import allure
from allure_commons.types import AttachmentType
from Page_login import Login_Page

class Governata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(10)

    @allure.feature("Governata Login")
    @allure.story("Verify login functionality")
    def test_Governata_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(3)

        # Attach screenshot of the login page at the start
        with allure.step("Attach screenshot of login page before actions"):
            allure.attach(driver.get_screenshot_as_png(),
                          name="Login Page Initial",
                          attachment_type=AttachmentType.PNG)

        with allure.step("Click Logo Button"):
            login.ClickLogoBtn()
            time.sleep(3)

        with allure.step("Enter email and password"):
            login.EnterEmail('Superadmin@example.com')
            login.EnterPassword('password')
            time.sleep(2)

        with allure.step("Click Login Button"):
            login.ClickLoginBtn()

        self.check = login.DetectloginPage()


        if self.check:
            with allure.step("Login Successful"):
                allure.attach(driver.get_screenshot_as_png(),
                              name="Login Success",
                              attachment_type=AttachmentType.PNG)
            print("Test_01: Verify Governata login page has been displayed successfully")
        else:
            time.sleep(4)
            with allure.step("Login Failed"):
                allure.attach(driver.get_screenshot_as_png(),
                              name="Login Failed",
                              attachment_type=AttachmentType.PNG)
            self.assertFalse(True, msg="Test_03: Verify Governata login failed")
            time.sleep(3)
        driver.quit()