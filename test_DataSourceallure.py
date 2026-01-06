import time
import unittest
import allure
from datetime import datetime
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import string
import os

from Page_DataSource import DataSource_Page
from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page
from Page_ServiceCatalog_ViewPage import ServiceCatalogView_Page

class Governata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com/")
        cls.driver.implicitly_wait(10)
        cls.screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(cls.screenshots_dir, exist_ok=True)

    # ---------------------------
    # Screenshot Helper
    # ---------------------------
    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(self.screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(path)
        allure.attach.file(path, name=name, attachment_type=allure.attachment_type.PNG)

    # ---------------------------
    # Safe Click Helper
    # ---------------------------
    def safe_click(self, xpath, timeout=15, name="click_action"):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.take_screenshot(f"{name}_clicked")

    # ---------------------------
    # Test A: Login
    # ---------------------------
    @allure.title("Governata Login Test")
    @allure.step("Login as Superadmin")
    def test_Governata_A(self):
        login = Login_Page(self.driver)
        try:
            self.safe_click("//img[@alt='Switch to English']", name="SwitchToEnglish")
            self.safe_click(login.clicklogobth, name="LogoButton")
            login.EnterEmail("Superadmin@example.com")
            login.EnterPassword("password")
            login.ClickLoginBtn()
            time.sleep(2)
            self.take_screenshot("Login_Page_After_Submit")
            assert login.DetectloginPage(), "Login failed"
        except Exception as e:
            self.take_screenshot("Login_Failure")
            raise e

    # ---------------------------
    # Test B: Service Catalog Page
    # ---------------------------
    @allure.title("Service Catalog Page Verification")
    @allure.step("Open Service Catalog page and verify")
    def test_Governata_B(self):
        servicecatalog = ServiceCatalog_Page(self.driver)
        try:
            time.sleep(2)
            servicecatalog.Click_ServiceCatalog()
            time.sleep(2)
            self.take_screenshot("ServiceCatalog_Page_Loaded")
            assert servicecatalog.DetectServiceCatalogPage(), "Service Catalog page not displayed"
        except Exception as e:
            self.take_screenshot("ServiceCatalog_Failure")
            raise e

    # ---------------------------
    # Test C: Create Service Catalog Entry
    # ---------------------------
    @allure.title("Create Service Catalog Entry")
    @allure.step("Fill Service Catalog Form")
    def test_Governata_C(self):
        servicecatalog = ServiceCatalog_Page(self.driver)
        try:
            servicecatalog.Click_AddServiceCatalog()
            time.sleep(2)
            servicecatalog.Enter_Titlename()
            time.sleep(2)
            servicecatalog.EnterApplicationTechnology()
            time.sleep(2)
            servicecatalog.EnterDatabaseTechnology()
            time.sleep(2)
            servicecatalog.EnterDatabaseEdition()
            time.sleep(2)
            servicecatalog.EnterDatabaseVersion()
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
            time.sleep(4)
            servicecatalog.EnterManufacturer()
            time.sleep(2)
            servicecatalog.ClickNextBtn()
            time.sleep(3)
            servicecatalog.EnterRole()
            time.sleep(3)
            servicecatalog.EnterDepartment()
            time.sleep(2)
            servicecatalog.ClickSubmitBtn()
            time.sleep(2)
            self.take_screenshot("ServiceCatalog_Entry_Created")
            assert servicecatalog.DetectServiceCatalogPage(), "Service Catalog not created"
        except Exception as e:
            self.take_screenshot("ServiceCatalog_Create_Failure")
            raise e

    # ---------------------------
    # Test D: Positive DataSource
    # ---------------------------
    @allure.title("Positive DataSource Creation")
    @allure.step("Create Microsoft SQL Server Data Source")
    def test_Governata_D(self):
        datasource = DataSource_Page(self.driver)
        try:
            self.driver.refresh()
            time.sleep(2)
            datasource.Click_DataSourcebtn()
            time.sleep(2)
            datasource.Click_Add_DataSource()
            time.sleep(1)
            datasource.Cick_Microsoft_Sql_Server()
            time.sleep(1)
            datasource.Click_ServiceCatalog_Dropdown()
            time.sleep(1)
            datasource.Enter_Name("manan"+ ''.join(random.choice(string.ascii_lowercase) for i in range(2)))
            time.sleep(1)
            datasource.Enter_Host("35.224.157.0")
            time.sleep(1)
            datasource.Enter_Port("1433")
            time.sleep(1)
            datasource.Enter_Database_Name("bbgun_smaller")
            time.sleep(1)
            datasource.Enter_User_Name("SA")
            time.sleep(1)
            datasource.Enter_Password("Qwerty@2024")
            time.sleep(1)
            datasource.Click_Test_Connection()
            time.sleep(1)
            datasource.Click_Add_DataSource_ConnectBtn()
            time.sleep(3)
            self.take_screenshot("Positive_DataSource_Created")
            assert datasource.DetectDataCatalogPage(), "Data Source creation failed"
        except Exception as e:
            self.take_screenshot("DataSource_Positive_Failure")
            raise e

    # ---------------------------
    # Test E: Negative DataSource
    # ---------------------------
    @allure.title("Negative DataSource Test")
    @allure.step("Enter invalid DataSource details")
    def test_Governata_E(self):
        datasource = DataSource_Page(self.driver)
        try:
            self.driver.refresh()
            time.sleep(2)
            datasource.Click_Add_DataSource()
            time.sleep(2)
            datasource.Cick_Microsoft_Sql_Server()
            time.sleep(2)
            datasource.Click_ServiceCatalog_Dropdown()
            time.sleep(2)
            datasource.Enter_Name("Invalid_Test")
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
            self.take_screenshot("Negative_DataSource_Test_Clicked")

            # Wait for alert
            try:
                alert = WebDriverWait(self.driver, 30).until(
                    lambda d: d.find_element(By.XPATH, "//div[contains(text(),'Connection test failed')]")
                    if "Connection test failed" in d.find_element(By.XPATH,
                                                                  "//div[contains(text(),'Connection test failed')]").text
                    else False
                )
                alert_text = alert.text
                self.take_screenshot("Negative_DataSource_Alert")
                assert "Connection test failed" in alert_text, f"Negative DataSource test failed. Found: '{alert_text}'"
            except TimeoutException:
                self.take_screenshot("Negative_DataSource_Alert_NotFound")
                raise AssertionError(
                    "Negative DataSource test failed: Alert 'Connection test failed' did not appear within 30 seconds."
                )
        except Exception as e:
            self.take_screenshot("DataSource_Negative_Failure")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
