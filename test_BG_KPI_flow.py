import unittest
from datetime import datetime
from config_reader import ConfigReader

from selenium.common import TimeoutException, NoSuchElementException
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

from Page_DataSource import DataSource_Page
from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page
from Page_ServiceCatalog_ViewPage import ServiceCatalogView_Page
from Page_BG_Term import BusinessGlossary_TermPage
from Page_BG_KPI import BusinessGlossary_KPIPage

class Governata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(10)

    def step(self, msg, action):
        try:
            action()
            print(f"PASS: {msg}")
        except Exception as e:
            self.fail(f"FAIL at: {msg} | Error: {str(e)}")

    def test_Governata_A(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        # ===============================
        # 0️⃣ Proper viewport
        # ===============================
        # driver.set_window_size(1366, 900)
        # driver.set_window_position(0, 0)

        # ===============================
        # 1️⃣ Switch to English
        # ===============================
        lang_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[text()='EN']]")
            )
        )
        driver.execute_script("arguments[0].click();", lang_btn)

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[contains(text(),'Email')]")
            )
        )

        # ===============================
        # 2️⃣ Email input
        # ===============================
        email = wait.until(
            EC.element_to_be_clickable((By.NAME, "email"))
        )
        email.click()
        email.clear()
        email.send_keys("Superadmin@example.com")

        # ===============================
        # 3️⃣ TAB → Password (THIS SCROLLS PAGE)
        # ===============================
        email.send_keys(Keys.TAB)

        password = wait.until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password.send_keys("password")

        # ===============================
        # 4️⃣ TAB → Login Button (THIS REVEALS BUTTON)
        # ===============================
        password.send_keys(Keys.TAB)

        sign_in_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Login']")
            )
        )

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", sign_in_btn)
        sign_in_btn.click()

        # Extra safety click
        driver.execute_script("arguments[0].click();", sign_in_btn)

        # ===============================
        # 5️⃣ Verify Login
        # ===============================
        # wait.until(EC.url_contains("/dashboard"))

        home_tab = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//span[text()='Home'])[2]")
            )
        )

        self.assertTrue(
            home_tab.is_displayed(),
            "❌ Test Failed: Home screen not visible after login"
        )

        print("✅ Test Passed: Login successful and Home screen is visible")

    def test_Governata_B(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        self.step("Click Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(1)
        self.step("Click Add Button", bg.Click_Add_Btn)
        time.sleep(1)
        self.driver.find_element(by=By.ID, value="type-1").click()
        time.sleep(1)
        self.step("Enter Term Definition EN", bg.Enter_Term_Definition)
        time.sleep(1)
        self.step("Enter Term Definition AR", bg.Enter_Term_Definition_Arabic)
        time.sleep(1)
        self.step("Click Service Catalog", bg.Click_Service_Catalog)
        time.sleep(1)
        self.step("Click Domain", bg.Click_Domain)
        time.sleep(1)
        self.step("Scroll Page", bg.ScrollModalToBottom)
        time.sleep(1)
        self.step("Click Folder", bg.Click_Folder)
        time.sleep(1)
        self.step("Click Related", bg.Click_Related)
        time.sleep(1)
        self.step("Enter Description", bg.Enter_Descp)
        time.sleep(1)
        self.step("Click Next", bg.Click_NextBtn)
        time.sleep(1)
        self.check = bg.Detect_Calculation_Descp()
        time.sleep(1)
        if self.check == True:
            print("Test_02:Verify that the Calculation Page is displayed Successfully")
        else:
            self.assertFalse(True, msg="Test_02: “Verify that the Calculation Page is not displayed")

    def test_Governata_C(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        bg.Calculation_ScrollToTop()
        bg.Enter_Calculation_Descp()
        bg.Enter_Formula()
        bg.Enter_Sql_Code()
        bg.Enter_Dimensions()
        bg.Click_NextBtn()
        self.check = bg.Detect_Frequency_Page()
        if self.check == True:
            print("Test_03:Verify that the Frequency Page is displayed Successfully")
        else:
            self.assertFalse(True, msg="Test_03: “Verify that the Frequency Page is not displayed")

    def test_Governata_D(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        bg.Click_Frequency()
        bg.Enter_Minimum_Expected_Value()
        bg.Enter_Maximum_Expected_Value()
        bg.Enter_Baseline_Year()
        bg.Enter_Baseline_Value()
        time.sleep(1)
        bg.Enter_Baseline_Unit()
        bg.Enter_Unit_of_Measure()
        bg.Enter_Target()
        bg.Enter_Data_Retention()
        bg.Click_NextBtn()
        time.sleep(1)
        self.check = bg.Detect_Stewardship_Page()
        if self.check == True:
            print("Test_04:Verify that the Stewardship Page is displayed Successfully")
        else:
            self.assertFalse(True, msg="Test_04: “Verify that the Stewardship Page is not displayed")
            time.sleep(5)

    def test_Governata_E(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        bg.Click_Business_Executive()
        bg.Click_Business_Steward()
        bg.Click_Data_Steward()
        bg.Click_Legal_Advisor()
        bg.Click_Department()
        bg.Click_Data_Office_Employee()
        bg.Click_Consumer()
        bg.Click_Finish_Btn()
        time.sleep(1)
        self.step("Verify Glossary Created", bg.Assert_Glossary_Created)
        time.sleep(2)


    def test_Governata_F(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        self.step("Click Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(2)
        bg.set_browser_zoom_75()
        time.sleep(5)
        # bg.Business_Glossary_ScrollToDown()
        bg.Action_Btn()
        time.sleep(1)
        bg.Click_Edit_Btn()
        time.sleep(1)
        bg.set_browser_zoom_100()
        time.sleep(2)
        bg.Enter_Term_Definition()
        time.sleep(2)
        bg.Enter_Term_Definition_Arabic()
        time.sleep(2)
        bg.Click_NextBtn()
        time.sleep(1)
        bg.Enter_Formula()
        time.sleep(1)
        bg.Click_NextBtn()
        time.sleep(1)
        bg.Click_NextBtn()
        time.sleep(1)
        bg.Click_Finish_Btn()
        time.sleep(1)
        self.step("Verify Glossary Created", bg.Assert_Glossary_Updated)

    def test_Governata_G(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        self.step("Click Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(2)
        bg.set_browser_zoom_75()
        bg.Action_Btn()
        time.sleep(1)
        bg.Click_View_Btn()
        time.sleep(1)
        bg.Click_Hierarchy_Btn()
        time.sleep(2)
        bg.Click_Calculation()
        # bg.Click_Attributes_Btn()
        time.sleep(1)
        bg.Click_Stewardship_Btn()
        time.sleep(1)
        bg.Click_Cross_Btn()
        time.sleep(1)
        self.check = bg.Detect_View_Page()
        if self.check == True:
            print("Test_04:Verify that the view Page is displayed Successfully")
        else:
            self.assertFalse(True, msg="Test_04: “Verify that the view Page is not displayed")

    def test_Governata_H(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        self.step("Click Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(2)
        bg.set_browser_zoom_75()
        bg.Action_Btn()
        time.sleep(1)
        bg.Click_Delete_Btn()
        time.sleep(1)
        bg.Click_Delete_Confirm_Btn()
        time.sleep(1)
        self.step("Verify Glossary Created", bg.Assert_Glossary_Deleted)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




