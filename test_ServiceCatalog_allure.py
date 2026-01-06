import unittest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

from Page_login import Login_Page
from Page_ServiceCatalog import ServiceCatalog_Page
from Page_ServiceCatalog_ViewPage import ServiceCatalogView_Page

# ===============  Screenshot Utility =============== #

def attach_screenshot(driver, name="Screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG
    )


class Governata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com/")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # ================================ Test A ================================ #
    @allure.title("Test_01: Verify Governata Login Successfully")
    def test_Governata_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(4)

        try:
            with allure.step("Click Logo Button & Select English Language"):

                # --- 1️⃣ Select English Language ---
                try:
                    english_flag_locator = (By.XPATH, "//img[@alt='Switch to English']")

                    english_flag = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located(english_flag_locator)
                    )
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable(english_flag_locator)
                    )

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", english_flag)
                    driver.execute_script("arguments[0].click();", english_flag)
                except Exception as e:
                    attach_screenshot(driver, "English Flag Error")
                    self.fail(f"Cannot select English language. Error: {e}")

                # --- 2️⃣ Click Logo Button ---
                try:
                    logo_locator = (By.XPATH, login.clicklogobth)

                    logo_btn = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located(logo_locator)
                    )
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable(logo_locator)
                    )

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logo_btn)
                    driver.execute_script("arguments[0].click();", logo_btn)
                except Exception as e:
                    attach_screenshot(driver, "Logo Button Error")
                    self.fail(f"Logo button not clickable. Error: {e}")

            # ======================= Login Steps ======================== #
            with allure.step("Enter Email & Password"):
                login.EnterEmail('Superadmin@example.com')
                login.EnterPassword('password')

            with allure.step("Click Login Button"):
                login.ClickLoginBtn()
                time.sleep(3)

            self.check = login.DetectloginPage()
            if self.check:
                attach_screenshot(driver, "Login Success")
                print("Verify Governata login page displayed successfully")
            else:
                raise Exception("Login Failed")

        except Exception as e:
            attach_screenshot(driver, "Login Failed Screenshot")
            raise e

    # ================================ Test B ================================ #
    @allure.title("Test_02: Verify Service Catalog Opens Successfully")
    def test_Governata_B(self):
        driver = self.driver
        servicecatalog = ServiceCatalog_Page(driver)

        try:
            with allure.step("Click Service Catalog"):
                servicecatalog.Click_ServiceCatalog()
                time.sleep(3)

            self.check = servicecatalog.DetectServiceCatalogPage()
            if self.check:
                attach_screenshot(driver, "Service Catalog Page Opened")
                print("Service Catalog page displayed successfully")
            else:
                raise Exception("Service Catalog page not loaded")

        except Exception as e:
            attach_screenshot(driver, "Service Catalog Error")
            raise e

    # ================================ Test C ================================ #
    @allure.title("Test_03:Verify Create New Service Catalog Record")
    def test_Governata_C(self):
        driver = self.driver
        servicecatalog = ServiceCatalog_Page(driver)

        try:
            with allure.step("Click Add Service Catalog"):
                servicecatalog.Click_AddServiceCatalog()
                time.sleep(2)

            with allure.step("Enter Title Name"):
                servicecatalog.Enter_Titlename()
                time.sleep(2)

            with allure.step("Enter Application Technology"):
                servicecatalog.EnterApplicationTechnology()
                time.sleep(2)

            with allure.step("Enter Database Technology"):
                servicecatalog.EnterDatabaseTechnology()
                time.sleep(2)

            with allure.step("Enter Database Edition"):
                servicecatalog.EnterDatabaseEdition()
                time.sleep(2)

            with allure.step("Enter Database Version"):
                servicecatalog.EnterDatabaseVersion()
                time.sleep(2)

            servicecatalog.ScrollDown()

            with allure.step("Enter Additional Fields"):
                servicecatalog.EnterApplicationInterface()
                time.sleep(2)
                servicecatalog.EnterLicenses()
                time.sleep(1)
                servicecatalog.ScrollDown()
                time.sleep(2)
                servicecatalog.EnterlicenseRenewalDate()
                time.sleep(2)
                servicecatalog.ScrollDown()
                time.sleep(2)
                servicecatalog.EnterProductionDate()

            with allure.step("Click Next Button"):
                servicecatalog.ClickNextBtn()
                time.sleep(3)

            servicecatalog.ScrollUp()

            with allure.step("Enter Manufacturer"):
                time.sleep(3)
                servicecatalog.EnterManufacturer()

            with allure.step("Next Button Page 2"):
                time.sleep(3)
                servicecatalog.ClickNextBtn()

            with allure.step("Enter Role & Department"):
                time.sleep(3)
                servicecatalog.EnterRole()
                time.sleep(3)
                servicecatalog.EnterDepartment()

            with allure.step("Click Submit Button"):
                servicecatalog.ClickSubmitBtn()

            self.check = servicecatalog.DetectServiceCatalogPage()
            if self.check:
                attach_screenshot(driver, "Service Catalog Created")
                print("Service Catalog created successfully")
            else:
                raise Exception("Service Catalog not created")

        except Exception as e:
            attach_screenshot(driver, "Create Catalog Error")
            raise e

    # ================================ Test D ================================ #
    @allure.title("Test_04: Verify Update Existing Service Catalog Record")
    def test_Governata_D(self):
        driver = self.driver
        servicecatalog = ServiceCatalog_Page(driver)
        view = ServiceCatalogView_Page(driver)

        try:
            with allure.step("Search and View Record"):
                time.sleep(2)
                view.ClickSeachInputField()
                time.sleep(2)
                view.Click_Database_Technologies()
                time.sleep(2)
                view.Click_RadioButton()
                time.sleep(2)
                view.Click_Manufacturer()
                time.sleep(2)
                view.Click_Manufacturer_Radiobtn()
                time.sleep(2)
                view.Click_ViewBtn()

            with allure.step("Scroll Inside View Page"):
                time.sleep(2)
                view.ScrollDivDown()
                time.sleep(2)
                view.ScrollDivUp()

            with allure.step("Click Update Button"):
                time.sleep(2)
                view.Click_UpdateBtn()
                time.sleep(2)

            with allure.step("Update Title"):
                time.sleep(2)
                servicecatalog.Enter_Titlename()

            with allure.step("Update Application Technology"):
                time.sleep(2)
                servicecatalog.EnterApplicationTechnology()

            with allure.step("Next to Submit"):
                time.sleep(2)
                servicecatalog.ClickNextBtn()
                time.sleep(2)
                servicecatalog.ScrollUp()
                time.sleep(3)
                servicecatalog.ClickNextBtn()
                time.sleep(2)
                servicecatalog.ClickSubmitBtn()

            self.check = servicecatalog.DetectServiceCatalogPage()
            if self.check:
                attach_screenshot(driver, "Record Updated")
                print("Record updated successfully")
            else:
                raise Exception("Record update failed")

        except Exception as e:
            attach_screenshot(driver, "Update Error")
            raise e

    # ================================ Test E ================================ #
    @allure.title("Test_05: Verify Delete Service Catalog Record")
    def test_Governata_E(self):
        driver = self.driver
        view = ServiceCatalogView_Page(driver)
        servicecatalog = ServiceCatalog_Page(driver)

        try:
            with allure.step("Click Delete Button"):
                time.sleep(2)
                view.Click_Delete()
                time.sleep(3)

            self.check = servicecatalog.DetectServiceCatalogPage()
            if self.check:
                attach_screenshot(driver, "Record Deleted")
                print("Verify Service Catalog deleted successfully")
            else:
                raise Exception("Verify Service Catalog delete failed")

        except Exception as e:
            attach_screenshot(driver, "Delete Error")
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()