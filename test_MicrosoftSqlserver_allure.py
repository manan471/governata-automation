import unittest
import allure
from config_reader import ConfigReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import string
import time

from Page_DataSource import DataSource_Page
from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page


@allure.feature("Governata Automation")
class Governata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(8)

    # ================= SCREENSHOT METHOD =================
    def attach_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    # ================= LOGIN TEST =================
    @allure.story("Login")
    @allure.title("Verify user login")
    def test_01_login(self):
        driver = self.driver
        login = Login_Page(driver)

        try:
            with allure.step("Select English"):
                WebDriverWait(driver, 50).until(
                    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Switch to English']"))
                ).click()

            with allure.step("Click Logo"):
                WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, login.clicklogobth))
                ).click()

            with allure.step("Enter credentials"):
                login.EnterEmail("Superadmin@example.com")
                login.EnterPassword("password")
                login.ClickLoginBtn()

            assert login.DetectloginPage() is True

            # ✅ PASS screenshot
            self.attach_screenshot("PASS_Login_Success")

        except Exception as e:
            self.attach_screenshot("FAIL_Login")
            self.fail(str(e))

    # ================= SERVICE CATALOG CREATE =================
    @allure.story("Service Catalog")
    @allure.title("Create Service Catalog")
    def test_02_create_service_catalog(self):
        driver = self.driver
        servicecatalog = ServiceCatalog_Page(driver)

        try:
            with allure.step("Open Service Catalog"):
                time.sleep(2)
                servicecatalog.Click_ServiceCatalog()

            with allure.step("Add Service Catalog"):
                servicecatalog.Click_AddServiceCatalog()
                time.sleep(2)

            with allure.step("Fill Form"):
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
                servicecatalog.EnterlicenseRenewalDate()
                time.sleep(2)
                servicecatalog.EnterProductionDate()
                time.sleep(2)
                servicecatalog.ClickNextBtn()
                time.sleep(2)
                servicecatalog.EnterManufacturer()
                time.sleep(2)
                servicecatalog.ClickNextBtn()
                time.sleep(2)
                servicecatalog.EnterRole()
                time.sleep(2)
                servicecatalog.EnterDepartment()
                time.sleep(2)
                servicecatalog.ClickSubmitBtn()
                time.sleep(2)

            assert servicecatalog.DetectServiceCatalogPage() is True

            # ✅ PASS screenshot
            self.attach_screenshot("PASS_ServiceCatalog_Created")

        except Exception as e:
            self.attach_screenshot("FAIL_ServiceCatalog_Create")
            self.fail(str(e))

    # ================= DATASOURCE POSITIVE =================
    @allure.story("Data Source")
    @allure.title("Create Data Source - Positive")
    def test_03_datasource_positive(self):
        driver = self.driver
        datasource = DataSource_Page(driver)
        time.sleep(3)

        try:
            driver.refresh()

            with allure.step("Open Data Source"):
                time.sleep(2)
                datasource.Click_DataSourcebtn()
                time.sleep(2)
                datasource.Click_Add_DataSource()
                time.sleep(2)
                datasource.Cick_Microsoft_Sql_Server()
                time.sleep(2)

            with allure.step("Enter Valid Details"):
                datasource.Enter_Name("manan" + ''.join(random.choice(string.ascii_lowercase) for _ in range(3)))
                time.sleep(2)
                datasource.Enter_Host(ConfigReader.database(None)['databases']['sqlserver']['host'])
                time.sleep(2)
                datasource.Enter_Port(str(ConfigReader.database(None)['databases']['sqlserver']['port']))
                time.sleep(2)
                datasource.Enter_Database_Name(ConfigReader.database(None)['databases']['sqlserver']['database'])
                time.sleep(2)
                datasource.Enter_User_Name(ConfigReader.database(None)['databases']['sqlserver']['username'])
                time.sleep(2)
                datasource.Enter_Password(ConfigReader.database(None)['databases']['sqlserver']['password'])
                time.sleep(2)

            with allure.step("Test Connection"):
                datasource.Click_Test_Connection()
                time.sleep(2)
                datasource.Click_Add_DataSource_ConnectBtn()
                time.sleep(2)

            assert datasource.DetectDataCatalogPage() is True

            # ✅ PASS screenshot
            time.sleep(2)
            self.attach_screenshot("PASS_DataSource_Positive")

        except Exception as e:
            time.sleep(1)
            self.attach_screenshot("FAIL_DataSource_Positive")
            self.fail(str(e))

    # ================= DATASOURCE NEGATIVE =================
    @allure.story("Data Source")
    @allure.title("Create Data Source - Negative")
    def test_04_datasource_negative(self):
        driver = self.driver
        datasource = DataSource_Page(driver)
        time.sleep(2)

        try:
            driver.refresh()
            time.sleep(2)

            with allure.step("Open Data Source"):
                time.sleep(2)
                datasource.Click_Add_DataSource()
                time.sleep(2)
                datasource.Cick_Microsoft_Sql_Server()
                time.sleep(2)

            with allure.step("Enter Invalid Data"):
                datasource.Enter_Name("Invalid_Test")
                time.sleep(1)
                datasource.Enter_Host("invalid-host")
                time.sleep(1)
                datasource.Enter_Port("9999")
                time.sleep(1)
                datasource.Enter_Database_Name("WrongDB")
                time.sleep(1)
                datasource.Enter_User_Name("wrongUser")
                time.sleep(1)
                datasource.Enter_Password("wrongPass")
                time.sleep(1)
                datasource.Click_Test_Connection()
                time.sleep(1)

            with allure.step("Verify Error Message"):
                WebDriverWait(driver, 50).until(
                    EC.text_to_be_present_in_element(
                        (By.XPATH, "//div[contains(text(),'Connection test failed')]"),
                        "Connection test failed"
                    )
                )

            # ✅ PASS screenshot (Negative test passed)
            self.attach_screenshot("PASS_DataSource_Negative")

        except Exception as e:
            self.attach_screenshot("FAIL_DataSource_Negative")
            self.fail(str(e))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()