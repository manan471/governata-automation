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
        cls.driver.implicitly_wait(8)

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
        bg_term = BusinessGlossary_TermPage(self.driver)

        self.step("Click Business Glossary", bg_term.Click_BusinessGlossary)
        time.sleep(2)
        self.step("Click Add Button", bg_term.Click_Add_Btn)
        time.sleep(2)
        self.step("Enter Term Definition EN", bg_term.Enter_Term_Definition)
        time.sleep(2)
        self.step("Enter Term Definition AR", bg_term.Enter_Term_Definition_Arabic)
        time.sleep(2)
        self.step("Click Service Catalog", bg_term.Click_Service_Catalog)
        time.sleep(2)
        self.step("Click Domain", bg_term.Click_Domain)
        time.sleep(2)
        self.step("Scroll Page", bg_term.ScrollModalToBottom)
        time.sleep(2)
        self.step("Click Folder", bg_term.Click_Folder)
        time.sleep(2)
        self.step("Click Related", bg_term.Click_Related)
        time.sleep(2)
        self.step("Enter Description", bg_term.Enter_Descp)
        time.sleep(2)
        self.step("Click Next", bg_term.Click_NextBtn)
        time.sleep(2)
        assert bg_term.DetectServiceCatalogPage(), "Attributes page not opened"

    def test_Governata_C(self):
        bg_term = BusinessGlossary_TermPage(self.driver)
        time.sleep(1)
        self.step("Enter Attribute Name EN", bg_term.Enter_Attribute_Name)
        time.sleep(1)
        self.step("Enter Attribute Name AR", bg_term.Enter_Attribute_Name_Ar)
        time.sleep(1)
        self.step("Select Data Type", bg_term.Click_Data_type)
        time.sleep(1)
        self.step("Select Classification", bg_term.Click_Classification)
        time.sleep(1)
        self.step("Scroll Attributes Page", bg_term.Attribute_ScrollModalToBottom)
        time.sleep(1)
        self.step("Enter Attribute Description EN", bg_term.Enter_Attribute_Descp)
        time.sleep(1)
        self.step("Enter Attribute Description AR", bg_term.Enter_Attribute_Descp_Ar)
        time.sleep(1)
        self.step("Click Next", bg_term.Click_NextBtn)
        time.sleep(1)

        assert bg_term.Detect_Stewardship_Page(), "Stewardship page not opened"

    def test_Governata_D(self):
        bg_term = BusinessGlossary_TermPage(self.driver)

        time.sleep(1)
        self.step("Scroll Stewardship Page", bg_term.Stewardship_ScrollModalToTop)
        time.sleep(1)
        self.step("Select Business Executive", bg_term.Click_Business_Executive)
        time.sleep(1)
        self.step("Select Business Steward", bg_term.Click_Business_Steward)
        time.sleep(1)
        self.step("Select Data Steward", bg_term.Click_Data_Steward)
        time.sleep(1)
        self.step("Select Legal Advisor", bg_term.Click_Legal_Advisor)
        time.sleep(1)
        self.step("Select Department", bg_term.Click_Department)
        time.sleep(1)
        self.step("Select Data Office Employee", bg_term.Click_Data_Office_Employee)
        time.sleep(1)
        self.step("Click Finish Button", bg_term.Click_FinishBtn)
        time.sleep(1)
        self.step("Verify Glossary Created", bg_term.Assert_Glossary_Created)



    def test_Governata_F(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        bg_term = BusinessGlossary_TermPage(self.driver)

        self.step("Click Business Glossary", bg_term.Click_BusinessGlossary)
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
        bg_term.Enter_Term_Definition()
        time.sleep(2)
        bg_term.Enter_Term_Definition_Arabic()
        time.sleep(2)
        bg.Click_NextBtn()
        time.sleep(1)
        # bgterm.Click_Data_type()
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
        # bg.Click_Calculation()
        bg.Click_Attributes_Btn()
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
        bg.Click_Delete_Btn()
        bg.Click_Delete_Confirm_Btn()
        self.step("Verify Glossary Created", bg.Assert_Glossary_Deleted)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




















