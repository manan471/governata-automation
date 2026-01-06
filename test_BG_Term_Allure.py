import unittest
import time
import random
import string
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from allure_commons.types import AttachmentType

from Page_login import Login_Page
from Page_BG_Term import BusinessGlossary_TermPage
from Page_BG_KPI import BusinessGlossary_KPIPage


class Governata(unittest.TestCase):

    # =========================
    # SETUP
    # =========================
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(8)

    # =========================
    # SCREENSHOT HELPER
    # =========================
    def take_screenshot(self, name):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=AttachmentType.PNG
        )

    # =========================
    # STEP WRAPPER (AUTO SCREENSHOT)
    # =========================
    def step(self, msg, action):
        with allure.step(msg):
            try:
                action()
                self.take_screenshot(f"PASS - {msg}")
                print(f"PASS: {msg}")
            except Exception as e:
                self.take_screenshot(f"FAIL - {msg}")
                self.fail(f"FAIL at: {msg} | Error: {str(e)}")

    # =========================
    # TEST A – LOGIN
    # =========================
    @allure.feature("Authentication")
    @allure.story("Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Authentication")
    @allure.story("Login")
    @allure.title("Verify user can login successfully and Home screen is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Governata_A(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        with allure.step("Switch application language to English"):
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

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Language switched to English",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Enter login credentials"):
            email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email.click()
            email.clear()
            email.send_keys("Superadmin@example.com")

            email.send_keys(Keys.TAB)

            password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
            password.send_keys("password")

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Credentials entered",
                attachment_type=AttachmentType.PNG
            )

        with allure.step("Click Login button"):
            password.send_keys(Keys.TAB)

            sign_in_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Login']")
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                sign_in_btn
            )
            sign_in_btn.click()

            # Extra safety click
            driver.execute_script("arguments[0].click();", sign_in_btn)

        with allure.step("Verify Home screen is visible after login"):
            home_tab = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "(//span[text()='Home'])[2]")
                )
            )

            # Assertion
            self.assertTrue(
                home_tab.is_displayed(),
                "❌ Test Failed: Home screen not visible after login"
            )

            # Screenshot on PASS
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Home screen visible - Login successful",
                attachment_type=AttachmentType.PNG
            )
            time.sleep(2)
        # =========================
    # TEST B – CREATE BG TERM
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("Create Business Glossary Term")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_Governata_B(self):
        bg = BusinessGlossary_TermPage(self.driver)

        self.step("Click Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(1)
        self.step("Click Add Button", bg.Click_Add_Btn)
        time.sleep(1)
        self.step("Enter Term Definition EN", bg.Enter_Term_Definition)
        time.sleep(1)
        self.step("Enter Term Definition AR", bg.Enter_Term_Definition_Arabic)
        time.sleep(3)
        self.step("Select Service Catalog", bg.Click_Service_Catalog)
        time.sleep(3)
        self.step("Select Domain", bg.Click_Domain)
        time.sleep(2)
        self.step("Scroll Modal", bg.ScrollModalToBottom)
        time.sleep(1)
        self.step("Select Folder", bg.Click_Folder)
        time.sleep(1)
        self.step("Select Related", bg.Click_Related)
        time.sleep(1)
        self.step("Enter Description", bg.Enter_Descp)
        time.sleep(1)
        self.step("Click Next", bg.Click_NextBtn)
        time.sleep(1)

        assert bg.DetectServiceCatalogPage(), "Attributes page not opened"
        time.sleep(2)

    # =========================
    # TEST C – ATTRIBUTES
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("Add Attributes")
    def test_Governata_C(self):
        bg = BusinessGlossary_TermPage(self.driver)

        self.step("Enter Attribute Name EN", bg.Enter_Attribute_Name)
        time.sleep(1)
        self.step("Enter Attribute Name AR", bg.Enter_Attribute_Name_Ar)
        time.sleep(1)
        self.step("Select Data Type", bg.Click_Data_type)
        time.sleep(1)
        self.step("Select Classification", bg.Click_Classification)
        time.sleep(1)
        self.step("Scroll Attributes Page", bg.Attribute_ScrollModalToBottom)
        time.sleep(1)
        self.step("Enter Attribute Description EN", bg.Enter_Attribute_Descp)
        time.sleep(1)
        self.step("Enter Attribute Description AR", bg.Enter_Attribute_Descp_Ar)
        time.sleep(1)
        self.step("Click Next", bg.Click_NextBtn)
        time.sleep(1)

        assert bg.Detect_Stewardship_Page(), "Stewardship page not opened"
        time.sleep(2)

    # =========================
    # TEST D – STEWARDSHIP
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("Assign Stewardship & Finish")
    def test_Governata_D(self):
        bg = BusinessGlossary_TermPage(self.driver)

        self.step("Scroll Stewardship Page", bg.Stewardship_ScrollModalToTop)
        time.sleep(1)
        self.step("Select Business Executive", bg.Click_Business_Executive)
        time.sleep(1)
        self.step("Select Business Steward", bg.Click_Business_Steward)
        time.sleep(1)
        self.step("Select Data Steward", bg.Click_Data_Steward)
        time.sleep(1)
        self.step("Select Legal Advisor", bg.Click_Legal_Advisor)
        time.sleep(1)
        self.step("Select Department", bg.Click_Department)
        time.sleep(1)
        self.step("Select Data Office Employee", bg.Click_Data_Office_Employee)
        time.sleep(1)
        self.step("Click Finish", bg.Click_FinishBtn)
        time.sleep(1)
        self.step("Verify Glossary Created", bg.Assert_Glossary_Created)
        time.sleep(2)

    # =========================
    # TEST F – UPDATE BG
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("Update Business Glossary")
    def test_Governata_F(self):
        bg = BusinessGlossary_KPIPage(self.driver)
        bg_term = BusinessGlossary_TermPage(self.driver)

        time.sleep(1)
        self.step("Open Business Glossary", bg_term.Click_BusinessGlossary)
        time.sleep(1)
        bg.set_browser_zoom_75()
        time.sleep(1)
        self.step("Open Action Menu", bg.Action_Btn)
        time.sleep(1)
        self.step("Click Edit", bg.Click_Edit_Btn)
        time.sleep(1)

        bg.set_browser_zoom_100()
        time.sleep(1)
        self.step("Update Term Definition EN", bg_term.Enter_Term_Definition)
        time.sleep(1)
        self.step("Update Term Definition AR", bg_term.Enter_Term_Definition_Arabic)
        time.sleep(1)
        self.step("Click Next", bg.Click_NextBtn)
        time.sleep(1)
        self.step("Click Next Again", bg.Click_NextBtn)
        time.sleep(1)
        self.step("Click Finish", bg.Click_Finish_Btn)
        time.sleep(1)
        self.step("Verify Glossary Updated", bg.Assert_Glossary_Updated)
        time.sleep(2)

    # =========================
    # TEST G – VIEW BG
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("View Glossary")
    def test_Governata_G(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        self.step("Open Business Glossary", bg.Click_BusinessGlossary)
        time.sleep(1)
        bg.set_browser_zoom_75()
        time.sleep(1)
        self.step("Open Action Menu", bg.Action_Btn)
        time.sleep(1)
        self.step("Click View", bg.Click_View_Btn)
        time.sleep(1)
        bg.set_browser_zoom_100()
        self.step("Open Hierarchy", bg.Click_Hierarchy_Btn)
        time.sleep(1)
        self.step("Open Attributes", bg.Click_Attributes_Btn)
        time.sleep(1)
        self.step("Open Stewardship", bg.Click_Stewardship_Btn)
        time.sleep(1)
        self.step("Close View", bg.Click_Cross_Btn)
        time.sleep(1)

        assert bg.Detect_View_Page(), "View page not displayed"
        time.sleep(2)

    # =========================
    # TEST H – DELETE BG
    # =========================
    @allure.feature("Business Glossary")
    @allure.story("Delete Business Glossary")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Governata_H(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        self.step("Open Business Glossary", bg.Click_BusinessGlossary)
        bg.set_browser_zoom_75()
        time.sleep(1)
        self.step("Open Action Menu", bg.Action_Btn)
        time.sleep(1)
        self.step("Click Delete", bg.Click_Delete_Btn)
        time.sleep(1)
        self.step("Confirm Delete", bg.Click_Delete_Confirm_Btn)
        time.sleep(1)
        self.step("Verify Glossary Deleted", bg.Assert_Glossary_Deleted)
        time.sleep(2)

    # =========================
    # TEARDOWN
    # =========================
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
