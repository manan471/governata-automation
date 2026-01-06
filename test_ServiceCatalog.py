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
from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page
from Page_ServiceCatalog_ViewPage import ServiceCatalogView_Page

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

        time.sleep(2)
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



    def test_Governata_B(self):
        driver = self.driver
        login = Login_Page(driver)
        servicecatalog = ServiceCatalog_Page(driver)
        servicecatalog.Click_ServiceCatalog()
        time.sleep(4)
        self.check = servicecatalog.DetectServiceCatalogPage()
        time.sleep(3)
        if self.check == True:
            print("Test_02:Verify Service Catalog page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_02: Verify Service Catalog login failed")

    def test_Governata_C(self):
        driver = self.driver
        login = Login_Page(driver)
        servicecatalog = ServiceCatalog_Page(driver)
        servicecatalog.Click_AddServiceCatalog()
        time.sleep(1)
        try:
            servicecatalog.Enter_Titlename()
            print("3-A Verify that the Title Name field accepts input and the value is entered successfully.")
        except:
            print("Verify Enter Title name fail")
        # servicecatalog.Enter_Titlename()
        time.sleep(1)

        try:
            servicecatalog.EnterApplicationTechnology()
            print("3-B Verify that the Application Technology field accepts input and the value is entered successfully")
        except Exception:
            print("Verify EnterApplicationTechnology failed")
        # servicecatalog.EnterApplicationTechnology()
        time.sleep(1)
        try:
            servicecatalog.EnterDatabaseTechnology()
            print("3-C Verify that the Database Technology field accepts input and the value is entered successfully")
        except Exception:
            print("Verify EnterDatabaseTechnology failed")
        # servicecatalog.EnterDatabaseTechnology()
        try:
            servicecatalog.EnterDatabaseEdition()
            print("3-D Verify that the Database Edition field accepts input and the edition is entered successfully.")
        except Exception as e:
            print("Verify EnterDatabaseEdition failed")
        # servicecatalog.EnterDatabaseEdition()
        time.sleep(1)
        try:
            servicecatalog.EnterDatabaseVersion()
            print("3-E Verify that the Database Version field accepts input and the version is entered successfully. ")
        except Exception as e:
            print("Verify EnterDatabaseVersion failed")
        # servicecatalog.EnterDatabaseVersion()
        time.sleep(2)
        servicecatalog.ScrollDown()
        time.sleep(2)

        servicecatalog.EnterApplicationInterface()
        time.sleep(1)
        servicecatalog.EnterLicenses()
        time.sleep(1)
        servicecatalog.ScrollDown()
        time.sleep(1)
        servicecatalog.EnterlicenseRenewalDate()
        time.sleep(1)
        servicecatalog.ScrollDown()
        time.sleep(1)
        servicecatalog.EnterProductionDate()
        time.sleep(1)
        servicecatalog.ClickNextBtn()
        time.sleep(2)
        servicecatalog.ScrollUp()
        time.sleep(2)
        servicecatalog.EnterManufacturer()
        time.sleep(2)
        try:
            servicecatalog.ClickNextBtn()
            print("3-F Verify that the Next button is functioning correctly and successfully")
        except Exception:
            print("Verify Click NextBtn failed")
        # servicecatalog.ClickNextBtn()
        time.sleep(2)
        servicecatalog.EnterRole()
        time.sleep(2)
        servicecatalog.EnterDepartment()
        time.sleep(2)
        try:
            servicecatalog.ClickSubmitBtn()
            print("3-G Verify that the Submit button is functioning correctly and successfully submits the form")
        except Exception:
            print("Verify Click Submit button failed")
        # servicecatalog.ClickSubmitBtn()
        self.check = servicecatalog.DetectServiceCatalogPage()
        time.sleep(3)
        if self.check == True:
            print("Test_03:Verify that the Service Catalog is created successfully and the page is displayed properly")
        else:
            self.assertFalse(True, msg="Test_03: “Verify that the Service Catalog is not Created")
    def test_Governata_D(self):
        driver = self.driver
        login = Login_Page(driver)
        servicecatalog = ServiceCatalog_Page(driver)
        servicecatalogviewpage = ServiceCatalogView_Page(driver)
        time.sleep(1)
        servicecatalogviewpage.ClickSeachInputField()
        time.sleep(4)
        servicecatalogviewpage.Click_Database_Technologies()
        time.sleep(2)
        servicecatalogviewpage.Click_RadioButton()
        time.sleep(2)
        servicecatalogviewpage.Click_Manufacturer()
        time.sleep(2)
        servicecatalogviewpage.Click_Manufacturer_Radiobtn()
        time.sleep(2)
        servicecatalogviewpage.Click_ViewBtn()
        time.sleep(2)
        servicecatalogviewpage.ScrollDivDown()
        time.sleep(2)
        servicecatalogviewpage.ScrollDivUp()
        time.sleep(3)
        servicecatalogviewpage.Click_UpdateBtn()
        time.sleep(5)
        try:
            servicecatalog.Enter_Titlename()
            print("3-A Verify that the Title Name field accepts input and the value is entered successfully.")
        except:
            print("Verify Enter Title name fail")
            # servicecatalog.Enter_Titlename()
        time.sleep(1)

        try:
            servicecatalog.EnterApplicationTechnology()
            print("3-B Verify that the Application Technology field accepts input and the value is entered successfully")
        except Exception:
            print("Verify EnterApplicationTechnology failed")
            # servicecatalog.EnterApplicationTechnology()
        time.sleep(1)
        try:
            servicecatalog.EnterDatabaseTechnology()
            print("3-C Verify that the Database Technology field accepts input and the value is entered successfully")
        except Exception:
            print("Verify EnterDatabaseTechnology failed")
            # servicecatalog.EnterDatabaseTechnology()
        # try:
        #     servicecatalog.EnterDatabaseEdition()
        #     print("3-D Verify that the Database Edition field accepts input and the edition is entered successfully.")
        # except Exception as e:
        #     print("Verify EnterDatabaseEdition failed")
        #     # servicecatalog.EnterDatabaseEdition()
        # time.sleep(1)
        # try:
        #     servicecatalog.EnterDatabaseVersion()
        #     print("3-E Verify that the Database Version field accepts input and the version is entered successfully. ")
        # except Exception as e:
        #     print("Verify EnterDatabaseVersion failed")
            # servicecatalog.EnterDatabaseVersion()
        # time.sleep(2)
        # servicecatalog.ScrollDown()
        # time.sleep(2)
        #
        # servicecatalog.EnterApplicationInterface()
        # time.sleep(1)
        # servicecatalog.EnterLicenses()
        # time.sleep(1)
        # servicecatalog.ScrollDown()
        # time.sleep(1)
        # try:
        #     servicecatalog.EnterlicenseRenewalDate()
        # except:
        #     print("Verify EnterlicenseRenewalDate failed")
        # time.sleep(2)
        # servicecatalog.ScrollDown()
        # time.sleep(3)
        # try:
        #     servicecatalog.EnterProductionDate()
        #     time.sleep(2)
        # except:
        #     print("Verify EnterProductionDate failed")
        #     time.sleep(3)
        servicecatalog.ClickNextBtn()
        time.sleep(3)
        servicecatalog.ScrollUp()
        time.sleep(2)
        # servicecatalog.EnterManufacturer()
        # time.sleep(2)
        try:
            servicecatalog.ClickNextBtn()
            print("3-F Verify that the Next button is functioning correctly and successfully")
        except Exception:
            print("Verify Click NextBtn failed")
            # servicecatalog.ClickNextBtn()
        # servicecatalog.EnterRole()
        # time.sleep(2)
        # servicecatalog.EnterDepartment()
        time.sleep(2)
        try:
            servicecatalog.ClickSubmitBtn()
            print("3-G Verify that the Submit button is functioning correctly and successfully submits the form")
        except Exception:
            print("Verify Click Submit button failed")
            # servicecatalog.ClickSubmitBtn()
        self.check = servicecatalog.DetectServiceCatalogPage()
        time.sleep(3)
        if self.check == True:
            print("Test_03:Verify that the Service Catalog is Update Record successfully and the page is displayed properly")
        else:
            self.assertFalse(True, msg="Test_03: “Verify that the Service Catalog is not  Update Record")
    def test_Governata_E(self):
        driver = self.driver
        login = Login_Page(driver)
        servicecatalog = ServiceCatalog_Page(driver)
        servicecatalogviewpage = ServiceCatalogView_Page(driver)
        time.sleep(2)
        servicecatalogviewpage.Click_Delete()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()






















