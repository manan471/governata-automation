import unittest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Page_login import Login_Page
from Page_DataSource import DataSource_Page


class Governata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://data-governance-peach.vercel.app")
        cls.wait = WebDriverWait(cls.driver, 20)

    # UNIVERSAL SAFE CLICK (with auto-wait after click)
    def safe_click(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)   # ← Small stable delay after every click

    # UNIVERSAL SAFE SENDKEY
    def safe_type(self, send_function, value):
        send_function(value)
        time.sleep(1)   # ← Small delay after text input

    # ---------------------------------------------------------
    # TEST A: LOGIN
    # ---------------------------------------------------------
    def test_A_Login(self):
        driver = self.driver
        login = Login_Page(driver)

        self.safe_click("//img[@alt='Switch to English']")
        self.safe_click(login.clicklogobth)

        self.safe_type(login.EnterEmail, "Superadmin@example.com")
        self.safe_type(login.EnterPassword, "password")

        login.ClickLoginBtn()
        time.sleep(2)

        self.assertTrue(login.DetectloginPage(), "Login Failed")
        print("✔ Login Successful")

    # ---------------------------------------------------------
    # TEST B: POSITIVE DATASOURCE CREATION
    # ---------------------------------------------------------
    def test_B_Create_DataSource(self):
        driver = self.driver
        datasource = DataSource_Page(driver)

        self.safe_click(datasource.dataSource_btn)
        self.safe_click(datasource.add_DataSource)
        self.safe_click(datasource.microsoft_sql)

        dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, datasource.drop_ServiceCatalog)))
        self.driver.execute_script("arguments[0].click();", dropdown)
        time.sleep(1)

        # Enter Fields
        self.safe_type(datasource.Enter_Name, "manan" + ''.join(random.choice(string.ascii_lowercase) for _ in range(2)))
        self.safe_type(datasource.Enter_Host, "35.224.157.0")
        self.safe_type(datasource.Enter_Port, "1433")
        self.safe_type(datasource.Enter_Database_Name, "bbgun_smaller")
        self.safe_type(datasource.Enter_User_Name, "SA")
        self.safe_type(datasource.Enter_Password, "Qwerty@2024")

        datasource.Click_Test_Connection()
        time.sleep(2)

        datasource.Click_Add_DataSource_ConnectBtn()
        time.sleep(2)

        self.assertTrue(datasource.DetectDataCatalogPage(), "Datasource creation failed")
        print("✔ Positive Test Passed: Data Source Created Successfully")

    # ---------------------------------------------------------
    # TEST C: NEGATIVE TEST
    # ---------------------------------------------------------
    def test_C_Negative_DataSource(self):
        driver = self.driver
        datasource = DataSource_Page(driver)

        self.safe_click(datasource.dataSource_btn)
        self.safe_click(datasource.add_DataSource)
        self.safe_click(datasource.microsoft_sql)

        dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, datasource.drop_ServiceCatalog)))
        self.driver.execute_script("arguments[0].click();", dropdown)
        time.sleep(1)

        self.safe_type(datasource.Enter_Name, "InvalidTest")
        self.safe_type(datasource.Enter_Host, "invalid-host")
        self.safe_type(datasource.Enter_Port, "9999")
        self.safe_type(datasource.Enter_Database_Name, "WrongDB")
        self.safe_type(datasource.Enter_User_Name, "wrongUser")
        self.safe_type(datasource.Enter_Password, "wrongPass")

        datasource.Click_Test_Connection()
        time.sleep(2)

        alert = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Connection test failed')]"))
        )

        self.assertIn("Connection test failed", alert.text)
        print("✔ Negative Test Passed: Connection failed as expected")


if __name__ == "__main__":
    unittest.main()
