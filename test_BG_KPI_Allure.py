import unittest
import time
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_BG_KPI import BusinessGlossary_KPIPage


# ===============================
# 🔹 ALLURE SCREENSHOT HELPER
# ===============================
def attach_screenshot(driver, name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG
    )


@allure.feature("Governata – Business Glossary KPI")
class Governata(unittest.TestCase):

    # ===============================
    # 🔹 SETUP
    # ===============================
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://uat.governata.com")
        cls.driver.implicitly_wait(10)
        time.sleep(1)

    # =================================================
    # 🔹 TEST A: LOGIN
    # =================================================
    @allure.story("Authentication")
    @allure.title("Login and verify Home screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Governata_A_Login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Switch to English
            lang_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='EN']]"))
            )
            driver.execute_script("arguments[0].click();", lang_btn)
            time.sleep(1)

            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//label[contains(text(),'Email')]")
                )
            )
            time.sleep(1)

            # Enter Email
            email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email.send_keys("Superadmin@example.com")
            time.sleep(1)
            email.send_keys(Keys.TAB)
            time.sleep(1)

            # Enter Password
            password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
            password.send_keys("password")
            time.sleep(1)
            password.send_keys(Keys.TAB)
            time.sleep(1)

            # Click Login
            sign_in_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                sign_in_btn
            )
            time.sleep(1)
            sign_in_btn.click()
            time.sleep(1)

            # Verify Home
            home_tab = wait.until(
                EC.visibility_of_element_located((By.XPATH, "(//span[text()='Home'])[2]"))
            )
            self.assertTrue(home_tab.is_displayed())
            time.sleep(1)

            attach_screenshot(driver, "PASS - Login Successful")

        except Exception as e:
            attach_screenshot(driver, "FAIL - Login")
            raise e

    # =================================================
    # 🔹 TEST B: CREATE KPI – TERM INFO
    # =================================================
    @allure.story("KPI Lifecycle")
    @allure.title("Create KPI – Term Information")
    def test_Governata_B_Create_Term(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_BusinessGlossary()
            time.sleep(1)

            bg.Click_Add_Btn()
            time.sleep(1)

            self.driver.find_element(By.ID, "type-1").click()
            time.sleep(1)

            bg.Enter_Term_Definition()
            time.sleep(1)

            bg.Enter_Term_Definition_Arabic()
            time.sleep(1)

            bg.Click_Service_Catalog()
            time.sleep(1)

            bg.Click_Domain()
            time.sleep(1)

            bg.ScrollModalToBottom()
            time.sleep(1)

            bg.Click_Folder()
            time.sleep(1)

            bg.Click_Related()
            time.sleep(1)

            bg.Enter_Descp()
            time.sleep(1)

            bg.Click_NextBtn()
            time.sleep(1)

            self.assertTrue(bg.Detect_Calculation_Descp())
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - KPI Term Created")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - KPI Term")
            raise e

    # =================================================
    # 🔹 TEST C: CALCULATION
    # =================================================
    @allure.story("KPI Lifecycle")
    @allure.title("KPI Calculation Page")
    def test_Governata_C_Calculation(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Calculation_ScrollToTop()
            time.sleep(1)

            bg.Enter_Calculation_Descp()
            time.sleep(1)

            bg.Enter_Formula()
            time.sleep(1)

            bg.Enter_Sql_Code()
            time.sleep(1)

            bg.Enter_Dimensions()
            time.sleep(1)

            bg.Click_NextBtn()
            time.sleep(1)

            self.assertTrue(bg.Detect_Frequency_Page())
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - Calculation Page")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - Calculation Page")
            raise e

    # =================================================
    # 🔹 TEST D: FREQUENCY
    # =================================================
    @allure.story("KPI Lifecycle")
    @allure.title("KPI Frequency Page")
    def test_Governata_D_Frequency(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_Frequency()
            time.sleep(1)

            bg.Enter_Minimum_Expected_Value()
            time.sleep(1)

            bg.Enter_Maximum_Expected_Value()
            time.sleep(1)

            bg.Enter_Baseline_Year()
            time.sleep(1)

            bg.Enter_Baseline_Value()
            time.sleep(1)

            bg.Enter_Baseline_Unit()
            time.sleep(1)

            bg.Enter_Unit_of_Measure()
            time.sleep(1)

            bg.Enter_Target()
            time.sleep(1)

            bg.Enter_Data_Retention()
            time.sleep(1)

            bg.Click_NextBtn()
            time.sleep(1)

            self.assertTrue(bg.Detect_Stewardship_Page())
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - Frequency Page")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - Frequency Page")
            raise e

    # =================================================
    # 🔹 TEST E: STEWARDSHIP + FINISH
    # =================================================
    @allure.story("KPI Lifecycle")
    @allure.title("KPI Stewardship & Finish")
    def test_Governata_E_Finish(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_Business_Executive()
            time.sleep(1)

            bg.Click_Business_Steward()
            time.sleep(1)

            bg.Click_Data_Steward()
            time.sleep(1)

            bg.Click_Legal_Advisor()
            time.sleep(1)

            bg.Click_Department()
            time.sleep(1)

            bg.Click_Data_Office_Employee()
            time.sleep(1)

            bg.Click_Consumer()
            time.sleep(1)

            bg.Click_Finish_Btn()
            time.sleep(1)

            bg.Assert_Glossary_Created()
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - KPI Created")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - KPI Finish")
            raise e

    # =================================================
    # 🔹 TEST F: EDIT KPI
    # =================================================
    @allure.story("KPI Management")
    @allure.title("Edit KPI")
    def test_Governata_F_Edit(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_BusinessGlossary()
            time.sleep(1)
            bg.set_browser_zoom_75()
            time.sleep(2)
            bg.Action_Btn()
            time.sleep(1)
            bg.Click_Edit_Btn()
            time.sleep(1)
            bg.set_browser_zoom_100()
            time.sleep(1)

            bg.Enter_Term_Definition()
            time.sleep(1)

            bg.Enter_Term_Definition_Arabic()
            time.sleep(1)

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

            bg.Assert_Glossary_Updated()
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - KPI Updated")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - KPI Edit")
            raise e

    # =================================================
    # 🔹 TEST G: VIEW KPI
    # =================================================
    @allure.story("KPI Management")
    @allure.title("View KPI")
    def test_Governata_G_View(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_BusinessGlossary()
            time.sleep(1)
            bg.set_browser_zoom_75()
            time.sleep(1)
            bg.Action_Btn()
            time.sleep(1)

            bg.Click_View_Btn()
            time.sleep(1)
            bg.set_browser_zoom_100()
            time.sleep(1)
            bg.Click_Hierarchy_Btn()
            time.sleep(1)

            bg.Click_Calculation()
            time.sleep(1)

            bg.Click_Stewardship_Btn()
            time.sleep(1)

            bg.Click_Cross_Btn()
            time.sleep(1)

            self.assertTrue(bg.Detect_View_Page())
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - KPI View")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - KPI View")
            raise e

    # =================================================
    # 🔹 TEST H: DELETE KPI
    # =================================================
    @allure.story("KPI Management")
    @allure.title("Delete KPI")
    def test_Governata_H_Delete(self):
        bg = BusinessGlossary_KPIPage(self.driver)

        try:
            bg.Click_BusinessGlossary()
            time.sleep(1)
            bg.set_browser_zoom_75()
            time.sleep(1)
            bg.Action_Btn()
            time.sleep(1)
            bg.Click_Delete_Btn()
            time.sleep(1)

            bg.Click_Delete_Confirm_Btn()
            time.sleep(1)

            bg.Assert_Glossary_Deleted()
            time.sleep(1)

            attach_screenshot(self.driver, "PASS - KPI Deleted")

        except Exception as e:
            attach_screenshot(self.driver, "FAIL - KPI Delete")
            raise e

    # ===============================
    # 🔹 TEARDOWN
    # ===============================
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()
