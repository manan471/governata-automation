import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class DataSourcePostgresSql_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.click_datasourcebtn = "//span[text() = 'Data Sources']"
        self.click_add_datasource = "//button[text() = 'Add Data Source']"
        self.click_microsoft_Sql_Server = "(//button[text() = 'Add Connection'])[2]"
        self.click_servicecatalog_dropdown = "react-select-2-input"
        self.click_test_Connection = "//button[text() = 'Test Connection']"
        self.click_add_datasource_connection = "(//button[text() = 'Add Data Source'])[2]"
        self.detect_data_source_page = "//p[text() = 'Connected Data Source']"
        self.error_message_xpath = "//div[contains(text(),'Connection Failed')]"
        self.click_crossbtn = "//button[@class = 'absolute right-1.5 top-1.5 rounded-md bg-[#F3F4F6] p-2 text-gray-900 transition-all duration-200 ease-in-out hover:bg-[#E5E7EB] hover:text-black focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 active:bg-[#D1D5DB] disabled:pointer-events-none dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600 rtl:left-4 rtl:right-auto']"
        self.click_system_username = "system_username"
        self.click_system_password  = "system_password"
        self.click_service_name_id = "service_name"
        self.click_mysql = "(//button[text() = 'Add Connection'])[1]"
        self.click_postgresssql = "(//button[text() = 'Add Connection'])[6]"

    def Click_PostgressSql(self):
        self.driver.find_element(by=By.XPATH, value=self.click_postgresssql).click()
        time.sleep(2)

    def Click_MySql(self):
        self.driver.find_element(by=By.XPATH, value=self.click_mysql).click()
        time.sleep(2)


    def Click_Service_Name_Id(self, name):
        self.robust_input((By.NAME, "service_name"), name)

    def Click_System_Password(self, name):
        self.robust_input((By.NAME, "system_password"), name)



    def Click_System_UserName(self, name):
        self.robust_input((By.NAME, "system_username"), name)


    def Click_CrossBtn(self):
        self.driver.find_element(By.XPATH, self.click_crossbtn).click()
        time.sleep(2)

    def robust_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()


    def robust_input(self, locator, value):
        field = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        field.clear()
        field.send_keys(value)

    # ---------- Page actions ----------
    def Click_DataSourcebtn(self):
        self.robust_click((By.XPATH, self.click_datasourcebtn))

    def Click_Add_DataSource(self):
        self.robust_click((By.XPATH, self.click_add_datasource))

    def Cick_Microsoft_Sql_Server(self):
        self.robust_click((By.XPATH, self.click_microsoft_Sql_Server))

    def Click_ServiceCatalog_Dropdown(self):
        self.robust_click((By.ID, self.click_servicecatalog_dropdown))
        time.sleep(2)
        self.driver.find_element(By.ID, self.click_servicecatalog_dropdown).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def Click_Test_Connection(self):
        self.robust_click((By.XPATH, self.click_test_Connection))

    def Click_Add_DataSource_ConnectBtn(self):
        self.robust_click((By.XPATH, self.click_add_datasource_connection))

    def Enter_Name(self, name):
        self.robust_input((By.NAME, "name"), name)

    def Enter_Host(self, host):
        self.robust_input((By.NAME, "host"), host)

    def Enter_Port(self, port):
        self.robust_input((By.NAME, "port"), port)

    def Enter_Database_Name(self, db_name):
        self.robust_input((By.NAME, "database_name"), db_name)

    def Enter_User_Name(self, username):
        self.robust_input((By.NAME, "username"), username)

    def Enter_Password(self, password):
        self.robust_input((By.NAME, "password"), password)

    # ---------- Detection ----------
    def DetectDataCatalogPage(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.detect_data_source_page)))
            return True
        except TimeoutException:
            return False

    # ---------- Negative validation ----------
    def Check_Connection_Failed(self, timeout=10):
        """
        Robustly detect transient validation error for invalid connection
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                error_elem = self.driver.find_element(By.XPATH,
                                                      "//div[contains(@class,'alert-error') and contains(text(),'Validation failed')]")
                if error_elem.is_displayed():
                    print("Validation Error Displayed: Connection Invalid")
                    return True
            except:
                pass
            time.sleep(0.2)  # short poll interval
        print("Validation Error NOT Displayed")
        return False
