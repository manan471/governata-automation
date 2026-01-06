import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from Page_login import Login_Page
import time


class Governata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://data-governance-peach.vercel.app")
        cls.driver.implicitly_wait(10)

    def test_Governata_A(self):
        driver = self.driver
        login = Login_Page(driver)

        # --- 1️⃣ Select English Language ---
        try:
            english_flag = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='Switch to English']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", english_flag)
            driver.execute_script("arguments[0].click();", english_flag)
        except Exception as e:
            self.assertFalse(True, msg=f"Cannot select English language. Error: {e}")

        # --- 2️⃣ Click Logo Button ---
        try:
            logo_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, login.clicklogobth))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", logo_btn)
            driver.execute_script("arguments[0].click();", logo_btn)
        except Exception as e:
            self.assertFalse(True, msg=f"Logo button not clickable. Error: {e}")

        time.sleep(4)
        login.EnterEmail('Superadmin@example.com')
        login.EnterPassword('password')
        time.sleep(2)
        login.ClickLoginBtn()
        self.check = login.DetectloginPage()
        time.sleep(3)
        if self.check == True:
            print("Test_01:Verify Governata login page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_01: Verify Governata login failed")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
