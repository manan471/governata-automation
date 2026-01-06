import unittest
from datetime import datetime

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

from Page_DataSourceMySql import DataSourceMySql_Page
from Page_DataSourcePostgresSql import DataSourcePostgresSql_Page
from config_reader import ConfigReader


from Page_DataSource import DataSource_Page
from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page
from Page_ServiceCatalog_ViewPage import ServiceCatalogView_Page
from Page_DataSourceOralce import DataSourceOracle_Page

class Governata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(10)

    def test_Governata_A(self):
        driver = self.driver
        login = Login_Page(driver)

        # =====================================
        # 1️⃣ Explicit wait ONLY for language switch
        # =====================================
        try:
            wait = WebDriverWait(driver, 40)

            lang_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[.//span[text()='EN']]")
                )
            )
            driver.execute_script("arguments[0].click();", lang_btn)

            # Confirm English UI loaded
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h1[contains(text(),'Sign')]")
                )
            )

        except Exception as e:
            self.assertFalse(True, msg=f"❌ Language switch failed: {e}")

        # =====================================
        # 2️⃣ Login (NO explicit wait here)
        # =====================================
        email = driver.find_element(By.NAME, "email")
        email.click()
        email.clear()
        email.send_keys("Superadmin@example.com")
        time.sleep(2)

        # TAB → password
        email.send_keys(Keys.TAB)

        password = driver.switch_to.active_element
        password.send_keys("password")
        time.sleep(2)

        # TAB → Sign In + ENTER
        password.send_keys(Keys.TAB)
        password.send_keys(Keys.ENTER)

        # =====================================
        # 3️⃣ Verify Login
        # =====================================
        self.check = login.DetectloginPage()
        time.sleep(2)
        if self.check:
            print("✅ Test_01: Governata login successful")
        else:
            self.assertFalse(True, msg="❌ Test_01: Governata login failed")



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
        time.sleep(2)
        servicecatalog.EnterLicenses()
        time.sleep(2)
        servicecatalog.ScrollDown()
        time.sleep(2)
        servicecatalog.EnterlicenseRenewalDate()
        time.sleep(2)
        servicecatalog.ScrollDown()
        time.sleep(2)
        servicecatalog.EnterProductionDate()
        time.sleep(2)
        servicecatalog.ClickNextBtn()
        time.sleep(2)
        servicecatalog.ScrollUp()
        time.sleep(3)
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
        datasource = DataSource_Page(driver)
        oralce = DataSourceOracle_Page(driver)
        mysql = DataSourceMySql_Page(driver)
        postgresssql = DataSourcePostgresSql_Page(driver)

        # datasource.Click_CrossBtn()
        self.driver.refresh()
        time.sleep(2)
        oralce.Click_DataSourcebtn()
        time.sleep(1)
        oralce.Click_Add_DataSource()
        time.sleep(1)
        postgresssql.Click_PostgressSql()
        time.sleep(2)
        oralce.Click_ServiceCatalog_Dropdown()
        time.sleep(2)
        oralce.Enter_Name("manan"+ ''.join(random.choice(string.ascii_lowercase) for i in range(2)))
        time.sleep(1)
        oralce.Enter_Host(str(ConfigReader.database(None)['databases']['postgres']['host']))
        time.sleep(1)
        oralce.Enter_Port(str(ConfigReader.database(None)['databases']['postgres']['port']))
        time.sleep(2)
        oralce.Enter_Database_Name(str(ConfigReader.database(None)['databases']['postgres']['database']))
        time.sleep(2)
        oralce.Enter_User_Name(str(ConfigReader.database(None)['databases']['postgres']['username']))
        time.sleep(2)
        oralce.Enter_Password(str(ConfigReader.database(None)['databases']['postgres']['password']))
        time.sleep(2)
        oralce.Click_Test_Connection()
        time.sleep(1)
        oralce.Click_Add_DataSource_ConnectBtn()
        time.sleep(2)
        self.check = oralce.DetectDataCatalogPage()
        time.sleep(3)
        if self.check == True:
            print("Test_01:Verified that the PostgresSql data source connection has been created successfully")
        else:
            self.assertFalse(True, msg="Verified PostgresSql Data Source Connection Creation Failed")

    def test_Governata_E(self):
        driver = self.driver
        login = Login_Page(driver)
        self.driver.refresh()
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[@id='add-data-source']"))
        # )
        servicecatalog = ServiceCatalog_Page(driver)
        datasource = DataSource_Page(driver)
        # datasource.Click_DataSourcebtn()
        datasource.Click_Add_DataSource()
        datasource.Cick_Microsoft_Sql_Server()
        time.sleep(2)
        datasource.Click_ServiceCatalog_Dropdown()
        time.sleep(2)
        datasource.Click_Test_Connection()
        # Enter dummy / invalid data
        datasource.Enter_Name("Invalid_Test")
        time.sleep(2)
        datasource.Click_Test_Connection()
        time.sleep(2)
        datasource.Enter_Host("invalid-host")
        time.sleep(2)
        datasource.Enter_Port("9999")
        time.sleep(2)
        datasource.Enter_Database_Name("WrongDB")
        time.sleep(2)
        datasource.Enter_User_Name("wrongUser")
        time.sleep(2)
        datasource.Enter_Password("wrongPass")
        time.sleep(2)
        datasource.Click_Test_Connection()
        time.sleep(2)
        # Wait for alert
        try:
            alert = WebDriverWait(self.driver, 30).until(
                lambda d: d.find_element(By.XPATH, "//div[contains(text(),'Connection test failed')]")
                if "Connection test failed" in d.find_element(By.XPATH,
                                                              "//div[contains(text(),'Connection test failed')]").text
                else False
            )
            alert_text = alert.text
            # self.take_screenshot("Negative_DataSource_Alert")
            assert "Connection test failed" in alert_text, f"Negative DataSource test failed. Found: '{alert_text}'"
        except TimeoutException:
            # self.take_screenshot("Negative_DataSource_Alert_NotFound")
            raise AssertionError(
                "Negative DataSource test failed: Alert 'Connection test failed' did not appear within 30 seconds."
            )

        # except Exception as e:
        #     self.take_screenshot("DataSource_Negative_Failure")
        #     raise e


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

