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

class Login_Page():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.loginbtn = "//button[text() = 'Login']"
        self.visibilitylogin = "//span[text() = 'Home']"
        self.clicklogobth = "//div[@class = 'flex size-12 items-center justify-center rounded-md']"

    def set_browser_zoom_75(self):
        # Browser zoom 80%
        self.driver.execute_script("document.body.style.zoom='75%'")
        time.sleep(2)

    def ClickLogoBtn(self, timeout=10):
        """Wait for the Logo button to be clickable and then click it"""
        try:
            logo_btn = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.clicklogobth))
            )
            logo_btn.click()
        except Exception as e:
            raise Exception(f"Logo button not clickable. Error: {e}")
    # def ClickLogoBtn(self):
    #     self.driver.find_element(by=By.XPATH, value=self.clicklogobth).click()
    #     time.sleep(3)

    def EnterEmail(self, email):
        self.driver.find_element(by=By.NAME, value=self.email).send_keys(email)
        time.sleep(1)


    def EnterPassword(self, password):
        self.driver.find_element(by=By.NAME, value=self.password).send_keys(password)
        time.sleep(1)

    def ClickLoginBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.loginbtn).click()
        time.sleep(2)

    def DetectloginPage(self):
        time.sleep(2)
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.visibilitylogin))):
            return True
        else:
            return False